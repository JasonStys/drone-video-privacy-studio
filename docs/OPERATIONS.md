<!-- Jason Stys: local setup, retention, backup/recovery, diagnostics and release/rollback runbook. -->
# Operations and release runbook

## Install and launch

Use the exact README setup with 64-bit Python 3.12–3.14 and Node 24. Hash-locked `--only-binary=:all:` install refuses an unexpected source/native build; do not remove locks to bypass a missing wheel. Build UI once, initialize a private path, provision accounts interactively, then run loopback only. CLI flag order is `python -m workbench --db PRIVATE_PATH command`. Do not store runtime under a public/synced folder. Apply OS access controls/disk encryption and back up privately.

No installer, public host, app store signing, new cloud account, scheduled deletion or external AI/detection service is included. The browser application works with the local Python service; it does not run its decoder on a remote device without an explicitly reviewed hosting design. A responsive mobile UI is tested against the local service, not evidence of a shipped Android/iOS native binary.

## Retention and capacity

Retention is immutable at import (1–30 days); it cannot be extended silently in the UI. Expired clips disappear from the active library and all API reads/process/review/export deny access. Expiry is **logical denial**, not automatic disk deletion. Up to 12 retained clips, including expired clips; five revisions each. File output cap 32 MiB is enforced during/after encoding; native buffers can transiently exceed the threshold before abort. Original cap 20 MiB. Keep room for scratch and backups; a >=256 MiB free-space precheck is not a disk quota or a guarantee against concurrent external disk consumption.

After following any organizational hold obligations, stop the service and run:

```powershell
.venv/Scripts/python -m workbench purge-expired
.venv/Scripts/python -m workbench purge-expired --confirm
```

First command only reports expired count/bytes. Second removes only files inside generated expired clip folders, after validating **all** target folders and allowed names and refusing symlinks/unexpected/nested files. It then removes expired clip/revision/review rows; minimal audit events remain. It does not delete active media, arbitrary directories, users, sessions, backups or downloads. Do not run concurrent service instances. Deleted local media is recoverable only from a separately retained backup; it is not moved to trash or securely erased. Never purge a real workspace merely to test this command; tests use disposable directories.

## Backup, restore and interruption

If browser H.264 support is absent, use the included frame-by-frame review path. It sequentially decodes a selected current-version preview/revision frame in the same deadline-limited native worker, returns a clean PNG and discards scratch. It is not continuous video streaming, and rapid parallel frame requests deliberately receive backpressure. The UI disables heavy actions while its frame request is pending.

Stop the service, take a consistent private copy of the SQLite file and sibling `media` directory, encrypt/protect it and apply a separate retention policy. Never attach it to GitHub. To restore, stop service, restore the matched pair to a private directory and use `--db`. This is a source-reproducible lab, not an online backup system; rehearse with synthetic accounts before real data.

Ordinary worker rejection/crash/deadline removes scratch and publishes no revision. Parent force-kill or power loss can leave private `media/job-*` scratch or unreferenced revision files. Stop the app, back up privately, inspect the exact app-generated folder and DB reference before removal; there is intentionally no broad startup cleanup. If files have unexpected links/content, investigate instead of broad recursive delete. A renamed orphan not referenced by SQLite is never served by the API.

## Diagnosis

- Reproduce with a new synthetic exercise. If it also fails, check pinned Python/PyAV wheels, available disk and ignored job state; do not loosen pixel/approval guards.
- 422 may indicate unsupported VFR/fractional fps, dimensions, multiple video streams, corrupt/truncated decode, out-of-timeline masks, output size or deadline. The HTTP service intentionally hides raw decoder diagnostics. Use an isolated disposable worker invocation with **synthetic non-sensitive data** for developer diagnosis.
- 503 hash mismatch means stop using that workspace. Compare an approved backup; do not rewrite stored hashes to make tampered data appear valid.
- 409 means refresh or resolve an explicit constraint. Reprocessing invalidates approval; it cannot be restored by selecting an old download URL.
- Login failures share a one-minute direct-client budget. `proxy_headers=False` is required, including loopback. Spoofed forwarding headers must not generate a new client identity.
- Browser H.264 decode varies by OS build. Inspect a synthetic clip with a supported updated browser. Do not confuse a browser codec problem with native test failure.

## Release checklist / rollback

Before publishing: clean source-only Git diff; no runtime/credentials/media; complete docs/source maps; strict TS build, formatter/linter, Python >=90% branch-aware package gate, presentation-helper 100% gate, real video pixel/stream/timing tests, actual-service browser/accessibility/race tests, live complete dependency audits, platform matrix and both CodeQL languages. Confirm exact pushed head, not a stale green run. Check Actions storage; no artifact/cache uploads here. Never delete prior runs/caches without fresh user approval.

No schema migration is introduced in 0.1.0. Stop service and retain a private consistent backup before future schema changes. If a source release regresses, check out the last known-green commit and rebuild its locked environment/UI against a compatible backed-up schema; do not blindly replace a live database. Block a release for any failed gate, export leak, stale-review bypass, privacy-boundary regression or missing native platform validation. A green portfolio CI is not production accreditation.
