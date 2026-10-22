"""Jason Stys: actual PNG fallback decoding, frame boundaries and object-level access tests; lines: docs/SOURCE_MAP.md."""

import io
import json

import av
import pytest

from workbench import media, worker


def test_private_frame_endpoint_uses_processed_pixels_and_no_metadata(client, processed, login):
    """Codec-limited browsers receive actual current redacted pixels, not an unrelated placeholder."""
    path = f"/api/clips/{processed['id']}/frame/redacted?version=1&index=39"
    response = client.get(path)
    assert response.status_code == 200 and response.headers["content-type"] == "image/png"
    assert response.headers["cache-control"] == "no-store"
    assert response.content[:8] == b"\x89PNG\r\n\x1a\n"
    assert b"PRIVATE-SYNTHETIC" not in response.content
    with av.open(io.BytesIO(response.content)) as frame:
        values = list(frame.decode(video=0))
        assert len(values) == 1
        pixels = values[0].to_ndarray(format="rgb24")
        assert pixels[65:105, 138:178].max() <= 24
        assert pixels[250:275, 410:500].max() <= 24
    assert client.get(path.replace("index=39", "index=40")).status_code == 422
    assert client.get(path.replace("version=1", "version=0")).status_code == 409
    assert client.get(path.replace("index=39", "index=-1")).status_code == 422
    login("bob")
    assert client.get(path).status_code == 404


def test_frame_renderer_native_bounds_and_worker_branch(tmp_path, video):
    """PNG output has exactly IHDR/IDAT/IEND chunks and no ancillary/source tags."""
    output = tmp_path / "result.png"
    media.frame_png(video, output, 0)
    with av.open(str(output)) as result:
        assert next(result.decode(video=0)).width == 640
    with pytest.raises(ValueError):
        media.frame_png(video, output, 600)
    with pytest.raises(ValueError, match="not found"):
        media.frame_png(video, output, 40)
    (tmp_path / "source.mp4").write_bytes(video.read_bytes())
    (tmp_path / "job.json").write_text(json.dumps({"action": "frame", "index": 0}))
    worker.execute(tmp_path)
    assert output.is_file()


def test_native_source_size_guard_before_read(tmp_path, monkeypatch):
    """Do not read an oversized source into Python memory before enforcing the limit."""
    source = tmp_path / "source.mp4"
    source.write_bytes(b"a" * 20)
    monkeypatch.setattr(media, "MAX_BYTES", 10)
    with pytest.raises(ValueError, match="bounded"):
        media.transcode(source, tmp_path / "out.mp4", [])


def test_workspace_capacity_enforced_before_decoder(client, imported, app):
    """Expired/active records count toward the twelve-clip disk budget until explicitly purged."""
    with app.state.store.connect(True) as db:
        for index in range(11):
            db.execute(
                "INSERT INTO clips SELECT ?,creator,title,purpose,source_digest,preview_digest,info,version,created,expires FROM clips WHERE id=?",
                (f"{index:032x}", imported["id"]),
            )
    assert client.post("/api/examples/flood", json={}).status_code == 409
