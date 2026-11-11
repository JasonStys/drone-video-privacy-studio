<!-- Jason Stys: actual profile-alias reproduction, pre-mutation repair and explicit local/native evidence boundaries. -->
# Profile path admission — 11 November 2026

## Reproduced boundary

The earlier accepted source `3bf83dbf0230cd1401ac4592e91e94a9d08ea606` checked only the final directory's symbolic-link flag before creating/resolving a profile. Actual Windows directory junctions, both at the selected path and above a nonexistent child, were accepted and created identity/lock/SQLite files in an initially empty owned target. Separate inert `sys.frozen`/executable/internal-root contexts demonstrated that the same real `Profile` implementation also admitted profile creation under program directories. These were synthetic empty fixtures, not private accounts or installed-user-directory changes.

This is a practical trusted-OS-owner path-selection/alias error, not a demonstrated remote privilege escalation. No production data, live aircraft/hardware or Docker was used. Earlier 0.2.0 release bytes and results remain historical and are not overwritten by this patch.

## Repair

The 0.2.1 source adds `workbench/profile_paths.py`: inspect every existing ancestor without following aliases before mkdir; reject symbolic links and Windows reparse points/junctions; refuse frozen executable/internal trees and enclosing `.app` bundles. Inspect the marker, lock, database and journal/WAL/SHM companions before workspace mutation. Existing files must be regular and singly linked. Descriptor identity/regular-file checks precede lock writes, and missing read-only identities cannot create files. Privacy additionally refuses an aliased footage root.

The marker schema, database schema, account provisioning, HTTP roles/CSRF, cookie namespace, supported file workflows and domain calculations are unchanged. Ordinary external profiles reopen without reset or migration.

## Local validation

On patched Python 3.14.10, the complete original parent suite plus new regressions passed **276 tests**, with **94.24%** branch-aware package coverage (unchanged 90% minimum). The parent suite also mandates thirteen actual Tcl/Tk notice cases in a fresh bounded interpreter; these are reported separately, not padded into the parent total. One pre-existing Windows symbolic-link-capability skip remains explicit.

The new file contributes 16 meaningful admission cases: actual Windows final/ancestor junctions; real hardlinked marker/lock/DB/recovery members; frozen executable/internal/macOS bundle boundaries; directory/type/traversal errors; missing-read refusal; a real precreated identity replacement and descriptor closure. The original profile tests retain genuine account hashing/login, exclusive owner locking and exact database-dump persistence checks.

The 7 TypeScript helper tests and production type/build gates passed with their existing coverage requirements. Original Python lint/format, source navigation/privacy/pin checks and compiled-application acceptance remain required. The native consumer additionally invokes `tools/profile_admission_smoke.py`: the actual frozen executable must reject four real selections (program/internal/final alias/ancestor alias), return an error and leave program/empty-target files unchanged before the original full application journey proceeds. Hosted and exact-clean native results are pending for this patch until their recorded runs complete; this report does not claim them in advance.

## Actual Windows candidate checkpoint

The actual produced/extracted 0.2.1 Windows executable passed all four new refusal cases, with program files and empty alias targets unchanged, followed by the original full application browser/file/role/domain/export/Quit/persistence journey. Its source identity is explicitly **dirty local candidate**, not a clean hosted build or published-release identity. Archive SHA256: `84cadd9d1f8cf18fbe179270d180a01656dcf5d8b196235c47e9821ef52b8edf`. No installed app, real account, existing data, shortcut, older release or Docker installation was changed.

Privacy additionally passed explicit official-wheel setup followed by offline processing and independent decoding of all40 frames (640×360,10fps), moving/plate mask pixels, retained outside context, video-only output and downloaded-byte hash. All24 original source browser journeys also passed across Chromium, Firefox, WebKit and mobile WebKit (three engines/four profiles).

## Limits

The same OS account/administrator is trusted. These admission and descriptor-identity checks do not establish a race-proof namespace against concurrent same-user file replacement; SQLite still uses pathname-based connections. This is an unsigned portable application, not a signed installer, clean-OS transaction or security certification. No existing application, profile, shortcut or published archive was replaced during source validation.

## Postprocessed CodeQL test-oracle hygiene

Delayed aggregate analysis identified a permissive default mode in the new test's replacement opener and two negative paths whose descriptor would not be closed if the production refusal regressed. The test helper now defaults to 0600; each negative oracle closes any unexpectedly returned descriptor in finally and still fails explicitly. The production opener already used 0600, so this is test-fixture/error-path hygiene, not a demonstrated runtime world-writable profile. No production schema, role, permission, admission decision or native deadline changed. Fresh exact-head workflow and aggregate/SARIF postprocessing checks are required; a successful scanner job alone is not clearance.
