"""Jason Stys: actual metadata-shaped license/attribution inventory without bytecode. Lines: docs/SOURCE_MAP.md."""

from importlib.metadata import distribution
from pathlib import Path
from types import SimpleNamespace

from tools.runtime_notices import notice_paths


def test_windows_metadata_paths_retain_attribution_and_nonstandard_license_suffixes(tmp_path):
    """A complete notice folder includes AUTHORS.rst/LICENSE.APACHE, but not Python source or compiled bytecode."""
    names = [
        Path("package.dist-info/licenses/LICENSE.APACHE"),
        Path("package.dist-info/licenses/AUTHORS.rst"),
        Path("package.dist-info/licenses/__pycache__/AUTHORS.cpython-314.pyc"),
        Path("package.dist-info/licenses/AUTHORS.py"),
    ]
    info = SimpleNamespace(files=names, locate_file=lambda name: tmp_path / name)
    assert notice_paths(info) == [tmp_path / names[0], tmp_path / names[1]]


def test_actual_locked_runtime_notices_are_text_and_keep_original_license(tmp_path):
    """The real installed NumPy wheel's license inventory is not inferred from the simplified path fixture."""
    notices = notice_paths(distribution("numpy"))
    assert notices and any(path.name.upper().startswith("LICENSE") for path in notices)
    for path in notices:
        raw = path.read_bytes()
        assert raw and b"\0" not in raw and path.suffix.lower() not in {".py", ".pyc", ".pyo"}
        raw.decode("utf-8")
