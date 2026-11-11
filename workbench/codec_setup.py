"""Jason Stys: explicit official-wheel setup, bounded extraction and verified offline reuse. Lines: docs/SOURCE_MAP.md.

Pin selection, install and activate keep native codecs outside our downloadable
application. No footage, profile, password, pip or source-build hook is involved.
"""

import base64
import csv
import hashlib
import importlib
import io
import json
import os
import platform
import re
import shutil
import stat
import sys
import sysconfig
import tempfile
import time
import urllib.request
import zipfile
from email.parser import BytesParser
from pathlib import Path, PurePosixPath

PRODUCT = "drone-video-privacy-studio"
VERSION = "19.0.2"
DIST = "av-19.0.2.dist-info"
MAX_WHEEL = 40 * 1024 * 1024
MAX_MEMBER = 128 * 1024 * 1024
MAX_EXPANDED = 512 * 1024 * 1024
MAX_MEMBERS = 4096
STORE_ID = {"schema_version": 1, "product": PRODUCT, "purpose": "official-codec-dependency"}


def require(condition, message):
    """Keep setup, provenance and extraction refusals active under optimized Python."""
    if not condition:
        raise ValueError(message)


def bounded_file(path: Path, limit: int) -> bytes:
    """Read one regular descriptor with a byte cap and exact opened-size check."""
    require(not path.is_symlink(), "Linked dependency file refused")
    descriptor = os.open(
        path,
        os.O_RDONLY
        | getattr(os, "O_BINARY", 0)
        | getattr(os, "O_NONBLOCK", 0)
        | getattr(os, "O_NOFOLLOW", 0),
    )
    with os.fdopen(descriptor, "rb") as stream:
        info = os.fstat(stream.fileno())
        require(
            stat.S_ISREG(info.st_mode) and 0 <= info.st_size <= limit,
            "Dependency file type/size invalid",
        )
        # Size was read from this opened descriptor. One extra byte detects
        # growth without allocating the128MiB member cap for each tiny file.
        raw = stream.read(min(info.st_size + 1, limit + 1))
    require(
        len(raw) == info.st_size and len(raw) <= limit,
        "Dependency file changed or exceeded its bound",
    )
    return raw


def pins() -> dict:
    """The public resource pins exactly three reviewed native platform wheels, not arbitrary URLs."""
    root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[1]))
    value = json.loads(bounded_file(root / "workbench/resources/pyav-wheels.json", 8192))
    require(
        set(value) == {"schema_version", "product", "dependency", "version", "wheels"}
        and type(value["schema_version"]) is int
        and value["schema_version"] == 1
        and value["product"] == PRODUCT
        and value["dependency"] == "av"
        and value["version"] == VERSION
        and set(value["wheels"]) == {"win32-amd64", "linux-x86_64", "darwin-arm64"},
        "Unknown official-wheel manifest",
    )
    for row in value["wheels"].values():
        require(
            set(row) == {"filename", "url", "bytes", "sha256", "tag"}
            and re.fullmatch(r"[a-f0-9]{64}", row["sha256"])
            and type(row["bytes"]) is int
            and 0 < row["bytes"] <= MAX_WHEEL
            and row["filename"] == f"av-{VERSION}-{row['tag']}.whl"
            and re.fullmatch(r"cp312-abi3-[a-zA-Z0-9_]+", row["tag"])
            and re.fullmatch(
                r"https://files[.]pythonhosted[.]org/packages/[a-f0-9/]+/"
                + re.escape(row["filename"]),
                row["url"],
            ),
            "Invalid official-wheel pin",
        )
    return value["wheels"]


