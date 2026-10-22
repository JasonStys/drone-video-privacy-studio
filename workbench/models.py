"""Jason Stys: finite, bounded frame masks, telemetry and revision/review contracts.

Declarations, fields and local bindings: docs/SOURCE_MAP.md. Extras are rejected, never ignored.
"""

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

Unit = Annotated[float, Field(ge=0, le=1, allow_inf_nan=False)]
Frame = Annotated[int, Field(ge=0, le=599, strict=True)]


class StrictModel(BaseModel):
    """Reject unknown keys, non-finite values and implicit cross-type coercion."""

    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)


class Login(StrictModel):
    """Bound credentials before expensive password verification; no public registration."""

    username: str = Field(min_length=3, max_length=40)
    password: str = Field(min_length=1, max_length=128)


class Mask(StrictModel):
    """Normalized half-open rectangle, inclusive frame interval; eight-pixel margin is added."""

    first: Frame
    last: Frame
    x: Unit
    y: Unit
    width: Unit
    height: Unit
    reason: Literal["face", "plate", "sensitive", "other"]

    @model_validator(mode="after")
    def geometry(self):
        """Reject empty, inverted and out-of-frame rectangles rather than silently clipping intent."""
        if self.first > self.last or self.width <= 0 or self.height <= 0:
            raise ValueError("Empty or inverted mask")
        if self.x + self.width > 1 or self.y + self.height > 1:
            raise ValueError("Mask extends outside image")
        return self


class Sample(StrictModel):
    """Optional relative local coordinates, not live navigation or authoritative geolocation."""

    ms: int = Field(ge=0, le=20000)
    east_m: float = Field(ge=-10000, le=10000)
    north_m: float = Field(ge=-10000, le=10000)
    altitude_m: float = Field(ge=0, le=500)


class Plan(StrictModel):
    """Versioned masks and private notes; timeline uses decoded frame zero, never wall-clock time."""

    expected_version: int = Field(ge=0)
    masks: list[Mask] = Field(max_length=32)
    note: str = Field(max_length=500)
    telemetry: list[Sample] = Field(max_length=600)
    offset_ms: int = Field(ge=-5000, le=5000)

    @model_validator(mode="after")
    def time_order(self):
        """Require unique monotonically increasing telemetry timestamps."""
        if any(a.ms >= b.ms for a, b in zip(self.telemetry, self.telemetry[1:], strict=False)):
            raise ValueError("Telemetry timestamps must strictly increase")
        return self


class Review(StrictModel):
    """Independent human attestation, not proof of anonymity or lawful collection."""

    expected_version: int = Field(ge=1)
    decision: Literal["approve", "reject"]
    full_clip_checked: bool
    context_checked: bool
    note: str = Field(min_length=10, max_length=500)


def alignment(plan: Plan, frames: int, fps: int):
    """Report missing/offset/gappy telemetry; it is excluded from public exports regardless."""
    points = plan.telemetry
    if not points:
        return {"status": "absent", "warnings": ["No telemetry supplied; position unknown"]}
    start = points[0].ms + plan.offset_ms
    end = points[-1].ms + plan.offset_ms
    expected = (frames - 1) * 1000 / fps
    warnings = []
    if abs(start) > 250 or abs(end - expected) > 250:
        warnings.append("Telemetry endpoint drift exceeds 250 ms")
    if any(b.ms - a.ms > 1000 for a, b in zip(points, points[1:], strict=False)):
        warnings.append("Telemetry gap exceeds 1000 ms")
    return {"status": "warning" if warnings else "aligned", "warnings": warnings}
