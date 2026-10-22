"""Jason Stys: CLI initialization, private provisioning, local launcher and explicit purge tests; lines: docs/SOURCE_MAP.md."""

import sys

import pytest

from tools import browser_server
from workbench import __main__ as cli


def test_init_provision_mismatch_and_purge(tmp_path, monkeypatch, capsys):
    """OS-authorized setup never writes a password to stdout/history or overwrites accounts."""
    db = tmp_path / "db.sqlite3"
    monkeypatch.setattr(sys, "argv", ["studio", "--db", str(db), "init"])
    cli.main()
    monkeypatch.setattr(
        sys, "argv", ["studio", "--db", str(db), "user", "operator", "--role", "operator"]
    )
    answers = iter(["test-private-long-password", "test-private-long-password"])
    monkeypatch.setattr(cli.getpass, "getpass", lambda _p: next(answers))
    cli.main()
    assert "test-private-long-password" not in capsys.readouterr().out
    answers = iter(["test-private-long-password", "different"])
    with pytest.raises(SystemExit, match="Passwords differ"):
        cli.main()
    for confirm in [[], ["--confirm"]]:
        monkeypatch.setattr(sys, "argv", ["studio", "--db", str(db), "purge-expired", *confirm])
        cli.main()


def test_serve_and_invalid_port(tmp_path, monkeypatch):
    """Production launcher cannot bind all interfaces or trust spoofable proxy client headers."""
    seen = []
    monkeypatch.setattr(cli.uvicorn, "run", lambda *args, **kwargs: seen.append(kwargs))
    monkeypatch.setattr(sys, "argv", ["studio", "--db", str(tmp_path / "db.sqlite3"), "serve"])
    cli.main()
    assert seen[0]["host"] == "127.0.0.1" and seen[0]["proxy_headers"] is False
    monkeypatch.setattr(
        sys, "argv", ["studio", "--db", str(tmp_path / "db.sqlite3"), "serve", "--port", "80"]
    )
    with pytest.raises(SystemExit, match="1024"):
        cli.main()


def test_disposable_browser_server_private_random_accounts(tmp_path, monkeypatch):
    """Repeated demonstration setup preserves its local random credentials; never a web admin bypass."""
    first = browser_server.prepare(tmp_path)
    content = (tmp_path / "credentials.json").read_bytes()
    assert browser_server.prepare(tmp_path) == first
    assert (tmp_path / "credentials.json").read_bytes() == content
    seen = []
    monkeypatch.setattr(browser_server.uvicorn, "run", lambda *args, **kwargs: seen.append(kwargs))
    monkeypatch.setattr(sys, "argv", ["browser", "--directory", str(tmp_path)])
    browser_server.main()
    assert seen[0]["host"] == "127.0.0.1" and seen[0]["proxy_headers"] is False
