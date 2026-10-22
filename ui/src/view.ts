/** @file Jason Stys: pure presentation, mask validation and relative-position interpolation. Lines: docs/SOURCE_MAP.md. */
export interface Mask {
  first: number;
  last: number;
  x: number;
  y: number;
  width: number;
  height: number;
  reason: "face" | "plate" | "sensitive" | "other";
}
export interface Sample {
  ms: number;
  east_m: number;
  north_m: number;
  altitude_m: number;
}
/** Only these two fixed private media kinds may become a browser URL segment. */
export function mediaKind(input: string): "preview" | "redacted" {
  return input === "preview" ? "preview" : "redacted";
}
/** Validate draft intent before submission; server validation remains authoritative. */
export function validMask(mask: Mask, frames: number): boolean {
  return (
    [mask.x, mask.y, mask.width, mask.height, mask.first, mask.last].every(
      Number.isFinite,
    ) &&
    Number.isInteger(mask.first) &&
    Number.isInteger(mask.last) &&
    mask.first >= 0 &&
    mask.last >= mask.first &&
    mask.last < frames &&
    mask.x >= 0 &&
    mask.y >= 0 &&
    mask.width > 0 &&
    mask.height > 0 &&
    mask.x + mask.width <= 1 &&
    mask.y + mask.height <= 1
  );
}
/** Position is interpolated only inside supplied telemetry coverage, never extrapolated. */
export function positionAt(
  samples: Sample[],
  ms: number,
  offset: number,
): string {
  const time = ms - offset;
  if (
    samples.length === 0 ||
    time < samples[0].ms ||
    time > samples[samples.length - 1].ms
  )
    return "Position unknown";
  const next = samples.findIndex((point) => point.ms >= time);
  const right = samples[next];
  const left = samples[Math.max(0, next - 1)];
  if (right.ms - left.ms > 1000) return "Position unknown · telemetry gap";
  const fraction =
    right.ms === left.ms ? 0 : (time - left.ms) / (right.ms - left.ms);
  return `E ${(left.east_m + fraction * (right.east_m - left.east_m)).toFixed(1)} m · N ${(left.north_m + fraction * (right.north_m - left.north_m)).toFixed(1)} m · Alt ${(left.altitude_m + fraction * (right.altitude_m - left.altitude_m)).toFixed(1)} m (relative)`;
}
/** Approval belongs to one exact processed version; never infer approval from a previous revision. */
export function reviewLabel(version: number, decision?: string): string {
  if (version === 0) return "UNPROCESSED";
  return decision === "approve"
    ? `V${version} · APPROVED`
    : decision === "reject"
      ? `V${version} · REJECTED`
      : `V${version} · REVIEW REQUIRED`;
}
