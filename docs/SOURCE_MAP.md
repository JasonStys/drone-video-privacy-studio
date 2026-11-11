# Source declaration map

By Jason Stys. Headers link here for current exact physical lines.
Python/TypeScript ASTs index declarations, parameters and bindings; SQL lists non-comment schema lines. Lexical maps are navigation, not complete semantic symbol tables.

| File | Line | Declaration / variable |
| --- | ---: | --- |
| `launcher.py` | 6 | `main()` |
| `launcher.py` | 8 | `worker_mode` |
| `launcher.py` | 14 | `console_setup` |
| `tests/conftest.py` | 12 | `ORIGIN` |
| `tests/conftest.py` | 16 | `accounts()` |
| `tests/conftest.py` | 19 | `password` |
| `tests/conftest.py` | 20 | `name` |
| `tests/conftest.py` | 20 | `role` |
| `tests/conftest.py` | 30 | `app(tmp_path, accounts)` |
| `tests/conftest.py` | 32 | `instance` |
| `tests/conftest.py` | 33 | `db` |
| `tests/conftest.py` | 34 | `_` |
| `tests/conftest.py` | 34 | `hashed` |
| `tests/conftest.py` | 34 | `name` |
| `tests/conftest.py` | 34 | `role` |
| `tests/conftest.py` | 40 | `client(app)` |
| `tests/conftest.py` | 42 | `connection` |
| `tests/conftest.py` | 47 | `login(client, accounts)` |
| `tests/conftest.py` | 50 | `enter(name)` |
| `tests/conftest.py` | 51 | `response` |
| `tests/conftest.py` | 60 | `video(tmp_path_factory)` |
| `tests/conftest.py` | 62 | `path` |
| `tests/conftest.py` | 68 | `imported(client, login, video)` |
| `tests/conftest.py` | 71 | `response` |
| `tests/conftest.py` | 81 | `plan()` |
| `tests/conftest.py` | 112 | `processed(client, imported, plan)` |
| `tests/conftest.py` | 114 | `response` |
| `tests/runtime_notice_cases.py` | 10 | `ROOT` |
| `tests/runtime_notice_cases.py` | 14 | `interpreter()` |
| `tests/runtime_notice_cases.py` | 16 | `root` |
| `tests/runtime_notice_cases.py` | 24 | `test_actual_tcl_notice_reader_preserves_bytes_and_missing_identity(tmp_path, interpreter)` |
| `tests/runtime_notice_cases.py` | 26 | `path` |
| `tests/runtime_notice_cases.py` | 27 | `raw` |
| `tests/runtime_notice_cases.py` | 34 | `raw` |
| `tests/runtime_notice_cases.py` | 42 | `test_exact_mac_version_uses_verbatim_upstream_notice_and_binds_digest(tmp_path, kind, interpreter)` |
| `tests/runtime_notice_cases.py` | 46 | `library` |
| `tests/runtime_notice_cases.py` | 47 | `file` |
| `tests/runtime_notice_cases.py` | 48 | `target` |
| `tests/runtime_notice_cases.py` | 51 | `raw` |
| `tests/runtime_notice_cases.py` | 51 | `source` |
| `tests/runtime_notice_cases.py` | 78 | `test_unreviewed_platform_version_or_library_cannot_substitute_notice(version, library, system, interpreter)` |
| `tests/runtime_notice_cases.py` | 87 | `test_ubuntu_uses_actual_runtime_package_copyright_not_guessed_script_file(tmp_path, monkeypatch, kind, interpreter)` |
| `tests/runtime_notice_cases.py` | 91 | `fixture` |
| `tests/runtime_notice_cases.py` | 93 | `actual` |
| `tests/runtime_notice_cases.py` | 94 | `calls` |
| `tests/runtime_notice_cases.py` | 95 | `library` |
| `tests/runtime_notice_cases.py` | 96 | `package_path` |
| `tests/runtime_notice_cases.py` | 98 | `installed(interpreter, path)` |
| `tests/runtime_notice_cases.py` | 105 | `raw` |
| `tests/runtime_notice_cases.py` | 105 | `source` |
| `tests/runtime_notice_cases.py` | 110 | `test_present_invalid_runtime_notice_never_falls_back_to_other_terms(tmp_path, interpreter)` |
| `tests/runtime_notice_cases.py` | 118 | `test_mac_pre905_terms_require_exact_psf_sdk_recipe(tmp_path, monkeypatch, interpreter, python_version, accepted)` |
| `tests/runtime_notice_cases.py` | 123 | `library` |
| `tests/runtime_notice_cases.py` | 124 | `name` |
| `tests/runtime_notice_cases.py` | 128 | `raw` |
| `tests/runtime_notice_cases.py` | 128 | `source` |
| `tests/runtime_notice_cases.py` | 136 | `test_mac_pre905_changed_notice_is_rejected(tmp_path, monkeypatch, interpreter)` |
| `tests/runtime_notice_cases.py` | 140 | `path` |
| `tests/runtime_notice_cases.py` | 142 | `library` |
| `tests/test_cli.py` | 11 | `test_init_provision_mismatch_and_purge(tmp_path, monkeypatch, capsys)` |
| `tests/test_cli.py` | 13 | `db` |
| `tests/test_cli.py` | 19 | `answers` |
| `tests/test_cli.py` | 23 | `answers` |
| `tests/test_cli.py` | 26 | `confirm` |
| `tests/test_cli.py` | 31 | `test_serve_and_invalid_port(tmp_path, monkeypatch)` |
| `tests/test_cli.py` | 33 | `seen` |
| `tests/test_cli.py` | 45 | `test_disposable_browser_server_private_random_accounts(tmp_path, monkeypatch)` |
| `tests/test_cli.py` | 47 | `first` |
| `tests/test_cli.py` | 48 | `content` |
| `tests/test_cli.py` | 51 | `seen` |
| `tests/test_codec_bootstrap_entry.py` | 10 | `test_source_owner_and_profile_imports_do_not_load_codecs_before_consent()` |
| `tests/test_codec_bootstrap_entry.py` | 12 | `result` |
| `tests/test_codec_bootstrap_entry.py` | 27 | `test_frozen_cancel_returns_before_profile_or_server_launch(monkeypatch)` |
| `tests/test_codec_bootstrap_entry.py` | 31 | `calls` |
| `tests/test_codec_bootstrap_entry.py` | 34 | `_` |
| `tests/test_codec_bootstrap_entry.py` | 40 | `test_frozen_runtime_diagnostic_does_not_trigger_dependency_install(monkeypatch)` |
| `tests/test_codec_bootstrap_entry.py` | 47 | `_` |
| `tests/test_codec_bootstrap_entry.py` | 53 | `test_failed_frozen_dependency_import_is_nonzero_without_profile_fallback(monkeypatch, capsys)` |
| `tests/test_codec_bootstrap_entry.py` | 58 | `fail()` |
| `tests/test_codec_bootstrap_entry.py` | 66 | `_` |
| `tests/test_codec_setup.py` | 22 | `wheel_fixture()` |
| `tests/test_codec_setup.py` | 24 | `dist` |
| `tests/test_codec_setup.py` | 25 | `tag` |
| `tests/test_codec_setup.py` | 26 | `files` |
| `tests/test_codec_setup.py` | 35 | `records` |
| `tests/test_codec_setup.py` | 36 | `writer` |
| `tests/test_codec_setup.py` | 37 | `name` |
| `tests/test_codec_setup.py` | 37 | `raw` |
| `tests/test_codec_setup.py` | 48 | `output` |
| `tests/test_codec_setup.py` | 49 | `archive` |
| `tests/test_codec_setup.py` | 50 | `name` |
| `tests/test_codec_setup.py` | 50 | `raw` |
| `tests/test_codec_setup.py` | 51 | `item` |
| `tests/test_codec_setup.py` | 57 | `name` |
| `tests/test_codec_setup.py` | 57 | `raw` |
| `tests/test_codec_setup.py` | 60 | `item` |
| `tests/test_codec_setup.py` | 63 | `raw` |
| `tests/test_codec_setup.py` | 64 | `pin` |
| `tests/test_codec_setup.py` | 74 | `Response(class)` |
| `tests/test_codec_setup.py` | 77 | `__init__(self, raw, url)` |
| `tests/test_codec_setup.py` | 81 | `geturl(self)` |
| `tests/test_codec_setup.py` | 85 | `provider(raw, pin, calls)` |
| `tests/test_codec_setup.py` | 88 | `open_url(url)` |
| `tests/test_codec_setup.py` | 96 | `test_exact_published_wheel_manifest_retains_platform_abi_and_lock_pins()` |
| `tests/test_codec_setup.py` | 98 | `pins` |
| `tests/test_codec_setup.py` | 99 | `key` |
| `tests/test_codec_setup.py` | 99 | `row` |
| `tests/test_codec_setup.py` | 113 | `lock` |
| `tests/test_codec_setup.py` | 114 | `row` |
| `tests/test_codec_setup.py` | 151 | `test_unsupported_runtime_or_abi_never_selects_a_fallback(changes)` |
| `tests/test_codec_setup.py` | 153 | `values` |
| `tests/test_codec_setup.py` | 164 | `test_real_wheel_install_is_inert_complete_and_offline_reusable(tmp_path, monkeypatch)` |
| `tests/test_codec_setup.py` | 166 | `files` |
| `tests/test_codec_setup.py` | 166 | `pin` |
| `tests/test_codec_setup.py` | 166 | `raw` |
| `tests/test_codec_setup.py` | 167 | `calls` |
| `tests/test_codec_setup.py` | 167 | `home` |
| `tests/test_codec_setup.py` | 169 | `site` |
| `tests/test_codec_setup.py` | 172 | `p` |
| `tests/test_codec_setup.py` | 178 | `before` |
| `tests/test_codec_setup.py` | 179 | `p` |
| `tests/test_codec_setup.py` | 184 | `p` |
| `tests/test_codec_setup.py` | 191 | `test_failed_download_does_not_publish_or_clobber_existing_files(tmp_path, kind)` |
| `tests/test_codec_setup.py` | 193 | `_` |
| `tests/test_codec_setup.py` | 193 | `pin` |
| `tests/test_codec_setup.py` | 193 | `raw` |
| `tests/test_codec_setup.py` | 194 | `home` |
| `tests/test_codec_setup.py` | 196 | `protected` |
| `tests/test_codec_setup.py` | 198 | `altered` |
| `tests/test_codec_setup.py` | 208 | `fetch(_url)` |
| `tests/test_codec_setup.py` | 220 | `p` |
| `tests/test_codec_setup.py` | 235 | `test_actual_traversal_wheels_are_rejected_before_extraction(tmp_path, name)` |
| `tests/test_codec_setup.py` | 237 | `_` |
| `tests/test_codec_setup.py` | 237 | `pin` |
| `tests/test_codec_setup.py` | 237 | `raw` |
| `tests/test_codec_setup.py` | 262 | `test_independent_wheel_structure_metadata_record_and_inflation_negatives(kind, monkeypatch)` |
| `tests/test_codec_setup.py` | 264 | `dist` |
| `tests/test_codec_setup.py` | 266 | `change(files)` |
| `tests/test_codec_setup.py` | 286 | `_` |
| `tests/test_codec_setup.py` | 286 | `pin` |
| `tests/test_codec_setup.py` | 286 | `raw` |
| `tests/test_codec_setup.py` | 297 | `output` |
| `tests/test_codec_setup.py` | 298 | `source` |
| `tests/test_codec_setup.py` | 298 | `target` |
| `tests/test_codec_setup.py` | 299 | `item` |
| `tests/test_codec_setup.py` | 300 | `data` |
| `tests/test_codec_setup.py` | 302 | `data` |
| `tests/test_codec_setup.py` | 308 | `raw` |
| `tests/test_codec_setup.py` | 309 | `pin` |
| `tests/test_codec_setup.py` | 319 | `test_tampered_installed_dependency_is_preserved_and_not_repaired(tmp_path, kind)` |
| `tests/test_codec_setup.py` | 321 | `_` |
| `tests/test_codec_setup.py` | 321 | `pin` |
| `tests/test_codec_setup.py` | 321 | `raw` |
| `tests/test_codec_setup.py` | 322 | `home` |
| `tests/test_codec_setup.py` | 323 | `site` |
| `tests/test_codec_setup.py` | 324 | `path` |
| `tests/test_codec_setup.py` | 341 | `test_unknown_nonempty_dependency_directory_and_failed_atomic_publish_preserve_prior_state(tmp_path, monkeypatch)` |
| `tests/test_codec_setup.py` | 345 | `home` |
| `tests/test_codec_setup.py` | 348 | `_` |
| `tests/test_codec_setup.py` | 348 | `pin` |
| `tests/test_codec_setup.py` | 348 | `raw` |
| `tests/test_codec_setup.py` | 351 | `p` |
| `tests/test_codec_setup.py` | 352 | `owned` |
| `tests/test_codec_setup.py` | 354 | `competitor(_pending, pointer)` |
| `tests/test_codec_setup.py` | 355 | `output` |
| `tests/test_codec_setup.py` | 363 | `p` |
| `tests/test_codec_setup.py` | 367 | `test_offline_verification_refuses_unknown_directories_before_descending(tmp_path, monkeypatch, nested)` |
| `tests/test_codec_setup.py` | 371 | `_` |
| `tests/test_codec_setup.py` | 371 | `pin` |
| `tests/test_codec_setup.py` | 371 | `raw` |
| `tests/test_codec_setup.py` | 372 | `home` |
| `tests/test_codec_setup.py` | 373 | `site` |
| `tests/test_codec_setup.py` | 374 | `extra` |
| `tests/test_codec_setup.py` | 377 | `index` |
| `tests/test_codec_setup.py` | 378 | `child` |
| `tests/test_codec_setup.py` | 381 | `actual_scandir` |
| `tests/test_codec_setup.py` | 381 | `visited` |
| `tests/test_codec_setup.py` | 383 | `bounded_scan(path)` |
| `tests/test_codec_setup.py` | 384 | `path` |
| `tests/test_codec_setup.py` | 392 | `path` |
| `tests/test_codec_setup.py` | 397 | `test_actual_junction_or_symlink_cannot_replace_expected_dependency_directories(tmp_path, part)` |
| `tests/test_codec_setup.py` | 399 | `_` |
| `tests/test_codec_setup.py` | 399 | `pin` |
| `tests/test_codec_setup.py` | 399 | `raw` |
| `tests/test_codec_setup.py` | 400 | `home` |
| `tests/test_codec_setup.py` | 401 | `site` |
| `tests/test_codec_setup.py` | 402 | `original` |
| `tests/test_codec_setup.py` | 403 | `retained` |
| `tests/test_codec_setup.py` | 415 | `target` |
| `tests/test_codec_setup.py` | 419 | `test_offline_activation_requires_verified_source_path_and_exact_version(tmp_path, monkeypatch)` |
| `tests/test_codec_setup.py` | 421 | `_` |
| `tests/test_codec_setup.py` | 421 | `pin` |
| `tests/test_codec_setup.py` | 421 | `raw` |
| `tests/test_codec_setup.py` | 422 | `home` |
| `tests/test_codec_setup.py` | 423 | `site` |
| `tests/test_codec_setup.py` | 449 | `test_explicit_setup_cancel_opens_neither_network_nor_profile(tmp_path, monkeypatch)` |
| `tests/test_codec_setup.py` | 453 | `_` |
| `tests/test_codec_setup.py` | 453 | `pin` |
| `tests/test_codec_setup.py` | 453 | `raw` |
| `tests/test_codec_setup.py` | 454 | `calls` |
| `tests/test_codec_setup.py` | 456 | `root` |
| `tests/test_codec_setup.py` | 457 | `window` |
| `tests/test_codec_setup.py` | 468 | `test_real_setup_install_button_finishes_actual_inert_wheel_before_continuing(tmp_path, monkeypatch)` |
| `tests/test_codec_setup.py` | 474 | `_` |
| `tests/test_codec_setup.py` | 474 | `pin` |
| `tests/test_codec_setup.py` | 474 | `raw` |
| `tests/test_codec_setup.py` | 475 | `actual` |
| `tests/test_codec_setup.py` | 476 | `calls` |
| `tests/test_codec_setup.py` | 480 | `root` |
| `tests/test_codec_setup.py` | 481 | `home` |
| `tests/test_codec_setup.py` | 482 | `window` |
| `tests/test_codec_setup.py` | 486 | `deadline` |
| `tests/test_codec_setup.py` | 494 | `test_setup_failure_remains_visible_without_retry_or_profile_creation(tmp_path, monkeypatch)` |
| `tests/test_codec_setup.py` | 498 | `_` |
| `tests/test_codec_setup.py` | 498 | `pin` |
| `tests/test_codec_setup.py` | 499 | `calls` |
| `tests/test_codec_setup.py` | 501 | `offline()` |
| `tests/test_codec_setup.py` | 506 | `root` |
| `tests/test_codec_setup.py` | 507 | `window` |
| `tests/test_codec_setup.py` | 510 | `deadline` |
| `tests/test_codec_setup.py` | 520 | `test_console_consent_and_noninteractive_offline_refusal_are_explicit(tmp_path, monkeypatch, capsys)` |
| `tests/test_codec_setup.py` | 524 | `_` |
| `tests/test_codec_setup.py` | 524 | `pin` |
| `tests/test_codec_setup.py` | 524 | `raw` |
| `tests/test_codec_setup.py` | 525 | `home` |
| `tests/test_codec_setup.py` | 532 | `actual` |
| `tests/test_codec_setup.py` | 536 | `activations` |
| `tests/test_desktop_host.py` | 15 | `prepared(tmp_path)` |
| `tests/test_desktop_host.py` | 17 | `profile` |
| `tests/test_desktop_host.py` | 24 | `request(host, path)` |
| `tests/test_desktop_host.py` | 26 | `connection` |
| `tests/test_desktop_host.py` | 31 | `response` |
| `tests/test_desktop_host.py` | 37 | `test_actual_readiness_private_login_and_owned_stop(tmp_path)` |
| `tests/test_desktop_host.py` | 39 | `profile` |
| `tests/test_desktop_host.py` | 40 | `metadata` |
| `tests/test_desktop_host.py` | 41 | `host` |
| `tests/test_desktop_host.py` | 44 | `_` |
| `tests/test_desktop_host.py` | 44 | `code` |
| `tests/test_desktop_host.py` | 44 | `raw` |
| `tests/test_desktop_host.py` | 45 | `health` |
| `tests/test_desktop_host.py` | 50 | `login` |
| `tests/test_desktop_host.py` | 61 | `code` |
| `tests/test_desktop_host.py` | 61 | `headers` |
| `tests/test_desktop_host.py` | 61 | `raw` |
| `tests/test_desktop_host.py` | 69 | `cookie` |
| `tests/test_desktop_host.py` | 89 | `test_actual_partial_body_bounds_pre_shutdown_drain(tmp_path)` |
| `tests/test_desktop_host.py` | 91 | `profile` |
| `tests/test_desktop_host.py` | 92 | `host` |
| `tests/test_desktop_host.py` | 93 | `received` |
| `tests/test_desktop_host.py` | 95 | `ObserveRead(class)` |
| `tests/test_desktop_host.py` | 98 | `__init__(self, app)` |
| `tests/test_desktop_host.py` | 101 | `__call__(self, scope, receive, send)` |
| `tests/test_desktop_host.py` | 102 | `observed()` |
| `tests/test_desktop_host.py` | 103 | `message` |
| `tests/test_desktop_host.py` | 113 | `connection` |
| `tests/test_desktop_host.py` | 124 | `response` |
| `tests/test_desktop_host.py` | 140 | `test_startup_failure_is_never_reported_as_ready(tmp_path, monkeypatch, failure)` |
| `tests/test_desktop_host.py` | 142 | `profile` |
| `tests/test_desktop_host.py` | 143 | `host` |
| `tests/test_desktop_host.py` | 145 | `broken()` |
| `tests/test_desktop_host.py` | 163 | `test_two_actual_profiles_keep_sessions_in_one_host_scoped_cookie_jar(tmp_path)` |
| `tests/test_desktop_host.py` | 165 | `first` |
| `tests/test_desktop_host.py` | 166 | `second` |
| `tests/test_desktop_host.py` | 167 | `password` |
| `tests/test_desktop_host.py` | 171 | `hosts` |
| `tests/test_desktop_host.py` | 173 | `host` |
| `tests/test_desktop_host.py` | 175 | `client` |
| `tests/test_desktop_host.py` | 176 | `host` |
| `tests/test_desktop_host.py` | 176 | `name` |
| `tests/test_desktop_host.py` | 177 | `response` |
| `tests/test_desktop_host.py` | 183 | `cookie` |
| `tests/test_desktop_host.py` | 187 | `host` |
| `tests/test_desktop_host.py` | 187 | `users` |
| `tests/test_desktop_host.py` | 188 | `user` |
| `tests/test_desktop_host.py` | 189 | `foreign_cookie` |
| `tests/test_desktop_host.py` | 196 | `wrong_csrf` |
| `tests/test_desktop_host.py` | 213 | `host` |
| `tests/test_desktop_host.py` | 220 | `test_invalid_cookie_namespace_is_rejected_before_database_creation(tmp_path, invalid)` |
| `tests/test_desktop_host.py` | 224 | `database` |
| `tests/test_desktop_package.py` | 24 | `test_freeze_refuses_old_cached_or_prerelease_runtime(version, level, allowed)` |
| `tests/test_desktop_package.py` | 29 | `test_all_product_version_surfaces_agree()` |
| `tests/test_desktop_package.py` | 40 | `test_actual_codec_free_bundle_gate_refuses_payloads_not_just_the_freezer_flag(tmp_path, kind)` |
| `tests/test_desktop_package.py` | 42 | `modules` |
| `tests/test_desktop_package.py` | 45 | `path` |
| `tests/test_desktop_package.py` | 55 | `result` |
| `tests/test_desktop_package.py` | 66 | `test_mismatched_version_or_identity_cannot_build(tmp_path, surface)` |
| `tests/test_desktop_package.py` | 68 | `root` |
| `tests/test_desktop_package.py` | 69 | `path` |
| `tests/test_desktop_package.py` | 70 | `output` |
| `tests/test_desktop_package.py` | 73 | `selected` |
| `tests/test_desktop_package.py` | 81 | `path` |
| `tests/test_desktop_package.py` | 85 | `value` |
| `tests/test_desktop_package.py` | 109 | `test_source_cleanliness_is_not_a_release_flag_waiver(monkeypatch, dirty, ci, override, sha, allowed)` |
| `tests/test_desktop_package.py` | 114 | `output(command)` |
| `tests/test_desktop_package.py` | 131 | `value` |
| `tests/test_desktop_package.py` | 135 | `test_archive_rejection_remains_active_with_optimized_python()` |
| `tests/test_desktop_package.py` | 137 | `result` |
| `tests/test_desktop_profile.py` | 13 | `database_snapshot(store)` |
| `tests/test_desktop_profile.py` | 15 | `database` |
| `tests/test_desktop_profile.py` | 19 | `test_provision_persist_login_and_existing_roles(tmp_path)` |
| `tests/test_desktop_profile.py` | 21 | `path` |
| `tests/test_desktop_profile.py` | 22 | `profile` |
| `tests/test_desktop_profile.py` | 30 | `original` |
| `tests/test_desktop_profile.py` | 31 | `namespace` |
| `tests/test_desktop_profile.py` | 32 | `marker_bytes` |
| `tests/test_desktop_profile.py` | 39 | `reopened` |
| `tests/test_desktop_profile.py` | 46 | `client` |
| `tests/test_desktop_profile.py` | 48 | `response` |
| `tests/test_desktop_profile.py` | 54 | `db` |
| `tests/test_desktop_profile.py` | 55 | `row` |
| `tests/test_desktop_profile.py` | 55 | `values` |
| `tests/test_desktop_profile.py` | 56 | `value` |
| `tests/test_desktop_profile.py` | 61 | `test_invalid_duplicate_and_first_role_do_not_create_account(tmp_path)` |
| `tests/test_desktop_profile.py` | 63 | `profile` |
| `tests/test_desktop_profile.py` | 65 | `args` |
| `tests/test_desktop_profile.py` | 74 | `db` |
| `tests/test_desktop_profile.py` | 75 | `original_hash` |
| `tests/test_desktop_profile.py` | 83 | `db` |
| `tests/test_desktop_profile.py` | 104 | `test_invalid_marker_never_adopts_unknown_profile(tmp_path, content)` |
| `tests/test_desktop_profile.py` | 106 | `folder` |
| `tests/test_desktop_profile.py` | 114 | `test_unknown_folder_and_wrong_product_are_preserved(tmp_path)` |
| `tests/test_desktop_profile.py` | 116 | `important` |
| `tests/test_desktop_profile.py` | 125 | `marker` |
| `tests/test_desktop_profile.py` | 131 | `test_default_directory_is_per_user_and_outside_source(monkeypatch, tmp_path)` |
| `tests/test_desktop_resources.py` | 13 | `test_source_mode_is_explicit_and_frozen_missing_identity_fails(tmp_path, monkeypatch)` |
| `tests/test_desktop_resources.py` | 36 | `test_each_wrong_frozen_identity_surface_is_rejected(tmp_path, field, value)` |
| `tests/test_desktop_resources.py` | 38 | `path` |
| `tests/test_desktop_resources.py` | 40 | `valid` |
| `tests/test_desktop_resources.py` | 55 | `test_resources_are_real_regular_nonempty_bounded_files(tmp_path)` |
| `tests/test_desktop_resources.py` | 57 | `path` |
| `tests/test_desktop_resources.py` | 60 | `raw` |
| `tests/test_desktop_resources.py` | 68 | `test_console_owner_uses_actual_saved_profile_and_quits_without_password_input(tmp_path, monkeypatch, capsys)` |
| `tests/test_desktop_resources.py` | 74 | `path` |
| `tests/test_desktop_resources.py` | 75 | `profile` |
| `tests/test_desktop_resources.py` | 82 | `output` |
| `tests/test_desktop_resources.py` | 85 | `reopened` |
| `tests/test_desktop_resources.py` | 92 | `test_console_cannot_create_preset_first_account(tmp_path)` |
| `tests/test_desktop_resources.py` | 96 | `path` |
| `tests/test_desktop_resources.py` | 99 | `profile` |
| `tests/test_desktop_resources.py` | 106 | `test_entrypoint_requires_explicit_console_mode_and_real_resources(tmp_path, monkeypatch, capsys)` |
| `tests/test_desktop_resources.py` | 110 | `error` |
| `tests/test_desktop_resources.py` | 121 | `test_normal_entrypoint_presents_native_controls(tmp_path, monkeypatch)` |
| `tests/test_desktop_resources.py` | 125 | `observed` |
| `tests/test_desktop_resources.py` | 127 | `close_after_construct(root, directory, metadata)` |
| `tests/test_desktop_resources.py` | 141 | `test_actual_loaded_tk_matches_package_and_runtime_info_opens_no_profile(tmp_path, monkeypatch, capsys)` |
| `tests/test_desktop_resources.py` | 147 | `root` |
| `tests/test_desktop_resources.py` | 150 | `versions` |
| `tests/test_desktop_resources.py` | 159 | `_` |
| `tests/test_desktop_resources.py` | 162 | `output` |
| `tests/test_desktop_resources.py` | 163 | `record` |
| `tests/test_desktop_resources.py` | 164 | `name` |
| `tests/test_desktop_resources.py` | 168 | `test_console_interrupt_drains_the_actual_owned_host_and_releases_profile(tmp_path, monkeypatch, capsys)` |
| `tests/test_desktop_resources.py` | 174 | `path` |
| `tests/test_desktop_resources.py` | 175 | `profile` |
| `tests/test_desktop_resources.py` | 180 | `actual_host` |
| `tests/test_desktop_resources.py` | 181 | `observed` |
| `tests/test_desktop_resources.py` | 183 | `remember()` |
| `tests/test_desktop_resources.py` | 184 | `host` |
| `tests/test_desktop_resources.py` | 188 | `Interrupted(class)` |
| `tests/test_desktop_resources.py` | 189 | `__iter__(self)` |
| `tests/test_desktop_resources.py` | 200 | `reopened` |
| `tests/test_frames.py` | 12 | `test_private_frame_endpoint_uses_processed_pixels_and_no_metadata(client, processed, login)` |
| `tests/test_frames.py` | 14 | `path` |
| `tests/test_frames.py` | 15 | `response` |
| `tests/test_frames.py` | 20 | `frame` |
| `tests/test_frames.py` | 21 | `values` |
| `tests/test_frames.py` | 23 | `pixels` |
| `tests/test_frames.py` | 33 | `test_frame_renderer_native_bounds_and_worker_branch(tmp_path, video)` |
| `tests/test_frames.py` | 35 | `output` |
| `tests/test_frames.py` | 37 | `result` |
| `tests/test_frames.py` | 49 | `test_native_source_size_guard_before_read(tmp_path, monkeypatch)` |
| `tests/test_frames.py` | 51 | `source` |
| `tests/test_frames.py` | 58 | `test_workspace_capacity_enforced_before_decoder(client, imported, app)` |
| `tests/test_frames.py` | 60 | `db` |
| `tests/test_frames.py` | 61 | `index` |
| `tests/test_frozen_worker.py` | 13 | `test_media_worker_cannot_read_or_block_on_the_owners_real_input_pipe(tmp_path)` |
| `tests/test_frozen_worker.py` | 15 | `worker` |
| `tests/test_frozen_worker.py` | 20 | `parent` |
| `tests/test_frozen_worker.py` | 26 | `result` |
| `tests/test_frozen_worker.py` | 41 | `test_source_and_frozen_worker_commands_never_turn_inputs_into_modules(tmp_path, monkeypatch)` |
| `tests/test_frozen_worker.py` | 53 | `test_fixed_launcher_worker_executes_real_transcode_without_owner_window(tmp_path, video, monkeypatch)` |
| `tests/test_frozen_worker.py` | 61 | `result` |
| `tests/test_frozen_worker.py` | 65 | `error` |
| `tests/test_frozen_worker.py` | 71 | `test_worker_mode_requires_exactly_one_service_directory(arguments, monkeypatch)` |
| `tests/test_frozen_worker.py` | 74 | `error` |
| `tests/test_media.py` | 13 | `custom(path, frames, fps, width, height, codec, irregular, audio)` |
| `tests/test_media.py` | 17 | `container` |
| `tests/test_media.py` | 20 | `stream` |
| `tests/test_media.py` | 24 | `sound` |
| `tests/test_media.py` | 26 | `index` |
| `tests/test_media.py` | 27 | `frame` |
| `tests/test_media.py` | 32 | `packet` |
| `tests/test_media.py` | 34 | `packet` |
| `tests/test_media.py` | 37 | `frame` |
| `tests/test_media.py` | 41 | `packet` |
| `tests/test_media.py` | 43 | `packet` |
| `tests/test_media.py` | 47 | `test_inclusive_boundaries_rounding_and_overlap(tmp_path)` |
| `tests/test_media.py` | 49 | `destination` |
| `tests/test_media.py` | 49 | `source` |
| `tests/test_media.py` | 51 | `masks` |
| `tests/test_media.py` | 52 | `info` |
| `tests/test_media.py` | 54 | `result` |
| `tests/test_media.py` | 55 | `f` |
| `tests/test_media.py` | 55 | `frames` |
| `tests/test_media.py` | 61 | `all_mask` |
| `tests/test_media.py` | 63 | `pixels` |
| `tests/test_media.py` | 68 | `test_audio_and_source_text_removed_but_not_claimed_anonymous(tmp_path)` |
| `tests/test_media.py` | 70 | `destination` |
| `tests/test_media.py` | 70 | `source` |
| `tests/test_media.py` | 72 | `original` |
| `tests/test_media.py` | 74 | `info` |
| `tests/test_media.py` | 83 | `test_invalid_and_truncated_mp4_fails(tmp_path, data)` |
| `tests/test_media.py` | 85 | `source` |
| `tests/test_media.py` | 91 | `test_bounds_outside_masks_and_output_verifier(tmp_path, monkeypatch)` |
| `tests/test_media.py` | 93 | `destination` |
| `tests/test_media.py` | 93 | `source` |
| `tests/test_media.py` | 101 | `info` |
| `tests/test_media.py` | 120 | `test_unsupported_frame_rate_size_and_frame_budget(tmp_path, monkeypatch)` |
| `tests/test_media.py` | 122 | `destination` |
| `tests/test_media.py` | 122 | `source` |
| `tests/test_media.py` | 136 | `test_variable_frame_rate_and_video_only_verifier(tmp_path)` |
| `tests/test_media.py` | 138 | `destination` |
| `tests/test_media.py` | 138 | `source` |
| `tests/test_media.py` | 151 | `test_all_original_examples(tmp_path, scenario)` |
| `tests/test_media.py` | 153 | `destination` |
| `tests/test_media.py` | 153 | `source` |
| `tests/test_media.py` | 155 | `info` |
| `tests/test_models.py` | 24 | `test_invalid_masks(changes)` |
| `tests/test_models.py` | 41 | `test_telemetry_and_frame_tolerance(plan)` |
| `tests/test_models.py` | 43 | `parsed` |
| `tests/test_models.py` | 47 | `ms` |
| `tests/test_models.py` | 59 | `test_mask_budget_and_duplicate_timestamp(plan)` |
| `tests/test_models.py` | 65 | `point` |
| `tests/test_motion.py` | 16 | `anchor(frame, x, y, width, height)` |
| `tests/test_motion.py` | 24 | `intent()` |
| `tests/test_motion.py` | 29 | `test_rational_interpolation_contained_in_exact_partition_for_every_frame()` |
| `tests/test_motion.py` | 31 | `randomizer` |
| `tests/test_motion.py` | 32 | `_` |
| `tests/test_motion.py` | 33 | `length` |
| `tests/test_motion.py` | 34 | `anchors` |
| `tests/test_motion.py` | 35 | `frame` |
| `tests/test_motion.py` | 36 | `x` |
| `tests/test_motion.py` | 36 | `y` |
| `tests/test_motion.py` | 37 | `height` |
| `tests/test_motion.py` | 37 | `width` |
| `tests/test_motion.py` | 39 | `draft` |
| `tests/test_motion.py` | 42 | `generated` |
| `tests/test_motion.py` | 45 | `frame` |
| `tests/test_motion.py` | 46 | `active` |
| `tests/test_motion.py` | 46 | `mask` |
| `tests/test_motion.py` | 48 | `mask` |
| `tests/test_motion.py` | 49 | `fraction` |
| `tests/test_motion.py` | 50 | `interpolated` |
| `tests/test_motion.py` | 53 | `key` |
| `tests/test_motion.py` | 76 | `test_invalid_keyframe_intent_rejected(changes)` |
| `tests/test_motion.py` | 83 | `test_decoded_clip_bounds_are_authoritative(frames)` |
| `tests/test_motion.py` | 88 | `test_actual_transcode_and_redecode_contains_manual_motion_without_touching_other_frames(tmp_path)` |
| `tests/test_motion.py` | 94 | `output` |
| `tests/test_motion.py` | 94 | `source` |
| `tests/test_motion.py` | 96 | `draft` |
| `tests/test_motion.py` | 103 | `masks` |
| `tests/test_motion.py` | 104 | `info` |
| `tests/test_motion.py` | 106 | `decoded` |
| `tests/test_motion.py` | 107 | `frame` |
| `tests/test_motion.py` | 107 | `index` |
| `tests/test_motion.py` | 108 | `pixels` |
| `tests/test_motion.py` | 110 | `ratio` |
| `tests/test_motion.py` | 111 | `x` |
| `tests/test_motion.py` | 111 | `y` |
| `tests/test_motion.py` | 112 | `region` |
| `tests/test_motion.py` | 122 | `test_private_read_only_helper_and_real_processing(client, imported, login, app, monkeypatch)` |
| `tests/test_motion.py` | 124 | `endpoint` |
| `tests/test_motion.py` | 125 | `before` |
| `tests/test_motion.py` | 126 | `body` |
| `tests/test_motion.py` | 127 | `result` |
| `tests/test_motion.py` | 133 | `token` |
| `tests/test_motion.py` | 144 | `concurrent(draft, frames)` |
| `tests/test_motion.py` | 146 | `result` |
| `tests/test_network.py` | 15 | `test_forwarded_headers_do_not_bypass_real_server_throttle(tmp_path, monkeypatch)` |
| `tests/test_network.py` | 17 | `reservation` |
| `tests/test_network.py` | 19 | `port` |
| `tests/test_network.py` | 20 | `app` |
| `tests/test_network.py` | 23 | `server` |
| `tests/test_network.py` | 33 | `thread` |
| `tests/test_network.py` | 36 | `_` |
| `tests/test_network.py` | 41 | `origin` |
| `tests/test_network.py` | 42 | `client` |
| `tests/test_network.py` | 43 | `index` |
| `tests/test_network.py` | 44 | `response` |
| `tests/test_notice_inventory.py` | 10 | `test_windows_metadata_paths_retain_attribution_and_nonstandard_license_suffixes(tmp_path)` |
| `tests/test_notice_inventory.py` | 12 | `names` |
| `tests/test_notice_inventory.py` | 18 | `info` |
| `tests/test_notice_inventory.py` | 22 | `test_actual_locked_runtime_notices_are_text_and_keep_original_license(tmp_path)` |
| `tests/test_notice_inventory.py` | 24 | `notices` |
| `tests/test_notice_inventory.py` | 25 | `path` |
| `tests/test_notice_inventory.py` | 26 | `path` |
| `tests/test_notice_inventory.py` | 27 | `raw` |
| `tests/test_osv_policy.py` | 12 | `lock()` |
| `tests/test_osv_policy.py` | 24 | `report()` |
| `tests/test_osv_policy.py` | 32 | `name` |
| `tests/test_osv_policy.py` | 32 | `version` |
| `tests/test_osv_policy.py` | 39 | `test_complete_inventory()` |
| `tests/test_osv_policy.py` | 41 | `expected` |
| `tests/test_osv_policy.py` | 55 | `test_invalid_lock(change)` |
| `tests/test_osv_policy.py` | 57 | `data` |
| `tests/test_osv_policy.py` | 82 | `test_incomplete_or_finding_never_passes(change)` |
| `tests/test_osv_policy.py` | 84 | `data` |
| `tests/test_owner_window.py` | 11 | `database_snapshot(store)` |
| `tests/test_owner_window.py` | 13 | `database` |
| `tests/test_owner_window.py` | 18 | `window(tmp_path)` |
| `tests/test_owner_window.py` | 20 | `root` |
| `tests/test_owner_window.py` | 22 | `view` |
| `tests/test_owner_window.py` | 39 | `credentials(view, name, password, confirmation)` |
| `tests/test_owner_window.py` | 41 | `password` |
| `tests/test_owner_window.py` | 47 | `test_actual_buttons_first_account_staff_and_no_password_retention(window, monkeypatch)` |
| `tests/test_owner_window.py` | 49 | `_` |
| `tests/test_owner_window.py` | 49 | `view` |
| `tests/test_owner_window.py` | 50 | `opened` |
| `tests/test_owner_window.py` | 69 | `original_host` |
| `tests/test_owner_window.py` | 84 | `test_folder_choice_and_unknown_existing_files_are_not_adopted(window, tmp_path, monkeypatch)` |
| `tests/test_owner_window.py` | 86 | `_` |
| `tests/test_owner_window.py` | 86 | `view` |
| `tests/test_owner_window.py` | 87 | `original` |
| `tests/test_owner_window.py` | 91 | `target` |
| `tests/test_owner_window.py` | 93 | `note` |
| `tests/test_owner_window.py` | 102 | `test_cancelled_or_busy_quit_retains_owner_until_actual_completion(window, monkeypatch)` |
| `tests/test_owner_window.py` | 104 | `root` |
| `tests/test_owner_window.py` | 104 | `view` |
| `tests/test_owner_window.py` | 113 | `busy()` |
| `tests/test_owner_window.py` | 116 | `change` |
| `tests/test_owner_window.py` | 126 | `test_identified_profile_automatically_reopens_without_reset(tmp_path, monkeypatch)` |
| `tests/test_owner_window.py` | 128 | `path` |
| `tests/test_owner_window.py` | 129 | `profile` |
| `tests/test_owner_window.py` | 133 | `before` |
| `tests/test_owner_window.py` | 135 | `opened` |
| `tests/test_owner_window.py` | 137 | `root` |
| `tests/test_owner_window.py` | 139 | `view` |
| `tests/test_owner_window.py` | 155 | `test_quit_after_real_startup_failure_releases_owner_and_retains_failure_exit(tmp_path, monkeypatch)` |
| `tests/test_owner_window.py` | 159 | `path` |
| `tests/test_owner_window.py` | 160 | `profile` |
| `tests/test_owner_window.py` | 165 | `actual_host` |
| `tests/test_owner_window.py` | 167 | `failed_host()` |
| `tests/test_owner_window.py` | 168 | `host` |
| `tests/test_owner_window.py` | 170 | `fail()` |
| `tests/test_owner_window.py` | 178 | `root` |
| `tests/test_owner_window.py` | 180 | `view` |
| `tests/test_owner_window.py` | 187 | `test_minimum_window_keeps_lifecycle_controls_visible_and_long_status_scrollable(window)` |
| `tests/test_owner_window.py` | 189 | `root` |
| `tests/test_owner_window.py` | 189 | `view` |
| `tests/test_owner_window.py` | 194 | `control` |
| `tests/test_owner_window.py` | 195 | `top` |
| `tests/test_portable_archive.py` | 17 | `APPLICATION` |
| `tests/test_portable_archive.py` | 21 | `test_roundtrip_keeps_one_application_root_and_metadata(tmp_path, suffix)` |
| `tests/test_portable_archive.py` | 23 | `bundle` |
| `tests/test_portable_archive.py` | 27 | `destination` |
| `tests/test_portable_archive.py` | 30 | `extracted` |
| `tests/test_portable_archive.py` | 38 | `test_posix_archive_keeps_relative_link_and_executable_mode(tmp_path)` |
| `tests/test_portable_archive.py` | 40 | `path` |
| `tests/test_portable_archive.py` | 41 | `output` |
| `tests/test_portable_archive.py` | 42 | `member` |
| `tests/test_portable_archive.py` | 45 | `link` |
| `tests/test_portable_archive.py` | 48 | `bundle` |
| `tests/test_portable_archive.py` | 68 | `test_member_escape_or_alias_is_rejected_before_writes(tmp_path, name)` |
| `tests/test_portable_archive.py` | 70 | `target` |
| `tests/test_portable_archive.py` | 71 | `output` |
| `tests/test_portable_archive.py` | 73 | `sentinel` |
| `tests/test_portable_archive.py` | 81 | `test_tar_link_escape_rejected_without_creating_links(tmp_path, target)` |
| `tests/test_portable_archive.py` | 83 | `path` |
| `tests/test_portable_archive.py` | 84 | `output` |
| `tests/test_portable_archive.py` | 85 | `member` |
| `tests/test_portable_archive.py` | 93 | `test_zip_symlink_and_duplicate_members_are_rejected(tmp_path)` |
| `tests/test_portable_archive.py` | 95 | `path` |
| `tests/test_portable_archive.py` | 96 | `output` |
| `tests/test_portable_archive.py` | 97 | `member` |
| `tests/test_portable_archive.py` | 102 | `path` |
| `tests/test_portable_archive.py` | 103 | `output` |
| `tests/test_portable_archive.py` | 104 | `_` |
| `tests/test_portable_archive.py` | 105 | `member` |
| `tests/test_portable_archive.py` | 111 | `test_member_content_and_metadata_budgets_are_checked(tmp_path, monkeypatch)` |
| `tests/test_portable_archive.py` | 113 | `path` |
| `tests/test_portable_archive.py` | 114 | `output` |
| `tests/test_portable_archive.py` | 120 | `path` |
| `tests/test_portable_archive.py` | 121 | `output` |
| `tests/test_processing.py` | 17 | `test_worker_real_and_failed_main(tmp_path, video, monkeypatch)` |
| `tests/test_processing.py` | 25 | `error` |
| `tests/test_processing.py` | 30 | `test_job_timeout_failure_and_no_partial_publication(client, imported, plan, app, monkeypatch)` |
| `tests/test_processing.py` | 32 | `path` |
| `tests/test_processing.py` | 34 | `timeout()` |
| `tests/test_processing.py` | 48 | `test_backpressure_low_disk_storage_error_and_import_rollback(client, login, app, monkeypatch)` |
| `tests/test_processing.py` | 56 | `real_usage` |
| `tests/test_processing.py` | 60 | `disk_failure(_p)` |
| `tests/test_processing.py` | 68 | `insert_failure()` |
| `tests/test_processing.py` | 77 | `test_store_cas_source_hash_revision_budget_and_immutability(client, processed, app, plan)` |
| `tests/test_processing.py` | 79 | `store` |
| `tests/test_processing.py` | 80 | `identifier` |
| `tests/test_processing.py` | 81 | `user` |
| `tests/test_processing.py` | 82 | `result` |
| `tests/test_processing.py` | 83 | `error` |
| `tests/test_processing.py` | 87 | `error` |
| `tests/test_processing.py` | 92 | `db` |
| `tests/test_processing.py` | 94 | `db` |
| `tests/test_processing.py` | 102 | `test_capacity_retention_dry_run_confirm_and_unexpected_files(client, processed, app)` |
| `tests/test_processing.py` | 104 | `store` |
| `tests/test_processing.py` | 105 | `identifier` |
| `tests/test_processing.py` | 106 | `folder` |
| `tests/test_processing.py` | 108 | `db` |
| `tests/test_processing.py` | 118 | `db` |
| `tests/test_processing.py` | 127 | `test_missing_media_and_source_changed_after_verified_work(client, imported, plan, app, monkeypatch)` |
| `tests/test_processing.py` | 131 | `original_run` |
| `tests/test_processing.py` | 133 | `changed()` |
| `tests/test_processing.py` | 135 | `result` |
| `tests/test_processing.py` | 145 | `test_review_race_and_readonly_review(client, processed, app, monkeypatch)` |
| `tests/test_processing.py` | 147 | `store` |
| `tests/test_processing.py` | 148 | `identifier` |
| `tests/test_processing.py` | 149 | `real_file` |
| `tests/test_processing.py` | 151 | `moved()` |
| `tests/test_processing.py` | 153 | `result` |
| `tests/test_processing.py` | 154 | `db` |
| `tests/test_processing.py` | 163 | `error` |
| `tests/test_publication_text.py` | 15 | `edition(root, name, main, text)` |
| `tests/test_publication_text.py` | 17 | `path` |
| `tests/test_publication_text.py` | 19 | `package` |
| `tests/test_publication_text.py` | 34 | `test_named_office_xml_remains_visible(tmp_path, name, main)` |
| `tests/test_publication_text.py` | 36 | `text` |
| `tests/test_publication_text.py` | 40 | `test_unknown_binary_is_not_an_exclusion(tmp_path)` |
| `tests/test_publication_text.py` | 42 | `path` |
| `tests/test_publication_text.py` | 47 | `test_missing_document_root_is_rejected(tmp_path)` |
| `tests/test_publication_text.py` | 53 | `test_invalid_zip_is_rejected(tmp_path)` |
| `tests/test_publication_text.py` | 55 | `path` |
| `tests/test_publication_text.py` | 62 | `test_invalid_utf8_xml_is_rejected(tmp_path)` |
| `tests/test_publication_text.py` | 68 | `test_expansion_budget_is_active(tmp_path)` |
| `tests/test_publication_text.py` | 70 | `path` |
| `tests/test_publication_text.py` | 78 | `test_active_or_embedded_payloads_are_not_reviewed_text(tmp_path, member)` |
| `tests/test_publication_text.py` | 80 | `path` |
| `tests/test_publication_text.py` | 81 | `package` |
| `tests/test_publication_text.py` | 88 | `test_actual_repository_guard_reads_credentials_inside_word(tmp_path, monkeypatch, part)` |
| `tests/test_publication_text.py` | 97 | `path` |
| `tests/test_publication_text.py` | 98 | `token` |
| `tests/test_publication_text.py` | 100 | `package` |
| `tests/test_publication_text.py` | 112 | `spec` |
| `tests/test_publication_text.py` | 116 | `checker` |
| `tests/test_runtime_notices.py` | 13 | `test_all_thirteen_actual_notice_contracts_in_one_fresh_owned_interpreter()` |
| `tests/test_runtime_notices.py` | 15 | `root` |
| `tests/test_runtime_notices.py` | 16 | `cases` |
| `tests/test_runtime_notices.py` | 17 | `temporary` |
| `tests/test_runtime_notices.py` | 18 | `result_path` |
| `tests/test_runtime_notices.py` | 19 | `result` |
| `tests/test_runtime_notices.py` | 35 | `records` |
| `tests/test_runtime_notices.py` | 37 | `item` |
| `tests/test_runtime_notices.py` | 38 | `item` |
| `tests/test_runtime_notices.py` | 39 | `receipt` |
| `tests/test_runtime_notices.py` | 41 | `item` |
| `tests/test_runtime_notices.py` | 52 | `target` |
| `tests/test_security.py` | 15 | `test_authentication_csrf_cookie_and_revocation(client, login, accounts, app)` |
| `tests/test_security.py` | 27 | `user` |
| `tests/test_security.py` | 29 | `cookie` |
| `tests/test_security.py` | 30 | `db` |
| `tests/test_security.py` | 41 | `response` |
| `tests/test_security.py` | 49 | `test_no_password_reflection_and_exact_host_origin(client, accounts)` |
| `tests/test_security.py` | 51 | `body` |
| `tests/test_security.py` | 52 | `response` |
| `tests/test_security.py` | 79 | `test_upload_auth_type_size_and_invalid_video(client, login)` |
| `tests/test_security.py` | 81 | `path` |
| `tests/test_security.py` | 100 | `test_expiry_role_recheck_and_cookie_bounds(client, login, app)` |
| `tests/test_security.py` | 103 | `db` |
| `tests/test_security.py` | 106 | `db` |
| `tests/test_security.py` | 114 | `test_persistent_login_throttle_and_concurrent_verification_gate(client, app, monkeypatch)` |
| `tests/test_security.py` | 116 | `db` |
| `tests/test_security.py` | 125 | `db` |
| `tests/test_security.py` | 128 | `Busy(class)` |
| `tests/test_security.py` | 131 | `acquire(self, blocking)` |
| `tests/test_security.py` | 142 | `test_attempt_and_session_bounds(client, login, app)` |
| `tests/test_security.py` | 144 | `db` |
| `tests/test_security.py` | 147 | `index` |
| `tests/test_security.py` | 153 | `db` |
| `tests/test_security.py` | 165 | `index` |
| `tests/test_security.py` | 169 | `db` |
| `tests/test_security.py` | 184 | `test_cli_user_validation(app, name, password, role)` |
| `tests/test_security.py` | 190 | `test_cli_user_duplicate_and_transaction_rollback(app)` |
| `tests/test_security.py` | 192 | `store` |
| `tests/test_security.py` | 197 | `failed_transaction()` |
| `tests/test_security.py` | 199 | `db` |
| `tests/test_security.py` | 204 | `db` |
| `tests/test_security.py` | 208 | `test_body_capacity_and_port_validation(client, monkeypatch, tmp_path)` |
| `tests/test_security.py` | 211 | `Busy(class)` |
| `tests/test_security.py` | 214 | `acquire(self, blocking)` |
| `tests/test_security.py` | 224 | `test_path_validation_and_symlink(app, tmp_path)` |
| `tests/test_security.py` | 226 | `store` |
| `tests/test_security.py` | 227 | `invalid` |
| `tests/test_security.py` | 230 | `path` |
| `tests/test_workflow.py` | 11 | `review(version)` |
| `tests/test_workflow.py` | 23 | `test_complete_private_workflow_and_independent_pixel_oracle(client, processed, login, app)` |
| `tests/test_workflow.py` | 25 | `identifier` |
| `tests/test_workflow.py` | 26 | `path` |
| `tests/test_workflow.py` | 31 | `exported` |
| `tests/test_workflow.py` | 35 | `receipt` |
| `tests/test_workflow.py` | 45 | `secret` |
| `tests/test_workflow.py` | 54 | `media` |
| `tests/test_workflow.py` | 56 | `frames` |
| `tests/test_workflow.py` | 58 | `frame` |
| `tests/test_workflow.py` | 58 | `index` |
| `tests/test_workflow.py` | 59 | `pixels` |
| `tests/test_workflow.py` | 63 | `trail` |
| `tests/test_workflow.py` | 65 | `e` |
| `tests/test_workflow.py` | 73 | `test_new_revision_invalidates_approval_and_stale_editor(client, processed, login, plan)` |
| `tests/test_workflow.py` | 75 | `path` |
| `tests/test_workflow.py` | 101 | `test_cross_operator_object_denial(client, imported, login, endpoint)` |
| `tests/test_workflow.py` | 108 | `test_role_and_independence_boundaries(client, imported, login, plan, app)` |
| `tests/test_workflow.py` | 110 | `path` |
| `tests/test_workflow.py` | 116 | `db` |
| `tests/test_workflow.py` | 122 | `test_review_cannot_skip_attestation(client, processed, login, change)` |
| `tests/test_workflow.py` | 125 | `path` |
| `tests/test_workflow.py` | 131 | `test_drift_blocks_approval_but_absent_is_explicit(client, imported, plan, login)` |
| `tests/test_workflow.py` | 133 | `path` |
| `tests/test_workflow.py` | 135 | `response` |
| `tests/test_workflow.py` | 141 | `test_expired_source_revision_history_and_download_denied(client, processed, app)` |
| `tests/test_workflow.py` | 143 | `path` |
| `tests/test_workflow.py` | 144 | `db` |
| `tests/test_workflow.py` | 147 | `suffix` |
| `tests/test_workflow.py` | 158 | `test_tampered_media_plan_and_source_fail_closed(client, processed, app, plan)` |
| `tests/test_workflow.py` | 160 | `identifier` |
| `tests/test_workflow.py` | 161 | `path` |
| `tests/test_workflow.py` | 162 | `folder` |
| `tests/test_workflow.py` | 170 | `db` |
| `tests/test_workflow.py` | 176 | `test_range_requests_private_headers_and_no_original_endpoint(client, imported)` |
| `tests/test_workflow.py` | 178 | `path` |
| `tests/test_workflow.py` | 179 | `response` |
| `tests/test_workflow.py` | 183 | `suffix` |
| `tests/test_workflow.py` | 189 | `test_invalid_clip_unknown_scenario_and_unprocessed_download(client, imported, plan)` |
| `tools/audit_osv.py` | 17 | `ROOT` |
| `tools/audit_osv.py` | 18 | `VERSION` |
| `tools/audit_osv.py` | 19 | `BINARIES` |
| `tools/audit_osv.py` | 47 | `expected_packages(lock)` |
| `tools/audit_osv.py` | 51 | `expected` |
| `tools/audit_osv.py` | 52 | `location` |
| `tools/audit_osv.py` | 52 | `package` |
| `tools/audit_osv.py` | 55 | `name` |
| `tools/audit_osv.py` | 56 | `version` |
| `tools/audit_osv.py` | 73 | `verify_report(report, expected)` |
| `tools/audit_osv.py` | 81 | `scanned` |
| `tools/audit_osv.py` | 82 | `result` |
| `tools/audit_osv.py` | 83 | `source` |
| `tools/audit_osv.py` | 91 | `item` |
| `tools/audit_osv.py` | 92 | `package` |
| `tools/audit_osv.py` | 99 | `findings` |
| `tools/audit_osv.py` | 108 | `main()` |
| `tools/audit_osv.py` | 110 | `checksum` |
| `tools/audit_osv.py` | 110 | `name` |
| `tools/audit_osv.py` | 111 | `directory` |
| `tools/audit_osv.py` | 113 | `binary` |
| `tools/audit_osv.py` | 115 | `url` |
| `tools/audit_osv.py` | 116 | `output` |
| `tools/audit_osv.py` | 116 | `response` |
| `tools/audit_osv.py` | 117 | `chunk` |
| `tools/audit_osv.py` | 122 | `config` |
| `tools/audit_osv.py` | 125 | `expected` |
| `tools/audit_osv.py` | 128 | `report` |
| `tools/audit_osv.py` | 129 | `command` |
| `tools/audit_osv.py` | 139 | `result` |
| `tools/audit_osv.py` | 144 | `scanned` |
| `tools/benchmark.py` | 16 | `main()` |
| `tools/benchmark.py` | 18 | `root` |
| `tools/benchmark.py` | 20 | `directory` |
| `tools/benchmark.py` | 21 | `path` |
| `tools/benchmark.py` | 23 | `masks` |
| `tools/benchmark.py` | 27 | `durations` |
| `tools/benchmark.py` | 28 | `_` |
| `tools/benchmark.py` | 29 | `start` |
| `tools/benchmark.py` | 30 | `info` |
| `tools/benchmark.py` | 33 | `report` |
| `tools/browser_server.py` | 15 | `prepare(directory)` |
| `tools/browser_server.py` | 18 | `db` |
| `tools/browser_server.py` | 19 | `credentials` |
| `tools/browser_server.py` | 20 | `store` |
| `tools/browser_server.py` | 22 | `values` |
| `tools/browser_server.py` | 24 | `role` |
| `tools/browser_server.py` | 26 | `entry` |
| `tools/browser_server.py` | 26 | `role` |
| `tools/browser_server.py` | 32 | `main()` |
| `tools/browser_server.py` | 34 | `parser` |
| `tools/browser_server.py` | 37 | `args` |
| `tools/browser_server.py` | 38 | `db` |
| `tools/check_repo.py` | 10 | `main()` |
| `tools/check_repo.py` | 12 | `path` |
| `tools/check_repo.py` | 13 | `relative` |
| `tools/check_repo.py` | 14 | `content` |
| `tools/check_repo.py` | 32 | `ref` |
| `tools/check_repo.py` | 35 | `budget` |
| `tools/check_repo.py` | 35 | `suffix` |
| `tools/check_repo.py` | 36 | `size` |
| `tools/check_repo.py` | 37 | `p` |
| `tools/docs_index.py` | 18 | `ROOT` |
| `tools/docs_index.py` | 19 | `EXCLUDE` |
| `tools/docs_index.py` | 33 | `SPECIAL` |
| `tools/docs_index.py` | 55 | `files()` |
| `tools/docs_index.py` | 57 | `result` |
| `tools/docs_index.py` | 58 | `children` |
| `tools/docs_index.py` | 58 | `directory` |
| `tools/docs_index.py` | 58 | `names` |
| `tools/docs_index.py` | 59 | `child` |
| `tools/docs_index.py` | 60 | `name` |
| `tools/docs_index.py` | 66 | `render()` |
| `tools/docs_index.py` | 68 | `catalog` |
| `tools/docs_index.py` | 76 | `source` |
| `tools/docs_index.py` | 85 | `path` |
| `tools/docs_index.py` | 86 | `relative` |
| `tools/docs_index.py` | 87 | `content` |
| `tools/docs_index.py` | 88 | `description` |
| `tools/docs_index.py` | 91 | `line` |
| `tools/docs_index.py` | 99 | `records` |
| `tools/docs_index.py` | 101 | `node` |
| `tools/docs_index.py` | 103 | `args` |
| `tools/docs_index.py` | 106 | `a` |
| `tools/docs_index.py` | 114 | `line` |
| `tools/docs_index.py` | 114 | `value` |
| `tools/docs_index.py` | 117 | `line` |
| `tools/docs_index.py` | 117 | `name` |
| `tools/docs_index.py` | 118 | `node` |
| `tools/docs_index.py` | 132 | `main()` |
| `tools/docs_index.py` | 134 | `content` |
| `tools/docs_index.py` | 134 | `relative` |
| `tools/docs_index.py` | 135 | `path` |
| `tools/package_app.py` | 28 | `ROOT` |
| `tools/package_app.py` | 29 | `APPLICATION` |
| `tools/package_app.py` | 30 | `PRODUCT` |
| `tools/package_app.py` | 33 | `build_python_supported(version, releaselevel)` |
| `tools/package_app.py` | 43 | `configuration(root)` |
| `tools/package_app.py` | 45 | `project` |
| `tools/package_app.py` | 46 | `package` |
| `tools/package_app.py` | 47 | `lock` |
| `tools/package_app.py` | 48 | `version` |
| `tools/package_app.py` | 62 | `source_metadata(version)` |
| `tools/package_app.py` | 68 | `command` |
| `tools/package_app.py` | 69 | `source` |
| `tools/package_app.py` | 70 | `changed` |
| `tools/package_app.py` | 92 | `codec_free_inventory(bundle, modules)` |
| `tools/package_app.py` | 94 | `modules` |
| `tools/package_app.py` | 96 | `name` |
| `tools/package_app.py` | 99 | `files` |
| `tools/package_app.py` | 100 | `path` |
| `tools/package_app.py` | 101 | `relative` |
| `tools/package_app.py` | 105 | `part` |
| `tools/package_app.py` | 121 | `main(argv)` |
| `tools/package_app.py` | 123 | `parser` |
| `tools/package_app.py` | 130 | `args` |
| `tools/package_app.py` | 150 | `version` |
| `tools/package_app.py` | 151 | `notices` |
| `tools/package_app.py` | 151 | `versions` |
| `tools/package_app.py` | 152 | `metadata` |
| `tools/package_app.py` | 154 | `generated` |
| `tools/package_app.py` | 156 | `identity_file` |
| `tools/package_app.py` | 158 | `notice_file` |
| `tools/package_app.py` | 160 | `pyinstaller` |
| `tools/package_app.py` | 161 | `licenses` |
| `tools/package_app.py` | 163 | `path` |
| `tools/package_app.py` | 167 | `build` |
| `tools/package_app.py` | 168 | `command` |
| `tools/package_app.py` | 187 | `destination` |
| `tools/package_app.py` | 187 | `source` |
| `tools/package_app.py` | 198 | `source_path` |
| `tools/package_app.py` | 200 | `source_path` |
| `tools/package_app.py` | 201 | `command` |
| `tools/package_app.py` | 202 | `hidden` |
| `tools/package_app.py` | 207 | `command` |
| `tools/package_app.py` | 208 | `command` |
| `tools/package_app.py` | 209 | `environment` |
| `tools/package_app.py` | 215 | `bundle` |
| `tools/package_app.py` | 218 | `executable` |
| `tools/package_app.py` | 219 | `embedded` |
| `tools/package_app.py` | 220 | `codec_inventory` |
| `tools/package_app.py` | 222 | `suffix` |
| `tools/package_app.py` | 223 | `name` |
| `tools/package_app.py` | 224 | `output` |
| `tools/package_app.py` | 230 | `archive` |
| `tools/package_app.py` | 230 | `sidecar` |
| `tools/package_app.py` | 234 | `temporary` |
| `tools/package_app.py` | 235 | `extracted` |
| `tools/package_app.py` | 236 | `executable` |
| `tools/package_app.py` | 251 | `stream` |
| `tools/package_app.py` | 252 | `digest` |
| `tools/portable_archive.py` | 17 | `MAX_BYTES` |
| `tools/portable_archive.py` | 18 | `MAX_MEMBERS` |
| `tools/portable_archive.py` | 21 | `require(condition, message)` |
| `tools/portable_archive.py` | 27 | `safe_name(name, application)` |
| `tools/portable_archive.py` | 29 | `parts` |
| `tools/portable_archive.py` | 30 | `raw_parts` |
| `tools/portable_archive.py` | 38 | `part` |
| `tools/portable_archive.py` | 39 | `char` |
| `tools/portable_archive.py` | 44 | `safe_link(name, target, application)` |
| `tools/portable_archive.py` | 51 | `char` |
| `tools/portable_archive.py` | 54 | `resolved` |
| `tools/portable_archive.py` | 60 | `create_archive(bundle, archive)` |
| `tools/portable_archive.py` | 66 | `members` |
| `tools/portable_archive.py` | 68 | `total` |
| `tools/portable_archive.py` | 69 | `path` |
| `tools/portable_archive.py` | 78 | `total` |
| `tools/portable_archive.py` | 82 | `path` |
| `tools/portable_archive.py` | 84 | `target` |
| `tools/portable_archive.py` | 85 | `path` |
| `tools/portable_archive.py` | 88 | `target` |
| `tools/portable_archive.py` | 89 | `path` |
| `tools/portable_archive.py` | 97 | `inspected(archive, application)` |
| `tools/portable_archive.py` | 102 | `members` |
| `tools/portable_archive.py` | 103 | `total` |
| `tools/portable_archive.py` | 104 | `names` |
| `tools/portable_archive.py` | 106 | `source` |
| `tools/portable_archive.py` | 107 | `member` |
| `tools/portable_archive.py` | 111 | `total` |
| `tools/portable_archive.py` | 112 | `kind` |
| `tools/portable_archive.py` | 114 | `source` |
| `tools/portable_archive.py` | 115 | `member` |
| `tools/portable_archive.py` | 124 | `total` |
| `tools/portable_archive.py` | 129 | `kind` |
| `tools/portable_archive.py` | 136 | `member` |
| `tools/portable_archive.py` | 137 | `name` |
| `tools/portable_archive.py` | 143 | `archive_metadata(archive, application)` |
| `tools/portable_archive.py` | 145 | `kind` |
| `tools/portable_archive.py` | 145 | `members` |
| `tools/portable_archive.py` | 146 | `expected` |
| `tools/portable_archive.py` | 147 | `m` |
| `tools/portable_archive.py` | 147 | `selected` |
| `tools/portable_archive.py` | 149 | `member` |
| `tools/portable_archive.py` | 150 | `size` |
| `tools/portable_archive.py` | 155 | `source` |
| `tools/portable_archive.py` | 156 | `value` |
| `tools/portable_archive.py` | 158 | `source` |
| `tools/portable_archive.py` | 159 | `stream` |
| `tools/portable_archive.py` | 161 | `value` |
| `tools/portable_archive.py` | 166 | `extract_archive(archive, destination, application)` |
| `tools/portable_archive.py` | 168 | `kind` |
| `tools/portable_archive.py` | 168 | `members` |
| `tools/portable_archive.py` | 171 | `source` |
| `tools/portable_archive.py` | 172 | `member` |
| `tools/portable_archive.py` | 173 | `target` |
| `tools/portable_archive.py` | 178 | `total` |
| `tools/portable_archive.py` | 179 | `incoming` |
| `tools/portable_archive.py` | 179 | `outgoing` |
| `tools/portable_archive.py` | 180 | `chunk` |
| `tools/portable_archive.py` | 181 | `total` |
| `tools/portable_archive.py` | 186 | `source` |
| `tools/portable_archive.py` | 188 | `bundle` |
| `tools/portable_archive.py` | 190 | `path` |
| `tools/publication_text.py` | 11 | `EDITION_ROOTS` |
| `tools/publication_text.py` | 16 | `MAX_PACKAGE_BYTES` |
| `tools/publication_text.py` | 17 | `MAX_EXPANDED_BYTES` |
| `tools/publication_text.py` | 18 | `MAX_MEMBER_BYTES` |
| `tools/publication_text.py` | 19 | `MAX_MEMBERS` |
| `tools/publication_text.py` | 22 | `public_text(path, root)` |
| `tools/publication_text.py` | 24 | `relative` |
| `tools/publication_text.py` | 28 | `source` |
| `tools/publication_text.py` | 31 | `package` |
| `tools/publication_text.py` | 32 | `members` |
| `tools/publication_text.py` | 33 | `member` |
| `tools/publication_text.py` | 33 | `names` |
| `tools/publication_text.py` | 38 | `member` |
| `tools/publication_text.py` | 40 | `result` |
| `tools/publication_text.py` | 41 | `member` |
| `tools/publication_text.py` | 51 | `stream` |
| `tools/publication_text.py` | 52 | `payload` |
| `tools/runtime_notices.py` | 10 | `UPSTREAM_904` |
| `tools/runtime_notices.py` | 22 | `notice_paths(info)` |
| `tools/runtime_notices.py` | 26 | `path` |
| `tools/runtime_notices.py` | 30 | `part` |
| `tools/runtime_notices.py` | 36 | `read_tcl_notice(interpreter, path)` |
| `tools/runtime_notices.py` | 41 | `channel` |
| `tools/runtime_notices.py` | 43 | `code` |
| `tools/runtime_notices.py` | 48 | `raw` |
| `tools/runtime_notices.py` | 51 | `raw` |
| `tools/runtime_notices.py` | 57 | `gui_notice(interpreter, root, kind, version, library, system)` |
| `tools/runtime_notices.py` | 59 | `system` |
| `tools/runtime_notices.py` | 72 | `path` |
| `tools/runtime_notices.py` | 74 | `framework` |
| `tools/runtime_notices.py` | 77 | `commit` |
| `tools/runtime_notices.py` | 77 | `expected` |
| `tools/runtime_notices.py` | 78 | `stream` |
| `tools/runtime_notices.py` | 79 | `raw` |
| `tools/runtime_notices.py` | 95 | `stream` |
| `tools/runtime_notices.py` | 96 | `raw` |
| `tools/runtime_notices.py` | 110 | `collect(root)` |
| `tools/runtime_notices.py` | 114 | `window` |
| `tools/runtime_notices.py` | 117 | `versions` |
| `tools/runtime_notices.py` | 121 | `value` |
| `tools/runtime_notices.py` | 123 | `blocks` |
| `tools/runtime_notices.py` | 124 | `kind` |
| `tools/runtime_notices.py` | 124 | `library` |
| `tools/runtime_notices.py` | 124 | `version` |
| `tools/runtime_notices.py` | 128 | `provenance` |
| `tools/runtime_notices.py` | 128 | `raw` |
| `tools/runtime_notices.py` | 134 | `names` |
| `tools/runtime_notices.py` | 139 | `name` |
| `tools/runtime_notices.py` | 140 | `info` |
| `tools/runtime_notices.py` | 141 | `files` |
| `tools/runtime_notices.py` | 144 | `path` |
| `tools/runtime_notices.py` | 145 | `stream` |
| `tools/runtime_notices.py` | 146 | `raw` |
| `tools/runtime_notices.py` | 153 | `raw` |
| `tools/runtime_notices.py` | 153 | `title` |
| `tools/smoke_app.py` | 22 | `ROOT` |
| `tools/smoke_app.py` | 26 | `require(condition, message)` |
| `tools/smoke_app.py` | 32 | `request(url, path)` |
| `tools/smoke_app.py` | 34 | `target` |
| `tools/smoke_app.py` | 43 | `connection` |
| `tools/smoke_app.py` | 46 | `response` |
| `tools/smoke_app.py` | 47 | `raw` |
| `tools/smoke_app.py` | 57 | `main(argv)` |
| `tools/smoke_app.py` | 62 | `parser` |
| `tools/smoke_app.py` | 65 | `args` |
| `tools/smoke_app.py` | 66 | `executable` |
| `tools/smoke_app.py` | 67 | `expected` |
| `tools/smoke_app.py` | 75 | `output` |
| `tools/smoke_app.py` | 77 | `node` |
| `tools/smoke_app.py` | 79 | `profile_directory` |
| `tools/smoke_app.py` | 80 | `password` |
| `tools/smoke_app.py` | 84 | `allowed` |
| `tools/smoke_app.py` | 100 | `environment` |
| `tools/smoke_app.py` | 100 | `key` |
| `tools/smoke_app.py` | 100 | `value` |
| `tools/smoke_app.py` | 110 | `diagnostic` |
| `tools/smoke_app.py` | 119 | `lines` |
| `tools/smoke_app.py` | 120 | `line` |
| `tools/smoke_app.py` | 123 | `actual_runtime` |
| `tools/smoke_app.py` | 126 | `key` |
| `tools/smoke_app.py` | 131 | `setup` |
| `tools/smoke_app.py` | 149 | `pin` |
| `tools/smoke_app.py` | 172 | `profile` |
| `tools/smoke_app.py` | 173 | `expected_cookie` |
| `tools/smoke_app.py` | 175 | `role` |
| `tools/smoke_app.py` | 179 | `process` |
| `tools/smoke_app.py` | 189 | `events` |
| `tools/smoke_app.py` | 190 | `log` |
| `tools/smoke_app.py` | 192 | `read_output()` |
| `tools/smoke_app.py` | 195 | `line` |
| `tools/smoke_app.py` | 201 | `reader` |
| `tools/smoke_app.py` | 203 | `actual_exit` |
| `tools/smoke_app.py` | 203 | `forced` |
| `tools/smoke_app.py` | 203 | `passed` |
| `tools/smoke_app.py` | 203 | `url` |
| `tools/smoke_app.py` | 205 | `deadline` |
| `tools/smoke_app.py` | 207 | `remaining` |
| `tools/smoke_app.py` | 209 | `line` |
| `tools/smoke_app.py` | 212 | `ready` |
| `tools/smoke_app.py` | 219 | `url` |
| `tools/smoke_app.py` | 220 | `code` |
| `tools/smoke_app.py` | 220 | `raw` |
| `tools/smoke_app.py` | 267 | `receipt` |
| `tools/smoke_app.py` | 268 | `exported` |
| `tools/smoke_app.py` | 275 | `media` |
| `tools/smoke_app.py` | 285 | `frames` |
| `tools/smoke_app.py` | 287 | `frame` |
| `tools/smoke_app.py` | 287 | `index` |
| `tools/smoke_app.py` | 288 | `pixels` |
| `tools/smoke_app.py` | 318 | `actual_exit` |
| `tools/smoke_app.py` | 324 | `target` |
| `tools/smoke_app.py` | 326 | `connection` |
| `tools/smoke_app.py` | 332 | `reopened` |
| `tools/smoke_app.py` | 341 | `line` |
| `tools/smoke_app.py` | 343 | `passed` |
| `tools/smoke_app.py` | 351 | `forced` |
| `workbench/__init__.py` | 3 | `__version__` |
| `workbench/__main__.py` | 15 | `main()` |
| `workbench/__main__.py` | 17 | `parser` |
| `workbench/__main__.py` | 19 | `commands` |
| `workbench/__main__.py` | 21 | `cleanup` |
| `workbench/__main__.py` | 23 | `user` |
| `workbench/__main__.py` | 26 | `serve` |
| `workbench/__main__.py` | 28 | `args` |
| `workbench/__main__.py` | 29 | `store` |
| `workbench/__main__.py` | 35 | `password` |
| `workbench/api.py` | 23 | `HEADERS` |
| `workbench/api.py` | 31 | `BODY_GATE` |
| `workbench/api.py` | 34 | `create_app(database, port)` |
| `workbench/api.py` | 40 | `authority` |
| `workbench/api.py` | 40 | `origin` |
| `workbench/api.py` | 41 | `app` |
| `workbench/api.py` | 48 | `boundary(request, call_next)` |
| `workbench/api.py` | 50 | `acquired` |
| `workbench/api.py` | 50 | `response` |
| `workbench/api.py` | 66 | `media` |
| `workbench/api.py` | 67 | `expected` |
| `workbench/api.py` | 72 | `acquired` |
| `workbench/api.py` | 73 | `data` |
| `workbench/api.py` | 75 | `chunk` |
| `workbench/api.py` | 80 | `response` |
| `workbench/api.py` | 82 | `response` |
| `workbench/api.py` | 84 | `response` |
| `workbench/api.py` | 92 | `invalid(_request, error)` |
| `workbench/api.py` | 97 | `e` |
| `workbench/api.py` | 103 | `health()` |
| `workbench/api.py` | 116 | `login(body, request)` |
| `workbench/api.py` | 118 | `token` |
| `workbench/api.py` | 118 | `user` |
| `workbench/api.py` | 119 | `response` |
| `workbench/api.py` | 124 | `me(request)` |
| `workbench/api.py` | 129 | `logout(request)` |
| `workbench/api.py` | 132 | `response` |
| `workbench/api.py` | 137 | `clips(request)` |
| `workbench/api.py` | 142 | `upload(request, title, purpose, retention)` |
| `workbench/api.py` | 149 | `user` |
| `workbench/api.py` | 150 | `data` |
| `workbench/api.py` | 156 | `example(scenario, request)` |
| `workbench/api.py` | 168 | `clip(identifier, request)` |
| `workbench/api.py` | 173 | `history(identifier, request)` |
| `workbench/api.py` | 178 | `process(identifier, body, request)` |
| `workbench/api.py` | 183 | `motion_draft(identifier, body, request)` |
| `workbench/api.py` | 185 | `user` |
| `workbench/api.py` | 188 | `saved` |
| `workbench/api.py` | 192 | `masks` |
| `workbench/api.py` | 200 | `mask` |
| `workbench/api.py` | 205 | `review(identifier, body, request)` |
| `workbench/api.py` | 207 | `user` |
| `workbench/api.py` | 212 | `media(identifier, kind, request, version)` |
| `workbench/api.py` | 219 | `path` |
| `workbench/api.py` | 227 | `manifest(identifier, request)` |
| `workbench/api.py` | 235 | `frame(identifier, kind, request, version, index)` |
| `workbench/api.py` | 251 | `index()` |
| `workbench/auth.py` | 17 | `HASHER` |
| `workbench/auth.py` | 18 | `DUMMY` |
| `workbench/auth.py` | 19 | `VERIFY_GATE` |
| `workbench/auth.py` | 22 | `add_user(store, username, password, role)` |
| `workbench/auth.py` | 32 | `hashed` |
| `workbench/auth.py` | 33 | `db` |
| `workbench/auth.py` | 37 | `sign_in(request, username, password)` |
| `workbench/auth.py` | 39 | `store` |
| `workbench/auth.py` | 40 | `now` |
| `workbench/auth.py` | 41 | `client` |
| `workbench/auth.py` | 44 | `db` |
| `workbench/auth.py` | 46 | `row` |
| `workbench/auth.py` | 55 | `user` |
| `workbench/auth.py` | 66 | `csrf` |
| `workbench/auth.py` | 66 | `token` |
| `workbench/auth.py` | 67 | `db` |
| `workbench/auth.py` | 80 | `session_cookie_name(request)` |
| `workbench/auth.py` | 85 | `identity(request)` |
| `workbench/auth.py` | 87 | `token` |
| `workbench/auth.py` | 90 | `db` |
| `workbench/auth.py` | 91 | `row` |
| `workbench/auth.py` | 100 | `authorize(request, role)` |
| `workbench/auth.py` | 102 | `user` |
| `workbench/auth.py` | 112 | `sign_out(request)` |
| `workbench/auth.py` | 115 | `db` |
| `workbench/codec_setup.py` | 27 | `PRODUCT` |
| `workbench/codec_setup.py` | 28 | `VERSION` |
| `workbench/codec_setup.py` | 29 | `DIST` |
| `workbench/codec_setup.py` | 30 | `MAX_WHEEL` |
| `workbench/codec_setup.py` | 31 | `MAX_MEMBER` |
| `workbench/codec_setup.py` | 32 | `MAX_EXPANDED` |
| `workbench/codec_setup.py` | 33 | `MAX_MEMBERS` |
| `workbench/codec_setup.py` | 34 | `STORE_ID` |
| `workbench/codec_setup.py` | 37 | `require(condition, message)` |
| `workbench/codec_setup.py` | 43 | `bounded_file(path, limit)` |
| `workbench/codec_setup.py` | 46 | `descriptor` |
| `workbench/codec_setup.py` | 53 | `stream` |
| `workbench/codec_setup.py` | 54 | `info` |
| `workbench/codec_setup.py` | 59 | `raw` |
| `workbench/codec_setup.py` | 67 | `pins()` |
| `workbench/codec_setup.py` | 69 | `root` |
| `workbench/codec_setup.py` | 70 | `value` |
| `workbench/codec_setup.py` | 81 | `row` |
| `workbench/codec_setup.py` | 99 | `selected_pin()` |
| `workbench/codec_setup.py` | 101 | `system` |
| `workbench/codec_setup.py` | 102 | `machine` |
| `workbench/codec_setup.py` | 103 | `python` |
| `workbench/codec_setup.py` | 104 | `gil_disabled` |
| `workbench/codec_setup.py` | 111 | `key` |
| `workbench/codec_setup.py` | 114 | `family` |
| `workbench/codec_setup.py` | 114 | `version` |
| `workbench/codec_setup.py` | 120 | `version` |
| `workbench/codec_setup.py` | 128 | `dependency_home()` |
| `workbench/codec_setup.py` | 130 | `explicit` |
| `workbench/codec_setup.py` | 132 | `result` |
| `workbench/codec_setup.py` | 135 | `base` |
| `workbench/codec_setup.py` | 137 | `base` |
| `workbench/codec_setup.py` | 139 | `base` |
| `workbench/codec_setup.py` | 140 | `result` |
| `workbench/codec_setup.py` | 151 | `store(home)` |
| `workbench/codec_setup.py` | 160 | `marker` |
| `workbench/codec_setup.py` | 167 | `output` |
| `workbench/codec_setup.py` | 176 | `wheel_members(raw, pin)` |
| `workbench/codec_setup.py` | 182 | `archive` |
| `workbench/codec_setup.py` | 183 | `items` |
| `workbench/codec_setup.py` | 185 | `x` |
| `workbench/codec_setup.py` | 188 | `files` |
| `workbench/codec_setup.py` | 188 | `total` |
| `workbench/codec_setup.py` | 189 | `item` |
| `workbench/codec_setup.py` | 192 | `mode` |
| `workbench/codec_setup.py` | 192 | `name` |
| `workbench/codec_setup.py` | 193 | `path` |
| `workbench/codec_setup.py` | 199 | `part` |
| `workbench/codec_setup.py` | 210 | `total` |
| `workbench/codec_setup.py` | 215 | `member` |
| `workbench/codec_setup.py` | 216 | `data` |
| `workbench/codec_setup.py` | 222 | `required` |
| `workbench/codec_setup.py` | 230 | `metadata` |
| `workbench/codec_setup.py` | 231 | `wheel` |
| `workbench/codec_setup.py` | 240 | `records` |
| `workbench/codec_setup.py` | 242 | `row` |
| `workbench/codec_setup.py` | 244 | `row` |
| `workbench/codec_setup.py` | 247 | `digest` |
| `workbench/codec_setup.py` | 247 | `name` |
| `workbench/codec_setup.py` | 247 | `size` |
| `workbench/codec_setup.py` | 251 | `expected` |
| `workbench/codec_setup.py` | 261 | `NoRedirect(class)` |
| `workbench/codec_setup.py` | 264 | `redirect_request(self, req, fp, code, msg, headers, newurl)` |
| `workbench/codec_setup.py` | 268 | `download(pin)` |
| `workbench/codec_setup.py` | 270 | `opener` |
| `workbench/codec_setup.py` | 273 | `deadline` |
| `workbench/codec_setup.py` | 274 | `response` |
| `workbench/codec_setup.py` | 276 | `output` |
| `workbench/codec_setup.py` | 277 | `chunk` |
| `workbench/codec_setup.py` | 283 | `raw` |
| `workbench/codec_setup.py` | 288 | `pointer_name(pin)` |
| `workbench/codec_setup.py` | 293 | `installed(home, pin)` |
| `workbench/codec_setup.py` | 297 | `pointer` |
| `workbench/codec_setup.py` | 301 | `value` |
| `workbench/codec_setup.py` | 310 | `directory` |
| `workbench/codec_setup.py` | 318 | `files` |
| `workbench/codec_setup.py` | 319 | `site` |
| `workbench/codec_setup.py` | 327 | `expected_directories` |
| `workbench/codec_setup.py` | 329 | `name` |
| `workbench/codec_setup.py` | 330 | `parent` |
| `workbench/codec_setup.py` | 333 | `actual` |
| `workbench/codec_setup.py` | 333 | `pending` |
| `workbench/codec_setup.py` | 333 | `visited` |
| `workbench/codec_setup.py` | 335 | `current` |
| `workbench/codec_setup.py` | 340 | `entries` |
| `workbench/codec_setup.py` | 341 | `entry` |
| `workbench/codec_setup.py` | 342 | `visited` |
| `workbench/codec_setup.py` | 347 | `path` |
| `workbench/codec_setup.py` | 348 | `name` |
| `workbench/codec_setup.py` | 359 | `info` |
| `workbench/codec_setup.py` | 369 | `name` |
| `workbench/codec_setup.py` | 369 | `raw` |
| `workbench/codec_setup.py` | 374 | `install(home, pin)` |
| `workbench/codec_setup.py` | 377 | `pointer` |
| `workbench/codec_setup.py` | 382 | `raw` |
| `workbench/codec_setup.py` | 383 | `files` |
| `workbench/codec_setup.py` | 384 | `directory` |
| `workbench/codec_setup.py` | 385 | `published` |
| `workbench/codec_setup.py` | 388 | `data` |
| `workbench/codec_setup.py` | 388 | `name` |
| `workbench/codec_setup.py` | 389 | `path` |
| `workbench/codec_setup.py` | 391 | `output` |
| `workbench/codec_setup.py` | 395 | `final` |
| `workbench/codec_setup.py` | 397 | `directory` |
| `workbench/codec_setup.py` | 398 | `pending` |
| `workbench/codec_setup.py` | 407 | `published` |
| `workbench/codec_setup.py` | 421 | `activate(home, pin)` |
| `workbench/codec_setup.py` | 423 | `site` |
| `workbench/codec_setup.py` | 431 | `av` |
| `workbench/codec_window.py` | 10 | `TERMS` |
| `workbench/codec_window.py` | 20 | `DependencyWindow(class)` |
| `workbench/codec_window.py` | 23 | `__init__(self, root, home, pin)` |
| `workbench/codec_window.py` | 32 | `shell` |
| `workbench/codec_window.py` | 34 | `actions` |
| `workbench/codec_window.py` | 51 | `scrollbar` |
| `workbench/codec_window.py` | 62 | `install(self)` |
| `workbench/codec_window.py` | 72 | `run()` |
| `workbench/codec_window.py` | 84 | `poll(self)` |
| `workbench/codec_window.py` | 90 | `error` |
| `workbench/codec_window.py` | 102 | `cancel(self)` |
| `workbench/codec_window.py` | 112 | `description(pin)` |
| `workbench/codec_window.py` | 121 | `ensure()` |
| `workbench/codec_window.py` | 123 | `home` |
| `workbench/codec_window.py` | 123 | `pin` |
| `workbench/codec_window.py` | 136 | `root` |
| `workbench/codec_window.py` | 137 | `window` |
| `workbench/desktop.py` | 21 | `ROOT` |
| `workbench/desktop.py` | 24 | `read_resource(path)` |
| `workbench/desktop.py` | 26 | `descriptor` |
| `workbench/desktop.py` | 29 | `stream` |
| `workbench/desktop.py` | 30 | `info` |
| `workbench/desktop.py` | 33 | `raw` |
| `workbench/desktop.py` | 39 | `identity(root)` |
| `workbench/desktop.py` | 42 | `value` |
| `workbench/desktop.py` | 61 | `console_session(directory, metadata)` |
| `workbench/desktop.py` | 63 | `profile` |
| `workbench/desktop.py` | 64 | `host` |
| `workbench/desktop.py` | 68 | `host` |
| `workbench/desktop.py` | 75 | `line` |
| `workbench/desktop.py` | 90 | `main(argv)` |
| `workbench/desktop.py` | 92 | `parser` |
| `workbench/desktop.py` | 107 | `args` |
| `workbench/desktop.py` | 111 | `metadata` |
| `workbench/desktop.py` | 116 | `root` |
| `workbench/desktop.py` | 119 | `versions` |
| `workbench/desktop.py` | 124 | `directory` |
| `workbench/desktop.py` | 132 | `root` |
| `workbench/desktop.py` | 133 | `window` |
| `workbench/desktop_host.py` | 16 | `OwnedServer(class)` |
| `workbench/desktop_host.py` | 19 | `__init__(self, config, ready, record)` |
| `workbench/desktop_host.py` | 25 | `startup(self, sockets)` |
| `workbench/desktop_host.py` | 34 | `Host(class)` |
| `workbench/desktop_host.py` | 37 | `__init__(self, profile, metadata)` |
| `workbench/desktop_host.py` | 54 | `app` |
| `workbench/desktop_host.py` | 56 | `config` |
| `workbench/desktop_host.py` | 76 | `_run(self)` |
| `workbench/desktop_host.py` | 89 | `start(self, timeout)` |
| `workbench/desktop_host.py` | 97 | `stop(self, timeout)` |
| `workbench/desktop_profile.py` | 17 | `PRODUCT` |
| `workbench/desktop_profile.py` | 18 | `ROLES` |
| `workbench/desktop_profile.py` | 19 | `FIRST_ROLE` |
| `workbench/desktop_profile.py` | 22 | `default_directory()` |
| `workbench/desktop_profile.py` | 25 | `base` |
| `workbench/desktop_profile.py` | 27 | `base` |
| `workbench/desktop_profile.py` | 29 | `base` |
| `workbench/desktop_profile.py` | 35 | `read_marker(path)` |
| `workbench/desktop_profile.py` | 37 | `descriptor` |
| `workbench/desktop_profile.py` | 38 | `stream` |
| `workbench/desktop_profile.py` | 39 | `info` |
| `workbench/desktop_profile.py` | 42 | `raw` |
| `workbench/desktop_profile.py` | 45 | `value` |
| `workbench/desktop_profile.py` | 57 | `Profile(class)` |
| `workbench/desktop_profile.py` | 60 | `__init__(self, directory)` |
| `workbench/desktop_profile.py` | 66 | `marker` |
| `workbench/desktop_profile.py` | 70 | `stream` |
| `workbench/desktop_profile.py` | 74 | `namespace` |
| `workbench/desktop_profile.py` | 76 | `lock` |
| `workbench/desktop_profile.py` | 96 | `database` |
| `workbench/desktop_profile.py` | 105 | `count_users(self)` |
| `workbench/desktop_profile.py` | 107 | `database` |
| `workbench/desktop_profile.py` | 110 | `create_account(self, username, password, confirmation, role)` |
| `workbench/desktop_profile.py` | 120 | `close(self)` |
| `workbench/media.py` | 20 | `MAX_BYTES` |
| `workbench/media.py` | 21 | `MAX_FRAMES` |
| `workbench/media.py` | 22 | `MAX_PIXELS` |
| `workbench/media.py` | 23 | `MAX_OUTPUT` |
| `workbench/media.py` | 26 | `sha(path)` |
| `workbench/media.py` | 31 | `rectangle(mask, width, height)` |
| `workbench/media.py` | 41 | `paint(array, masks, index)` |
| `workbench/media.py` | 43 | `height` |
| `workbench/media.py` | 43 | `width` |
| `workbench/media.py` | 44 | `mask` |
| `workbench/media.py` | 46 | `x0` |
| `workbench/media.py` | 46 | `x1` |
| `workbench/media.py` | 46 | `y0` |
| `workbench/media.py` | 46 | `y1` |
| `workbench/media.py` | 50 | `encoder(path, width, height, fps)` |
| `workbench/media.py` | 52 | `container` |
| `workbench/media.py` | 53 | `stream` |
| `workbench/media.py` | 66 | `emit(container, stream, array, index, fps)` |
| `workbench/media.py` | 68 | `frame` |
| `workbench/media.py` | 70 | `packet` |
| `workbench/media.py` | 74 | `finish(container, stream)` |
| `workbench/media.py` | 76 | `packet` |
| `workbench/media.py` | 81 | `transcode(source, destination, masks)` |
| `workbench/media.py` | 90 | `data` |
| `workbench/media.py` | 93 | `options` |
| `workbench/media.py` | 94 | `original` |
| `workbench/media.py` | 97 | `stream` |
| `workbench/media.py` | 98 | `dropped_streams` |
| `workbench/media.py` | 99 | `declared_frames` |
| `workbench/media.py` | 100 | `height` |
| `workbench/media.py` | 100 | `width` |
| `workbench/media.py` | 101 | `rate` |
| `workbench/media.py` | 116 | `fps` |
| `workbench/media.py` | 120 | `output` |
| `workbench/media.py` | 120 | `video` |
| `workbench/media.py` | 121 | `count` |
| `workbench/media.py` | 121 | `first_time` |
| `workbench/media.py` | 123 | `frame` |
| `workbench/media.py` | 123 | `index` |
| `workbench/media.py` | 128 | `timestamp` |
| `workbench/media.py` | 130 | `first_time` |
| `workbench/media.py` | 135 | `array` |
| `workbench/media.py` | 140 | `count` |
| `workbench/media.py` | 143 | `mask` |
| `workbench/media.py` | 164 | `verify(path, info, masks)` |
| `workbench/media.py` | 170 | `media` |
| `workbench/media.py` | 175 | `stream` |
| `workbench/media.py` | 178 | `count` |
| `workbench/media.py` | 179 | `frame` |
| `workbench/media.py` | 179 | `index` |
| `workbench/media.py` | 191 | `array` |
| `workbench/media.py` | 192 | `mask` |
| `workbench/media.py` | 195 | `x0` |
| `workbench/media.py` | 195 | `y0` |
| `workbench/media.py` | 196 | `x1` |
| `workbench/media.py` | 197 | `y1` |
| `workbench/media.py` | 200 | `count` |
| `workbench/media.py` | 205 | `synthetic(path, scenario)` |
| `workbench/media.py` | 209 | `output` |
| `workbench/media.py` | 209 | `stream` |
| `workbench/media.py` | 212 | `index` |
| `workbench/media.py` | 213 | `array` |
| `workbench/media.py` | 228 | `frame_png(source, destination, index)` |
| `workbench/media.py` | 240 | `clip` |
| `workbench/media.py` | 242 | `current` |
| `workbench/media.py` | 242 | `frame` |
| `workbench/media.py` | 246 | `pixels` |
| `workbench/media.py` | 248 | `chunk(kind, content)` |
| `workbench/media.py` | 257 | `row` |
| `workbench/media.py` | 257 | `rows` |
| `workbench/media.py` | 258 | `header` |
| `workbench/models.py` | 10 | `Unit` |
| `workbench/models.py` | 11 | `Frame` |
| `workbench/models.py` | 14 | `StrictModel(class)` |
| `workbench/models.py` | 17 | `model_config` |
| `workbench/models.py` | 20 | `Login(class)` |
| `workbench/models.py` | 23 | `username` |
| `workbench/models.py` | 24 | `password` |
| `workbench/models.py` | 27 | `Mask(class)` |
| `workbench/models.py` | 30 | `first` |
| `workbench/models.py` | 31 | `last` |
| `workbench/models.py` | 32 | `x` |
| `workbench/models.py` | 33 | `y` |
| `workbench/models.py` | 34 | `width` |
| `workbench/models.py` | 35 | `height` |
| `workbench/models.py` | 36 | `reason` |
| `workbench/models.py` | 39 | `geometry(self)` |
| `workbench/models.py` | 48 | `Sample(class)` |
| `workbench/models.py` | 51 | `ms` |
| `workbench/models.py` | 52 | `east_m` |
| `workbench/models.py` | 53 | `north_m` |
| `workbench/models.py` | 54 | `altitude_m` |
| `workbench/models.py` | 57 | `Plan(class)` |
| `workbench/models.py` | 60 | `expected_version` |
| `workbench/models.py` | 61 | `masks` |
| `workbench/models.py` | 62 | `note` |
| `workbench/models.py` | 63 | `telemetry` |
| `workbench/models.py` | 64 | `offset_ms` |
| `workbench/models.py` | 67 | `time_order(self)` |
| `workbench/models.py` | 69 | `a` |
| `workbench/models.py` | 69 | `b` |
| `workbench/models.py` | 74 | `MotionDraft(class)` |
| `workbench/models.py` | 77 | `expected_version` |
| `workbench/models.py` | 78 | `start` |
| `workbench/models.py` | 79 | `end` |
| `workbench/models.py` | 80 | `segments` |
| `workbench/models.py` | 83 | `keyframes(self)` |
| `workbench/models.py` | 96 | `Review(class)` |
| `workbench/models.py` | 99 | `expected_version` |
| `workbench/models.py` | 100 | `decision` |
| `workbench/models.py` | 101 | `full_clip_checked` |
| `workbench/models.py` | 102 | `context_checked` |
| `workbench/models.py` | 103 | `note` |
| `workbench/models.py` | 106 | `alignment(plan, frames, fps)` |
| `workbench/models.py` | 108 | `points` |
| `workbench/models.py` | 111 | `start` |
| `workbench/models.py` | 112 | `end` |
| `workbench/models.py` | 113 | `expected` |
| `workbench/models.py` | 114 | `warnings` |
| `workbench/models.py` | 117 | `a` |
| `workbench/models.py` | 117 | `b` |
| `workbench/motion.py` | 10 | `motion_masks(draft, frames)` |
| `workbench/motion.py` | 14 | `end` |
| `workbench/motion.py` | 14 | `start` |
| `workbench/motion.py` | 15 | `length` |
| `workbench/motion.py` | 16 | `count` |
| `workbench/motion.py` | 18 | `edges(frame)` |
| `workbench/motion.py` | 20 | `fraction` |
| `workbench/motion.py` | 23 | `a` |
| `workbench/motion.py` | 23 | `b` |
| `workbench/motion.py` | 30 | `masks` |
| `workbench/motion.py` | 31 | `index` |
| `workbench/motion.py` | 32 | `first` |
| `workbench/motion.py` | 33 | `last` |
| `workbench/motion.py` | 34 | `left` |
| `workbench/motion.py` | 34 | `right` |
| `workbench/motion.py` | 35 | `x` |
| `workbench/motion.py` | 35 | `y` |
| `workbench/motion.py` | 36 | `width` |
| `workbench/motion.py` | 37 | `height` |
| `workbench/owner_window.py` | 19 | `OwnerWindow(class)` |
| `workbench/owner_window.py` | 22 | `__init__(self, root, directory, metadata)` |
| `workbench/owner_window.py` | 41 | `shell` |
| `workbench/owner_window.py` | 44 | `actions` |
| `workbench/owner_window.py` | 52 | `content` |
| `workbench/owner_window.py` | 55 | `scrollbar` |
| `workbench/owner_window.py` | 59 | `body` |
| `workbench/owner_window.py` | 60 | `item` |
| `workbench/owner_window.py` | 81 | `location` |
| `workbench/owner_window.py` | 93 | `account` |
| `workbench/owner_window.py` | 103 | `caption` |
| `workbench/owner_window.py` | 103 | `index` |
| `workbench/owner_window.py` | 103 | `secret` |
| `workbench/owner_window.py` | 103 | `variable` |
| `workbench/owner_window.py` | 112 | `entry` |
| `workbench/owner_window.py` | 135 | `choose_directory(self)` |
| `workbench/owner_window.py` | 137 | `selected` |
| `workbench/owner_window.py` | 143 | `open_profile(self)` |
| `workbench/owner_window.py` | 149 | `control` |
| `workbench/owner_window.py` | 166 | `create_account(self)` |
| `workbench/owner_window.py` | 188 | `start_host(self)` |
| `workbench/owner_window.py` | 200 | `open_browser(self)` |
| `workbench/owner_window.py` | 205 | `quit(self)` |
| `workbench/owner_window.py` | 215 | `stop(self)` |
| `workbench/retention.py` | 10 | `purge(store, confirm)` |
| `workbench/retention.py` | 16 | `db` |
| `workbench/retention.py` | 17 | `ids` |
| `workbench/retention.py` | 18 | `row` |
| `workbench/retention.py` | 20 | `targets` |
| `workbench/retention.py` | 21 | `identifier` |
| `workbench/retention.py` | 22 | `folder` |
| `workbench/retention.py` | 23 | `files` |
| `workbench/retention.py` | 24 | `file` |
| `workbench/retention.py` | 34 | `files` |
| `workbench/retention.py` | 34 | `folder` |
| `workbench/retention.py` | 34 | `identifier` |
| `workbench/retention.py` | 35 | `file` |
| `workbench/retention.py` | 43 | `_` |
| `workbench/retention.py` | 43 | `file` |
| `workbench/retention.py` | 43 | `files` |
| `workbench/runtime_gui.py` | 7 | `inspect_tk(root, metadata)` |
| `workbench/runtime_gui.py` | 9 | `versions` |
| `workbench/runtime_gui.py` | 13 | `value` |
| `workbench/runtime_gui.py` | 16 | `name` |
| `workbench/runtime_gui.py` | 16 | `value` |
| `workbench/schema.sql` | 3 | `PRAGMA foreign_keys = ON;` |
| `workbench/schema.sql` | 4 | `CREATE TABLE IF NOT EXISTS users (` |
| `workbench/schema.sql` | 5 | `name TEXT PRIMARY KEY, password_hash TEXT NOT NULL,` |
| `workbench/schema.sql` | 6 | `role TEXT NOT NULL CHECK(role IN ('admin','operator','reviewer'))` |
| `workbench/schema.sql` | 7 | `);` |
| `workbench/schema.sql` | 8 | `CREATE TABLE IF NOT EXISTS sessions (` |
| `workbench/schema.sql` | 9 | `digest TEXT PRIMARY KEY, username TEXT NOT NULL REFERENCES users(name),` |
| `workbench/schema.sql` | 10 | `csrf TEXT NOT NULL, expires REAL NOT NULL, created REAL NOT NULL` |
| `workbench/schema.sql` | 11 | `);` |
| `workbench/schema.sql` | 12 | `CREATE INDEX IF NOT EXISTS sessions_user ON sessions(username);` |
| `workbench/schema.sql` | 13 | `CREATE TABLE IF NOT EXISTS attempts (client TEXT PRIMARY KEY, count INTEGER NOT NULL, started REAL NOT NULL);` |
| `workbench/schema.sql` | 14 | `CREATE TABLE IF NOT EXISTS clips (` |
| `workbench/schema.sql` | 15 | `id TEXT PRIMARY KEY, creator TEXT NOT NULL REFERENCES users(name), title TEXT NOT NULL,` |
| `workbench/schema.sql` | 16 | `purpose TEXT NOT NULL, source_digest TEXT NOT NULL, preview_digest TEXT NOT NULL,` |
| `workbench/schema.sql` | 17 | `info TEXT NOT NULL, version INTEGER NOT NULL DEFAULT 0,` |
| `workbench/schema.sql` | 18 | `created REAL NOT NULL, expires REAL NOT NULL` |
| `workbench/schema.sql` | 19 | `);` |
| `workbench/schema.sql` | 20 | `CREATE INDEX IF NOT EXISTS clips_creator ON clips(creator, created DESC);` |
| `workbench/schema.sql` | 21 | `CREATE TABLE IF NOT EXISTS revisions (` |
| `workbench/schema.sql` | 22 | `clip TEXT NOT NULL REFERENCES clips(id) ON DELETE CASCADE, version INTEGER NOT NULL,` |
| `workbench/schema.sql` | 23 | `actor TEXT NOT NULL REFERENCES users(name), plan TEXT NOT NULL, plan_digest TEXT NOT NULL,` |
| `workbench/schema.sql` | 24 | `media_digest TEXT NOT NULL, info TEXT NOT NULL, created REAL NOT NULL,` |
| `workbench/schema.sql` | 25 | `PRIMARY KEY (clip,version)` |
| `workbench/schema.sql` | 26 | `);` |
| `workbench/schema.sql` | 27 | `CREATE TABLE IF NOT EXISTS reviews (` |
| `workbench/schema.sql` | 28 | `clip TEXT NOT NULL, version INTEGER NOT NULL, actor TEXT NOT NULL REFERENCES users(name),` |
| `workbench/schema.sql` | 29 | `decision TEXT NOT NULL CHECK(decision IN ('approve','reject')), note TEXT NOT NULL,` |
| `workbench/schema.sql` | 30 | `created REAL NOT NULL, PRIMARY KEY(clip,version),` |
| `workbench/schema.sql` | 31 | `FOREIGN KEY(clip,version) REFERENCES revisions(clip,version) ON DELETE CASCADE` |
| `workbench/schema.sql` | 32 | `);` |
| `workbench/schema.sql` | 33 | `CREATE TABLE IF NOT EXISTS audit (` |
| `workbench/schema.sql` | 34 | `id INTEGER PRIMARY KEY, at REAL NOT NULL, actor TEXT NOT NULL, clip TEXT NOT NULL,` |
| `workbench/schema.sql` | 35 | `event TEXT NOT NULL, version INTEGER NOT NULL` |
| `workbench/schema.sql` | 36 | `);` |
| `workbench/schema.sql` | 37 | `CREATE INDEX IF NOT EXISTS audit_clip ON audit(clip,id DESC);` |
| `workbench/schema.sql` | 38 | `CREATE TRIGGER IF NOT EXISTS immutable_revision BEFORE UPDATE ON revisions BEGIN SELECT RAISE(ABORT,'immutable revision'); END;` |
| `workbench/schema.sql` | 39 | `CREATE TRIGGER IF NOT EXISTS immutable_review BEFORE UPDATE ON reviews BEGIN SELECT RAISE(ABORT,'immutable review'); END;` |
| `workbench/service.py` | 22 | `ROOT` |
| `workbench/service.py` | 23 | `PROCESSING` |
| `workbench/service.py` | 27 | `workspace(store)` |
| `workbench/service.py` | 34 | `scratch` |
| `workbench/service.py` | 42 | `worker_command(directory)` |
| `workbench/service.py` | 51 | `run(directory, masks, scenario, frame)` |
| `workbench/service.py` | 65 | `result` |
| `workbench/service.py` | 87 | `import_clip(store, user, title, purpose, retention, data, scenario)` |
| `workbench/service.py` | 91 | `directory` |
| `workbench/service.py` | 95 | `result` |
| `workbench/service.py` | 96 | `identifier` |
| `workbench/service.py` | 97 | `target` |
| `workbench/service.py` | 105 | `file` |
| `workbench/service.py` | 112 | `process(store, identifier, user, plan)` |
| `workbench/service.py` | 116 | `clip` |
| `workbench/service.py` | 119 | `mask` |
| `workbench/service.py` | 121 | `source` |
| `workbench/service.py` | 130 | `directory` |
| `workbench/service.py` | 132 | `mask` |
| `workbench/service.py` | 132 | `result` |
| `workbench/service.py` | 134 | `publish(version)` |
| `workbench/service.py` | 142 | `render_frame(store, identifier, user, kind, version, index)` |
| `workbench/service.py` | 144 | `source` |
| `workbench/service.py` | 145 | `clip` |
| `workbench/service.py` | 148 | `directory` |
| `workbench/service.py` | 150 | `data` |
| `workbench/store.py` | 19 | `canonical(value)` |
| `workbench/store.py` | 24 | `digest(value)` |
| `workbench/store.py` | 29 | `Store(class)` |
| `workbench/store.py` | 32 | `__init__(self, path)` |
| `workbench/store.py` | 38 | `db` |
| `workbench/store.py` | 42 | `connect(self, write)` |
| `workbench/store.py` | 44 | `db` |
| `workbench/store.py` | 56 | `folder(self, identifier)` |
| `workbench/store.py` | 60 | `path` |
| `workbench/store.py` | 65 | `event(self, db, user, identifier, event, version)` |
| `workbench/store.py` | 72 | `get(self, identifier, user, db)` |
| `workbench/store.py` | 75 | `connection` |
| `workbench/store.py` | 77 | `row` |
| `workbench/store.py` | 82 | `clip` |
| `workbench/store.py` | 84 | `revision` |
| `workbench/store.py` | 89 | `value` |
| `workbench/store.py` | 97 | `review` |
| `workbench/store.py` | 105 | `list(self, user)` |
| `workbench/store.py` | 107 | `db` |
| `workbench/store.py` | 108 | `rows` |
| `workbench/store.py` | 112 | `row` |
| `workbench/store.py` | 114 | `capacity(self)` |
| `workbench/store.py` | 116 | `db` |
| `workbench/store.py` | 122 | `insert(self, identifier, user, title, purpose, retention, result)` |
| `workbench/store.py` | 124 | `db` |
| `workbench/store.py` | 126 | `now` |
| `workbench/store.py` | 143 | `save(self, identifier, user, plan, result, move)` |
| `workbench/store.py` | 145 | `db` |
| `workbench/store.py` | 146 | `clip` |
| `workbench/store.py` | 151 | `version` |
| `workbench/store.py` | 153 | `content` |
| `workbench/store.py` | 171 | `file(self, identifier, user, kind, record, version)` |
| `workbench/store.py` | 173 | `db` |
| `workbench/store.py` | 174 | `clip` |
| `workbench/store.py` | 179 | `revision` |
| `workbench/store.py` | 181 | `expected` |
| `workbench/store.py` | 181 | `name` |
| `workbench/store.py` | 189 | `expected` |
| `workbench/store.py` | 189 | `name` |
| `workbench/store.py` | 190 | `path` |
| `workbench/store.py` | 202 | `review(self, identifier, user, body)` |
| `workbench/store.py` | 205 | `db` |
| `workbench/store.py` | 206 | `clip` |
| `workbench/store.py` | 207 | `revision` |
| `workbench/store.py` | 228 | `history(self, identifier, user)` |
| `workbench/store.py` | 230 | `db` |
| `workbench/store.py` | 232 | `revisions` |
| `workbench/store.py` | 234 | `r` |
| `workbench/store.py` | 239 | `events` |
| `workbench/store.py` | 241 | `r` |
| `workbench/store.py` | 248 | `manifest(self, identifier, user)` |
| `workbench/store.py` | 250 | `clip` |
| `workbench/store.py` | 251 | `path` |
| `workbench/store.py` | 252 | `revision` |
| `workbench/store.py` | 261 | `key` |
| `workbench/worker.py` | 15 | `execute(directory)` |
| `workbench/worker.py` | 17 | `job` |
| `workbench/worker.py` | 18 | `source` |
| `workbench/worker.py` | 24 | `masks` |
| `workbench/worker.py` | 24 | `value` |
| `workbench/worker.py` | 25 | `info` |
| `workbench/worker.py` | 27 | `result` |
| `workbench/worker.py` | 35 | `main()` |
| `ui/src/env.d.ts` | 2 | `__APP_VERSION__` |
| `ui/src/main.ts` | 11 | `User` |
| `ui/src/main.ts` | 16 | `Plan` |
| `ui/src/main.ts` | 23 | `Clip` |
| `ui/src/main.ts` | 41 | `user` |
| `ui/src/main.ts` | 42 | `clip` |
| `ui/src/main.ts` | 43 | `masks` |
| `ui/src/main.ts` | 44 | `epoch` |
| `ui/src/main.ts` | 45 | `busy` |
| `ui/src/main.ts` | 46 | `logoutPending` |
| `ui/src/main.ts` | 47 | `frameMode` |
| `ui/src/main.ts` | 48 | `videoGeneration` |
| `ui/src/main.ts` | 49 | `frameLoading` |
| `ui/src/main.ts` | 50 | `motionFields` |
| `ui/src/main.ts` | 51 | `motionLegend` |
| `ui/src/main.ts` | 53 | `motionHelp` |
| `ui/src/main.ts` | 57 | `[id, title, initial]` |
| `ui/src/main.ts` | 64 | `label` |
| `ui/src/main.ts` | 66 | `input` |
| `ui/src/main.ts` | 76 | `motionButton` |
| `ui/src/main.ts` | 83 | `motionIntent` |
| `ui/src/main.ts` | 110 | `request` |
| `ui/src/main.ts` | 111 | `identity` |
| `ui/src/main.ts` | 112 | `count` |
| `ui/src/main.ts` | 113 | `result` |
| `ui/src/main.ts` | 132 | `el` |
| `ui/src/main.ts` | 132 | `id` |
| `ui/src/main.ts` | 136 | `value` |
| `ui/src/main.ts` | 136 | `id` |
| `ui/src/main.ts` | 140 | `text` |
| `ui/src/main.ts` | 140 | `id` |
| `ui/src/main.ts` | 140 | `message` |
| `ui/src/main.ts` | 144 | `buttons` |
| `ui/src/main.ts` | 146 | `id` |
| `ui/src/main.ts` | 148 | `button` |
| `ui/src/main.ts` | 153 | `api` |
| `ui/src/main.ts` | 153 | `path` |
| `ui/src/main.ts` | 153 | `body` |
| `ui/src/main.ts` | 153 | `raw` |
| `ui/src/main.ts` | 154 | `generation` |
| `ui/src/main.ts` | 155 | `response` |
| `ui/src/main.ts` | 171 | `result` |
| `ui/src/main.ts` | 182 | `task` |
| `ui/src/main.ts` | 182 | `action` |
| `ui/src/main.ts` | 185 | `generation` |
| `ui/src/main.ts` | 192 | `error` |
| `ui/src/main.ts` | 200 | `reset` |
| `ui/src/main.ts` | 208 | `video` |
| `ui/src/main.ts` | 227 | `id` |
| `ui/src/main.ts` | 241 | `id` |
| `ui/src/main.ts` | 245 | `library` |
| `ui/src/main.ts` | 246 | `rows` |
| `ui/src/main.ts` | 247 | `list` |
| `ui/src/main.ts` | 249 | `row` |
| `ui/src/main.ts` | 250 | `button` |
| `ui/src/main.ts` | 264 | `signedIn` |
| `ui/src/main.ts` | 264 | `next` |
| `ui/src/main.ts` | 273 | `show` |
| `ui/src/main.ts` | 273 | `next` |
| `ui/src/main.ts` | 282 | `metrics` |
| `ui/src/main.ts` | 284 | `[amount, label]` |
| `ui/src/main.ts` | 290 | `div` |
| `ui/src/main.ts` | 292 | `strong` |
| `ui/src/main.ts` | 294 | `small` |
| `ui/src/main.ts` | 299 | `kind` |
| `ui/src/main.ts` | 302 | `frame` |
| `ui/src/main.ts` | 346 | `loadVideo` |
| `ui/src/main.ts` | 348 | `generation` |
| `ui/src/main.ts` | 351 | `image` |
| `ui/src/main.ts` | 362 | `video` |
| `ui/src/main.ts` | 378 | `useFrames` |
| `ui/src/main.ts` | 392 | `loadFrame` |
| `ui/src/main.ts` | 394 | `index` |
| `ui/src/main.ts` | 399 | `generation` |
| `ui/src/main.ts` | 400 | `image` |
| `ui/src/main.ts` | 422 | `drawMasks` |
| `ui/src/main.ts` | 423 | `overlay` |
| `ui/src/main.ts` | 425 | `list` |
| `ui/src/main.ts` | 430 | `mask` |
| `ui/src/main.ts` | 431 | `item` |
| `ui/src/main.ts` | 439 | `rect` |
| `ui/src/main.ts` | 443 | `[key, amount]` |
| `ui/src/main.ts` | 456 | `frame` |
| `ui/src/main.ts` | 470 | `event` |
| `ui/src/main.ts` | 473 | `next` |
| `ui/src/main.ts` | 482 | `csrf` |
| `ui/src/main.ts` | 492 | `response` |
| `ui/src/main.ts` | 517 | `event` |
| `ui/src/main.ts` | 520 | `file` |
| `ui/src/main.ts` | 523 | `params` |
| `ui/src/main.ts` | 533 | `event` |
| `ui/src/main.ts` | 536 | `mask` |
| `ui/src/main.ts` | 564 | `_` |
| `ui/src/main.ts` | 564 | `index` |
| `ui/src/main.ts` | 582 | `body` |
| `ui/src/main.ts` | 592 | `event` |
| `ui/src/main.ts` | 630 | `video` |
| `ui/src/main.ts` | 657 | `releaseFooter` |
| `ui/src/view.test.ts` | 15 | `mask` |
| `ui/src/view.test.ts` | 32 | `change` |
| `ui/src/view.test.ts` | 51 | `points` |
| `ui/src/view.ts` | 2 | `Mask` |
| `ui/src/view.ts` | 11 | `Sample` |
| `ui/src/view.ts` | 18 | `mediaKind` |
| `ui/src/view.ts` | 18 | `input` |
| `ui/src/view.ts` | 22 | `validMask` |
| `ui/src/view.ts` | 22 | `mask` |
| `ui/src/view.ts` | 22 | `frames` |
| `ui/src/view.ts` | 41 | `positionAt` |
| `ui/src/view.ts` | 42 | `samples` |
| `ui/src/view.ts` | 43 | `ms` |
| `ui/src/view.ts` | 44 | `offset` |
| `ui/src/view.ts` | 46 | `time` |
| `ui/src/view.ts` | 53 | `next` |
| `ui/src/view.ts` | 53 | `point` |
| `ui/src/view.ts` | 54 | `right` |
| `ui/src/view.ts` | 55 | `left` |
| `ui/src/view.ts` | 57 | `fraction` |
| `ui/src/view.ts` | 62 | `reviewLabel` |
| `ui/src/view.ts` | 62 | `version` |
| `ui/src/view.ts` | 62 | `decision` |
| `tests/browser/workspace.spec.ts` | 6 | `directory` |
| `tests/browser/workspace.spec.ts` | 8 | `signIn` |
| `tests/browser/workspace.spec.ts` | 8 | `page` |
| `tests/browser/workspace.spec.ts` | 8 | `role` |
| `tests/browser/workspace.spec.ts` | 9 | `account` |
| `tests/browser/workspace.spec.ts` | 19 | `loaded` |
| `tests/browser/workspace.spec.ts` | 19 | `page` |
| `tests/browser/workspace.spec.ts` | 24 | `video` |
| `tests/browser/workspace.spec.ts` | 25 | `image` |
| `tests/browser/workspace.spec.ts` | 37 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 69 | `black` |
| `tests/browser/workspace.spec.ts` | 69 | `node` |
| `tests/browser/workspace.spec.ts` | 70 | `video` |
| `tests/browser/workspace.spec.ts` | 73 | `canvas` |
| `tests/browser/workspace.spec.ts` | 76 | `context` |
| `tests/browser/workspace.spec.ts` | 104 | `download` |
| `tests/browser/workspace.spec.ts` | 106 | `file` |
| `tests/browser/workspace.spec.ts` | 111 | `receiptDownload` |
| `tests/browser/workspace.spec.ts` | 113 | `receipt` |
| `tests/browser/workspace.spec.ts` | 128 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 165 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 173 | `created` |
| `tests/browser/workspace.spec.ts` | 174 | `response` |
| `tests/browser/workspace.spec.ts` | 179 | `original` |
| `tests/browser/workspace.spec.ts` | 181 | `title` |
| `tests/browser/workspace.spec.ts` | 200 | `frameResponse` |
| `tests/browser/workspace.spec.ts` | 201 | `response` |
| `tests/browser/workspace.spec.ts` | 214 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 219 | `release` |
| `tests/browser/workspace.spec.ts` | 220 | `received` |
| `tests/browser/workspace.spec.ts` | 221 | `hold` |
| `tests/browser/workspace.spec.ts` | 221 | `resolve` |
| `tests/browser/workspace.spec.ts` | 224 | `responseReady` |
| `tests/browser/workspace.spec.ts` | 224 | `resolve` |
| `tests/browser/workspace.spec.ts` | 227 | `route` |
| `tests/browser/workspace.spec.ts` | 228 | `response` |
| `tests/browser/workspace.spec.ts` | 244 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 281 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 284 | `release` |
| `tests/browser/workspace.spec.ts` | 285 | `observed` |
| `tests/browser/workspace.spec.ts` | 286 | `hold` |
| `tests/browser/workspace.spec.ts` | 286 | `resolve` |
| `tests/browser/workspace.spec.ts` | 289 | `responseReady` |
| `tests/browser/workspace.spec.ts` | 289 | `resolve` |
| `tests/browser/workspace.spec.ts` | 292 | `route` |
| `tests/browser/workspace.spec.ts` | 293 | `response` |
| `tools/browser_checks.mjs` | 8 | `project` |
| `tools/browser_checks.mjs` | 9 | `result` |
| `tools/native_feature_smoke.mjs` | 8 | `[base, output]` |
| `tools/native_feature_smoke.mjs` | 15 | `origin` |
| `tools/native_feature_smoke.mjs` | 16 | `browser` |
| `tools/native_feature_smoke.mjs` | 17 | `context` |
| `tools/native_feature_smoke.mjs` | 22 | `page` |
| `tools/native_feature_smoke.mjs` | 23 | `errors` |
| `tools/native_feature_smoke.mjs` | 24 | `external` |
| `tools/native_feature_smoke.mjs` | 25 | `exchanges` |
| `tools/native_feature_smoke.mjs` | 26 | `error` |
| `tools/native_feature_smoke.mjs` | 27 | `request` |
| `tools/native_feature_smoke.mjs` | 41 | `response` |
| `tools/native_feature_smoke.mjs` | 53 | `login` |
| `tools/native_feature_smoke.mjs` | 53 | `role` |
| `tools/native_feature_smoke.mjs` | 65 | `logout` |
| `tools/native_feature_smoke.mjs` | 66 | `pending` |
| `tools/native_feature_smoke.mjs` | 67 | `response` |
| `tools/native_feature_smoke.mjs` | 77 | `loaded` |
| `tools/native_feature_smoke.mjs` | 82 | `video` |
| `tools/native_feature_smoke.mjs` | 83 | `image` |
| `tools/native_feature_smoke.mjs` | 95 | `download` |
| `tools/native_feature_smoke.mjs` | 95 | `link` |
| `tools/native_feature_smoke.mjs` | 95 | `filename` |
| `tools/native_feature_smoke.mjs` | 96 | `pending` |
| `tools/native_feature_smoke.mjs` | 98 | `item` |
| `tools/native_feature_smoke.mjs` | 120 | `importResponse` |
| `tools/native_feature_smoke.mjs` | 121 | `response` |
| `tools/native_feature_smoke.mjs` | 131 | `clips` |
| `tools/native_feature_smoke.mjs` | 135 | `id` |
| `tools/native_feature_smoke.mjs` | 144 | `[field, value]` |
| `tools/native_feature_smoke.mjs` | 161 | `[field, value]` |
| `tools/native_feature_smoke.mjs` | 180 | `processResponse` |
| `tools/native_feature_smoke.mjs` | 181 | `response` |
| `tools/native_feature_smoke.mjs` | 192 | `premature` |
| `tools/native_feature_smoke.mjs` | 196 | `frameResponse` |
| `tools/native_feature_smoke.mjs` | 197 | `response` |
| `tools/native_feature_smoke.mjs` | 239 | `receipt` |
| `tools/native_feature_smoke.mjs` | 273 | `cookies` |
| `tools/source_index.mjs` | 7 | `collect` |
| `tools/source_index.mjs` | 7 | `root` |
| `tools/source_index.mjs` | 10 | `a` |
| `tools/source_index.mjs` | 10 | `b` |
| `tools/source_index.mjs` | 11 | `entry` |
| `tools/source_index.mjs` | 12 | `name` |
| `tools/source_index.mjs` | 20 | `file` |
| `tools/source_index.mjs` | 23 | `name` |
| `tools/source_index.mjs` | 27 | `source` |
| `tools/source_index.mjs` | 33 | `records` |
| `tools/source_index.mjs` | 35 | `visit` |
| `tools/source_index.mjs` | 35 | `node` |
| `tools/source_index.mjs` | 44 | `name` |
| `tools/source_index.mjs` | 48 | `line` |
| `tools/source_index.mjs` | 59 | `row` |
| `playwright.config.ts` | 5 | `directory` |
| `playwright.config.ts` | 8 | `local` |
| `playwright.config.ts` | 12 | `python` |
