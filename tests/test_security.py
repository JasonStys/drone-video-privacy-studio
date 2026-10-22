"""Jason Stys: exact-origin, session, request bounds and private-path regressions; lines: docs/SOURCE_MAP.md."""

import hashlib
import secrets
import sqlite3
import time

import pytest
from fastapi import HTTPException

from workbench import api, auth
from workbench.store import Store


def test_authentication_csrf_cookie_and_revocation(client, login, accounts, app):
    """Session bearer never lives raw in SQLite; logout instantly revokes it."""
    assert client.get("/api/me").status_code == 401
    assert client.get("/api/clips").status_code == 401
    assert (
        client.post("/api/login", json={"username": "alice", "password": "wrong"}).status_code
        == 401
    )
    assert (
        client.post("/api/login", json={"username": "unknown", "password": "wrong"}).status_code
        == 401
    )
    user = login()
    assert client.get("/api/me").json()["name"] == "alice"
    cookie = client.cookies["video_session"]
    with app.state.store.connect() as db:
        assert db.execute(
            "SELECT digest FROM sessions WHERE digest=?",
            (hashlib.sha256(cookie.encode()).hexdigest(),),
        ).fetchone()
        assert not db.execute("SELECT digest FROM sessions WHERE digest=?", (cookie,)).fetchone()
        assert (
            db.execute("SELECT password_hash FROM users WHERE name='alice'").fetchone()[0]
            != accounts["alice"][0]
        )
    assert client.post("/api/logout", json={}, headers={"X-CSRF-Token": "wrong"}).status_code == 403
    response = client.post("/api/logout", json={})
    assert response.status_code == 200
    assert client.get("/api/me").status_code == 401
    client.cookies.set("video_session", cookie)
    assert client.get("/api/me").status_code == 401
    assert user["role"] == "operator"


def test_no_password_reflection_and_exact_host_origin(client, accounts):
    """Cross-origin requests and malformed credentials never reflect supplied secrets."""
    body = {"username": "alice", "password": accounts["alice"][0] * 20}
    response = client.post("/api/login", json=body)
    assert response.status_code == 422 and accounts["alice"][0] not in response.text
    assert client.get("/healthz", headers={"Host": "evil.example"}).status_code == 400
    assert (
        client.post("/api/login", json={}, headers={"Origin": "https://evil.example"}).status_code
        == 403
    )
    assert (
        client.post("/api/login", json={}, headers={"Sec-Fetch-Site": "cross-site"}).status_code
        == 403
    )
    assert client.get("/api/me", headers={"Origin": "https://evil.example"}).status_code == 403
    assert client.put("/api/login", json={}).status_code == 405
    assert (
        client.post("/api/login", content="x", headers={"Content-Type": "text/plain"}).status_code
        == 415
    )
    assert (
        client.post(
            "/api/login", content=b"a" * 65537, headers={"Content-Type": "application/json"}
        ).status_code
        == 413
    )
    assert client.get("/healthz").json()["status"] == "ok"
    assert "frame-ancestors 'none'" in client.get("/healthz").headers["content-security-policy"]


def test_upload_auth_type_size_and_invalid_video(client, login):
    """Authentication happens before video bytes are accepted; MIME alone is insufficient."""
    path = "/api/clips/import?title=Bad+clip&purpose=Authorized+synthetic+test"
    assert client.post(path, content=b"x", headers={"Content-Type": "video/mp4"}).status_code == 401
    login()
    assert (
        client.post(
            path, content=b"x", headers={"Content-Type": "application/octet-stream"}
        ).status_code
        == 415
    )
    assert client.post(path, content=b"x", headers={"Content-Type": "video/mp4"}).status_code == 422
    assert (
        client.post(
            path, content=b"x" * (20 * 1024 * 1024 + 1), headers={"Content-Type": "video/mp4"}
        ).status_code
        == 413
    )
    assert client.get("/api/clips").json() == []


def test_expiry_role_recheck_and_cookie_bounds(client, login, app):
    """Expired token, overlong token and changed server-side role cannot keep earlier authority."""
    login()
    with app.state.store.connect(True) as db:
        db.execute("UPDATE users SET role='reviewer' WHERE name='alice'")
    assert client.get("/api/me").json()["role"] == "reviewer"
    with app.state.store.connect(True) as db:
        db.execute("UPDATE sessions SET expires=?", (time.time() - 1,))
    assert client.get("/api/me").status_code == 401
    client.cookies.clear()
    client.cookies.set("video_session", "x" * 101)
    assert client.get("/api/me").status_code == 401


