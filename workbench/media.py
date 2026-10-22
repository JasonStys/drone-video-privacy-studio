"""Jason Stys: bounded real MP4 decoding, new-frame redaction and clean H.264 encoding.

Exact functions/variables: docs/SOURCE_MAP.md. Run only in the killable worker process.
No downloaded models, recognition, network URLs, stream-copy, or source metadata reuse.
"""

import hashlib
import io
import math
import struct
import zlib
from fractions import Fraction
from pathlib import Path

import av
import numpy as np

from workbench.models import Mask

MAX_BYTES = 20 * 1024 * 1024
MAX_FRAMES = 600
MAX_PIXELS = 1280 * 720
MAX_OUTPUT = 32 * 1024 * 1024


def sha(path: Path):
    """Hash bounded application-owned media without exposing its private filename."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rectangle(mask: Mask, width: int, height: int):
    """Round outward and pad eight pixels against codec edge bleed; output uses exclusive ends."""
    return (
        max(0, math.floor(mask.x * width) - 8),
        max(0, math.floor(mask.y * height) - 8),
        min(width, math.ceil((mask.x + mask.width) * width) + 8),
        min(height, math.ceil((mask.y + mask.height) * height) + 8),
    )


def paint(array, masks: list[Mask], index: int):
    """Replace pixels in place; inclusive frame endpoints and overlapping masks form a union."""
    height, width = array.shape[:2]
    for mask in masks:
        if mask.first <= index <= mask.last:
            x0, y0, x1, y1 = rectangle(mask, width, height)
            array[y0:y1, x0:x1] = 0


def encoder(path: Path, width: int, height: int, fps: int):
    """Create a fresh video-only MP4; no source streams/metadata/side-data are remuxed."""
    container = av.open(str(path), mode="w", format="mp4", options={"movflags": "+faststart"})
    stream = container.add_stream("libx264", rate=fps)
    stream.width, stream.height = width, height
    stream.pix_fmt = "yuv420p"
    stream.codec_context.thread_count = 1
    stream.options = {
        "crf": "18",
        "preset": "veryfast",
        "tune": "zerolatency",
        "profile": "baseline",
    }
    return container, stream


def emit(container, stream, array, index, fps):
    """Reconstruct RGB pixels only; normalize presentation timestamps to decoded frame zero."""
    frame = av.VideoFrame.from_ndarray(array, format="rgb24")
    frame.pts, frame.time_base = index, Fraction(1, fps)
    for packet in stream.encode(frame):
        container.mux(packet)


def finish(container, stream):
    """Flush delayed packets before closing; partial outputs are never published by the service."""
    for packet in stream.encode():
        container.mux(packet)
    container.close()


def transcode(source: Path, destination: Path, masks: list[Mask]):
    """Validate full bounded CFR decode, mask frames and produce an entirely new video stream.

    Input: self-contained MP4 H.264/MPEG-4, even dimensions <=1280x720 and <=921600 pixels,
    1..30 integer fps, <=20 seconds / 600 frames. Timestamp irregularity fails closed.
    Memory: O(input bytes + width*height); time O(frames*(pixels + masks)).
    """
    if source.stat().st_size > MAX_BYTES:
        raise ValueError("Expected a bounded self-contained MP4")
    data = source.read_bytes()
    if not 16 <= len(data) <= MAX_BYTES or data[4:8] != b"ftyp":
        raise ValueError("Expected a bounded self-contained MP4")
    options = {"protocol_whitelist": "pipe", "enable_drefs": "0", "use_absolute_path": "0"}
    with av.open(io.BytesIO(data), mode="r", format="mov", options=options) as original:
        if len(original.streams.video) != 1 or len(original.streams) > 4:
            raise ValueError("Expected one video stream and at most four streams")
        stream = original.streams.video[0]
        dropped_streams = len(original.streams) - 1
        declared_frames = stream.frames
        width, height = stream.width, stream.height
        rate = stream.average_rate
        if (
            stream.codec_context.name not in {"h264", "mpeg4"}
            or width < 16
            or height < 16
            or width > 1280
            or height > 720
            or width * height > MAX_PIXELS
            or width % 2
            or height % 2
            or rate is None
            or rate.denominator != 1
            or not 1 <= rate <= 30
        ):
            raise ValueError("Unsupported codec, size or frame rate")
        fps = rate.numerator
        if declared_frames < 1 or declared_frames > min(MAX_FRAMES, 20 * fps):
            raise ValueError("Declared frame/duration limits exceeded")
        stream.codec_context.thread_count = 1
        output, video = encoder(destination, width, height, fps)
        count, first_time = 0, None
        try:
            for index, frame in enumerate(original.decode(stream)):
                if index >= min(MAX_FRAMES, 20 * fps) or frame.is_corrupt:
                    raise ValueError("Video is corrupt or exceeds frame/duration limits")
                if frame.width != width or frame.height != height or frame.pts is None:
                    raise ValueError("Changing dimensions or missing timestamp")
                timestamp = float(frame.pts * frame.time_base)
                if first_time is None:
                    first_time = timestamp
                if abs(timestamp - first_time - index / fps) > 0.001:
                    raise ValueError(
                        "Only constant frame rate clips with continuous timestamps are supported"
                    )
                array = frame.to_ndarray(format="rgb24")
                paint(array, masks, index)
                emit(output, video, array, index, fps)
                if destination.stat().st_size > MAX_OUTPUT:
                    raise ValueError("Output exceeds 32 MiB")
                count += 1
            if count != declared_frames:
                raise ValueError("Decoded frame count differs from declared timeline")
            if count == 0 or any(mask.last >= count for mask in masks):
                raise ValueError("No frames or mask outside decoded timeline")
            finish(output, video)
        except BaseException:
            output.close()
            raise
    if destination.stat().st_size > MAX_OUTPUT:
        raise ValueError("Output exceeds 32 MiB")
    return {
        "frames": count,
        "fps": fps,
        "width": width,
        "height": height,
        "duration_ms": round(count * 1000 / fps),
        "dropped_streams": dropped_streams,
        "audio_exported": False,
        "source_metadata_copied": False,
        "bytes": destination.stat().st_size,
    }


def verify(path: Path, info: dict, masks: list[Mask]):
    """Independently decode emitted media, check stream whitelist, timing and black mask interiors.

    This checks requested masks, not missed identifiers elsewhere. Codec noise tolerance is 24/255.
    Technical encoder/MP4 metadata is permitted; user-origin text, GPS, audio and side streams are not.
    """
    with av.open(str(path), mode="r", format="mov") as media:
        if len(media.streams) != 1 or media.streams[0].type != "video":
            raise ValueError("Output contains a non-video stream")
        if set(media.metadata) - {"major_brand", "minor_version", "compatible_brands", "encoder"}:
            raise ValueError("Unexpected output metadata")
        stream = media.streams.video[0]
        if set(stream.metadata) - {"language", "handler_name", "vendor_id", "encoder"}:
            raise ValueError("Unexpected stream metadata")
        count = 0
        for index, frame in enumerate(media.decode(video=0)):
            if (
                index >= info["frames"]
                or frame.width != info["width"]
                or frame.height != info["height"]
            ):
                raise ValueError("Output frame count or size mismatch")
            if (
                frame.pts is None
                or abs(float(frame.pts * frame.time_base) - index / info["fps"]) > 0.001
            ):
                raise ValueError("Output timestamp mismatch")
            array = frame.to_ndarray(format="rgb24")
            for mask in masks:
                if mask.first <= index <= mask.last:
                    # Check the requested rectangle, excluding only the added safety margin.
                    x0, y0 = math.floor(mask.x * frame.width), math.floor(mask.y * frame.height)
                    x1 = min(frame.width, math.ceil((mask.x + mask.width) * frame.width))
                    y1 = min(frame.height, math.ceil((mask.y + mask.height) * frame.height))
                    if array[y0:y1, x0:x1].max() > 24:
                        raise ValueError("Requested redaction pixels failed output verification")
            count += 1
        if count != info["frames"]:
            raise ValueError("Output ended early")


def synthetic(path: Path, scenario: str):
    """Original 4-second moving geometry, not real people, locations or operational surveillance."""
    if scenario not in {"flood", "inspection", "training"}:
        raise ValueError("Unknown synthetic scenario")
    output, stream = encoder(path, 640, 360, 10)
    output.metadata["title"] = "PRIVATE-SYNTHETIC-SOURCE-MARKER"
    output.metadata["comment"] = "GPS=FICTIONAL; must not enter exports"
    for index in range(40):
        array = np.zeros((360, 640, 3), dtype=np.uint8)
        array[:] = {"flood": (30, 75, 105), "inspection": (61, 78, 71), "training": (57, 55, 91)}[
            scenario
        ]
        # Water/roof/road geometry plus two deliberately conspicuous sensitive test patches.
        array[205:360, :] = (45, 105, 133)
        array[40:170, 350:590] = (140, 150, 145)
        array[:, 270:325] = (95, 105, 115)
        array[65:105, 60 + index * 2 : 100 + index * 2] = (245, 191, 98)
        array[250:275, 410:500] = (245, 245, 240)
        array[257:266, 420:490:4] = (20, 20, 25)
        emit(output, stream, array, index, 10)
    finish(output, stream)


def frame_png(source: Path, destination: Path, index: int):
    """Render one authenticated preview/revision frame as metadata-free PNG for codec-limited browsers.

    The source is previously verified application-generated MP4, not a client-selected path.
    Sequential decoding avoids inaccurate keyframe seeking. No raw original is used here.
    """
    if not 0 <= index < MAX_FRAMES or source.stat().st_size > MAX_OUTPUT:
        raise ValueError("Frame outside supported bounds")
    with av.open(
        io.BytesIO(source.read_bytes()),
        format="mov",
        options={"protocol_whitelist": "pipe", "enable_drefs": "0", "use_absolute_path": "0"},
    ) as clip:
        clip.streams.video[0].codec_context.thread_count = 1
        for current, frame in enumerate(clip.decode(video=0)):
            if current == index:
                if frame.width * frame.height > MAX_PIXELS:
                    raise ValueError("Oversized review frame")
                pixels = frame.to_ndarray(format="rgb24")

                def chunk(kind, content):
                    """PNG length/type/payload/CRC, no ancillary metadata chunks."""
                    return (
                        struct.pack(">I", len(content))
                        + kind
                        + content
                        + struct.pack(">I", zlib.crc32(kind + content))
                    )

                rows = b"".join(b"\x00" + row.tobytes() for row in pixels)
                header = struct.pack(">IIBBBBB", frame.width, frame.height, 8, 2, 0, 0, 0)
                destination.write_bytes(
                    b"\x89PNG\r\n\x1a\n"
                    + chunk(b"IHDR", header)
                    + chunk(b"IDAT", zlib.compress(rows))
                    + chunk(b"IEND", b"")
                )
                return
    raise ValueError("Frame not found")
