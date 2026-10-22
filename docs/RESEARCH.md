<!-- Jason Stys: primary-source research, design interpretation and third-party licensing notes. -->
# Research and provenance

Reviewed 2026-10-21. These sources inform design; this project is not endorsed, certified or legally approved by them. Time/byte/geometry thresholds below are engineering decisions, not regulatory safe harbors.

| Primary source | Applied interpretation |
| --- | --- |
| [NTIA UAS privacy/transparency/accountability multistakeholder process](https://www.ntia.gov/other-publication/2016/multistakeholder-process-unmanned-aircraft-systems) and [NTIA summary](https://www.ntia.gov/blog/2016/finding-common-ground-uas) | Minimize collection/use/sharing and make handling visible. Apply restricted originals, documented purpose, retention and narrowly scoped exports. Voluntary guidance is not a universal legal permission or substitute for consent/agency policy. |
| [OWASP file-upload guidance](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | Treat MIME/filename/signatures as insufficient; validate actual content, cap resources, generate names, keep media outside webroot, require authorization/CSRF. Re-encoding is defense in depth, not proof of safe parsing. |
| [OWASP input validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) | Strict finite bounded input and server-side validation; no reflected private data. Parameterized SQL and text-only DOM output remain independent controls. |
| [PyAV 19.0.2 official docs](https://pyav.basswood.io/docs/stable/) and [PyPI package](https://pypi.org/project/av/19.0.2/) | Direct native frame/stream access with bundled FFmpeg wheels on supported OSes. Use current documented API and test actual rational/timestamp behavior; old PyAV documentation is not assumed compatible. Explicitly close containers. |
| [FFmpeg protocols](https://ffmpeg.org/ffmpeg-protocols.html) | No remote URL input; fixed demuxer, custom bytes I/O, disabled external MOV references and protocol allowlisting. This does not create an OS sandbox. |
| [FFmpeg security](https://ffmpeg.org/security.html) | Native parsers/codecs require a separate security update review; source-level application scans do not audit all bundled binaries. Reproduce actual issues, do not report speculative scanner output as a confirmed vulnerability. |
| [NumPy project](https://pypi.org/project/numpy/) | Use contiguous vectorized array slice assignment for masks instead of per-pixel Python loops; document O(F×pixels) cost rather than claim all work is constant time. |
| [Google OSV-Scanner](https://github.com/google/osv-scanner/releases/tag/v2.7.0) | Checksum-pin official scanner; use live advisory results and independently require all locked npm identities. Zero current known advisories is not proof of security. |

## Decisions that are not taken from regulations

[Playwright's official browser documentation](https://playwright.dev/docs/browsers) notes that media codecs vary by operating system. Actual Windows WebKit tests could not decode the application's H.264 preview. The response is a real authenticated server-decoded PNG review mode, not a codec-availability skip, fake image or weakened privacy test. Continuous video still works where the browser decoder is available.

Twenty seconds, 20 MiB input, 32 MiB output, integer fps, fixed MP4 codec allowlist, eight-pixel margin, requested-pixel tolerance 24/255, 250 ms endpoint drift, 1000 ms telemetry gap, 12 clips/five revisions, one worker and 90-second deadline define this lab's supported envelope. They are explicit, tested limits—not claims that footage outside/inside them is unlawful/lawful or anonymous. Redaction remains manual and contextual.

## Original fixtures and measurable claims

All video fixtures are generated from original colored geometry by Jason Stys; no dataset, real person, actual plate, real coordinates, scraped surveillance or third-party artwork is included. The moving patch/mock plate are known pixel oracles, not an accuracy benchmark on real face recognition. No detector precision/recall, privacy certification or general native fuzzing coverage is claimed. Performance is measured locally and in CI on the exact controlled fixture; see validation.

## Third-party notices

Original repository source is MIT. PyAV metadata identifies BSD-3-Clause; NumPy has its own BSD-style license. Python/npm dependencies and vendor tools retain their licenses. **Bundled FFmpeg and enabled codecs (including libx264) have independent LGPL/GPL and possible patent/distribution obligations.** See [FFmpeg legal guidance](https://ffmpeg.org/legal.html) and the installed wheel's license notices before repackaging/distributing a binary. This source repository publishes no wheels, copied codec binaries, installer or runtime media; it instructs users/CI to fetch vendor dependencies. MIT on the original code does not relicense those libraries. No commercial codec/patent advice is provided.
