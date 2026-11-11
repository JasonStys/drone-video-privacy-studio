"""Jason Stys: genuine wheel/RECORD, extraction, consent, offline/tamper and preservation regressions. Lines: docs/SOURCE_MAP.md."""

import base64
import csv
import hashlib
import io
import json
import os
import stat
import sys
import time
import zipfile
from pathlib import Path
from types import SimpleNamespace

import pytest

from workbench import codec_setup as setup
from workbench import codec_window


def wheel_fixture(*, change=None, extras=(), mode=None, compression=zipfile.ZIP_DEFLATED):
    """Build a real independent inert wheel with complete separately computed RECORD identities."""
    dist = "av-19.0.2.dist-info"
    tag = "cp312-abi3-win_amd64"
    files = {
        "av/__init__.py": b"raise RuntimeError('test wheel must never execute during installation')\n",
        "av/empty.txt": b"",
        f"{dist}/METADATA": b"Metadata-Version: 2.4\nName: av\nVersion: 19.0.2\n\n",
        f"{dist}/WHEEL": f"Wheel-Version: 1.0\nRoot-Is-Purelib: false\nTag: {tag}\n\n".encode(),
        f"{dist}/licenses/LICENSE.txt": b"Independent inert copyright fixture; retain this complete notice.\n",
    }
    if change:
        change(files)
    records = io.StringIO(newline="")
    writer = csv.writer(records)
    for name, raw in sorted(files.items()):
        writer.writerow(
            (
                name,
                "sha256="
                + base64.urlsafe_b64encode(hashlib.sha256(raw).digest()).decode().rstrip("="),
                str(len(raw)),
            )
        )
    writer.writerow((f"{dist}/RECORD", "", ""))
    files[f"{dist}/RECORD"] = records.getvalue().encode()
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=compression) as archive:
        for name, raw in files.items():
            item = zipfile.ZipInfo(name)
            item.compress_type = compression
            if mode:
                item.create_system = 3
                item.external_attr = mode << 16
            archive.writestr(item, raw)
        for name, raw in extras:
            # ZipInfo's constructor normalizes Windows separators; assign the
            # literal archive name afterward to test the reader's real guard.
            item = zipfile.ZipInfo()
            item.filename = name
            archive.writestr(item, raw)
    raw = output.getvalue()
    pin = {
        "filename": "av-19.0.2-" + tag + ".whl",
        "tag": tag,
        "url": "https://files.pythonhosted.org/packages/aa/bb/cc/av-19.0.2-" + tag + ".whl",
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }
    return raw, pin, files


class Response(io.BytesIO):
    """A real byte stream exposes a separately checked exact provider URL; no actual test internet call."""

    def __init__(self, raw, url):
        super().__init__(raw)
        self.url = url

    def geturl(self):
        return self.url


def provider(raw, pin, calls=None):
    """Controlled official-shaped response; records whether explicit consent actually caused a fetch."""

    def open_url(url, *, timeout):
        if calls is not None:
            calls.append((url, timeout))
        return Response(raw, pin["url"])

    return open_url


def test_exact_published_wheel_manifest_retains_platform_abi_and_lock_pins():
    """Real official metadata is bound to independent known Windows/Linux/Mac SHA256s, not inferred success."""
    pins = setup.pins()
    assert {key: (row["bytes"], row["sha256"]) for key, row in pins.items()} == {
        "win32-amd64": (
            28150949,
            "3ce5a1d7b916d13c16ac58f1756f0fee4af2d53f02bc1403e18550b50d375a22",
        ),
        "linux-x86_64": (
            34990159,
            "9c1da7aad0fa6c13b4a5c1e7985be0d13f8526a96284573acaf3d55ead6d3fe8",
        ),
        "darwin-arm64": (
            18556422,
            "b0dff6dfcc6ff9944fbbff15bc4ee2d90a2c1695d493bdea96e86f48823e9feb",
        ),
    }
    lock = (Path(__file__).resolve().parents[1] / "requirements.lock").read_text(encoding="utf-8")
    for row in pins.values():
        assert row["sha256"] in lock and "cp312-abi3-" in row["filename"]
    assert (
        setup.selected_pin(system="win32", machine="AMD64", python=(3, 14), gil_disabled=False)
        == pins["win32-amd64"]
    )
    assert (
        setup.selected_pin(
            system="linux",
            machine="x86_64",
            python=(3, 14),
            gil_disabled=False,
            libc=("glibc", "2.28"),
        )
        == pins["linux-x86_64"]
    )
    assert (
        setup.selected_pin(
            system="darwin", machine="arm64", python=(3, 14), gil_disabled=False, mac="14.0"
        )
        == pins["darwin-arm64"]
    )


