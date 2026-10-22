"""Jason Stys: interrupted jobs, rollback, integrity/CAS and explicit retention failures; lines: docs/SOURCE_MAP.md."""

import json
import subprocess
import sys
import time
from types import SimpleNamespace

import pytest
from fastapi import HTTPException

from workbench import service, worker
from workbench.models import Plan, Review
from workbench.retention import purge


def test_worker_real_and_failed_main(tmp_path, video, monkeypatch):
    """Call the real worker entry, inspect its verified result, then reproduce invalid job failure."""
    (tmp_path / "source.mp4").write_bytes(video.read_bytes())
    (tmp_path / "job.json").write_text(json.dumps({"masks": [], "scenario": None}))
    monkeypatch.setattr(sys, "argv", ["worker", str(tmp_path)])
    worker.main()
    assert json.loads((tmp_path / "result.json").read_text())["info"]["frames"] == 40
    (tmp_path / "job.json").write_text("bad")
    with pytest.raises(SystemExit) as error:
        worker.main()
    assert error.value.code == 2


def test_job_timeout_failure_and_no_partial_publication(client, imported, plan, app, monkeypatch):
    """Timeout/nonzero exit/missing result all fail closed; scratch directories are removed."""
    path = f"/api/clips/{imported['id']}/process"

    def timeout(*_args, **_kwargs):
        """Reproduce a worker deadline without waiting ninety seconds."""
        raise subprocess.TimeoutExpired("fixed-worker", 90)

    monkeypatch.setattr(service.subprocess, "run", timeout)
    assert client.post(path, json=plan).status_code == 422
    monkeypatch.setattr(service.subprocess, "run", lambda *_a, **_k: SimpleNamespace(returncode=2))
    assert client.post(path, json=plan).status_code == 422
    monkeypatch.setattr(service.subprocess, "run", lambda *_a, **_k: SimpleNamespace(returncode=0))
    assert client.post(path, json=plan).status_code == 422
    assert client.get(f"/api/clips/{imported['id']}").json()["version"] == 0
    assert not list(app.state.store.media.glob("job-*"))


def test_backpressure_low_disk_storage_error_and_import_rollback(client, login, app, monkeypatch):
    """Resource pressure must not create a clip, leaked scratch file or partial database record."""
    login()
    assert service.PROCESSING.acquire(blocking=False)
    try:
        assert client.post("/api/examples/flood", json={}).status_code == 429
    finally:
        service.PROCESSING.release()
    real_usage = service.shutil.disk_usage
    monkeypatch.setattr(service.shutil, "disk_usage", lambda _p: SimpleNamespace(free=1))
    assert client.post("/api/examples/flood", json={}).status_code == 507

    def disk_failure(_p):
        """Reproduce inaccessible media storage."""
        raise OSError("Simulated storage outage")

    monkeypatch.setattr(service.shutil, "disk_usage", disk_failure)
    assert client.post("/api/examples/flood", json={}).status_code == 503
    monkeypatch.setattr(service.shutil, "disk_usage", real_usage)

    def insert_failure(*_a, **_k):
        """Fail after verified media generation, before successful clip commit."""
        raise OSError("Simulated DB failure")

    monkeypatch.setattr(app.state.store, "insert", insert_failure)
    assert client.post("/api/examples/flood", json={}).status_code == 503
    assert list(app.state.store.media.iterdir()) == []


def test_store_cas_source_hash_revision_budget_and_immutability(client, processed, app, plan):
    """CAS protects both early and late publication; SQL immutable records cannot be edited."""
    store = app.state.store
    identifier = processed["id"]
    user = {"name": "alice", "role": "operator"}
    result = {"source_digest": "bad", "media_digest": "bad", "info": {}}
    with pytest.raises(HTTPException) as error:
        store.save(identifier, user, Plan.model_validate(plan), result, lambda _: None)
    assert error.value.status_code == 409
    plan["expected_version"] = 1
    with pytest.raises(HTTPException) as error:
        store.save(identifier, user, Plan.model_validate(plan), result, lambda _: None)
    assert error.value.status_code == 503
    import sqlite3

    with pytest.raises(sqlite3.IntegrityError), store.connect(True) as db:
        db.execute("UPDATE revisions SET actor='admin' WHERE clip=?", (identifier,))
    with store.connect(True) as db:
        db.execute("UPDATE clips SET version=5 WHERE id=?", (identifier,))
    plan["expected_version"] = 5
    assert client.post(f"/api/clips/{identifier}/process", json=plan).status_code == 409
    with pytest.raises(HTTPException):
        store.file(identifier, user, "unknown")


def test_capacity_retention_dry_run_confirm_and_unexpected_files(client, processed, app):
    """Purge validates targets, defaults to no deletion and never removes active clips."""
    store = app.state.store
    identifier = processed["id"]
    folder = store.folder(identifier)
    assert purge(store)["expired_clips"] == 0
    with store.connect(True) as db:
        db.execute("UPDATE clips SET expires=? WHERE id=?", (time.time() - 1, identifier))
    assert purge(store)["media_bytes"] > 0 and folder.is_dir()
    (folder / "unexpected.txt").write_text("not an application media file")
    with pytest.raises(ValueError):
        purge(store, confirm=True)
    assert (folder / "source.mp4").is_file()
    (folder / "unexpected.txt").unlink()
    assert purge(store, confirm=True) == {"expired_clips": 1, "media_bytes": None, "deleted": True}
    assert not folder.exists()
    with store.connect() as db:
        assert db.execute("SELECT count(*) FROM clips").fetchone()[0] == 0
        assert db.execute("SELECT count(*) FROM revisions").fetchone()[0] == 0
        assert (
            db.execute("SELECT event FROM audit ORDER BY id DESC LIMIT 1").fetchone()[0]
            == "expired_media_purged"
        )


def test_missing_media_and_source_changed_after_verified_work(
    client, imported, plan, app, monkeypatch
):
    """A valid but replaced source cannot be promoted under the original identity/hash."""
    original_run = service.run

    def changed(*args, **kwargs):
        """Keep real video processing, perturb only its source identity to reproduce stale/corrupt publication."""
        result = original_run(*args, **kwargs)
        result["source_digest"] = "0" * 64
        return result

    monkeypatch.setattr(service, "run", changed)
    assert client.post(f"/api/clips/{imported['id']}/process", json=plan).status_code == 503
    (app.state.store.folder(imported["id"]) / "preview.mp4").unlink()
    assert client.get(f"/api/clips/{imported['id']}/media/preview?version=0").status_code == 503


def test_review_race_and_readonly_review(client, processed, app, monkeypatch):
    """Review rechecks version after verifying bytes, guarding an interleaving editor commit."""
    store = app.state.store
    identifier = processed["id"]
    real_file = store.file

    def moved(*args, **kwargs):
        """Interleave a valid new processed revision after file verification but before review transaction."""
        result = real_file(*args, **kwargs)
        with store.connect(True) as db:
            db.execute(
                "INSERT INTO revisions SELECT clip,2,actor,plan,plan_digest,media_digest,info,created FROM revisions WHERE clip=? AND version=1",
                (identifier,),
            )
            db.execute("UPDATE clips SET version=2 WHERE id=?", (identifier,))
        return result

    monkeypatch.setattr(store, "file", moved)
    with pytest.raises(HTTPException) as error:
        store.review(
            identifier,
            {"name": "reviewer", "role": "reviewer"},
            Review(
                expected_version=1,
                decision="approve",
                full_clip_checked=True,
                context_checked=True,
                note="Independent all-frame review",
            ),
        )
    assert error.value.status_code == 409
