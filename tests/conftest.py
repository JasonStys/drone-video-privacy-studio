"""Jason Stys: isolated real SQLite/auth fixtures and original generated video; lines: docs/SOURCE_MAP.md."""

import secrets

import pytest
from fastapi.testclient import TestClient

from workbench.api import create_app
from workbench.auth import HASHER
from workbench.media import synthetic

ORIGIN = "http://127.0.0.1:8891"


@pytest.fixture(scope="session")
def accounts():
    """Hash random disposable passwords once; no test credentials enter source or reports."""
    return {
        name: (password := secrets.token_urlsafe(24), HASHER.hash(password), role)
        for name, role in [
            ("alice", "operator"),
            ("bob", "operator"),
            ("reviewer", "reviewer"),
            ("admin", "admin"),
        ]
    }


@pytest.fixture
def app(tmp_path, accounts):
    """Each test owns a new database/media root; no user workspace is opened."""
    instance = create_app(tmp_path / "db.sqlite3")
    with instance.state.store.connect(True) as db:
        for name, (_, hashed, role) in accounts.items():
            db.execute("INSERT INTO users VALUES(?,?,?)", (name, hashed, role))
    return instance


@pytest.fixture
def client(app):
    """Use exact local Host/Origin even under ASGI transport."""
    with TestClient(app, base_url=ORIGIN, headers={"Origin": ORIGIN}) as connection:
        yield connection


@pytest.fixture
def login(client, accounts):
    """Sign in through real Argon2/session code, replacing the current test client's session."""

    def enter(name="alice"):
        response = client.post("/api/login", json={"username": name, "password": accounts[name][0]})
        assert response.status_code == 200
        client.headers["X-CSRF-Token"] = response.json()["csrf"]
        return response.json()

    return enter


@pytest.fixture(scope="session")
def video(tmp_path_factory):
    """Four seconds, forty real encoded frames, conspicuous patches and private metadata markers."""
    path = tmp_path_factory.mktemp("synthetic-video") / "source.mp4"
    synthetic(path, "flood")
    return path


@pytest.fixture
def imported(client, login, video):
    """Exercise the real upload, worker subprocess, decoder, encoder and database commit."""
    login()
    response = client.post(
        "/api/clips/import?title=Synthetic+review&purpose=Authorized+synthetic+training&retention=7",
        content=video.read_bytes(),
        headers={"Content-Type": "video/mp4"},
    )
    assert response.status_code == 200, response.text
    return response.json()


@pytest.fixture
def plan():
    """Independent expected regions enclose all motion of generated patch and mock plate."""
    return {
        "expected_version": 0,
        "masks": [
            {
                "first": 0,
                "last": 39,
                "x": 0.06,
                "y": 0.15,
                "width": 0.24,
                "height": 0.18,
                "reason": "face",
            },
            {
                "first": 0,
                "last": 39,
                "x": 0.62,
                "y": 0.67,
                "width": 0.18,
                "height": 0.13,
                "reason": "plate",
            },
        ],
        "note": "Check moving test patch, mock plate and context",
        "telemetry": [],
        "offset_ms": 0,
    }


@pytest.fixture
def processed(client, imported, plan):
    """Create a real verified first revision; it deliberately has no reviewer approval."""
    response = client.post(f"/api/clips/{imported['id']}/process", json=plan)
    assert response.status_code == 200, response.text
    return response.json()
