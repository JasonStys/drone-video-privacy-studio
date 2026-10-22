/** @file Jason Stys: independent draft-geometry, timing and exact-version presentation tests. Lines: docs/SOURCE_MAP.md. */
import { describe, expect, it } from "vitest";
import {
  mediaKind,
  positionAt,
  reviewLabel,
  validMask,
  type Mask,
} from "./view";
it("constrains media URL segments to a fixed union, including hostile DOM values", () => {
  expect(mediaKind("preview")).toBe("preview");
  expect(mediaKind("redacted")).toBe("redacted");
  expect(mediaKind('x\" onerror=alert(1)')).toBe("redacted");
});
const mask: Mask = {
  first: 0,
  last: 39,
  x: 0.1,
  y: 0.1,
  width: 0.2,
  height: 0.2,
  reason: "face",
};
describe("frame-safe masks", () => {
  it("accepts full image and inclusive first/last frame", () => {
    expect(validMask(mask, 40)).toBe(true);
    expect(validMask({ ...mask, x: 0, y: 0, width: 1, height: 1 }, 40)).toBe(
      true,
    );
  });
  it("rejects nonfinite, fractional, inverted, empty and out of bounds", () => {
    for (const change of [
      { x: NaN },
      { x: Infinity },
      { first: 0.1 },
      { last: 1.2 },
      { first: -1 },
      { first: 30, last: 20 },
      { last: 40 },
      { x: -0.1 },
      { y: -0.1 },
      { width: 0 },
      { height: 0 },
      { x: 0.9 },
      { y: 0.9 },
    ])
      expect(validMask({ ...mask, ...change }, 40)).toBe(false);
  });
});
describe("relative telemetry, no extrapolation", () => {
  const points = [
    { ms: 0, east_m: 0, north_m: 10, altitude_m: 20 },
    { ms: 1000, east_m: 10, north_m: 20, altitude_m: 40 },
  ];
  it("reports absent/outside timestamps as unknown", () => {
    expect(positionAt([], 0, 0)).toBe("Position unknown");
    expect(positionAt(points, -1, 0)).toBe("Position unknown");
    expect(positionAt(points, 1001, 0)).toBe("Position unknown");
  });
  it("interpolates, applies offset and keeps exact endpoints", () => {
    expect(positionAt(points, 600, 100)).toContain(
      "E 5.0 m · N 15.0 m · Alt 30.0 m",
    );
    expect(positionAt(points, 0, 0)).toContain("E 0.0 m");
    expect(positionAt(points, 1000, 0)).toContain("E 10.0 m");
  });
  it("does not invent coordinates through a gap", () => {
    expect(
      positionAt([points[0], { ...points[1], ms: 2000 }], 500, 0),
    ).toContain("telemetry gap");
  });
});
it("never labels an unprocessed or unreviewed version approved", () => {
  expect(reviewLabel(0, "approve")).toBe("UNPROCESSED");
  expect(reviewLabel(1)).toBe("V1 · REVIEW REQUIRED");
  expect(reviewLabel(2, "reject")).toBe("V2 · REJECTED");
  expect(reviewLabel(3, "approve")).toBe("V3 · APPROVED");
});