def test_persistent_login_throttle_and_concurrent_verification_gate(client, app, monkeypatch):
    """Different usernames share direct-client throttling; hash concurrency is independently bounded."""
    with app.state.store.connect(True) as db:
        db.execute(
            "INSERT INTO attempts VALUES(?,20,?)",
            (hashlib.sha256(b"testclient").hexdigest(), time.time()),
        )
    assert (
        client.post("/api/login", json={"username": "unknown", "password": "wrong"}).status_code
        == 429
    )
    with app.state.store.connect(True) as db:
        db.execute("DELETE FROM attempts")

    class Busy:
        """Independent occupied hashing slot without allocating Argon memory."""

        def acquire(self, blocking):
            """Reject additional verification under pressure."""
            return False

    monkeypatch.setattr(auth, "VERIFY_GATE", Busy())
    assert (
        client.post("/api/login", json={"username": "unknown", "password": "wrong"}).status_code
        == 429
    )


def test_attempt_and_session_bounds(client, login, app):
    """Unbounded addresses or sessions cannot grow memory-hard auth work/state indefinitely."""
    with app.state.store.connect(True) as db:
        db.executemany(
            "INSERT INTO attempts VALUES(?,1,?)",
            [(str(index), time.time()) for index in range(1000)],
        )
    assert (
        client.post("/api/login", json={"username": "unknown", "password": "wrong"}).status_code
        == 429
    )
    with app.state.store.connect(True) as db:
        db.execute("DELETE FROM attempts")
        db.executemany(
            "INSERT INTO sessions VALUES(?,?,?,?,?)",
            [
                (
                    secrets.token_hex(32),
                    "alice",
                    "test-csrf",
                    time.time() + 3600,
                    time.time() + index,
                )
                for index in range(12)
            ],
        )
    login()
    with app.state.store.connect() as db:
        assert (
            db.execute("SELECT count(*) FROM sessions WHERE username='alice'").fetchone()[0] == 10
        )


@pytest.mark.parametrize(
    "name,password,role",
    [
        ("Bad", "a" * 14, "operator"),
        ("valid", "short", "operator"),
        ("valid", "a" * 129, "operator"),
        ("valid", "a" * 14, "owner"),
    ],
)
def test_cli_user_validation(app, name, password, role):
    """CLI refuses weak/unbounded credentials, invalid roles and ambiguous usernames."""
    with pytest.raises(ValueError):
        auth.add_user(app.state.store, name, password, role)


def test_cli_user_duplicate_and_transaction_rollback(app):
    """Provisioning never overwrites accounts; failed transactions leave no partial audit."""
    store = app.state.store
    auth.add_user(store, "new-user", secrets.token_urlsafe(24), "operator")
    with pytest.raises(sqlite3.IntegrityError):
        auth.add_user(store, "new-user", secrets.token_urlsafe(24), "operator")
    with pytest.raises(RuntimeError), store.connect(True) as db:
        store.event(db, "alice", "none", "should_rollback")
        raise RuntimeError("Simulated failure")
    with store.connect() as db:
        assert db.execute("SELECT count(*) FROM audit").fetchone()[0] == 0


def test_body_capacity_and_port_validation(client, monkeypatch, tmp_path):
    """Backpressure is visible rather than buffering arbitrary concurrent upload bodies."""

    class Busy:
        """Occupied body reader slots."""

        def acquire(self, blocking):
            """Refuse this request without reading its payload."""
            return False

    monkeypatch.setattr(api, "BODY_GATE", Busy())
    assert client.post("/api/login", json={}).status_code == 429
    with pytest.raises(ValueError):
        api.create_app(tmp_path / "invalid.sqlite3", 80)


def test_path_validation_and_symlink(app, tmp_path):
    """No relative traversal, absolute paths, URLs or outside directory symlinks are accepted."""
    store: Store = app.state.store
    for invalid in ["../escape", "https://example.com", "f" * 31, "F" * 32]:
        with pytest.raises(HTTPException):
            store.folder(invalid)
    path = store.media / ("a" * 32)
    try:
        path.symlink_to(tmp_path, target_is_directory=True)
    except OSError:
        pytest.skip("OS does not grant symlink creation to this test process")
    with pytest.raises(HTTPException):
        store.folder("a" * 32)
