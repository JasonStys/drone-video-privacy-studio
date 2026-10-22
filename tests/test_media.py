"""Jason Stys: real codec, frame-boundary, audio/metadata minimization and failure oracles; lines: docs/SOURCE_MAP.md."""

from fractions import Fraction

import av
import numpy as np
import pytest

from workbench import media
from workbench.models import Mask


def custom(
    path, frames=4, fps=10, width=160, height=96, codec="libx264", irregular=False, audio=False
):
    """Independent codec fixture with optional AAC audio and private container/stream metadata."""
    with av.open(str(path), "w", format="mp4") as container:
        container.metadata["title"] = "private-source-title"
        container.metadata["comment"] = "private-location-marker"
        stream = container.add_stream(codec, rate=fps)
        stream.width, stream.height, stream.pix_fmt = width, height, "yuv420p"
        stream.metadata["title"] = "private-stream-title"
        if audio:
            sound = container.add_stream("aac", rate=48000)
            sound.layout = "mono"
        for index in range(frames):
            frame = av.VideoFrame.from_ndarray(
                np.full((height, width, 3), 230, dtype=np.uint8), format="rgb24"
            )
            frame.pts = index if not irregular or index == 0 else index + 1
            frame.time_base = Fraction(1, fps)
            for packet in stream.encode(frame):
                container.mux(packet)
        for packet in stream.encode():
            container.mux(packet)
        if audio:
            frame = av.AudioFrame.from_ndarray(
                np.zeros((1, 4800), dtype=np.float32), format="fltp", layout="mono"
            )
            frame.sample_rate, frame.pts, frame.time_base = 48000, 0, Fraction(1, 48000)
            for packet in sound.encode(frame):
                container.mux(packet)
            for packet in sound.encode():
                container.mux(packet)


def test_inclusive_boundaries_rounding_and_overlap(tmp_path):
    """Frames 1 and 2 masked, 0 and 3 unchanged; no off-by-one leak at either endpoint."""
    source, destination = tmp_path / "source.mp4", tmp_path / "out.mp4"
    custom(source)
    masks = [Mask(first=1, last=2, x=0.1, y=0.1, width=0.3, height=0.3, reason="plate")]
    info = media.transcode(source, destination, masks)
    media.verify(destination, info, masks)
    with av.open(str(destination)) as result:
        frames = [f.to_ndarray(format="rgb24") for f in result.decode(video=0)]
    assert frames[0][15:30, 20:50].min() > 150
    assert frames[1][15:30, 20:50].max() <= 24
    assert frames[2][15:30, 20:50].max() <= 24
    assert frames[3][15:30, 20:50].min() > 150
    assert media.rectangle(masks[0], 160, 96) == (8, 1, 72, 47)
    all_mask = Mask(first=0, last=0, x=0, y=0, width=1, height=1, reason="other")
    assert media.rectangle(all_mask, 160, 96) == (0, 0, 160, 96)
    pixels = np.full((96, 160, 3), 255, dtype=np.uint8)
    media.paint(pixels, masks + [all_mask], 0)
    assert pixels.max() == 0


def test_audio_and_source_text_removed_but_not_claimed_anonymous(tmp_path):
    """Fresh output contains exactly one video stream and no user-origin metadata markers."""
    source, destination = tmp_path / "source.mp4", tmp_path / "out.mp4"
    custom(source, audio=True)
    with av.open(str(source)) as original:
        assert len(original.streams.audio) == 1
    info = media.transcode(source, destination, [])
    media.verify(destination, info, [])
    assert info["dropped_streams"] == 1 and info["audio_exported"] is False
    assert b"private-source-title" not in destination.read_bytes()
    assert b"private-location-marker" not in destination.read_bytes()
    assert b"private-stream-title" not in destination.read_bytes()


