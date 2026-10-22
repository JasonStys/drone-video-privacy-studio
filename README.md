<!-- Jason Stys: project purpose, practical demo, privacy boundaries and full file navigation. -->
# Drone Video Privacy Studio

[![Validation](https://github.com/JasonStys/drone-video-privacy-studio/actions/workflows/validate.yml/badge.svg)](https://github.com/JasonStys/drone-video-privacy-studio/actions/workflows/validate.yml)
[![CodeQL](https://github.com/JasonStys/drone-video-privacy-studio/actions/workflows/codeql.yml/badge.svg)](https://github.com/JasonStys/drone-video-privacy-studio/actions/workflows/codeql.yml)

A working, local aerial-video review application by **Jason Stys**. Import authorized footage, minimize visible identifiers with time-bounded solid masks, inspect the actual processed video and obtain an independent review before exporting a video-only derivative. Original footage and private notes stay in an authenticated local workspace, outside the public repository and webroot.

This is a deliberately bounded privacy-engineering portfolio lab—not an identity-recognition system, anonymity certificate, live drone controller, public cloud service, legal approval or certified evidence-management product.

## What works

- **Actual video processing:** Python/PyAV decodes every frame, creates new RGB frames, applies solid rectangles with an eight-pixel margin and encodes a fresh H.264 MP4. A second decode verifies count, timing, stream/metadata allowlists and requested masked pixels. No stream-copy shortcut.
- **Precise redaction intent:** up to 32 normalized rectangles, inclusive first/last frame indices, overlapping-mask unions, private annotations and a scrub-able TypeScript review desk. Processing always starts from the original, not a degraded prior revision.
- **Restricted source access:** originals are stored privately, never served raw. Authorized staff can view a sanitized but **unredacted** review preview. Operators see only their own clips; designated reviewers/admins can read their organization's clips. This is one local organization, not multiple isolated tenants.
- **Revision-bound approval:** edits create immutable revisions and invalidate approval. A different designated reviewer must attest to full-clip and contextual inspection. Rejection, missing sign-off, stale versions, expired retention or integrity failure block exports server-side.
- **Data-minimized exports:** fresh video only, with no copied source audio, user-origin metadata, source filename, subtitles, attachments or telemetry. Downloadable minimal receipts contain the derivative hash and technical dimensions/timing—not identities, source hashes, private notes or original titles. Technical MP4/encoder fields remain.
- **Telemetry synchronization:** optional strictly ordered relative-coordinate samples, explicit offset, per-frame interpolated position and visible drift/gap warnings. No extrapolation outside coverage. Unresolved provided-timeline drift blocks approval; absent telemetry is explicitly unknown. Telemetry never enters exported media/receipts.
- **Account and retention controls:** local CLI provisioning, Argon2id passwords, hashed opaque one-hour sessions, CSRF/origin/Host checks, bounded login/body/processing concurrency, private access history, configurable 1–30-day retention, immediate expiry lockout and dry-run-first OS-owner purge.
- **Three original synthetic scenarios:** flood-response assessment, authorized infrastructure inspection and privacy-review training. Moving person-colored geometry and mock license-plate text are test targets, not real people, actual locations or operational footage.
- **Portable browser UI:** responsive desktop/mobile layout, in-app help, keyboard access, no external fonts, advertisements, analytics, model APIs or runtime cloud uploads. Built with TypeScript/HTML/CSS, Python and SQL, chosen for their actual roles rather than padding languages.

## Scope and important limits

Supported input is **self-contained MP4, one H.264/MPEG-4 video stream, integer constant 1–30 fps, even dimensions from 16×16 to 1280×720, at most 921,600 pixels, 20 seconds / 600 frames and 20 MiB**. Declared and fully decoded frame counts must agree. Fractional-rate/VFR clips, unsupported codecs, damaged/ambiguous timelines and remote URLs are rejected rather than silently retimed. Normalize longer or unsupported footage in a separately secured workflow first. Other input streams (at most four total) are not exported.

There is **no automatic face/plate detector**. A mask only protects its specified rectangle/time interval; moving subjects outside it, scenery, reflected text, clothing and other contextual identifiers can remain. Human attestations can be mistaken or dishonest. Automated pixel checks verify requested masks, not overall anonymity, completeness or legal authority. Raw original bytes (including original audio/metadata) remain private on disk until retention purge; the review preview is still sensitive.

The subprocess deadline and size/codec caps are defense in depth, **not an OS sandbox**. Untrusted codecs can contain vulnerabilities. This release is for trusted local staff using controlled short clips; do not expose it to public uploads. Runtime data is not encrypted by this application; use OS accounts, restricted directory permissions and disk encryption. The OS owner, backups and authorized organizational reviewers can access data. See [security boundaries](docs/SECURITY_MODEL.md) before using real footage.

## Run locally

Codec-limited browsers can use **frame-by-frame review**: the service renders the selected authenticated current-version frame as a fresh metadata-free PNG. The UI falls back automatically on playback failure and also offers an explicit button. Move the slider, then **Load selected frame**; no audio or persistent PNG cache is created. Continuous playback is optional; the MP4 export remains real H.264. This fallback is tested on Windows WebKit rather than skipping inspection when its video codec is unavailable.

These controls are **not DRM**: authorized reviewers/operators can save or screen-capture media they are allowed to view, including an unapproved private preview. Approval gates the designated export route; it cannot stop a permitted reader from misusing already disclosed pixels. Use trusted staff and organizational sharing controls.

Requires Python 3.12–3.14 (64-bit) and Node.js 24. Windows, Linux and macOS native wheels are validated in CI. FFmpeg is bundled in the pinned PyAV wheel; no Docker, system FFmpeg, GPU, recognition model or API key is needed. Browser H.264 decoding is required; codecs supplied by the OS/browser can vary.

```powershell
python -m venv .venv
.venv/Scripts/python -m pip install --only-binary=:all: --require-hashes -r requirements.lock
npm ci --ignore-scripts --no-audit
npm run build
.venv/Scripts/python -m workbench init
.venv/Scripts/python -m workbench user editor --role operator
.venv/Scripts/python -m workbench user second-reviewer --role reviewer
.venv/Scripts/python -m workbench serve
```

On Linux/macOS use `.venv/bin/python` instead of `.venv/Scripts/python`. Passwords are entered interactively, not in command history. Open **http://127.0.0.1:8891**. Do not bind a different interface or put this local HTTP release behind a public proxy. No default production password or public registration exists. `--db` must precede the CLI subcommand when selecting another private workspace.

For an isolated synthetic demo only:

```powershell
.venv/Scripts/python -m tools.browser_server --directory .runtime/demo --port 8891
```

Random disposable credentials are written only to `.runtime/demo/credentials.json`. Read them locally; do not publish/share that file. These are test accounts, not real user provisioning. See the [step-by-step guide](docs/USER_GUIDE.md).

## Test and validate

```powershell
.venv/Scripts/python -m pip install --only-binary=:all: --require-hashes -r requirements-dev.lock
npm ci --ignore-scripts --no-audit
npm run format:check
npm test
npm run build
.venv/Scripts/python -m ruff check workbench tests tools
.venv/Scripts/python -m ruff format --check workbench tests tools
.venv/Scripts/python -m pytest --cov=workbench --cov-report=term-missing
.venv/Scripts/python tools/docs_index.py --check
.venv/Scripts/python tools/check_repo.py
.venv/Scripts/python -m tools.benchmark
.venv/Scripts/python -m pip_audit --disable-pip --no-deps -r requirements-dev.lock
.venv/Scripts/python tools/audit_osv.py
npx playwright install --with-deps chromium firefox webkit
npm run test:e2e
```

The required live OSV check independently verifies every locked npm name/version and zero findings; `npm ci --no-audit` avoids the unreliable installation-time advisory endpoint, not vulnerability scanning. Python uses a complete hash lock and a required live audit. Neither audit suppresses findings. Advisory databases cannot guarantee absence of unknown or bundled native-library vulnerabilities.

CI tests Python 3.12/3.14 on Ubuntu plus Python 3.14 on Windows/macOS; real-service browser journeys run Chromium, Firefox, WebKit and mobile WebKit. CodeQL checks Python and JavaScript/TypeScript security-and-quality. No Actions artifact/cache uploads are configured. Evidence, measurements and disclosed limits: [validation report](docs/VALIDATION.md), [test plan](docs/TESTING.md).

## Repository navigation

| Area | Main responsibility |
| --- | --- |
| `workbench/media.py`, `worker.py` | Real bounded decoding, frame masks, fresh encoding, output verification; fixed killable worker entry. |
| `workbench/models.py` | Strict mask, annotation, telemetry, review and synchronization contracts. |
| `workbench/service.py` | One-job backpressure, deadline, scratch cleanup and verified atomic publication. |
| `workbench/store.py`, `schema.sql` | Parameterized SQLite, object authorization, revision integrity, independent approval, expiry, private history and minimal receipts. |
| `workbench/auth.py`, `api.py`, `__main__.py`, `retention.py` | Local accounts/sessions, protected routes, CLI launch/provisioning and explicit expired-media purge. |
| `ui/` | Responsive TypeScript/HTML/CSS review desk, scrubber, masks, telemetry position and help. |
| `tests/` | Real media/pixel/stream oracles, role/session/HTTP/retention/race tests and browser acceptance. |
| `tools/` | Isolated demo, measured benchmark, complete dependency audit, generated docs and source hygiene. |
| `.github/workflows/` | Immutable-reference cross-platform validation and CodeQL, without stored artifacts/caches. |

Every authored file has a responsibility in the [complete file catalog](docs/FILE_CATALOG.md). Header links lead to the [generated exact function/class/parameter/variable line map](docs/SOURCE_MAP.md); CI rejects stale maps. Also see [ADR/architecture](docs/ARCHITECTURE.md), [API](docs/API.md), [operations/retention](docs/OPERATIONS.md) and [research](docs/RESEARCH.md).

## Author and license

Made by **Jason Stys** · [GitHub portfolio](https://github.com/JasonStys) · [Contact on LinkedIn](https://www.linkedin.com/in/jason-stys-31b30b351/).

Original source is MIT licensed. PyAV and its bundled FFmpeg/codecs retain their own licenses and obligations; this repository distributes source/locks, not a repackaged native installer. See [third-party notes](docs/RESEARCH.md). No employer endorsement or regulatory certification is implied.
