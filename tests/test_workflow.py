"""Jason Stys: real media/auth/revision workflow and export leakage regression tests; lines: docs/SOURCE_MAP.md."""

import hashlib
import json
import time

import av
import pytest


def review(version=1, **changes):
    """Explicit human review contract, not an automated approval hidden in processing."""
    return {
        "expected_version": version,
        "decision": "approve",
        "full_clip_checked": True,
        "context_checked": True,
        "note": "Inspected all generated frames, patch motion and context",
        **changes,
    }


def test_complete_private_workflow_and_independent_pixel_oracle(client, processed, login, app):
    """Pixels in both identifiers must be dark in all forty frames; source marker/notes must not leak."""
    identifier = processed["id"]
    path = f"/api/clips/{identifier}"
    assert client.get(path + "/media/export?version=1").status_code == 409
    assert client.post(path + "/review", json=review()).status_code == 403
    login("reviewer")
    assert client.post(path + "/review", json=review()).status_code == 200
    exported = client.get(path + "/media/export?version=1")
    assert exported.status_code == 200
    assert "attachment" in exported.headers["content-disposition"]
    assert b"PRIVATE-SYNTHETIC-SOURCE-MARKER" not in exported.content
    receipt = client.get(path + "/manifest").json()
    assert receipt["sha256"] == hashlib.sha256(exported.content).hexdigest()
    assert (
        receipt["audio_included"]
        is receipt["telemetry_included"]
        is receipt["anonymity_guaranteed"]
        is False
    )
    assert not any(
        secret in json.dumps(receipt)
        for secret in [
            "alice",
            "Authorized",
            "Check moving",
            "source_digest",
            "east_m",
            "Synthetic review",
        ]
    )
    with av.open(str(app.state.store.folder(identifier) / "revision-1.mp4")) as media:
        assert len(media.streams) == 1
        frames = list(media.decode(video=0))
        assert len(frames) == 40
        for index, frame in enumerate(frames):
            pixels = frame.to_ndarray(format="rgb24")
            assert pixels[65:105, 60 + index * 2 : 100 + index * 2].max() <= 24
            assert pixels[250:275, 410:500].max() <= 24
            assert pixels[180, 200].mean() > 20  # A useful non-sensitive area survives.
    trail = client.get(path + "/history").json()
    assert trail["revisions"][0]["version"] == 1
    assert {e["event"] for e in trail["events"]} >= {
        "clip_imported",
        "revision_processed",
        "review_approve",
        "export_accessed",
    }


def test_new_revision_invalidates_approval_and_stale_editor(client, processed, login, plan):
    """Approval never flows forward; stale posts cannot overwrite a newer revision."""
    path = f"/api/clips/{processed['id']}"
    login("reviewer")
    assert client.post(path + "/review", json=review()).status_code == 200
    login()
    assert client.post(path + "/process", json=plan).status_code == 409
    plan["expected_version"] = 1
    assert client.post(path + "/process", json=plan).json()["version"] == 2
    assert client.get(path + "/media/export?version=2").status_code == 409
    assert client.get(path + "/media/redacted?version=1").status_code == 409
    login("reviewer")
    assert client.post(path + "/review", json=review()).status_code == 409
    assert client.post(path + "/review", json=review(2, decision="reject")).status_code == 200
    assert client.get(path + "/manifest").status_code == 409


@pytest.mark.parametrize(
    "endpoint",
    [
        "",
        "/history",
        "/manifest",
        "/media/preview?version=0",
        "/media/redacted?version=0",
        "/media/export?version=0",
    ],
)
def test_cross_operator_object_denial(client, imported, login, endpoint):
    """Another operator learns no clip details, media, history or export receipt."""
    login("bob")
    assert client.get(f"/api/clips/{imported['id']}" + endpoint).status_code == 404
    assert client.get("/api/clips").json() == []


def test_role_and_independence_boundaries(client, imported, login, plan, app):
    """Reviewers cannot create/edit; changing account role cannot allow self-review."""
    path = f"/api/clips/{imported['id']}"
    login("reviewer")
    assert client.post("/api/examples/flood", json={}).status_code == 403
    assert client.post(path + "/process", json=plan).status_code == 403
    login()
    assert client.post(path + "/process", json=plan).status_code == 200
    with app.state.store.connect(True) as db:
        db.execute("UPDATE users SET role='reviewer' WHERE name='alice'")
    assert client.post(path + "/review", json=review()).status_code == 403


