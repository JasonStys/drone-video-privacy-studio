"""Jason Stys: rational per-frame containment, actual encoded pixels and private helper guards. Map: docs/SOURCE_MAP.md."""

import math
import random
from fractions import Fraction

import av
import pytest
from pydantic import ValidationError

from workbench import media, service
from workbench.models import MotionDraft, Plan
from workbench.motion import motion_masks


def anchor(frame, x=0.1, y=0.1, width=0.2, height=0.2, **changes):
    """Manual fictional rectangle on a decoded frame, not a detected identity."""
    return (
        dict(first=frame, last=frame, x=x, y=y, width=width, height=height, reason="sensitive")
        | changes
    )


def intent(**changes):
    """Forty-frame teaching clip with two marked anchors."""
    return dict(expected_version=0, start=anchor(0), end=anchor(39, x=0.6), segments=8) | changes


def test_rational_interpolation_contained_in_exact_partition_for_every_frame():
    """Independent Fraction interpolation, including reverse motion, scale change and edge anchors."""
    randomizer = random.Random(4107)  # noqa: S311 - deterministic geometry oracle, no secrets
    for _ in range(120):
        length = randomizer.randint(2, 60)
        anchors = []
        for frame in (0, length - 1):
            x, y = randomizer.randint(0, 75), randomizer.randint(0, 75)
            width, height = randomizer.randint(1, 100 - x), randomizer.randint(1, 100 - y)
            anchors.append(anchor(frame, x / 100, y / 100, width / 100, height / 100))
        draft = MotionDraft.model_validate(
            intent(start=anchors[0], end=anchors[1], segments=randomizer.randint(1, 32))
        )
        generated = motion_masks(draft, length)
        assert len(generated) == min(length, draft.segments)
        assert generated[0].first == 0 and generated[-1].last == length - 1
        for frame in range(length):
            active = [mask for mask in generated if mask.first <= frame <= mask.last]
            assert len(active) == 1
            mask = active[0]
            fraction = Fraction(frame, length - 1)
            interpolated = {
                key: Fraction(str(anchors[0][key])) * (1 - fraction)
                + Fraction(str(anchors[1][key])) * fraction
                for key in ("x", "y", "width", "height")
            }
            assert mask.x <= float(interpolated["x"]) + 1e-12
            assert mask.y <= float(interpolated["y"]) + 1e-12
            assert mask.x + mask.width + 1e-12 >= float(interpolated["x"] + interpolated["width"])
            assert mask.y + mask.height + 1e-12 >= float(interpolated["y"] + interpolated["height"])


@pytest.mark.parametrize(
    "changes",
    [
        {"start": anchor(0, last=1)},
        {"end": anchor(0)},
        {"end": anchor(39, reason="plate")},
        {"segments": 0},
        {"segments": 33},
        {"segments": True},
        {"start": anchor(0, x=0.9)},
        {"start": anchor(0, width=0)},
        {"start": anchor(0, x=float("nan"))},
        {"extra": "forbidden"},
    ],
)
def test_invalid_keyframe_intent_rejected(changes):
    """Do not silently clip invalid geometry, frame order or requested resource bounds."""
    with pytest.raises(ValidationError):
        MotionDraft.model_validate(intent(**changes))


@pytest.mark.parametrize("frames", [0, 39, 601])
def test_decoded_clip_bounds_are_authoritative(frames):
    with pytest.raises(ValueError, match="timeline"):
        motion_masks(MotionDraft.model_validate(intent()), frames)


def test_actual_transcode_and_redecode_contains_manual_motion_without_touching_other_frames(
    tmp_path,
):
    """Independent pixel oracle on white frames; only frames2..7 are meant to be masked."""
    from test_media import custom

    source, output = tmp_path / "white.mp4", tmp_path / "redacted.mp4"
    custom(source, frames=10)
    draft = MotionDraft.model_validate(
        intent(
            start=anchor(2, x=0.125, y=0.25, width=0.125, height=0.125),
            end=anchor(7, x=0.625, y=0.5, width=0.125, height=0.125),
            segments=3,
        )
    )
    masks = motion_masks(draft, 10)
    info = media.transcode(source, output, masks)
    media.verify(output, info, masks)
    with av.open(str(output)) as decoded:
        for index, frame in enumerate(decoded.decode(video=0)):
            pixels = frame.to_ndarray(format="rgb24")
            if 2 <= index <= 7:
                ratio = Fraction(index - 2, 5)
                x, y = Fraction(1, 8) + ratio / 2, Fraction(1, 4) + ratio / 4
                region = pixels[
                    math.ceil(y * 96) : math.floor((y + Fraction(1, 8)) * 96),
                    math.ceil(x * 160) : math.floor((x + Fraction(1, 8)) * 160),
                ]
                assert region.size and region.max() <= 24
                assert pixels[:3, :3].min() > 150
            else:
                assert pixels.min() > 150


def test_private_read_only_helper_and_real_processing(client, imported, login, app, monkeypatch):
    """Owner/admin only; no media/revision/event mutation until the ordinary process endpoint."""
    endpoint = f"/api/clips/{imported['id']}/motion-draft"
    before = app.state.store.history(imported["id"], {"name": "alice", "role": "operator"})
    body = intent()
    result = client.post(endpoint, json=body)
    assert result.status_code == 200, result.text
    assert len(result.json()["masks"]) == 8
    assert app.state.store.history(imported["id"], {"name": "alice", "role": "operator"}) == before
    assert client.post(endpoint, json={**body, "expected_version": 99}).status_code == 409
    assert client.post(endpoint, json={**body, "end": anchor(40)}).status_code == 422
    token = client.headers.pop("X-CSRF-Token")
    assert client.post(endpoint, json=body).status_code == 403
    client.headers["X-CSRF-Token"] = token
    login("bob")
    assert client.post(endpoint, json=body).status_code == 404
    login("reviewer")
    assert client.post(endpoint, json=body).status_code == 403
    login("admin")
    assert client.post(endpoint, json=body).status_code == 200
    login("alice")

    def concurrent(draft, frames):
        """Real verified processing advances the revision before helper completion."""
        result = motion_masks(draft, frames)
        service.process(
            app.state.store,
            imported["id"],
            {"name": "alice", "role": "operator"},
            Plan(
                expected_version=0,
                masks=result,
                note="Synthetic manual motion planning validation",
                telemetry=[],
                offset_ms=0,
            ),
        )
        return result

    monkeypatch.setattr("workbench.api.motion_masks", concurrent)
    assert client.post(endpoint, json=body).status_code == 409
    assert client.get(f"/api/clips/{imported['id']}").json()["version"] == 1
    assert client.get(f"/api/clips/{imported['id']}/media/export?version=1").status_code == 409