@pytest.mark.parametrize(
    "changes",
    [
        {"python": (3, 12)},
        {"python": (3, 15)},
        {"gil_disabled": True},
        {"machine": "arm64"},
        {"system": "unknown"},
        {"system": "linux", "machine": "x86_64", "libc": ("musl", "1.2")},
        {"system": "linux", "machine": "x86_64", "libc": ("glibc", "2.27")},
        {"system": "darwin", "machine": "arm64", "mac": "13.6"},
    ],
)
def test_unsupported_runtime_or_abi_never_selects_a_fallback(changes):
    """A plausible wrong architecture, free-threaded ABI or older OS is refused, not silently given another wheel."""
    values = {
        "system": "win32",
        "machine": "amd64",
        "python": (3, 14),
        "gil_disabled": False,
        **changes,
    }
    with pytest.raises(ValueError):
        setup.selected_pin(**values)


def test_real_wheel_install_is_inert_complete_and_offline_reusable(tmp_path, monkeypatch):
    """Actual ZIP files and record hashes survive install; a later verified read performs no fetch/import."""
    raw, pin, files = wheel_fixture()
    home, calls = tmp_path / "dependencies", []
    assert setup.installed(home, pin) is None and not home.exists()
    site = setup.install(home, pin, open_url=provider(raw, pin, calls))
    assert calls == [(pin["url"], 30)]
    assert {
        p.relative_to(site).as_posix(): p.read_bytes() for p in site.rglob("*") if p.is_file()
    } == files
    monkeypatch.setattr(
        setup, "download", lambda *_a, **_k: pytest.fail("offline verification attempted download")
    )
    assert setup.installed(home, pin) == site
    before = {
        p.relative_to(home).as_posix(): p.read_bytes() for p in home.rglob("*") if p.is_file()
    }
    with pytest.raises(ValueError, match="preserved"):
        setup.install(home, pin)
    assert before == {
        p.relative_to(home).as_posix(): p.read_bytes() for p in home.rglob("*") if p.is_file()
    }


@pytest.mark.parametrize(
    "kind", ["truncated", "oversized", "same-size-corrupt", "redirect", "offline"]
)
def test_failed_download_does_not_publish_or_clobber_existing_files(tmp_path, kind):
    """Every failure happens on actual streamed bytes, preserving a prior unrelated install marker and no activation pointer."""
    raw, pin, _ = wheel_fixture()
    home = tmp_path / "dependencies"
    setup.store(home, create=True)
    protected = home / "unrelated-owned-receipt.txt"
    protected.write_bytes(b"preserve exactly")
    altered = (
        raw[:-1]
        if kind == "truncated"
        else raw + b"extra"
        if kind == "oversized"
        else b"!" + raw[1:]
        if kind == "same-size-corrupt"
        else raw
    )

    def fetch(_url, *, timeout):
        assert timeout == 30
        if kind == "offline":
            raise OSError("offline fixture")
        return Response(
            altered, "https://untrusted.invalid/codec" if kind == "redirect" else pin["url"]
        )

    with pytest.raises((ValueError, OSError)):
        setup.install(home, pin, open_url=fetch)
    assert protected.read_bytes() == b"preserve exactly"
    assert not (home / setup.pointer_name(pin)).exists()
    assert not any(p.name.startswith((".installing-", ".installed-")) for p in home.iterdir())


@pytest.mark.parametrize(
    "name",
    [
        "../escape.py",
        "/escape.py",
        "av/../escape.py",
        "av\\escape.py",
        "C:/escape.py",
        "av//escape.py",
        "other/script.py",
    ],
)
def test_actual_traversal_wheels_are_rejected_before_extraction(tmp_path, name):
    """Even a matching whole-wheel digest cannot authorize an escaping or unexpected package path."""
    raw, pin, _ = wheel_fixture(extras=[(name, b"inert payload")])
    with pytest.raises(ValueError, match="Unsafe"):
        setup.install(tmp_path / "dependencies", pin, open_url=provider(raw, pin))
    assert not (tmp_path / "escape.py").exists()


