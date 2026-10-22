# Source declaration map

By Jason Stys. Headers link here for current exact physical lines.
Python/TypeScript ASTs index declarations, parameters and bindings; SQL lists non-comment schema lines. Lexical maps are navigation, not complete semantic symbol tables.

| File | Line | Declaration / variable |
| --- | ---: | --- |
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
| `tests/test_security.py` | 196 | `db` |
| `tests/test_security.py` | 199 | `db` |
| `tests/test_security.py` | 203 | `test_body_capacity_and_port_validation(client, monkeypatch, tmp_path)` |
| `tests/test_security.py` | 206 | `Busy(class)` |
| `tests/test_security.py` | 209 | `acquire(self, blocking)` |
| `tests/test_security.py` | 219 | `test_path_validation_and_symlink(app, tmp_path)` |
| `tests/test_security.py` | 221 | `store` |
| `tests/test_security.py` | 222 | `invalid` |
| `tests/test_security.py` | 225 | `path` |
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
| `tools/check_repo.py` | 9 | `main()` |
| `tools/check_repo.py` | 11 | `path` |
| `tools/check_repo.py` | 12 | `relative` |
| `tools/check_repo.py` | 13 | `content` |
| `tools/check_repo.py` | 31 | `ref` |
| `tools/check_repo.py` | 34 | `budget` |
| `tools/check_repo.py` | 34 | `suffix` |
| `tools/check_repo.py` | 35 | `size` |
| `tools/check_repo.py` | 36 | `p` |
| `tools/docs_index.py` | 13 | `ROOT` |
| `tools/docs_index.py` | 14 | `EXCLUDE` |
| `tools/docs_index.py` | 28 | `SPECIAL` |
| `tools/docs_index.py` | 40 | `files()` |
| `tools/docs_index.py` | 42 | `result` |
| `tools/docs_index.py` | 43 | `children` |
| `tools/docs_index.py` | 43 | `directory` |
| `tools/docs_index.py` | 43 | `names` |
| `tools/docs_index.py` | 44 | `child` |
| `tools/docs_index.py` | 45 | `name` |
| `tools/docs_index.py` | 51 | `render()` |
| `tools/docs_index.py` | 53 | `catalog` |
| `tools/docs_index.py` | 61 | `source` |
| `tools/docs_index.py` | 70 | `path` |
| `tools/docs_index.py` | 71 | `relative` |
| `tools/docs_index.py` | 72 | `content` |
| `tools/docs_index.py` | 73 | `description` |
| `tools/docs_index.py` | 76 | `line` |
| `tools/docs_index.py` | 84 | `records` |
| `tools/docs_index.py` | 86 | `node` |
| `tools/docs_index.py` | 88 | `args` |
| `tools/docs_index.py` | 91 | `a` |
| `tools/docs_index.py` | 99 | `line` |
| `tools/docs_index.py` | 99 | `value` |
| `tools/docs_index.py` | 102 | `line` |
| `tools/docs_index.py` | 102 | `name` |
| `tools/docs_index.py` | 103 | `node` |
| `tools/docs_index.py` | 117 | `main()` |
| `tools/docs_index.py` | 119 | `content` |
| `tools/docs_index.py` | 119 | `relative` |
| `tools/docs_index.py` | 120 | `path` |
| `workbench/__main__.py` | 15 | `main()` |
| `workbench/__main__.py` | 17 | `parser` |
| `workbench/__main__.py` | 19 | `commands` |
| `workbench/__main__.py` | 21 | `cleanup` |
| `workbench/__main__.py` | 23 | `user` |
| `workbench/__main__.py` | 26 | `serve` |
| `workbench/__main__.py` | 28 | `args` |
| `workbench/__main__.py` | 29 | `store` |
| `workbench/__main__.py` | 35 | `password` |
| `workbench/api.py` | 21 | `HEADERS` |
| `workbench/api.py` | 29 | `BODY_GATE` |
| `workbench/api.py` | 32 | `create_app(database, port)` |
| `workbench/api.py` | 36 | `authority` |
| `workbench/api.py` | 36 | `origin` |
| `workbench/api.py` | 37 | `app` |
| `workbench/api.py` | 43 | `boundary(request, call_next)` |
| `workbench/api.py` | 45 | `acquired` |
| `workbench/api.py` | 45 | `response` |
| `workbench/api.py` | 61 | `media` |
| `workbench/api.py` | 62 | `expected` |
| `workbench/api.py` | 67 | `acquired` |
| `workbench/api.py` | 68 | `data` |
| `workbench/api.py` | 70 | `chunk` |
| `workbench/api.py` | 75 | `response` |
| `workbench/api.py` | 77 | `response` |
| `workbench/api.py` | 79 | `response` |
| `workbench/api.py` | 87 | `invalid(_request, error)` |
| `workbench/api.py` | 92 | `e` |
| `workbench/api.py` | 98 | `health()` |
| `workbench/api.py` | 103 | `login(body, request)` |
| `workbench/api.py` | 105 | `token` |
| `workbench/api.py` | 105 | `user` |
| `workbench/api.py` | 106 | `response` |
| `workbench/api.py` | 111 | `me(request)` |
| `workbench/api.py` | 116 | `logout(request)` |
| `workbench/api.py` | 119 | `response` |
| `workbench/api.py` | 124 | `clips(request)` |
| `workbench/api.py` | 129 | `upload(request, title, purpose, retention)` |
| `workbench/api.py` | 136 | `user` |
| `workbench/api.py` | 137 | `data` |
| `workbench/api.py` | 143 | `example(scenario, request)` |
| `workbench/api.py` | 155 | `clip(identifier, request)` |
| `workbench/api.py` | 160 | `history(identifier, request)` |
| `workbench/api.py` | 165 | `process(identifier, body, request)` |
| `workbench/api.py` | 170 | `review(identifier, body, request)` |
| `workbench/api.py` | 172 | `user` |
| `workbench/api.py` | 177 | `media(identifier, kind, request, version)` |
| `workbench/api.py` | 184 | `path` |
| `workbench/api.py` | 192 | `manifest(identifier, request)` |
| `workbench/api.py` | 200 | `frame(identifier, kind, request, version, index)` |
| `workbench/api.py` | 216 | `index()` |
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
| `workbench/auth.py` | 80 | `identity(request)` |
| `workbench/auth.py` | 82 | `token` |
| `workbench/auth.py` | 85 | `db` |
| `workbench/auth.py` | 86 | `row` |
| `workbench/auth.py` | 95 | `authorize(request, role)` |
| `workbench/auth.py` | 97 | `user` |
| `workbench/auth.py` | 107 | `sign_out(request)` |
| `workbench/auth.py` | 110 | `db` |
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
| `workbench/models.py` | 74 | `Review(class)` |
| `workbench/models.py` | 77 | `expected_version` |
| `workbench/models.py` | 78 | `decision` |
| `workbench/models.py` | 79 | `full_clip_checked` |
| `workbench/models.py` | 80 | `context_checked` |
| `workbench/models.py` | 81 | `note` |
| `workbench/models.py` | 84 | `alignment(plan, frames, fps)` |
| `workbench/models.py` | 86 | `points` |
| `workbench/models.py` | 89 | `start` |
| `workbench/models.py` | 90 | `end` |
| `workbench/models.py` | 91 | `expected` |
| `workbench/models.py` | 92 | `warnings` |
| `workbench/models.py` | 95 | `a` |
| `workbench/models.py` | 95 | `b` |
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
| `workbench/service.py` | 42 | `run(directory, masks, scenario, frame)` |
| `workbench/service.py` | 56 | `result` |
| `workbench/service.py` | 77 | `import_clip(store, user, title, purpose, retention, data, scenario)` |
| `workbench/service.py` | 81 | `directory` |
| `workbench/service.py` | 85 | `result` |
| `workbench/service.py` | 86 | `identifier` |
| `workbench/service.py` | 87 | `target` |
| `workbench/service.py` | 95 | `file` |
| `workbench/service.py` | 102 | `process(store, identifier, user, plan)` |
| `workbench/service.py` | 106 | `clip` |
| `workbench/service.py` | 109 | `mask` |
| `workbench/service.py` | 111 | `source` |
| `workbench/service.py` | 120 | `directory` |
| `workbench/service.py` | 122 | `mask` |
| `workbench/service.py` | 122 | `result` |
| `workbench/service.py` | 124 | `publish(version)` |
| `workbench/service.py` | 132 | `render_frame(store, identifier, user, kind, version, index)` |
| `workbench/service.py` | 134 | `source` |
| `workbench/service.py` | 135 | `clip` |
| `workbench/service.py` | 138 | `directory` |
| `workbench/service.py` | 140 | `data` |
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
| `ui/src/main.ts` | 10 | `User` |
| `ui/src/main.ts` | 15 | `Plan` |
| `ui/src/main.ts` | 22 | `Clip` |
| `ui/src/main.ts` | 40 | `user` |
| `ui/src/main.ts` | 41 | `clip` |
| `ui/src/main.ts` | 42 | `masks` |
| `ui/src/main.ts` | 43 | `epoch` |
| `ui/src/main.ts` | 44 | `busy` |
| `ui/src/main.ts` | 45 | `logoutPending` |
| `ui/src/main.ts` | 46 | `frameMode` |
| `ui/src/main.ts` | 47 | `videoGeneration` |
| `ui/src/main.ts` | 48 | `frameLoading` |
| `ui/src/main.ts` | 50 | `el` |
| `ui/src/main.ts` | 50 | `id` |
| `ui/src/main.ts` | 54 | `value` |
| `ui/src/main.ts` | 54 | `id` |
| `ui/src/main.ts` | 58 | `text` |
| `ui/src/main.ts` | 58 | `id` |
| `ui/src/main.ts` | 58 | `message` |
| `ui/src/main.ts` | 62 | `buttons` |
| `ui/src/main.ts` | 63 | `button` |
| `ui/src/main.ts` | 68 | `api` |
| `ui/src/main.ts` | 68 | `path` |
| `ui/src/main.ts` | 68 | `body` |
| `ui/src/main.ts` | 68 | `raw` |
| `ui/src/main.ts` | 69 | `generation` |
| `ui/src/main.ts` | 70 | `response` |
| `ui/src/main.ts` | 86 | `result` |
| `ui/src/main.ts` | 97 | `task` |
| `ui/src/main.ts` | 97 | `action` |
| `ui/src/main.ts` | 100 | `generation` |
| `ui/src/main.ts` | 107 | `error` |
| `ui/src/main.ts` | 115 | `reset` |
| `ui/src/main.ts` | 123 | `video` |
| `ui/src/main.ts` | 142 | `id` |
| `ui/src/main.ts` | 156 | `id` |
| `ui/src/main.ts` | 160 | `library` |
| `ui/src/main.ts` | 161 | `rows` |
| `ui/src/main.ts` | 162 | `list` |
| `ui/src/main.ts` | 164 | `row` |
| `ui/src/main.ts` | 165 | `button` |
| `ui/src/main.ts` | 179 | `signedIn` |
| `ui/src/main.ts` | 179 | `next` |
| `ui/src/main.ts` | 188 | `show` |
| `ui/src/main.ts` | 188 | `next` |
| `ui/src/main.ts` | 197 | `metrics` |
| `ui/src/main.ts` | 199 | `[amount, label]` |
| `ui/src/main.ts` | 205 | `div` |
| `ui/src/main.ts` | 207 | `strong` |
| `ui/src/main.ts` | 209 | `small` |
| `ui/src/main.ts` | 214 | `kind` |
| `ui/src/main.ts` | 217 | `frame` |
| `ui/src/main.ts` | 261 | `loadVideo` |
| `ui/src/main.ts` | 263 | `generation` |
| `ui/src/main.ts` | 266 | `image` |
| `ui/src/main.ts` | 277 | `video` |
| `ui/src/main.ts` | 293 | `useFrames` |
| `ui/src/main.ts` | 307 | `loadFrame` |
| `ui/src/main.ts` | 309 | `generation` |
| `ui/src/main.ts` | 310 | `image` |
| `ui/src/main.ts` | 332 | `drawMasks` |
| `ui/src/main.ts` | 333 | `overlay` |
| `ui/src/main.ts` | 335 | `list` |
| `ui/src/main.ts` | 340 | `mask` |
| `ui/src/main.ts` | 341 | `item` |
| `ui/src/main.ts` | 349 | `rect` |
| `ui/src/main.ts` | 353 | `[key, amount]` |
| `ui/src/main.ts` | 366 | `frame` |
| `ui/src/main.ts` | 380 | `event` |
| `ui/src/main.ts` | 383 | `next` |
| `ui/src/main.ts` | 392 | `csrf` |
| `ui/src/main.ts` | 402 | `response` |
| `ui/src/main.ts` | 427 | `event` |
| `ui/src/main.ts` | 430 | `file` |
| `ui/src/main.ts` | 433 | `params` |
| `ui/src/main.ts` | 443 | `event` |
| `ui/src/main.ts` | 446 | `mask` |
| `ui/src/main.ts` | 474 | `_` |
| `ui/src/main.ts` | 474 | `index` |
| `ui/src/main.ts` | 492 | `body` |
| `ui/src/main.ts` | 502 | `event` |
| `ui/src/main.ts` | 540 | `video` |
| `ui/src/view.test.ts` | 4 | `mask` |
| `ui/src/view.test.ts` | 21 | `change` |
| `ui/src/view.test.ts` | 40 | `points` |
| `ui/src/view.ts` | 2 | `Mask` |
| `ui/src/view.ts` | 11 | `Sample` |
| `ui/src/view.ts` | 18 | `validMask` |
| `ui/src/view.ts` | 18 | `mask` |
| `ui/src/view.ts` | 18 | `frames` |
| `ui/src/view.ts` | 37 | `positionAt` |
| `ui/src/view.ts` | 38 | `samples` |
| `ui/src/view.ts` | 39 | `ms` |
| `ui/src/view.ts` | 40 | `offset` |
| `ui/src/view.ts` | 42 | `time` |
| `ui/src/view.ts` | 49 | `next` |
| `ui/src/view.ts` | 49 | `point` |
| `ui/src/view.ts` | 50 | `right` |
| `ui/src/view.ts` | 51 | `left` |
| `ui/src/view.ts` | 53 | `fraction` |
| `ui/src/view.ts` | 58 | `reviewLabel` |
| `ui/src/view.ts` | 58 | `version` |
| `ui/src/view.ts` | 58 | `decision` |
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
| `tests/browser/workspace.spec.ts` | 127 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 135 | `created` |
| `tests/browser/workspace.spec.ts` | 136 | `response` |
| `tests/browser/workspace.spec.ts` | 141 | `original` |
| `tests/browser/workspace.spec.ts` | 143 | `title` |
| `tests/browser/workspace.spec.ts` | 162 | `frameResponse` |
| `tests/browser/workspace.spec.ts` | 163 | `response` |
| `tests/browser/workspace.spec.ts` | 176 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 181 | `release` |
| `tests/browser/workspace.spec.ts` | 182 | `received` |
| `tests/browser/workspace.spec.ts` | 183 | `hold` |
| `tests/browser/workspace.spec.ts` | 183 | `resolve` |
| `tests/browser/workspace.spec.ts` | 186 | `responseReady` |
| `tests/browser/workspace.spec.ts` | 186 | `resolve` |
| `tests/browser/workspace.spec.ts` | 189 | `route` |
| `tests/browser/workspace.spec.ts` | 190 | `response` |
| `tests/browser/workspace.spec.ts` | 206 | `{ page, }` |
| `tools/browser_checks.mjs` | 8 | `project` |
| `tools/browser_checks.mjs` | 9 | `result` |
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
