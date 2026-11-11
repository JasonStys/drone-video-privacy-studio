"""Jason Stys: fixed frozen-worker dispatch and real encoded video outputs. Lines: docs/SOURCE_MAP.md."""

import json
import subprocess
import sys

import pytest

import launcher
from workbench import service


def test_media_worker_cannot_read_or_block_on_the_owners_real_input_pipe(tmp_path):
    """A genuine child reads EOF while its parent's separate console command remains untouched."""
    worker = (
        "import json,sys; from pathlib import Path; "
        "(Path(sys.argv[1])/'result.json').write_text("
        "json.dumps({'worker_input':sys.stdin.read()}),encoding='utf-8')"
    )
    parent = (
        "import json,sys; from pathlib import Path; from workbench import service; "
        f"service.worker_command=lambda directory:[sys.executable,'-c',{worker!r},str(directory)]; "
        "result=service.run(Path(sys.argv[1]),[]); "
        "result['owner_input']=sys.stdin.read(); print(json.dumps(result))"
    )
    result = subprocess.run(
        [sys.executable, "-c", parent, str(tmp_path)],
        cwd=service.ROOT,
        input="synthetic-owner-command\n",
        text=True,
        capture_output=True,
        check=True,
        timeout=10,
    )
    assert json.loads(result.stdout) == {
        "worker_input": "",
        "owner_input": "synthetic-owner-command\n",
    }


def test_source_and_frozen_worker_commands_never_turn_inputs_into_modules(tmp_path, monkeypatch):
    """A service-owned path stays one argument; frozen work cannot launch the owner GUI or an arbitrary module."""
    assert service.worker_command(tmp_path) == [
        sys.executable,
        "-m",
        "workbench.worker",
        str(tmp_path),
    ]
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    assert service.worker_command(tmp_path) == [sys.executable, "--media-worker", str(tmp_path)]


def test_fixed_launcher_worker_executes_real_transcode_without_owner_window(
    tmp_path, video, monkeypatch
):
    """The actual launcher mode runs the real decoder/encoder/verification and returns the independent40-frame fixture."""
    (tmp_path / "source.mp4").write_bytes(video.read_bytes())
    (tmp_path / "job.json").write_text(json.dumps({"masks": [], "scenario": None}))
    monkeypatch.setattr(sys, "argv", ["native", "--media-worker", str(tmp_path)])
    assert launcher.main() == 0
    result = json.loads((tmp_path / "result.json").read_text())
    assert result["info"]["frames"] == 40 and (tmp_path / "result.mp4").is_file()
    (tmp_path / "job.json").write_text("bad")
    monkeypatch.setattr(sys, "argv", ["native", "--media-worker", str(tmp_path)])
    with pytest.raises(SystemExit) as error:
        launcher.main()
    assert error.value.code == 2


@pytest.mark.parametrize("arguments", [["--media-worker"], ["--media-worker", "one", "two"]])
def test_worker_mode_requires_exactly_one_service_directory(arguments, monkeypatch):
    """Malformed native worker invocation fails before touching a profile or loading owner controls."""
    monkeypatch.setattr(sys, "argv", ["native", *arguments])
    with pytest.raises(SystemExit) as error:
        launcher.main()
    assert error.value.code == 2
