<!-- Jason Stys: explicit official-wheel acquisition, codec-free download boundary and honest upstream obligations. -->
# Native video dependency setup and distribution scope

The application download contains the authored application, patched Python and
its non-codec runtime dependencies with their original notices. It **excludes
PyAV, av.libs and FFmpeg/codec binaries**. Before opening any workspace or footage,
a first-run native setup window shows the exact provider, version, URL, byte
length, ABI, SHA256 and terms. The user can Install or Cancel. Merely displaying
the window makes no network request.

This is a technical distribution design, not legal clearance, upstream relicensing
or a codec-patent license. Original application source remains MIT. The user
acquires the official upstream wheel directly from PyPI's file provider; our
repository/release does not republish that codec payload. PyAV and its bundled
native libraries retain their own original terms and notices.

## Exact supported wheel identities

The resource `workbench/resources/pyav-wheels.json` pins PyAV 19.0.2. These
`cp312-abi3` wheels support standard CPython 3.14. Free-threaded Python, other CPUs,
older OS/ABI families and arbitrary wheels have no fallback.

| Native platform | Bytes | SHA256 |
| --- | ---: | --- |
| Windows x64 | 28,150,949 | `3ce5a1d7b916d13c16ac58f1756f0fee4af2d53f02bc1403e18550b50d375a22` |
| Linux x86_64, glibc 2.28+ | 34,990,159 | `9c1da7aad0fa6c13b4a5c1e7985be0d13f8526a96284573acaf3d55ead6d3fe8` |
| macOS 14+, Apple Silicon | 18,556,422 | `b0dff6dfcc6ff9944fbbff15bc4ee2d90a2c1695d493bdea96e86f48823e9feb` |

[Official versioned metadata](https://pypi.org/pypi/av/19.0.2/json) supplies those
exact file URLs, lengths and hashes; they also occur in the source lock.
[Exact upstream source and terms](https://github.com/PyAV-Org/PyAV/tree/a4ad0133b13eb84067dc6e8105eb1fc8f8b93c4f)
should be reviewed for the intended use. A displayed FFmpeg runtime license
string alone is not clearance for its complete linked-codec combination.

## Explicit setup and offline verification

Setup contacts only the complete pinned HTTPS `files.pythonhosted.org/packages/`
URL. Redirects, proxy/environment credentials, arbitrary URLs, pip and source
builds are unsupported. Standard verified TLS remains. A 30-second socket timeout
and 90-second between-chunk deadline bound one streamed attempt; no retries occur.
No footage, account, filename, profile or review data are sent. The provider still
sees ordinary connection/request metadata. This request is separate from the
subsequently offline local workflow.

The exact whole-wheel length/SHA must match before parsing. Limits remain 40 MiB
wheel, 4,096 members, 128 MiB/member and 512 MiB expanded. Only regular files/directories
inside `av`, `av.libs` and the exact versioned dist-info namespace are accepted.
Traversal, raw backslashes, links/special files, duplicate names, encryption and
unsupported compression fail. Package/version/ABI and the complete RECORD hashes
and lengths are independently checked. All original wheel files and notices stay
in a separate private dependency store. No downloaded installer/build hook is
executed; normal import necessarily executes the explicitly trusted verified PyAV
library code.

Only a completely extracted wheel receives an exclusive atomic activation pointer.
An earlier pointer/install or unrelated nonempty directory is never overwritten.
Before every native app or worker import, the original wheel and all extracted
bytes are reverified offline. Changed or unexpected files are preserved and refused,
not silently repaired or downloaded. The store uses the current OS user's local
application-data area outside the program and footage/account profiles. An explicit
trusted-owner `DVP_DEPENDENCY_HOME` override supports isolated acceptance or a
chosen dependency location; it does not alter browser permissions. A hostile OS
owner, administrator or malware with equivalent filesystem access is outside the
trust boundary.

Cancel before Install performs no fetch and opens no profile. Once Install starts,
the owned setup thread must finish its bounded operation before close; its controls
explain that state. Failure stays visible and requires Quit/reopen. First setup
cannot work offline and provider/TLS availability is not guaranteed; successful
installed use is offline.

## Validation and remaining limits

Packaging excludes `av` at freezer analysis and checks the actual embedded PYZ
module inventory plus extracted file tree for codec payloads. Each native platform
must acquire its own pinned wheel through explicit consent, then run the original
real 40-frame import/mask/process/independent-review/export/pixel/receipt/Quit journey
from the extracted application without developer-runtime PATH or a source-service
fallback. Source Tk tests exercise actual Install/Cancel controls. Optional console
`--install-codecs` uses the same installer only after literal `INSTALL` consent;
this is not a manually clicked frozen-window claim.

Earlier combined-binary/source-license investigation remains private historical
held evidence. It is not a codec asset in this release. No whole upstream codec
rebuild, bit-identical codec reproduction, legal certification, patent clearance
or absence of native-library vulnerabilities is claimed. Media parsing remains a
trusted-local short-clip workflow, not an OS sandbox or public upload service.