def selected_pin(*, system=None, machine=None, python=None, gil_disabled=None, libc=None, mac=None):
    """Only standard CPython3.14 and the actually validated OS/CPU/ABI families can use setup."""
    system = sys.platform if system is None else system
    machine = platform.machine().lower() if machine is None else machine.lower()
    python = sys.version_info[:2] if python is None else python
    gil_disabled = (
        sysconfig.get_config_var("Py_GIL_DISABLED") if gil_disabled is None else gil_disabled
    )
    require(
        python == (3, 14) and not gil_disabled,
        "This native dependency requires standard CPython3.14",
    )
    key = f"{system}-{machine}"
    require(key in pins(), "Unsupported native platform/CPU; no wheel was downloaded")
    if system == "linux":
        family, version = platform.libc_ver() if libc is None else libc
        require(
            family == "glibc" and tuple(map(int, version.split(".")[:2])) >= (2, 28),
            "The reviewed Linux wheel requires glibc2.28 or later",
        )
    if system == "darwin":
        version = platform.mac_ver()[0] if mac is None else mac
        require(
            int(version.split(".")[0]) >= 14,
            "The reviewed Apple Silicon wheel requires macOS14 or later",
        )
    return pins()[key]


def dependency_home() -> Path:
    """Keep dependencies separate from profiles; an explicit OS-owner override is useful for isolated acceptance."""
    explicit = os.environ.get("DVP_DEPENDENCY_HOME")
    if explicit:
        result = Path(explicit)
    else:
        if sys.platform == "win32":
            base = Path(os.environ["LOCALAPPDATA"])
        elif sys.platform == "darwin":
            base = Path.home() / "Library/Application Support"
        else:
            base = Path(os.environ.get("XDG_DATA_HOME", str(Path.home() / ".local/share")))
        result = base / "JasonStysPortfolio" / PRODUCT / "dependencies"
    require(
        result.is_absolute()
        and not result.is_symlink()
        and not result.is_junction()
        and result.resolve() == result,
        "Dependency directory must be an absolute non-linked path",
    )
    return result


def store(home: Path, *, create=False):
    """Never adopt unknown nonempty directories or replace an existing dependency-store identity."""
    require(
        home.is_absolute()
        and not home.is_symlink()
        and not home.is_junction()
        and home.resolve() == home,
        "Linked dependency store refused",
    )
    marker = home / "dependency-store.json"
    if not home.exists():
        if not create:
            return False
        home.mkdir(parents=True, mode=0o700)
    if not marker.exists():
        require(create and not any(home.iterdir()), "Unknown dependency directory preserved")
        with marker.open("x", encoding="utf-8") as output:
            json.dump(STORE_ID, output)
    require(
        not marker.is_symlink() and json.loads(bounded_file(marker, 1024)) == STORE_ID,
        "Dependency store identity differs",
    )
    return True