@pytest.mark.parametrize("change", [{"full_clip_checked": False}, {"context_checked": False}])
def test_review_cannot_skip_attestation(client, processed, login, change):
    """Both review confirmations are server-enforced, not just disabled UI controls."""
    login("reviewer")
    path = f"/api/clips/{processed['id']}/review"
    assert client.post(path, json=review(**change)).status_code == 409
    assert client.post(path, json=review(decision="reject", **change)).status_code == 200
    assert client.post(path, json=review()).status_code == 409


def test_drift_blocks_approval_but_absent_is_explicit(client, imported, plan, login):
    """Optional absent positions are unknown; contradictory provided telemetry must be resolved."""
    path = f"/api/clips/{imported['id']}"
    plan["telemetry"] = [{"ms": 1000, "east_m": 0.0, "north_m": 0.0, "altitude_m": 40.0}]
    response = client.post(path + "/process", json=plan)
    assert response.json()["revision"]["alignment"]["status"] == "warning"
    login("reviewer")
    assert client.post(path + "/review", json=review()).status_code == 409


def test_expired_source_revision_history_and_download_denied(client, processed, app):
    """Expiry is enforced on every endpoint, including ranges and receipts."""
    path = f"/api/clips/{processed['id']}"
    with app.state.store.connect(True) as db:
        db.execute("UPDATE clips SET expires=? WHERE id=?", (time.time() - 1, processed["id"]))
    assert client.get("/api/clips").json() == []
    for suffix in [
        "",
        "/history",
        "/manifest",
        "/media/preview?version=1",
        "/media/redacted?version=1",
        "/media/export?version=1",
    ]:
        assert client.get(path + suffix).status_code == 410


def test_tampered_media_plan_and_source_fail_closed(client, processed, app, plan):
    """Modified bytes or stored masks do not silently produce trusted review/export evidence."""
    identifier = processed["id"]
    path = f"/api/clips/{identifier}"
    folder = app.state.store.folder(identifier)
    (folder / "preview.mp4").write_bytes(b"tampered")
    assert client.get(path + "/media/preview?version=1").status_code == 503
    (folder / "revision-1.mp4").write_bytes(b"tampered")
    assert client.get(path + "/media/redacted?version=1").status_code == 503
    (folder / "source.mp4").write_bytes(b"tampered")
    plan["expected_version"] = 1
    assert client.post(path + "/process", json=plan).status_code == 503
    with app.state.store.connect(True) as db:
        db.execute("DROP TRIGGER immutable_revision")
        db.execute("UPDATE revisions SET plan='{}' WHERE clip=?", (identifier,))
    assert client.get(path).status_code == 503


def test_range_requests_private_headers_and_no_original_endpoint(client, imported):
    """Browser playback uses authenticated ranges, while raw source and runtime paths stay private."""
    path = f"/api/clips/{imported['id']}"
    response = client.get(path + "/media/preview?version=0", headers={"Range": "bytes=0-31"})
    assert response.status_code == 206 and len(response.content) == 32
    assert response.headers["cache-control"] == "no-store"
    assert response.headers["x-content-type-options"] == "nosniff"
    for suffix in ["/source.mp4", "/media/original?version=0"]:
        assert client.get(path + suffix).status_code in {404, 422}
    assert client.get("/.runtime/workspace.sqlite3").status_code == 404
    assert client.get("/media/").status_code == 404


def test_invalid_clip_unknown_scenario_and_unprocessed_download(client, imported, plan):
    """Invalid IDs and enum names are not filesystem or worker commands."""
    assert client.post("/api/examples/unknown", json={}).status_code == 422
    assert client.get("/api/clips/not-a-real-id").status_code == 404
    assert client.get(f"/api/clips/{imported['id']}/media/redacted?version=0").status_code == 409
    plan["masks"][0]["last"] = 40
    assert client.post(f"/api/clips/{imported['id']}/process", json=plan).status_code == 422
