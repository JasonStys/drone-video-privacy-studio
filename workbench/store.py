"""Jason Stys: transactional source/revision/review ledger and fail-closed private media paths.

Exact methods, parameters and variables: docs/SOURCE_MAP.md. Database is outside the webroot.
"""

import hashlib
import json
import re
import sqlite3
import time
from contextlib import contextmanager
from pathlib import Path

from fastapi import HTTPException

from workbench.models import Plan, alignment


def canonical(value):
    """Stable finite JSON for independent revision integrity checks."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    """Hash canonical plan content; hashes detect accidents, not a malicious OS administrator."""
    return hashlib.sha256(canonical(value).encode()).hexdigest()


class Store:
    """One local staff workspace; operators see their clips, reviewers/admin see this organization."""

    def __init__(self, path: Path):
        """Create application-owned media directories and schema without replacing existing data."""
        self.path = path.resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.media = self.path.parent / "media"
        self.media.mkdir(exist_ok=True)
        with self.connect() as db:
            db.executescript(Path(__file__).with_name("schema.sql").read_text(encoding="utf-8"))

    @contextmanager
    def connect(self, write=False):
        """Close every connection; commit only complete writes under BEGIN IMMEDIATE."""
        db = sqlite3.connect(self.path, timeout=5)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys=ON")
        try:
            if write:
                db.execute("BEGIN IMMEDIATE")
            yield db
            if write:
                db.commit()
        finally:
            db.close()

    def folder(self, identifier: str):
        """Resolve only generated 32-hex IDs; refuse symlinks/junction escapes and user paths."""
        if not re.fullmatch(r"[0-9a-f]{32}", identifier):
            raise HTTPException(404, "Clip not found")
        path = self.media / identifier
        if path.is_symlink() or path.resolve().parent != self.media.resolve():
            raise HTTPException(503, "Media directory integrity failure")
        return path

    def event(self, db, user, identifier, event, version=0):
        """Append structured access/state events without passwords, tokens, filenames or clip notes."""
        db.execute(
            "INSERT INTO audit(at,actor,clip,event,version) VALUES(?,?,?,?,?)",
            (time.time(), user, identifier, event, version),
        )

    def get(self, identifier, user, db=None):
        """Object access before details, expiry on every read, and revision hash verification."""
        if db is None:
            with self.connect() as connection:
                return self.get(identifier, user, connection)
        row = db.execute("SELECT * FROM clips WHERE id=?", (identifier,)).fetchone()
        if row is None or (user["role"] == "operator" and row["creator"] != user["name"]):
            raise HTTPException(404, "Clip not found")
        if row["expires"] <= time.time():
            raise HTTPException(410, "Retention expired; access/export blocked")
        clip = dict(row)
        clip["info"] = json.loads(clip["info"])
        revision = db.execute(
            "SELECT * FROM revisions WHERE clip=? AND version=?", (identifier, clip["version"])
        ).fetchone()
        clip["revision"] = None
        if revision:
            value = dict(revision)
            value["plan"] = json.loads(value["plan"])
            value["info"] = json.loads(value["info"])
            if digest(value["plan"]) != value["plan_digest"]:
                raise HTTPException(503, "Plan integrity failure")
            value["alignment"] = alignment(
                Plan.model_validate(value["plan"]), clip["info"]["frames"], clip["info"]["fps"]
            )
            review = db.execute(
                "SELECT actor,decision,note,created FROM reviews WHERE clip=? AND version=?",
                (identifier, clip["version"]),
            ).fetchone()
            value["review"] = dict(review) if review else None
            clip["revision"] = value
        return clip

    def list(self, user):
        """Bound history, hide expired objects and prevent cross-operator enumeration."""
        with self.connect() as db:
            rows = db.execute(
                "SELECT id,title,creator,version,expires FROM clips WHERE expires>? AND (? != 'operator' OR creator=?) ORDER BY created DESC LIMIT 40",
                (time.time(), user["role"], user["name"]),
            )
            return [dict(row) for row in rows]

    def capacity(self):
        """Hard clip budget: twelve retained clips, including expired entries until purged."""
        with self.connect() as db:
            if db.execute("SELECT count(*) FROM clips").fetchone()[0] >= 12:
                raise HTTPException(
                    409, "Workspace clip limit reached; archive/purge expired clips via CLI"
                )

    def insert(self, identifier, user, title, purpose, retention, result):
        """Publish only verified, moved media; caller holds the processing gate for capacity safety."""
        with self.connect(True) as db:
            self.event(db, user["name"], identifier, "clip_imported")
            now = time.time()
            db.execute(
                "INSERT INTO clips VALUES(?,?,?,?,?,?,?,?,?,?)",
                (
                    identifier,
                    user["name"],
                    title,
                    purpose,
                    result["source_digest"],
                    result["media_digest"],
                    canonical(result["info"]),
                    0,
                    now,
                    now + retention * 86400,
                ),
            )

    def save(self, identifier, user, plan: Plan, result, move):
        """Compare-and-swap after expensive work; new revision invalidates previous approval."""
        with self.connect(True) as db:
            clip = self.get(identifier, user, db)
            if plan.expected_version != clip["version"] or clip["version"] >= 5:
                raise HTTPException(409, "Revision changed or five-version limit reached")
            if result["source_digest"] != clip["source_digest"]:
                raise HTTPException(503, "Source integrity failure")
            version = clip["version"] + 1
            move(version)
            content = plan.model_dump()
            db.execute(
                "INSERT INTO revisions VALUES(?,?,?,?,?,?,?,?)",
                (
                    identifier,
                    version,
                    user["name"],
                    canonical(content),
                    digest(content),
                    result["media_digest"],
                    canonical(result["info"]),
                    time.time(),
                ),
            )
            db.execute("UPDATE clips SET version=? WHERE id=?", (version, identifier))
            self.event(db, user["name"], identifier, "revision_processed", version)
            return version

    def file(self, identifier, user, kind, record=True, version=None):
        """Authorize current media on each range/download; verify bytes and reject symlink files."""
        with self.connect(True) as db:
            clip = self.get(identifier, user, db)
            if kind not in {"preview", "redacted", "export"}:
                raise HTTPException(404, "Media not found")
            if version is not None and clip["version"] != version:
                raise HTTPException(409, "Revision changed; refresh")
            revision = clip["revision"]
            if kind == "preview":
                name, expected = "preview.mp4", clip["preview_digest"]
            else:
                if revision is None:
                    raise HTTPException(409, "Process a revision first")
                if kind == "export" and (
                    not revision["review"] or revision["review"]["decision"] != "approve"
                ):
                    raise HTTPException(409, "Independent current-revision approval required")
                name, expected = f"revision-{clip['version']}.mp4", revision["media_digest"]
            path = self.folder(identifier) / name
            if (
                path.is_symlink()
                or not path.is_file()
                or path.resolve().parent != self.folder(identifier).resolve()
                or hashlib.sha256(path.read_bytes()).hexdigest() != expected
            ):
                raise HTTPException(503, "Media integrity failure")
            if record:
                self.event(db, user["name"], identifier, f"{kind}_accessed", clip["version"])
            return path

    def review(self, identifier, user, body):
        """Require a different designated reviewer and exact revision; rejection never enables export."""
        self.file(identifier, user, "redacted", record=False, version=body.expected_version)
        with self.connect(True) as db:
            clip = self.get(identifier, user, db)
            revision = clip["revision"]
            if user["name"] in {clip["creator"], revision["actor"]}:
                raise HTTPException(403, "A different reviewer is required")
            if body.expected_version != clip["version"]:
                raise HTTPException(409, "Revision changed; review again")
            if revision["review"]:
                raise HTTPException(409, "Revision already reviewed; create a new revision")
            if body.decision == "approve" and (
                not body.full_clip_checked
                or not body.context_checked
                or revision["alignment"]["status"] == "warning"
            ):
                raise HTTPException(
                    409, "Full-clip/context confirmation and resolved telemetry drift required"
                )
            db.execute(
                "INSERT INTO reviews VALUES(?,?,?,?,?,?)",
                (identifier, clip["version"], user["name"], body.decision, body.note, time.time()),
            )
            self.event(db, user["name"], identifier, f"review_{body.decision}", clip["version"])

    def history(self, identifier, user):
        """Return private revision/access history only to an authorized clip reader."""
        with self.connect() as db:
            self.get(identifier, user, db)
            revisions = [
                dict(r)
                for r in db.execute(
                    "SELECT version,actor,plan_digest,media_digest,created FROM revisions WHERE clip=? ORDER BY version",
                    (identifier,),
                )
            ]
            events = [
                dict(r)
                for r in db.execute(
                    "SELECT at,actor,event,version FROM audit WHERE clip=? ORDER BY id DESC LIMIT 100",
                    (identifier,),
                )
            ]
            return {"revisions": revisions, "events": events}

    def manifest(self, identifier, user):
        """Minimal approved derivative receipt: omit title, identities, original hash, notes and telemetry."""
        clip = self.get(identifier, user)
        path = self.file(identifier, user, "export", version=clip["version"])
        revision = clip["revision"]
        return {
            "application": "Drone Video Privacy Studio",
            "author": "Jason Stys",
            "revision": clip["version"],
            "sha256": revision["media_digest"],
            "bytes": path.stat().st_size,
            "video": {
                key: clip["info"][key]
                for key in ("width", "height", "fps", "frames", "duration_ms")
            },
            "audio_included": False,
            "telemetry_included": False,
            "anonymity_guaranteed": False,
        }
