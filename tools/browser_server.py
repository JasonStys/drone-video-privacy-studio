"""Jason Stys: disposable synthetic UI acceptance/demo accounts; lines: docs/SOURCE_MAP.md."""

import argparse
import json
import secrets
from pathlib import Path

import uvicorn

from workbench.api import create_app
from workbench.auth import add_user
from workbench.store import Store


def prepare(directory: Path):
    """Generate random test-only credentials in ignored runtime, never print or commit passwords."""
    directory.mkdir(parents=True, exist_ok=True)
    db = directory / "workspace.sqlite3"
    credentials = directory / "credentials.json"
    store = Store(db)
    if not credentials.is_file():
        values = {
            role: {"username": f"demo-{role}", "password": secrets.token_urlsafe(24)}
            for role in ("admin", "operator", "reviewer")
        }
        for role, entry in values.items():
            add_user(store, entry["username"], entry["password"], role)
        credentials.write_text(json.dumps(values), encoding="utf-8")
    return db


def main():
    """Launch only the requested local sandbox; no real accounts or preapproved exports."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=Path(".runtime/browser"))
    parser.add_argument("--port", type=int, default=8892)
    args = parser.parse_args()
    db = prepare(args.directory)
    uvicorn.run(
        create_app(db, args.port),
        host="127.0.0.1",
        port=args.port,
        access_log=False,
        proxy_headers=False,
        limit_concurrency=24,
    )


if __name__ == "__main__":
    main()
