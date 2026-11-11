# Installed Windows 0.2.1 validation — 11 November 2026

By Jason Stys. This report describes the independently downloaded and installed **0.2.1** application from `7062adeee5f7c2476086b0143b31c156941fa06f`. Earlier Office editions and releases remain unchanged.

## Actual workflows and results

**Original installed workflow: Passed.** Actual import, moving-mask processing, independent review, metadata-minimized export and negative cases passed. Installed resources stayed unchanged.

**Same-profile upgrade: Passed.** Actual 0.2.0 to 0.2.1 retained revisions, media, reviews and every original audit event across three roles. New read/export events appended; both exits were normal.

**Distribution and security: Passed.** Both provider-hash-verified downloads, all 163 installed file hashes, current main workflows and two processed raw CodeQL analyses passed.

**Local boundary: Verified.** Only synthetic media/accounts were used. Desktop/Start-menu targets were verified; ordinary profile activation and clean-machine installation are separate untested scopes.

## Illustrated use and implementation

The [four-page guide](windows-application-guide-0.2.1.docx) contains actual installed screenshots, a worked user journey, immutable code and operating limits. The [review manifest](windows-application-guide-0.2.1.json) binds exact images, source, document and individually reviewed pages.

## Installation, accounts and limits

Verify the 0.2.1 ZIP and checksum, extract it completely and launch DroneVideoPrivacyStudio.exe. First-run consent installs one verified official PyAV wheel; later use rechecks and reuses it offline.

The app archive contains no PyAV/FFmpeg. Keep its companion notices, older version and stopped-profile backup. Help documents supported formats, roles, retention and export behavior. Local Docker is unchanged.

Use authorized media only. Region masks, video-only output and metadata minimization do not guarantee anonymity; audio and unsupported streams are excluded. No identity recognition, live surveillance or aircraft control is present.

The local OS owner can access stored files; app roles do not isolate records from that owner. Codec notices are not legal/patent clearance. The older 0.2.0 draft remains unpublished.

Individual Desktop and Start-menu targets were read-back verified. Actual installed executable acceptance is distinct from ordinary default-profile icon activation, which was not independently exercised. Only synthetic profiles/media were used. Existing ordinary accounts and Docker were not changed. This documentation commit still requires its own full hosted tests and processed security analysis.
