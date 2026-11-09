"""Jason Stys: conservative manual keyframe mask envelopes. Bindings: docs/SOURCE_MAP.md.

No detector, recognition, identity inference or real-world tracking. The existing
static-mask encoder/redecode and independent human-review gates remain authoritative.
"""

from workbench.models import Mask, MotionDraft


def motion_masks(draft: MotionDraft, frames: int) -> list[Mask]:
    """Partition inclusive frames; linear rectangle edge extrema occur at each chunk's endpoints."""
    if not 1 <= frames <= 600 or draft.end.last >= frames:
        raise ValueError("Keyframe outside decoded clip timeline")
    start, end = draft.start, draft.end
    length = end.first - start.first + 1
    count = min(length, draft.segments)

    def edges(frame):
        """Interpolate all four normalized edges only inside the two explicitly marked frames."""
        fraction = (frame - start.first) / (end.first - start.first)
        return [
            a + fraction * (b - a)
            for a, b in zip(
                (start.x, start.y, start.x + start.width, start.y + start.height),
                (end.x, end.y, end.x + end.width, end.y + end.height),
                strict=True,
            )
        ]

    masks = []
    for index in range(count):
        first = start.first + index * length // count
        last = start.first + (index + 1) * length // count - 1
        left, right = edges(first), edges(last)
        x, y = max(0.0, min(left[0], right[0])), max(0.0, min(left[1], right[1]))
        width = min(1.0 - x, max(left[2], right[2]) - x)
        height = min(1.0 - y, max(left[3], right[3]) - y)
        masks.append(
            Mask(first=first, last=last, x=x, y=y, width=width, height=height, reason=start.reason)
        )
    return masks
