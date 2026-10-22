"""Jason Stys: explicit OS-owner purge of expired app-owned media only; lines: docs/SOURCE_MAP.md.

No secure-erasure claim; backup/export copies remain separate. No automatic deletion scheduler.
"""

import re
import time


def purge(store, confirm=False):
    """Default to dry-run; resolve/validate all targets before deleting any expired clip files.

    Never traverse a symlink, arbitrary directory or nested content. Keep minimal audit evidence.
    A crash can leave an expired object partly purged, but expiry still denies all API access.
    """
    with store.connect(True) as db:
        ids = [
            row[0] for row in db.execute("SELECT id FROM clips WHERE expires<=?", (time.time(),))
        ]
        targets = []
        for identifier in ids:
            folder = store.folder(identifier)
            files = list(folder.iterdir()) if folder.is_dir() else []
            for file in files:
                if (
                    file.is_symlink()
                    or not file.is_file()
                    or file.resolve().parent != folder.resolve()
                    or not re.fullmatch(r"(?:source|preview|revision-[1-5])\.mp4", file.name)
                ):
                    raise ValueError("Unexpected media content; inspect privately before purging")
            targets.append((identifier, folder, files))
        if confirm:
            for identifier, folder, files in targets:
                for file in files:
                    file.unlink()
                if folder.is_dir():
                    folder.rmdir()
                db.execute("DELETE FROM clips WHERE id=?", (identifier,))
                store.event(db, "local-cli", identifier, "expired_media_purged")
        return {
            "expired_clips": len(ids),
            "media_bytes": sum(file.stat().st_size for _, _, files in targets for file in files)
            if not confirm
            else None,
            "deleted": confirm,
        }