def wheel_members(raw: bytes, pin: dict) -> dict[str, bytes]:
    """Hash the exact wheel, bound real inflation, validate RECORD/ABI and retain every actual upstream notice."""
    require(
        len(raw) == pin["bytes"] and hashlib.sha256(raw).hexdigest() == pin["sha256"],
        "Official wheel size/SHA256 differs",
    )
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        items = archive.infolist()
        require(
            0 < len(items) <= MAX_MEMBERS and len({x.filename for x in items}) == len(items),
            "Wheel member count/duplicate invalid",
        )
        total, files = 0, {}
        for item in items:
            # ZipInfo normalizes backslashes on Windows; inspect the original
            # stored name as well so the same refusal applies on every OS.
            name, mode = item.orig_filename, item.external_attr >> 16
            path = PurePosixPath(name)
            require(
                name
                and name == item.filename
                and "\\" not in name
                and not path.is_absolute()
                and not any(part in {"", ".", ".."} for part in name.rstrip("/").split("/"))
                and ":" not in name
                and path.parts[0] in {"av", "av.libs", DIST}
                and not stat.S_ISLNK(mode)
                and stat.S_IFMT(mode) in {0, stat.S_IFREG, stat.S_IFDIR}
                and not item.flag_bits & 1
                and item.compress_type in {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED},
                "Unsafe/unsupported wheel member",
            )
            if item.is_dir():
                continue
            total += item.file_size
            require(
                0 <= item.file_size <= MAX_MEMBER and total <= MAX_EXPANDED,
                "Wheel expansion exceeds budget",
            )
            with archive.open(item) as member:
                data = member.read(MAX_MEMBER + 1)
            require(
                len(data) == item.file_size and len(data) <= MAX_MEMBER,
                "Wheel member length differs/exceeds budget",
            )
            files[name] = data
    required = {
        f"{DIST}/METADATA",
        f"{DIST}/WHEEL",
        f"{DIST}/RECORD",
        f"{DIST}/licenses/LICENSE.txt",
        "av/__init__.py",
    }
    require(required <= set(files), "Wheel metadata/runtime notices incomplete")
    metadata = BytesParser().parsebytes(files[f"{DIST}/METADATA"])
    wheel = BytesParser().parsebytes(files[f"{DIST}/WHEEL"])
    require(
        metadata["Name"] == "av"
        and metadata["Version"] == VERSION
        and wheel["Wheel-Version"] == "1.0"
        and wheel.get_all("Tag") == [pin["tag"]]
        and wheel["Root-Is-Purelib"] == "false",
        "Wheel package/version/ABI differs",
    )
    records = list(csv.reader(io.StringIO(files[f"{DIST}/RECORD"].decode("utf-8"))))
    require(
        all(len(row) == 3 for row in records)
        and len(records) == len(files)
        and {row[0] for row in records} == set(files),
        "Wheel RECORD inventory differs",
    )
    for name, digest, size in records:
        if name == f"{DIST}/RECORD":
            require(digest == size == "", "Wheel RECORD self-entry differs")
        else:
            expected = "sha256=" + base64.urlsafe_b64encode(
                hashlib.sha256(files[name]).digest()
            ).decode().rstrip("=")
            require(
                digest == expected and size == str(len(files[name])),
                "Wheel RECORD hash/length differs",
            )
    return files


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Only the exact pinned HTTPS provider URL is contacted; redirects never become a new trust source."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Official-wheel redirects are not accepted")


def download(pin, *, open_url=None) -> bytes:
    """One bounded public dependency fetch, with no proxy credentials, profile data, retries or installer scripts."""
    opener = (
        open_url or urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect()).open
    )
    deadline = time.monotonic() + 90
    with opener(pin["url"], timeout=30) as response:
        require(response.geturl() == pin["url"], "Official-wheel authority/path changed")
        output = io.BytesIO()
        while chunk := response.read(min(1024 * 1024, pin["bytes"] - output.tell() + 1)):
            require(
                time.monotonic() <= deadline and output.tell() + len(chunk) <= pin["bytes"],
                "Wheel download exceeded length/deadline",
            )
            output.write(chunk)
    raw = output.getvalue()
    wheel_members(raw, pin)
    return raw


def pointer_name(pin):
    """An immutable wheel digest names only its small atomic activation pointer."""
    return f"av-{VERSION}-{pin['sha256']}.json"


def has_installation(home: Path, pin: dict) -> bool:
    """Presence chooses setup only; it never authorizes imports or substitutes for activate's complete verification."""
    if not store(home):
        return False
    pointer = home / pointer_name(pin)
    return pointer.exists() or pointer.is_symlink() or pointer.is_junction()


