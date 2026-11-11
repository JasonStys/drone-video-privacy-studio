"""Jason Stys: frozen setup precedes data, diagnostics stay codec-free and failed dependency import stops. Lines: docs/SOURCE_MAP.md."""

import subprocess
import sys

import launcher
from workbench import codec_window, desktop


def test_source_owner_and_profile_imports_do_not_load_codecs_before_consent():
    """An actual fresh interpreter imports the full native shell with no PyAV import or profile initialization."""
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import sys; import workbench.desktop,workbench.owner_window; assert 'av' not in sys.modules; print('native-shell-before-codecs')",
        ],
        cwd=desktop.ROOT,
        capture_output=True,
        text=True,
        check=True,
        timeout=10,
    )
    assert result.stdout.strip() == "native-shell-before-codecs"


def test_frozen_cancel_returns_before_profile_or_server_launch(monkeypatch):
    """A real entrypoint cancellation cannot continue into the existing native data window."""
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "argv", ["native"])
    calls = []
    monkeypatch.setattr(codec_window, "ensure", lambda **kwargs: calls.append(kwargs) or False)
    monkeypatch.setattr(
        desktop, "main", lambda: (_ for _ in ()).throw(AssertionError("cancel opened profile"))
    )
    assert launcher.main() == 0
    assert calls == [{"interactive": True, "console": False}]


def test_frozen_runtime_diagnostic_does_not_trigger_dependency_install(monkeypatch):
    """The packaged GUI/runtime identity can be checked offline before any optional dependency exists."""
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "argv", ["native", "--runtime-info"])
    monkeypatch.setattr(
        codec_window,
        "ensure",
        lambda **_kwargs: (_ for _ in ()).throw(AssertionError("diagnostic fetched dependency")),
    )
    monkeypatch.setattr(desktop, "main", lambda: 0)
    assert launcher.main() == 0


def test_failed_frozen_dependency_import_is_nonzero_without_profile_fallback(monkeypatch, capsys):
    """A platform DLL/import failure remains an actual setup failure, not a successful empty app."""
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "argv", ["native", "--no-window", "--no-browser"])

    def fail(**kwargs):
        assert kwargs == {"interactive": False, "console": False}
        raise ImportError("controlled DLL import failure")

    monkeypatch.setattr(codec_window, "ensure", fail)
    monkeypatch.setattr(
        desktop,
        "main",
        lambda: (_ for _ in ()).throw(AssertionError("failed import opened profile")),
    )
    assert launcher.main() == 1
    assert "controlled DLL import failure" in capsys.readouterr().err
