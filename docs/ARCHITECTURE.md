<!-- Jason Stys: architecture and accepted ADR for the local processing/review boundary. -->
# Architecture / ADR-001

Status: accepted for the bounded local portfolio release. Author: Jason Stys.

## Requirements and flow

Authorized staff need to review short recorded aerial clips without leaking originals or mistaking a mask overlay for processed video. A new edit must not inherit an old approval. Reviewers need exact time/geometry intent, private notes and a reproducible revision trail. Exports must minimize audio, metadata and unrelated organizational information.

```text
Browser (TypeScript, no third parties)
  -> exact-origin API + session/CSRF/object authorization
  -> single processing gate -> generated private scratch job
  -> fixed Python/PyAV worker [90-second kill deadline]
       decode -> RGB mask -> new H.264 stream -> independent decode/verify
  -> same-filesystem media rename + SQLite revision CAS
  -> independent current-revision reviewer
  -> reauthorized hash-checked video-only download / minimal receipt
```

SQL is the authority for identity, role, clip ownership, version, approval and expiry; frontend visibility is not authorization. Source and derived media live beside, not inside, the served build. The app has no network media fetcher or plugin loader.

## Decision and alternatives

Use Python for bounded media orchestration and NumPy pixel arrays, PyAV's FFmpeg bindings for actual native codecs, TypeScript/HTML/CSS for a small responsive UI, and SQLite for transactional local state. No custom C++/Rust wrapper is justified without benchmark evidence: codec work already runs natively, while extra FFI would expand attack/build surface. ONNX/OpenCV recognition is intentionally not included: no calibrated detector or representative privacy dataset has been validated.

Reject arbitrary formats, fractional/VFR timing and long clips rather than promise unsafe universal support. Fixed frame indices remove timing ambiguity from redaction. Preview is freshly transcoded without side streams but remains unredacted and restricted. Raw original is never an HTTP route.

Fresh RGB frames drop original frame metadata/side data; fresh muxing drops other streams. Encode H.264/yuv420p baseline for browser compatibility. Add eight pixels to masks against boundary codec bleed; independently decode and require requested region pixels <=24/255 in every applicable frame. This verifies application intent, not scene anonymity. Some technical encoder/container metadata is necessarily allowed.

One local process and one native job at a time simplify capacity/CAS and recovery. A subprocess contains ordinary crashes and permits a kill deadline, not hostile native code. No public multi-worker deployment is supported. A production untrusted-upload service would need OS-level network/CPU/memory isolation, a durable job queue, scoped service identities, private object storage and a dedicated native dependency/CVE program.

## Transactions and recovery

All writes use `BEGIN IMMEDIATE`; plan and revision records are immutable after insertion. Expensive work happens outside the transaction, followed by a version/source-hash compare-and-swap. A new version has no review. Review hashes the exact current media, then rechecks version inside a write transaction. Media routes require an expected version; receipt generation also checks the same snapshot. Files renamed before a failed DB commit are unreferenced and inaccessible, not automatically trusted.

Scratch contexts remove ordinary failed jobs. A force-killed service or power loss can leave `job-*` directories/unreferenced revision files; there is no startup deletion of arbitrary data. Stop the service and inspect those under the private application root per the runbook. Only expired clip IDs receive explicit purge. Filesystem and SQLite commits are not one atomic distributed transaction.

## Complexity and budgets

Decode/encode cost dominates: O(F×(W×H + M)); requested-pixel verification adds O(sum of covered mask areas over frames). RGB memory is O(W×H); input bytes are bounded at 20 MiB. Hashing is O(file bytes), with source <=20 MiB and output <=32 MiB. At most two request bodies are buffered; one job processes concurrently; at most 12 clips and five revisions per clip (roughly 2.5 GiB worst-case retained media, plus scratch/database/audit). These are bounds, not claims of constant memory inside native parsers or hard real-time guarantees. SQLite indices support scoped history; returned clips <=40, revisions <=5, events <=100. Audit persists locally until an OS-owner policy archives it; there is no unbounded public unauthenticated event writer.

Consequences: bounded useful demo with transparent limits; no streaming aircraft integration, identity inference, full-motion automatic tracking, signed installer, cloud tenancy, encryption-at-rest inside the app or forensic chain-of-custody certification.
