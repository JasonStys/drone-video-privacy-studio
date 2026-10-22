"""Jason Stys: geometry, strict typing and synchronization edge cases; lines: docs/SOURCE_MAP.md."""

import pytest
from pydantic import ValidationError

from workbench.models import Mask, Plan, alignment


@pytest.mark.parametrize(
    "changes",
    [
        {"width": 0},
        {"height": 0},
        {"first": 2, "last": 1},
        {"x": 0.9, "width": 0.2},
        {"y": 0.9, "height": 0.2},
        {"x": float("nan")},
        {"first": True},
        {"last": 600},
        {"x": "0.1"},
        {"extra": "unknown"},
    ],
)
def test_invalid_masks(changes):
    """Invalid intent is rejected, not coerced or truncated into a different privacy plan."""
    with pytest.raises(ValidationError):
        Mask.model_validate(
            {
                "first": 0,
                "last": 39,
                "x": 0.1,
                "y": 0.1,
                "width": 0.2,
                "height": 0.2,
                "reason": "face",
                **changes,
            }
        )


def test_telemetry_and_frame_tolerance(plan):
    """Absent, aligned, gapped and drifted coverage are visibly different states."""
    parsed = Plan.model_validate(plan)
    assert alignment(parsed, 40, 10)["status"] == "absent"
    plan["telemetry"] = [
        {"ms": ms, "east_m": 0.0, "north_m": 0.0, "altitude_m": 10.0}
        for ms in (0, 1000, 2000, 3000, 3900)
    ]
    assert alignment(Plan.model_validate(plan), 40, 10)["status"] == "aligned"
    plan["telemetry"].pop(1)
    assert "gap" in alignment(Plan.model_validate(plan), 40, 10)["warnings"][0]
    plan["offset_ms"] = 500
    assert len(alignment(Plan.model_validate(plan), 40, 10)["warnings"]) == 2
    plan["telemetry"].reverse()
    with pytest.raises(ValidationError):
        Plan.model_validate(plan)


def test_mask_budget_and_duplicate_timestamp(plan):
    """Bound work and reject ambiguous telemetry at one timestamp."""
    plan["masks"] = plan["masks"] * 17
    with pytest.raises(ValidationError):
        Plan.model_validate(plan)
    plan["masks"] = []
    point = {"ms": 0, "east_m": 0.0, "north_m": 0.0, "altitude_m": 10.0}
    plan["telemetry"] = [point, point]
    with pytest.raises(ValidationError):
        Plan.model_validate(plan)
