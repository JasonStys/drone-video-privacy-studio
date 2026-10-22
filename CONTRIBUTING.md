<!-- Jason Stys: reproducible contribution and privacy review requirements. -->
# Contributing

Use synthetic data only. Preserve object authorization, exact frame semantics, independent current-revision approval, data-minimized exports and explicit trust limits. Do not add automatic identity search, public remote media fetching, external analytics, real footage or hard-coded credentials.

Run all README validation commands, regenerate `python tools/docs_index.py` after source changes, and commit complete locks when dependencies change. Explain complexity/resource/privacy tradeoffs and add an independent regression for every fixed failure. Never remove a failing safety check, suppress an advisory or add a retry just to make CI green. Browser tests must exercise the real local backend. Native-library updates need their own release/security/license review.

Do not upload Actions artifacts/caches without discussing storage/retention. Use concise sanitized issue reports; see SECURITY.md for private vulnerability disclosure.
