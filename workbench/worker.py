"""Jason Stys: private fixed-command native video subprocess; lines: docs/SOURCE_MAP.md.

No shell, path/URL from browser, network calls or plugin execution. A subprocess is crash
containment with a deadline, NOT an OS sandbox; use only trusted local operators/short clips.
"""

import json
import sys
from pathlib import Path

from workbench.media import frame_png, sha, synthetic, transcode, verify
from workbench.models import Mask


def execute(directory: Path):
    """Consume a service-owned job file and leave verified media plus bounded JSON result."""
    job = json.loads((directory / "job.json").read_text(encoding="utf-8"))
    source = directory / "source.mp4"
    if job.get("action") == "frame":
        frame_png(source, directory / "result.png", job["index"])
        return
    if job.get("scenario"):
        synthetic(source, job["scenario"])
    masks = [Mask.model_validate(value) for value in job["masks"]]
    info = transcode(source, directory / "result.mp4", masks)
    verify(directory / "result.mp4", info, masks)
    result = {
        "info": info,
        "source_digest": sha(source),
        "media_digest": sha(directory / "result.mp4"),
    }
    (directory / "result.json").write_text(json.dumps(result), encoding="utf-8")


def main():
    """The parent checks exit/deadline; never return decoder diagnostics or private input data."""
    try:
        execute(Path(sys.argv[1]))
    except Exception:
        raise SystemExit(2) from None


if __name__ == "__main__":
    main()
