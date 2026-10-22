"""Jason Stys: private account provisioning and loopback-only launch; lines: docs/SOURCE_MAP.md."""

import argparse
import getpass
from pathlib import Path

import uvicorn

from workbench.api import create_app
from workbench.auth import add_user
from workbench.retention import purge
from workbench.store import Store


def main():
    """No web setup, email collection or public password reset; local OS owner provisions staff."""
    parser = argparse.ArgumentParser(description="Drone Video Privacy Studio by Jason Stys")
    parser.add_argument("--db", type=Path, default=Path(".runtime/workspace.sqlite3"))
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init")
    cleanup = commands.add_parser("purge-expired")
    cleanup.add_argument("--confirm", action="store_true")
    user = commands.add_parser("user")
    user.add_argument("name")
    user.add_argument("--role", choices=["admin", "operator", "reviewer"], required=True)
    serve = commands.add_parser("serve")
    serve.add_argument("--port", type=int, default=8891)
    args = parser.parse_args()
    store = Store(args.db)
    if args.command == "init":
        print("Private workspace initialized; existing clips/accounts preserved.")
    elif args.command == "purge-expired":
        print(purge(store, confirm=args.confirm))
    elif args.command == "user":
        password = getpass.getpass("New local password (14-128 characters): ")
        if password != getpass.getpass("Confirm password: "):
            raise SystemExit("Passwords differ")
        add_user(store, args.name, password, args.role)
        print("Local account created without writing password to source/history.")
    else:
        if not 1024 <= args.port <= 65535:
            raise SystemExit("Use a port from 1024 through 65535")
        uvicorn.run(
            create_app(args.db, args.port),
            host="127.0.0.1",
            port=args.port,
            access_log=False,
            proxy_headers=False,
            limit_concurrency=24,
        )


if __name__ == "__main__":
    main()
