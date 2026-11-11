"""Jason Stys: same full application or fixed private media-worker entry. Lines: docs/SOURCE_MAP.md."""

import json
import os
import sys
import time


def main():
    """Only the service's explicit one-directory worker mode avoids native owner controls; no module/command plugins."""
    worker_mode = sys.argv[1:2] == ["--media-worker"]
    if worker_mode and len(sys.argv) != 3:
        raise SystemExit(2)
    if getattr(sys, "frozen", False) and "--runtime-info" not in sys.argv[1:]:
        from workbench.codec_window import ensure

        console_setup = sys.argv[1:] == ["--install-codecs"]
        started = time.perf_counter()
        diagnostic = bool(os.environ.get("PORTABLE_SMOKE_NONCE"))
        if diagnostic:
            print('PORTFOLIO_CODEC_PHASE {"phase":"verification_start"}', flush=True)
        try:
            if not ensure(interactive=not worker_mode and "--no-window" not in sys.argv[1:], console=console_setup):
                return 0
        except (OSError, ValueError, RuntimeError, ImportError) as error:
            print(f"Video dependency setup failed: {error}", file=sys.stderr)
            return 1
        if diagnostic:
            print("PORTFOLIO_CODEC_PHASE " + json.dumps({"phase": "verification_complete", "elapsed_seconds": time.perf_counter() - started}), flush=True)
        if console_setup:
            print("Video dependency installed and verified; subsequent use is offline.", flush=True)
            return 0
    if worker_mode:
        from workbench.worker import main as worker_main

        sys.argv = [sys.argv[0], sys.argv[2]]
        worker_main()
        return 0
    from workbench.desktop import main as desktop_main

    return desktop_main()


if __name__ == "__main__":
    raise SystemExit(main())
