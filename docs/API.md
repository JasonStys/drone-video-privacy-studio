<!-- Jason Stys: endpoint contracts, role matrix, units and explicit failure semantics. -->
# Local API

Base: `http://127.0.0.1:8891`. Exact Host required. Every POST needs exact Origin; all except login need the live session's `X-CSRF-Token`. JSON writes are <=64 KiB with a five-second read deadline. The import route uses raw `video/mp4`, <=20 MiB and a 20-second read deadline. At most two body readers and one processing job are active. Unknown JSON fields, non-finite geometry, coerced types and duplicate/out-of-order telemetry are rejected. Error responses do not reflect payload values.

| Method / path | Role | Contract |
| --- | --- | --- |
| GET `/healthz` | anonymous | Liveness/mode only. |
| POST `/api/login` | anonymous | `{username,password}`; returns `{name,role,csrf}` and HttpOnly opaque cookie. |
| GET `/api/me` | signed in | Current server-resolved user/role/CSRF. |
| POST `/api/logout` | signed in | `{}`; revoke this session immediately and clear cookie. |
| GET `/api/clips` | signed in | Scoped active clip summaries, <=40 returned (capacity 12). |
| POST `/api/clips/import?title=...&purpose=...&retention=7` | operator/admin | Raw supported MP4; title 3–80 chars, purpose 10–300 chars, retention 1–30 days. No filename/URL field. Returns verified preview + private record. |
| POST `/api/examples/{flood,inspection,training}` | operator/admin | `{}`; generate original synthetic video through real worker. |
| GET `/api/clips/{id}` | authorized reader | Current private metadata/revision/plan/review/alignment. |
| GET `/api/clips/{id}/history` | authorized reader | <=5 revision hashes and <=100 latest private media/state events. |
| POST `/api/clips/{id}/process` | owner operator or admin | `Plan` below; creates verified next revision, no inherited approval. |
| POST `/api/clips/{id}/review` | independent reviewer | Exact version, approve/reject, explicit full-clip/context booleans, note 10–500 chars. |
| GET `/api/clips/{id}/media/{preview,redacted,export}?version=N` | authorized reader | Hash-checked current-version MP4; ranges supported. Preview remains sensitive. Export additionally requires current approval and attachment filename is generated. |
| GET `/api/clips/{id}/manifest` | authorized reader | Approved minimal downloadable receipt, no private title, user, notes, telemetry or source hash. |

Operators see only their own clip IDs. Reviewers/admins are organization-wide readers. Only operator/admin can import/process; only reviewer can review; neither source creator nor revision author can review their own clip even if their account role changes. Inaccessible/missing object returns 404, expired 410. Admin is not a review bypass. Original bytes have **no HTTP endpoint**.

## Plan example

GET `/api/clips/{id}/frame/{preview,redacted}?version=N&index=K` returns a clean `image/png` for codec-independent inspection. It has the same object/version/expiry checks as the corresponding private media, uses the single native job gate and rechecks current version after rendering. Frame index must be 0–599 and within the decoded timeline. No raw original is used, no cached PNG remains, and there is no anonymous frame route. Access is recorded as the corresponding preview/redacted media access.

```json
{
  "expected_version": 0,
  "masks": [
    {"first": 0, "last": 39, "x": 0.06, "y": 0.15, "width": 0.24, "height": 0.18, "reason": "face"}
  ],
  "note": "Check the full moving synthetic patch and contextual identifiers",
  "telemetry": [],
  "offset_ms": 0
}
```

Up to 32 masks; indices 0–599 within actual decoded count, inclusive endpoints. Rectangle is half-open in normalized pixel geometry; round outward and add eight pixels on all sides, clamped to image. Mask reason enum: face/plate/sensitive/other (review annotations, not learned recognition). Note <=500 chars. `expected_version` is the current version, zero before first processing; at most five revisions. A stale value is 409.

Optional <=600 samples: `{ms: 0..20000, east_m: -10000..10000, north_m: -10000..10000, altitude_m: 0..500}`, strictly increasing ms. Offset -5000..5000 ms is added to sample time. First/last must align within 250 ms to first/last frame timestamp; adjacent sample gaps >1000 ms warn and block approval. Position is relative and interpolated only inside coverage, never a live navigation measurement. Empty telemetry reports `absent`, not invented coordinates.

## Review example

```json
{"expected_version":1,"decision":"approve","full_clip_checked":true,"context_checked":true,"note":"Checked every synthetic frame and authorized sharing context"}
```

Rejection does not require the two approval confirmations but never permits export. Duplicate review is 409; rejected revision requires a new processed revision, not overwriting history. Approval is a human attestation, not an algorithmic guarantee.

Errors: 400 Host; 401 session; 403 role/origin/CSRF/self-review; 404 object; 405 method; 408 body deadline; 409 state/capacity; 410 expiry; 413 size; 415 content type; 422 validation/codec/deadline/pixel verification; 429 login/body/worker backpressure; 503 storage/integrity; 507 low disk. Details remain deliberately generic for native parser failures to avoid leaking private decoder diagnostics.