@pytest.mark.parametrize(
    "kind",
    [
        "duplicate",
        "symlink",
        "fifo",
        "bzip",
        "missing-license",
        "wrong-name",
        "wrong-version",
        "wrong-abi",
        "pure-python",
        "wheel-version",
        "record-hash",
        "record-missing",
        "member-budget",
        "total-budget",
    ],
)
def test_independent_wheel_structure_metadata_record_and_inflation_negatives(kind, monkeypatch):
    """A real ZIP with recomputed outer hash reaches each independent ABI/RECORD/expansion guard."""
    dist = setup.DIST

    def change(files):
        if kind == "missing-license":
            files.pop(f"{dist}/licenses/LICENSE.txt")
        elif kind == "wrong-name":
            files[f"{dist}/METADATA"] = b"Name: another\nVersion: 19.0.2\n"
        elif kind == "wrong-version":
            files[f"{dist}/METADATA"] = b"Name: av\nVersion: 0.0\n"
        elif kind == "wrong-abi":
            files[f"{dist}/WHEEL"] = (
                b"Wheel-Version: 1.0\nRoot-Is-Purelib: false\nTag: cp314-cp314t-win_amd64\n"
            )
        elif kind == "pure-python":
            files[f"{dist}/WHEEL"] = (
                b"Wheel-Version: 1.0\nRoot-Is-Purelib: true\nTag: cp312-abi3-win_amd64\n"
            )
        elif kind == "wheel-version":
            files[f"{dist}/WHEEL"] = (
                b"Wheel-Version: 2.0\nRoot-Is-Purelib: false\nTag: cp312-abi3-win_amd64\n"
            )

    raw, pin, _ = wheel_fixture(
        change=change,
        extras=[("av/__init__.py", b"different")] if kind == "duplicate" else (),
        mode=stat.S_IFLNK | 0o777
        if kind == "symlink"
        else stat.S_IFIFO | 0o600
        if kind == "fifo"
        else None,
        compression=zipfile.ZIP_BZIP2 if kind == "bzip" else zipfile.ZIP_DEFLATED,
    )
    if kind.startswith("record-"):
        output = io.BytesIO()
        with zipfile.ZipFile(io.BytesIO(raw)) as source, zipfile.ZipFile(output, "w") as target:
            for item in source.infolist():
                data = source.read(item)
                if item.filename.endswith("/RECORD"):
                    data = (
                        data.replace(b"sha256=", b"sha512=", 1)
                        if kind == "record-hash"
                        else data.split(b"\n", 1)[1]
                    )
                target.writestr(item, data)
        raw = output.getvalue()
        pin = {**pin, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
    if kind == "member-budget":
        monkeypatch.setattr(setup, "MAX_MEMBER", 32)
    if kind == "total-budget":
        monkeypatch.setattr(setup, "MAX_EXPANDED", 64)
    with pytest.raises(ValueError):
        setup.wheel_members(raw, pin)


@pytest.mark.parametrize("kind", ["member", "extra", "wheel", "pointer", "marker"])
def test_tampered_installed_dependency_is_preserved_and_not_repaired(tmp_path, kind):
    """Offline verification checks exact extracted contents as well as the original wheel and activation identity."""
    raw, pin, _ = wheel_fixture()
    home = tmp_path / "dependencies"
    site = setup.install(home, pin, open_url=provider(raw, pin))
    path = (
        site / "av/__init__.py"
        if kind == "member"
        else site / "av/extra.py"
        if kind == "extra"
        else site.parent / "official.whl"
        if kind == "wheel"
        else home / setup.pointer_name(pin)
        if kind == "pointer"
        else home / "dependency-store.json"
    )
    path.write_bytes(b"corrupt evidence; preserve it")
    with pytest.raises((ValueError, json.JSONDecodeError, zipfile.BadZipFile)):
        setup.installed(home, pin)
    assert path.read_bytes() == b"corrupt evidence; preserve it"


def test_unknown_nonempty_dependency_directory_and_failed_atomic_publish_preserve_prior_state(
    tmp_path, monkeypatch
):
    """No adoption of unrelated files, and exclusive pointer publication cannot replace a concurrent installation."""
    home = tmp_path / "unknown"
    home.mkdir()
    (home / "private.txt").write_bytes(b"unrelated")
    raw, pin, _ = wheel_fixture()
    with pytest.raises(ValueError, match="preserved"):
        setup.install(home, pin, open_url=provider(raw, pin))
    assert sorted(p.name for p in home.iterdir()) == ["private.txt"]
    owned = tmp_path / "owned"

    def competitor(_pending, pointer):
        with pointer.open("xb") as output:
            output.write(b"other writer's exact evidence")
        raise FileExistsError("concurrent pointer")

    monkeypatch.setattr(setup.os, "link", competitor)
    with pytest.raises(FileExistsError):
        setup.install(owned, pin, open_url=provider(raw, pin))
    assert (owned / setup.pointer_name(pin)).read_bytes() == b"other writer's exact evidence"
    assert not any(p.name.startswith(".installed-") for p in owned.iterdir())


@pytest.mark.parametrize("nested", [False, True])
def test_offline_verification_refuses_unknown_directories_before_descending(
    tmp_path, monkeypatch, nested
):
    """The old rglob accepted empty extras and traversed populated extras; neither is permitted by the exact tree."""
    raw, pin, _ = wheel_fixture()
    home = tmp_path / "dependencies"
    site = setup.install(home, pin, open_url=provider(raw, pin))
    extra = site / "av" / "unexpected"
    extra.mkdir()
    if nested:
        for index in range(20):
            child = extra / str(index) / "deeper"
            child.mkdir(parents=True)
            (child / "inert.txt").write_bytes(b"unrelated; preserve")
    actual_scandir, visited = setup.os.scandir, []

    def bounded_scan(path):
        path = Path(path)
        assert not path.is_relative_to(extra), "Unexpected subtree was traversed before refusal"
        visited.append(path)
        return actual_scandir(path)

    monkeypatch.setattr(setup.os, "scandir", bounded_scan)
    with pytest.raises(ValueError, match="Unexpected installed wheel entry|traversal exceeds"):
        setup.installed(home, pin)
    assert extra.is_dir() and all(not path.is_relative_to(extra) for path in visited)
    assert len(visited) <= 4


@pytest.mark.parametrize("part", ["site", "av"])
def test_actual_junction_or_symlink_cannot_replace_expected_dependency_directories(tmp_path, part):
    """Use a genuine Windows junction or POSIX symlink, including the site root rather than only leaf files."""
    raw, pin, _ = wheel_fixture()
    home = tmp_path / "dependencies"
    site = setup.install(home, pin, open_url=provider(raw, pin))
    original = site if part == "site" else site / "av"
    retained = site.parent / ("retained-" + part)
    original.rename(retained)
    if os.name == "nt":
        import _winapi

        _winapi.CreateJunction(str(retained), str(original))
        assert original.is_junction()
    else:
        original.symlink_to(retained, target_is_directory=True)
        assert original.is_symlink()
    with pytest.raises(ValueError, match="Linked"):
        setup.installed(home, pin)
    target = retained / "__init__.py" if part == "av" else retained / "av/__init__.py"
    assert target.read_bytes().startswith(b"raise RuntimeError")


def test_offline_activation_requires_verified_source_path_and_exact_version(tmp_path, monkeypatch):
    """An import resolver pointing at a developer copy cannot satisfy native provenance even after wheel verification."""
    raw, pin, _ = wheel_fixture()
    home = tmp_path / "dependencies"
    site = setup.install(home, pin, open_url=provider(raw, pin))
    monkeypatch.delitem(sys.modules, "av", raising=False)
    monkeypatch.setattr(sys, "path", list(sys.path))
    monkeypatch.setattr(sys, "dont_write_bytecode", False)
    monkeypatch.setenv("DVP_DEPENDENCY_HOME", "unchanged-before-activation")
    monkeypatch.setattr(
        setup.importlib,
        "import_module",
        lambda _name: SimpleNamespace(__file__=str(site / "av/__init__.py"), __version__="19.0.2"),
    )
    assert setup.activate(home, pin) == {
        "version": "19.0.2",
        "wheel_sha256": pin["sha256"],
        "offline_verification": True,
    }
    monkeypatch.setattr(
        setup.importlib,
        "import_module",
        lambda _name: SimpleNamespace(
            __file__=str(tmp_path / "developer/av/__init__.py"), __version__="19.0.2"
        ),
    )
    with pytest.raises(ValueError, match="another source"):
        setup.activate(home, pin)


def test_explicit_setup_cancel_opens_neither_network_nor_profile(tmp_path, monkeypatch):
    """Real Tk Cancel leaves even the dependency directory absent, before any accounts/footage are opened."""
    import tkinter as tk

    raw, pin, _ = wheel_fixture()
    calls = []
    monkeypatch.setattr(setup, "download", lambda *_a, **_k: calls.append("unexpected"))
    root = tk.Tk()
    window = codec_window.DependencyWindow(root, tmp_path / "dependencies", pin)
    root.update()
    assert pin["url"] in window.text.get("1.0", "end") and str(pin["bytes"]) not in window.text.get(
        "1.0", "end"
    )
    assert f"{pin['bytes']:,}" in window.text.get("1.0", "end")
    window.cancel_button.invoke()
    assert not window.accepted and calls == [] and not (tmp_path / "dependencies").exists()
    assert not raw.startswith(b"fake-success")


def test_real_setup_install_button_finishes_actual_inert_wheel_before_continuing(
    tmp_path, monkeypatch
):
    """Clicking the genuine Tk button causes exactly one actual installer and waits for its completion."""
    import tkinter as tk

    raw, pin, _ = wheel_fixture()
    actual = setup.install
    calls = []
    monkeypatch.setattr(
        setup, "install", lambda home, row: actual(home, row, open_url=provider(raw, pin, calls))
    )
    root = tk.Tk()
    home = tmp_path / "dependencies"
    window = codec_window.DependencyWindow(root, home, pin)
    root.update()
    window.install_button.invoke()
    window.install()
    deadline = time.monotonic() + 5
    while not window.accepted and time.monotonic() < deadline:
        root.update()
    assert (
        window.accepted and calls == [(pin["url"], 30)] and setup.installed(home, pin) is not None
    )


def test_setup_failure_remains_visible_without_retry_or_profile_creation(tmp_path, monkeypatch):
    """A genuine offline error is not converted to success or hidden behind another attempt."""
    import tkinter as tk

    _, pin, _ = wheel_fixture()
    calls = []

    def offline(*_args):
        calls.append(1)
        raise OSError("controlled offline")

    monkeypatch.setattr(setup, "install", offline)
    root = tk.Tk()
    window = codec_window.DependencyWindow(root, tmp_path / "dependencies", pin)
    try:
        window.install_button.invoke()
        deadline = time.monotonic() + 5
        while "Setup failed" not in window.status.get() and time.monotonic() < deadline:
            root.update()
        assert "controlled offline" in window.status.get() and not window.accepted
        assert calls == [1] and str(window.install_button["state"]) == "disabled"
        assert not (tmp_path / "dependencies").exists()
    finally:
        root.destroy()


def test_console_consent_and_noninteractive_offline_refusal_are_explicit(
    tmp_path, monkeypatch, capsys
):
    """Only exact INSTALL consent can invoke setup; automated worker mode cannot fetch implicitly."""
    raw, pin, _ = wheel_fixture()
    home = tmp_path / "dependencies"
    monkeypatch.setattr(setup, "selected_pin", lambda: pin)
    monkeypatch.setattr(setup, "dependency_home", lambda: home)
    monkeypatch.setattr("builtins.input", lambda _prompt: "cancel")
    assert codec_window.ensure(console=True) is False and not home.exists()
    with pytest.raises(ValueError, match="absent"):
        codec_window.ensure(interactive=False)
    actual = setup.install
    monkeypatch.setattr(
        setup, "install", lambda home, row: actual(home, row, open_url=provider(raw, pin))
    )
    activations = []
    monkeypatch.setattr(setup, "activate", lambda home, row: activations.append((home, row)))
    monkeypatch.setattr("builtins.input", lambda _prompt: "INSTALL")
    assert codec_window.ensure(console=True) is True
    assert codec_window.ensure(interactive=False) is True
    assert activations == [(home, pin), (home, pin)]
    assert pin["url"] in capsys.readouterr().out
