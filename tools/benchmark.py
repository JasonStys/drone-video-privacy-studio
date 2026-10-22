"""Jason Stys: measured real decode/mask/encode/verify benchmark, not a real-time guarantee. Lines: docs/SOURCE_MAP.md."""

import json
import platform
import statistics
import tempfile
import time
from pathlib import Path

import av

from workbench.media import sha, synthetic, transcode, verify
from workbench.models import Mask


def main():
    """Measure three reproducible synthetic 640x360/40-frame jobs including output pixel validation."""
    root = Path(".runtime")
    root.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="benchmark-", dir=root) as directory:
        path = Path(directory)
        synthetic(path / "source.mp4", "flood")
        masks = [
            Mask(first=0, last=39, x=0.06, y=0.15, width=0.24, height=0.18, reason="face"),
            Mask(first=0, last=39, x=0.62, y=0.67, width=0.18, height=0.13, reason="plate"),
        ]
        durations = []
        for _ in range(3):
            start = time.perf_counter()
            info = transcode(path / "source.mp4", path / "result.mp4", masks)
            verify(path / "result.mp4", info, masks)
            durations.append(time.perf_counter() - start)
        report = {
            "scenario": "original synthetic flood geometry",
            "frames": 40,
            "masks": 2,
            "dimensions": "640x360",
            "repeats": 3,
            "median_seconds": round(statistics.median(durations), 4),
            "max_seconds": round(max(durations), 4),
            "median_frames_per_second_including_verify": round(
                40 / statistics.median(durations), 1
            ),
            "output_bytes": info["bytes"],
            "output_sha256": sha(path / "result.mp4"),
            "python": platform.python_version(),
            "platform": platform.platform(),
            "pyav": av.__version__,
            "native_libraries": av.library_versions,
            "real_time_guaranteed": False,
        }
        (root / "benchmark.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report))


if __name__ == "__main__":
    main()