@pytest.mark.parametrize("data", [b"", b"not-a-video" * 10, b"\x00\x00\x00\x20ftyp" + b"x" * 50])
def test_invalid_and_truncated_mp4_fails(tmp_path, data):
    """File signature never substitutes for actual complete decoding."""
    source = tmp_path / "source.mp4"
    source.write_bytes(data)
    with pytest.raises((ValueError, av.error.FFmpegError)):
        media.transcode(source, tmp_path / "out.mp4", [])


def test_bounds_outside_masks_and_output_verifier(tmp_path, monkeypatch):
    """Decoded bounds, input/output byte caps and verification inconsistencies fail visibly."""
    source, destination = tmp_path / "source.mp4", tmp_path / "out.mp4"
    custom(source)
    with pytest.raises(ValueError, match="mask outside"):
        media.transcode(
            source,
            destination,
            [Mask(first=0, last=4, x=0, y=0, width=1, height=1, reason="other")],
        )
    info = media.transcode(source, destination, [])
    with pytest.raises(ValueError, match="redaction pixels"):
        media.verify(
            destination, info, [Mask(first=0, last=0, x=0, y=0, width=1, height=1, reason="other")]
        )
    with pytest.raises(ValueError, match="ended early"):
        media.verify(destination, {**info, "frames": 5}, [])
    with pytest.raises(ValueError, match="size mismatch"):
        media.verify(destination, {**info, "width": 100}, [])
    with pytest.raises(ValueError, match="timestamp mismatch"):
        media.verify(destination, {**info, "fps": 5}, [])
    monkeypatch.setattr(media, "MAX_OUTPUT", 1)
    with pytest.raises(ValueError, match="32 MiB"):
        media.transcode(source, destination, [])
    monkeypatch.setattr(media, "MAX_BYTES", 1)
    with pytest.raises(ValueError, match="bounded"):
        media.transcode(source, destination, [])


def test_unsupported_frame_rate_size_and_frame_budget(tmp_path, monkeypatch):
    """High fps/oversized frames and too many decoded frames are not silently downsampled."""
    source, destination = tmp_path / "source.mp4", tmp_path / "out.mp4"
    custom(source, fps=60)
    with pytest.raises(ValueError, match="Unsupported"):
        media.transcode(source, destination, [])
    custom(source)
    monkeypatch.setattr(media, "MAX_PIXELS", 1)
    with pytest.raises(ValueError, match="Unsupported"):
        media.transcode(source, destination, [])
    monkeypatch.setattr(media, "MAX_PIXELS", 1280 * 720)
    monkeypatch.setattr(media, "MAX_FRAMES", 2)
    with pytest.raises(ValueError, match="frame/duration"):
        media.transcode(source, destination, [])


def test_variable_frame_rate_and_video_only_verifier(tmp_path):
    """Irregular PTS and unexpected source metadata/audio cannot become approved derivative output."""
    source, destination = tmp_path / "source.mp4", tmp_path / "out.mp4"
    custom(source, irregular=True)
    with pytest.raises(ValueError):
        media.transcode(source, destination, [])
    custom(source, audio=True)
    with pytest.raises(ValueError, match="non-video stream"):
        media.verify(source, {"frames": 4, "width": 160, "height": 96, "fps": 10}, [])
    custom(source)
    with pytest.raises(ValueError, match="metadata"):
        media.verify(source, {"frames": 4, "width": 160, "height": 96, "fps": 10}, [])


@pytest.mark.parametrize("scenario", ["flood", "inspection", "training"])
def test_all_original_examples(tmp_path, scenario):
    """Every advertised example is encoded, decoded and verified, not mock fixture JSON."""
    source, destination = tmp_path / "source.mp4", tmp_path / "out.mp4"
    media.synthetic(source, scenario)
    info = media.transcode(source, destination, [])
    media.verify(destination, info, [])
    assert info["frames"] == 40 and info["fps"] == 10
    assert len(media.sha(destination)) == 64
    with pytest.raises(ValueError):
        media.synthetic(source, "unknown")
