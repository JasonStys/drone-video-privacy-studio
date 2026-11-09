# Manual keyframe mask planning validation — 2026-11-09

Jason Stys: conservative draft envelopes, actual codec/pixel verification and privacy guards.

`MotionDraft` requires two increasing single-frame, in-image rectangles with the
same human-supplied reason. `workbench/motion.py` partitions the inclusive interval
into at most32 disjoint frame chunks. Each linear rectangle edge reaches its
extremum at a chunk endpoint, so their rectangular union contains the assumed
intermediate rectangles. No extrapolation or automatic detector is used.
Time/memory are O(segments), at most32; clip timeline stays bounded at600frames.
The existing eight-pixel outward encoder margin remains unchanged.

The private owner/admin, CSRF-protected endpoint derives bounds from decoded clip
metadata, checks the exact version before/after, and writes no media, revision,
review or event. Reviewers cannot generate drafts and other operators cannot
access another owner's clip. UI applies a response only to unchanged clip/form
intent and enforces the existing combined32-mask cap. Processing and approval
remain separate explicit actions with all original gates intact.

## Observed local checks

- 97 Python tests passed, one existing OS-permission skip;96.08% branch-inclusive
  coverage, new motion module100%. Windows did not grant directory-symlink creation;
  that existing test remains enabled on capable hosts and required in Linux CI.
- 120 seeded independent Fraction interpolation cases check every frame's unique
  chunk and containment, including reverse movement, size changes and edges.
  Negative cases cover equal/reversed/multi-frame anchors, reason mismatch,
  nonfinite/out-of-image/empty geometry, invalid segments and decoded timeline.
- Actual H.264 transcode and second decode prove interpolated target-region pixels
  are dark in frames2..7 while frames0..1/8..9 and an unmasked corner stay unchanged.
  No generated envelope is used to define the target pixel oracle.
- Real private API tests prove no history mutation, owner/admin access and other
  operator/reviewer denial, CSRF/stale/bounds protection, actual concurrent
  verified processing rejection and continued export denial without review.
- 7 TypeScript tests at100% helper coverage; strict production build passed.
  All20 four-browser-engine journeys passed with real temporary services/codecs, playback or
  server-decoded PNG fallback, draft generation, real processing and WCAG checks;
  existing independent review, controlled download and logout races remain tested.
- Existing40-frame640x360 codec benchmark: three runs, median0.2248s including
  verification, output5816bytes; local throughput is not a real-time guarantee.
- Hash-locked Python advisory audit: no known vulnerabilities. Complete live OSV
  npm audit81/81 locked identities, zero findings. Lint/format/source-map/bundle
  and privacy gates remain required. Parent owns remote Actions/publication.

## Limits

Only manually assumed linear rectangle motion is modeled. Curved or nonlinear
motion, occlusion, missed identifiers, reflections, audio/context leakage and
lawfulness require human review; this is not anonymity certification. Envelopes
may over-mask useful content. No actual people, sensitive footage, aircraft,
recognition/identity data or operational surveillance was used in validation.
Originals remain private; local data trusts workstation permissions/its owner.
