<!-- Jason Stys: measured validation evidence and honest remaining release checks. -->
# Validation evidence

Validated locally on 2026-10-21 (Windows 11, Python 3.14.6, Node 24.18.1). GitHub native platform and CodeQL checks are pending initial publication; they will be recorded after actual completion. No pending check is represented as passed.

| Gate | Measured local result |
| --- | --- |
| Python real media/API/SQL/auth/network/CLI/retention | **81 passed, 1 explicit capability skip**; **95.83%** branch-aware application coverage (required >=90%). Symlink creation is unavailable to this Windows account; Linux/macOS CI exercises the test. |
| TypeScript presentation helpers | **6 passed**, **100%** statements/branches/functions/lines in the helper module. Not a claim of complete UI coverage. |
| Real-service browser journeys | **16 passed**, four per engine: Chromium, Firefox, WebKit and mobile WebKit, zero retries. Includes actual processed pixels, PNG fallback/frame-20 decode, upload, independent approval, export/receipt, new-revision invalidation, private logout race, responsive layout and automated WCAG checks. |
| Supply chain | Live pip audit: zero known findings. Checksum-pinned OSV 2.7.0: all **81/81** locked npm identities scanned, zero findings, no suppression. Bundled FFmpeg/codecs are not fully audited by these package advisory checks. |
| Build / lint / formatting / docs / hygiene | Strict TypeScript, Ruff, Prettier, generated navigation and binary/private-media-free source checks passed. JS approximately **4.2 KB gzip**, CSS **1.9 KB gzip**, within 40 KB/12 KB budgets. |
| Manual visual review | Authenticated synthetic flood clip created, two masks processed, both black regions visibly inspected, revision shown as requiring independent review; exports remain gated. Author/contact/help visible. Screenshot kept outside the source tree. |

## Measured processing benchmark

Three repeats on original synthetic 640×360, 40 frames at 10 fps with two full-clip masks. **Median 0.0987 seconds**, maximum 0.1001 seconds for native decode/mask/encode plus independent output verification; output 5,816 bytes. Approximately 405.2 decoded/verified frames/second for this tiny controlled fixture. This excludes worker startup, HTTP/database/browser costs and cannot be extrapolated to real footage, maximum dimensions or hard real-time operation. PyAV 19.0.2 wheel reported libavcodec/libavformat 63.1.102, libavutil 61.1.102. CI prints its own platform/native-library inventory and measurements.

## Reproduced problems corrected before publication

- PyAV 19's `AVRational` does not accept `int(rate)` as older APIs did: read the validated integer numerator. Real frame decoding/encoding and cross-platform CI guard compatibility.
- Container stream state is cleared on close: capture original dropped-stream count while open, rather than report an incorrect negative value.
- Windows WebKit cannot decode H.264 in this environment: add authenticated actual-frame PNG rendering with explicit/automatic fallback, same role/version/expiry checks and no PNG cache. Do not skip pixel review or fake a preview.
- Native frame rendering races an immediate next process request: disable heavy UI actions while its real frame request is pending, preserving server backpressure.
- Four engines sharing one direct-client login budget legitimately hit the 20/minute limiter: isolate each suite's real database/service, without changing production limits or adding retries. The real TCP spoofed-forwarding regression still checks the twenty-first attempt is denied.
- Browser label lookups were overly exact about wrapped select text: use role/name locators against the actual accessible controls.

Visible development-tool notices include the upstream Starlette/httpx TestClient deprecation and npm availability/NO_COLOR notices. They are not suppressed or mislabeled as application errors; they do not make a failed test pass.

Required gates and limitations are in [TESTING.md](TESTING.md). Current status is also visible in the [Validation workflow](https://github.com/JasonStys/drone-video-privacy-studio/actions/workflows/validate.yml) and [CodeQL](https://github.com/JasonStys/drone-video-privacy-studio/actions/workflows/codeql.yml). Only a successful run on the exact pushed head establishes final CI completion.