def installed(home: Path, pin: dict):
    """Verify the wheel and every extracted byte offline before import; unknown/tampered installs are preserved and refused."""
    if not store(home):
        return None
    pointer = home / pointer_name(pin)
    if not pointer.exists():
        return None
    require(not pointer.is_symlink(), "Linked dependency pointer refused")
    value = json.loads(bounded_file(pointer, 2048))
    require(
        set(value) == {"schema_version", "wheel_sha256", "directory"}
        and type(value["schema_version"]) is int
        and value["schema_version"] == 1
        and value["wheel_sha256"] == pin["sha256"]
        and re.fullmatch(r"[.]installed-[a-f0-9]{32}", value["directory"]),
        "Dependency activation identity differs",
    )
    directory = home / value["directory"]
    require(
        not directory.is_symlink()
        and not directory.is_junction()
        and directory.resolve() == directory
        and directory.is_dir(),
        "Dependency install path changed",
    )
    files = wheel_members(bounded_file(directory / "official.whl", MAX_WHEEL), pin)
    site = directory / "site"
    require(
        not site.is_symlink()
        and not site.is_junction()
        and site.is_dir()
        and site.resolve() == site,
        "Linked/missing dependency site refused",
    )
    expected_directories = {
        parent.as_posix()
        for name in files
        for parent in PurePosixPath(name).parents
        if parent != PurePosixPath(".")
    }
    actual, visited, pending = {}, 0, [site]
    while pending:
        current = pending.pop()
        require(
            current.resolve() == current and not current.is_symlink() and not current.is_junction(),
            "Linked dependency directory refused before traversal",
        )
        with os.scandir(current) as entries:
            for entry in entries:
                visited += 1
                require(
                    visited <= len(files) + len(expected_directories),
                    "Installed wheel traversal exceeds exact expected tree",
                )
                path = Path(entry.path)
                name = path.relative_to(site).as_posix()
                # Unknown directories are refused before being queued. Never
                # traverse an arbitrary subtree to discover its mismatch later.
                require(
                    name in files or name in expected_directories,
                    "Unexpected installed wheel entry",
                )
                require(
                    not entry.is_symlink() and not path.is_junction() and path.resolve() == path,
                    "Linked dependency member refused",
                )
                info = entry.stat(follow_symlinks=False)
                if name in expected_directories:
                    require(
                        stat.S_ISDIR(info.st_mode), "Expected dependency directory changed type"
                    )
                    pending.append(path)
                else:
                    require(stat.S_ISREG(info.st_mode), "Expected dependency file changed type")
                    actual[name] = path
    require(set(actual) == set(files), "Installed wheel inventory differs")
    for name, raw in files.items():
        require(bounded_file(actual[name], MAX_MEMBER) == raw, "Installed wheel member differs")
    return site


def install(home: Path, pin: dict, *, open_url=None) -> Path:
    """Install only after explicit consent, then atomically publish an absent pointer without overwriting prior state."""
    store(home, create=True)
    pointer = home / pointer_name(pin)
    require(
        not pointer.exists() and not pointer.is_symlink(),
        "Existing dependency evidence preserved; no overwrite",
    )
    raw = download(pin, open_url=open_url)
    files = wheel_members(raw, pin)
    directory = Path(tempfile.mkdtemp(prefix=".installing-", dir=home))
    published = False
    try:
        (directory / "official.whl").write_bytes(raw)
        for name, data in files.items():
            path = directory / "site" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as output:
                output.write(data)
        import uuid

        final = home / (".installed-" + uuid.uuid4().hex)
        directory.rename(final)
        directory = final
        pending = directory / "activation.json"
        pending.write_text(
            json.dumps(
                {"schema_version": 1, "wheel_sha256": pin["sha256"], "directory": directory.name}
            ),
            encoding="utf-8",
        )
        # A hard link publishes the complete immutable pointer exclusively on all three OSes.
        os.link(pending, pointer)
        published = True
        return installed(home, pin)
    finally:
        if not published:
            require(
                directory.is_absolute()
                and directory.parent == home
                and directory.resolve() == directory
                and directory.name.startswith((".installing-", ".installed-")),
                "Owned temporary dependency path changed; cleanup refused",
            )
            shutil.rmtree(directory)


def activate(home: Path, pin: dict):
    """Import only the exact verified local dependency tree; ordinary PyAV library import is not an installer/build hook."""
    site = installed(home, pin)
    require(
        site is not None, "Codec dependency is not installed; open the native setup window first"
    )
    require("av" not in sys.modules, "Codec loaded before native dependency verification")
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(site))
    importlib.invalidate_caches()
    av = importlib.import_module("av")
    require(
        Path(av.__file__).resolve().is_relative_to(site / "av") and av.__version__ == VERSION,
        "Loaded codec came from another source",
    )
    os.environ["DVP_DEPENDENCY_HOME"] = str(home)
    return {"version": VERSION, "wheel_sha256": pin["sha256"], "offline_verification": True}
