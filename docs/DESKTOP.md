<!-- Jason Stys: full native staff-workspace setup, supported media workflow, shutdown and packaging limits. -->
# Desktop application candidate

Version 0.2.1 packages the existing authenticated video review application. The
native owner window starts a private local service and opens the same browser UI;
it does not create a second demonstration product. No public binary has been
approved by this candidate report. The download excludes PyAV/FFmpeg codecs;
explicit first-run setup acquires an exact upstream wheel as described in
[dependency distribution](MULTIMEDIA_DISTRIBUTION.md).

## Open a private workspace

After obtaining an independently verified, approved release, extract the entire
portable archive into a new program directory. Run `DroneVideoPrivacyStudio.exe`
on Windows, or `DroneVideoPrivacyStudio` on its matching supported platform. These
are portable archives, not signed installers or OS package transactions.

1. On first launch, review the native video-dependency setup screen: it shows the
   exact official provider, file, byte length, SHA256, ABI and terms. **Cancel**
   performs no fetch and opens no workspace. **Install verified video dependency**
   makes the displayed bounded request; wait for completion. Failed setup stays
   visible and requires Quit/reopen. Later launches verify the installed wheel
   offline. First install requires provider/TLS connectivity.
2. Choose a new empty private workspace or this application's existing identified
   workspace. The default uses the current OS user's local application-data
   directory, outside the extracted program. Unknown nonempty folders and linked
   paths are refused; do not substitute another application's data directory.
3. Open the workspace. If it is new, create its first administrator by entering a
   username and a confirmed password in the native owner window. There is no
   preset password. This trusted computer-owner action is not a web signup route.
4. Provision separate operator and reviewer accounts as needed. The computer owner
   can provision staff; the browser's original role checks remain in effect.
5. Choose **Open full application** and sign in with the appropriate staff account.
   The process uses its own ephemeral loopback port, not an existing local server.

The computer owner, OS administrators and backups can access local data. This is
not encryption against the owner or tenant isolation. Protect the workspace with
OS permissions and disk encryption; keep it outside public/synced folders.

## Use the complete review desk

An operator imports a supported, authorized short MP4 and supplies its purpose and
retention. The [README limits](../README.md#scope-and-important-limits) apply to
every upload. Configure manual rectangles and inclusive frame intervals, or use
the moving-mask helper to prepare conservative envelopes. Those envelopes assume
linear motion; they are not detection or tracking of people.

Process a revision, inspect the actual video or choose **Use frame-by-frame
review**, then inspect selected decoded PNG frames. An export is blocked until a
different designated reviewer signs off the current revision after full-clip and
context review. Changing the plan invalidates prior approval. Download the fresh
video and minimal receipt only after that server-side review gate passes. Original
audio/metadata and private review fields are not copied to those exports; pixel
content outside chosen masks may still identify people or places.

## Quit and reopen

Use **Quit application** in the owner window. Closing its title-bar window uses
the same completion-based shutdown. Closing a browser tab alone leaves the owned
service running. During a slow operation, the owner window keeps its workspace
lock and reports that shutdown is still pending; it does not forcibly discard
work or silently start a second instance. A startup failure requires quitting
the owner window and reopening after correcting the displayed cause.

For a pre-provisioned test workspace, `--profile PATH --no-window --no-browser`
starts the same service without opening a browser. Enter `quit`, send EOF or use
Ctrl+C in that console to request normal shutdown. This mode cannot create
accounts or accept passwords in command arguments. It is an acceptance/automation
path, not a substitute for the normal owner window.

That mode and the media worker require an already verified dependency and never
download implicitly. An optional `--install-codecs` console setup displays the
same provider/identity/terms and requires the literal `INSTALL` response before
calling the same installer. It accepts no passwords or footage and does not open
a workspace. The trusted-owner `DVP_DEPENDENCY_HOME` override selects a separate
dependency store for isolated acceptance; it does not select or reset a profile.

Reopening the same identified workspace preserves its accounts and review records.
Do not delete its marker, account database or lock to force another instance.
Use the existing retention/purge workflow rather than manually deleting evidence.

## Build and validate

Use final Python 3.14.10 or a later reviewed 3.14 security patch for native builds,
Node 24 and the exact committed locks. From a clean reviewed checkout:

```text
python -m pip install --require-hashes -r requirements-dev.lock -r requirements-package.lock
npm ci --ignore-scripts
npm run build
python tools/package_app.py --output-root .runtime/portable-UNIQUE
```

Linux runs the packaging command under `xvfb-run -a` so the actual Tcl/Tk owner
controls and notices are tested. Install the exact locked Chromium build and its
OS dependencies before acceptance; no source-server/browser fallback exists.
Hosted builds reject dirty checkouts and mismatched Git identities. A local
`--allow-dirty` build labels itself as such and cannot become exact-source proof.

The packager first runs the mandatory 13 genuine Tcl notice cases in one fresh
bounded interpreter, then collects actual loaded GUI/runtime notices, freezes
the program, creates the native archive, safely extracts it and exercises that
executable. Acceptance uses only generated footage and a new private test profile,
clears developer runtimes from the child's PATH and verifies inner/outer source
identity, the real GUI, role separation, MP4/receipt exports and normal owner Quit.
A first explicit console dependency setup is recorded separately from the later
offline application journey. Freezer module/file inventories must prove the
download contains no PyAV/av.libs or codec payload. The exact upstream wheel is
fetched into the isolated test store, never an existing user's dependency store.
A separate decoder checks all 40 output frames, mask pixels, stream count and
receipt hash. A checksum is emitted only after every required check passes.

The three-platform workflow validates native archives; it neither publishes a
release nor uploads binaries, footage, screenshots, accounts or caches to Actions.
The isolated Tcl test records its 13 cases separately from the parent pytest
count. No test retries, coverage exclusions or lowered original gates were added.

Automated evidence includes actual source-level Tk controls, the frozen GUI
runtime diagnostic and real browser interaction against the extracted executable.
It does not claim a manually clicked native owner window, a clean OS install,
code signing, an OS sandbox or a successful full upstream codec rebuild.

## Profile path admission

Choose an ordinary physical directory outside the extracted application. Existing ancestors must be real directories: symbolic links and Windows reparse points (including junctions) are refused. The identity, owner lock, SQLite database and any journal/WAL/SHM companions must be regular singly linked files; an unsafe member is refused before opening/writing the workspace. The frozen executable/internal directories and enclosing macOS .app bundle are never data locations. Privacy footage also requires a real media root. Ordinary existing identified profiles need no migration/reset; their accounts, roles and cookie namespace remain compatible.

These are pre-mutation guards for accidental/trusted-owner path mistakes. The same OS account and administrators remain trusted; SQLite/pathname APIs do not provide an atomic namespace against a concurrent same-OS-user replacing entries after admission. Stop normally and retain the entire external profile. [Dated reproduction and validation](reports/PROFILE_PATH_ADMISSION_20261111.md).
