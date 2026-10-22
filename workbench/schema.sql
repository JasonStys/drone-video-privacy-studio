-- Jason Stys: private users, source clips, immutable processed revisions/reviews and access history.
-- Column and declaration locations: docs/SOURCE_MAP.md. One trusted local organization, not multi-tenant SaaS.
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS users (
 name TEXT PRIMARY KEY, password_hash TEXT NOT NULL,
 role TEXT NOT NULL CHECK(role IN ('admin','operator','reviewer'))
);
CREATE TABLE IF NOT EXISTS sessions (
 digest TEXT PRIMARY KEY, username TEXT NOT NULL REFERENCES users(name),
 csrf TEXT NOT NULL, expires REAL NOT NULL, created REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS sessions_user ON sessions(username);
CREATE TABLE IF NOT EXISTS attempts (client TEXT PRIMARY KEY, count INTEGER NOT NULL, started REAL NOT NULL);
CREATE TABLE IF NOT EXISTS clips (
 id TEXT PRIMARY KEY, creator TEXT NOT NULL REFERENCES users(name), title TEXT NOT NULL,
 purpose TEXT NOT NULL, source_digest TEXT NOT NULL, preview_digest TEXT NOT NULL,
 info TEXT NOT NULL, version INTEGER NOT NULL DEFAULT 0,
 created REAL NOT NULL, expires REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS clips_creator ON clips(creator, created DESC);
CREATE TABLE IF NOT EXISTS revisions (
 clip TEXT NOT NULL REFERENCES clips(id) ON DELETE CASCADE, version INTEGER NOT NULL,
 actor TEXT NOT NULL REFERENCES users(name), plan TEXT NOT NULL, plan_digest TEXT NOT NULL,
 media_digest TEXT NOT NULL, info TEXT NOT NULL, created REAL NOT NULL,
 PRIMARY KEY (clip,version)
);
CREATE TABLE IF NOT EXISTS reviews (
 clip TEXT NOT NULL, version INTEGER NOT NULL, actor TEXT NOT NULL REFERENCES users(name),
 decision TEXT NOT NULL CHECK(decision IN ('approve','reject')), note TEXT NOT NULL,
 created REAL NOT NULL, PRIMARY KEY(clip,version),
 FOREIGN KEY(clip,version) REFERENCES revisions(clip,version) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS audit (
 id INTEGER PRIMARY KEY, at REAL NOT NULL, actor TEXT NOT NULL, clip TEXT NOT NULL,
 event TEXT NOT NULL, version INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS audit_clip ON audit(clip,id DESC);
CREATE TRIGGER IF NOT EXISTS immutable_revision BEFORE UPDATE ON revisions BEGIN SELECT RAISE(ABORT,'immutable revision'); END;
CREATE TRIGGER IF NOT EXISTS immutable_review BEFORE UPDATE ON reviews BEGIN SELECT RAISE(ABORT,'immutable review'); END;
