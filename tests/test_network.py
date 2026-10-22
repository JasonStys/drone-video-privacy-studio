"""Jason Stys: real loopback server regression for spoofed client headers; lines: docs/SOURCE_MAP.md."""

import socket
import threading
import time
from types import SimpleNamespace

import httpx
import uvicorn

from workbench import auth
from workbench.api import create_app


def test_forwarded_headers_do_not_bypass_real_server_throttle(tmp_path, monkeypatch):
    """Real TCP requests with rotating X-Forwarded-For still share the direct loopback attempt budget."""
    with socket.socket() as reservation:
        reservation.bind(("127.0.0.1", 0))
        port = reservation.getsockname()[1]
    app = create_app(tmp_path / "network.sqlite3", port)
    # Throttle logic is tested over TCP; real password verification is exercised by API/security tests.
    monkeypatch.setattr(auth, "HASHER", SimpleNamespace(verify=lambda *_a: True))
    server = uvicorn.Server(
        uvicorn.Config(
            app,
            host="127.0.0.1",
            port=port,
            access_log=False,
            proxy_headers=False,
            log_level="error",
        )
    )
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    try:
        for _ in range(100):
            if server.started:
                break
            time.sleep(0.02)
        assert server.started
        origin = f"http://127.0.0.1:{port}"
        with httpx.Client(base_url=origin, timeout=5, trust_env=False) as client:
            for index in range(21):
                response = client.post(
                    "/api/login",
                    json={"username": "unknown", "password": "wrong"},
                    headers={
                        "Origin": origin,
                        "X-Forwarded-For": f"192.0.2.{index}",
                        "Forwarded": f"for=192.0.2.{index}",
                    },
                )
                assert response.status_code == (401 if index < 20 else 429)
    finally:
        server.should_exit = True
        thread.join(timeout=5)
        assert not thread.is_alive()
