"""Jason Stys: single-job processing, kill deadline, integrity binding and atomic publication.

Function/variable navigation: docs/SOURCE_MAP.md. Temporary failures never publish partial media.
"""

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import threading
import uuid
from contextlib import contextmanager
from pathlib import Path

from fastapi import HTTPException

from workbench.media import MAX_BYTES
from workbench.models import Plan

ROOT = Path(__file__).resolve().parents[1]
PROCESSING = threading.BoundedSemaphore(1)


@contextmanager
def workspace(store):
    """Bound global native work to one job; delete only this generated scratch directory on exit."""
    if not PROCESSING.acquire(blocking=False):
        raise HTTPException(429, "Video processor busy; try again after the current job")
    try:
        if shutil.disk_usage(store.media).free < 256 * 1024 * 1024:
            raise HTTPException(507, "Less than 256 MiB disk space; free local storage first")
        with tempfile.TemporaryDirectory(prefix="job-", dir=store.media) as scratch:
            yield Path(scratch)
    except OSError as error:
        raise HTTPException(503, "Private media storage unavailable") from error
    finally:
        PROCESSING.release()


def run(directory, masks, scenario=None, frame=None):
    """Execute only this package's worker, no shell; kill/wait after 90 s and discard all output on error."""
    (directory / "job.json").write_text(
        json.dumps(
            {
                "masks": masks,
                "scenario": scenario,
                "action": "frame" if frame is not None else "transcode",
                "index": frame,
            }
        ),
        encoding="utf-8",
    )
    try:
        result = subprocess.run(  # noqa: S603 - fixed interpreter/module; service-generated path, no shell or client command.
            [sys.executable, "-m", "workbench.worker", str(directory)],
            cwd=ROOT,
            timeout=90,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.TimeoutExpired as error:
        raise HTTPException(
            422, "Video processing deadline exceeded; no output published"
        ) from error
    if result.returncode == 0 and frame is not None and (directory / "result.png").is_file():
        return (directory / "result.png").read_bytes()
    if result.returncode != 0 or frame is not None or not (directory / "result.json").is_file():
        raise HTTPException(
            422, "Clip unsupported, corrupt or redaction verification failed; no output published"
        )
    return json.loads((directory / "result.json").read_text(encoding="utf-8"))


def import_clip(store, user, title, purpose, retention, data=None, scenario=None):
    """Keep raw original private, publish a video-only review preview after full decode/verification."""
    if user["role"] not in {"operator", "admin"}:
        raise HTTPException(403, "Operator or admin role required")
    with workspace(store) as directory:
        store.capacity()
        if data is not None:
            (directory / "source.mp4").write_bytes(data)
        result = run(directory, [], scenario)
        identifier = uuid.uuid4().hex
        target = store.folder(identifier)
        target.mkdir()
        try:
            (directory / "source.mp4").replace(target / "source.mp4")
            (directory / "result.mp4").replace(target / "preview.mp4")
            store.insert(identifier, user, title, purpose, retention, result)
        except BaseException:
            # Only our freshly generated directory, never a caller-selected path.
            for file in target.iterdir():
                file.unlink()
            target.rmdir()
            raise
    return store.get(identifier, user)


def process(store, identifier, user, plan: Plan):
    """Recompute from unchanged original, not a lossy previous revision; CAS protects concurrent edits."""
    if user["role"] not in {"operator", "admin"}:
        raise HTTPException(403, "Operator or admin role required")
    clip = store.get(identifier, user)
    if clip["version"] != plan.expected_version or clip["version"] >= 5:
        raise HTTPException(409, "Revision changed or five-version limit reached")
    if any(mask.last >= clip["info"]["frames"] for mask in plan.masks):
        raise HTTPException(422, "Mask exceeds clip frame count")
    source = store.folder(identifier) / "source.mp4"
    if source.is_symlink() or source.resolve().parent != store.folder(identifier).resolve():
        raise HTTPException(503, "Source integrity failure")
    if (
        not source.is_file()
        or source.stat().st_size > MAX_BYTES
        or hashlib.sha256(source.read_bytes()).hexdigest() != clip["source_digest"]
    ):
        raise HTTPException(503, "Source integrity failure")
    with workspace(store) as directory:
        shutil.copyfile(source, directory / "source.mp4")
        result = run(directory, [mask.model_dump() for mask in plan.masks])

        def publish(version):
            """Rename on the same filesystem before DB commit; unreferenced files are never served."""
            (directory / "result.mp4").replace(store.folder(identifier) / f"revision-{version}.mp4")

        store.save(identifier, user, plan, result, publish)
    return store.get(identifier, user)


def render_frame(store, identifier, user, kind, version, index):
    """Authorize/hash before and recheck after decoding; return one clean PNG, no on-disk preview cache."""
    source = store.file(identifier, user, kind, version=version)
    clip = store.get(identifier, user)
    if index >= clip["info"]["frames"]:
        raise HTTPException(422, "Frame outside clip timeline")
    with workspace(store) as directory:
        shutil.copyfile(source, directory / "source.mp4")
        data = run(directory, [], frame=index)
        store.file(identifier, user, kind, record=False, version=version)
        return data
