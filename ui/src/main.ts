/** @file Jason Stys: authenticated private video workspace, stale-response protection and safe DOM rendering. Lines: docs/SOURCE_MAP.md. */
import "./style.css";
import {
  mediaKind,
  positionAt,
  reviewLabel,
  validMask,
  type Mask,
  type Sample,
} from "./view";
interface User {
  name: string;
  role: string;
  csrf: string;
}
interface Plan {
  masks: Mask[];
  note: string;
  telemetry: Sample[];
  offset_ms: number;
  expected_version: number;
}
interface Clip {
  id: string;
  title: string;
  version: number;
  expires: number;
  info: {
    frames: number;
    fps: number;
    width: number;
    height: number;
    duration_ms: number;
  };
  revision: {
    plan: Plan;
    review: { decision: string; actor: string; note: string } | null;
    alignment: { status: string; warnings: string[] };
  } | null;
}
let user: User | null = null;
let clip: Clip | null = null;
let masks: Mask[] = [];
let epoch = 0;
let busy = false;
let logoutPending = false;
let frameMode = false;
let videoGeneration = 0;
let frameLoading = false;
/** Fixed markup IDs only; user data never becomes HTML or an executable selector. */
function el<T extends HTMLElement = HTMLElement>(id: string): T {
  return document.getElementById(id) as T;
}
/** Read one form control's literal value. */
function value(id: string): string {
  return el<HTMLInputElement>(id).value;
}
/** Keep all private text rendering in textContent. */
function text(id: string, message: string): void {
  el(id).textContent = message;
}
/** Keep native-frame backpressure visible; never invite a second heavy job before its preview finishes. */
function buttons(): void {
  for (const button of document.querySelectorAll<HTMLButtonElement>("button"))
    button.disabled =
      logoutPending || (button.id !== "logout" && (busy || frameLoading));
}
/** Expose only explicit safe same-origin routes; discard responses after logout/account/selection changes. */
async function api<T>(path: string, body?: unknown, raw?: File): Promise<T> {
  const generation = epoch;
  const response = await fetch(path, {
    method: body !== undefined || raw ? "POST" : "GET",
    headers: {
      ...(body !== undefined || raw
        ? {
            "Content-Type": raw ? "video/mp4" : "application/json",
            "X-CSRF-Token": user?.csrf ?? "",
          }
        : {}),
    },
    ...(raw
      ? { body: raw }
      : body !== undefined
        ? { body: JSON.stringify(body) }
        : {}),
  });
  const result = await response.json();
  if (generation !== epoch) throw new Error("Workspace changed");
  if (response.status === 401 && path !== "/api/login") {
    reset();
    text("message", "Session expired or revoked; sign in again");
    throw new Error("Session expired");
  }
  if (!response.ok) throw new Error(result.detail ?? "Request failed");
  return result as T;
}
/** Serialize UI operations, report errors and ignore obsolete in-flight responses. */
async function task(action: () => Promise<void>): Promise<void> {
  if (busy || logoutPending) return;
  busy = true;
  const generation = epoch;
  text("message", "Working locally…");
  buttons();
  try {
    await action();
    if (generation === epoch)
      text("message", "Ready · private local workspace");
  } catch (error) {
    if (generation === epoch) text("message", (error as Error).message);
  } finally {
    busy = false;
    buttons();
  }
}
/** Clear private media on sign-out, including pending browser fetches and controls. */
function reset(): void {
  epoch++;
  clip = null;
  masks = [];
  user = null;
  videoGeneration++;
  frameMode = false;
  frameLoading = false;
  const video = el<HTMLVideoElement>("video");
  video.pause();
  video.removeAttribute("src");
  video.load();
  el<HTMLImageElement>("review-image").removeAttribute("src");
  el("review-image").hidden = true;
  text("playback-status", "");
  el("clip-list").replaceChildren();
  el("mask-overlay").replaceChildren();
  el("masks").replaceChildren();
  el("metrics").replaceChildren();
  text("badge", "");
  text("position", "");
  text("frame-label", "");
  text("history-output", "");
  text("clip-title", "");
  text("review-state", "");
  text("alignment", "");
  text("identity", "");
  for (const id of [
    "note",
    "telemetry",
    "review-note",
    "title",
    "purpose",
    "password",
    "file",
  ])
    el<HTMLInputElement>(id).value = "";
  el("workspace").hidden = true;
  el("clip-panel").hidden = true;
  el("exports").hidden = true;
  el("login-panel").hidden = false;
  for (const id of ["export-video", "export-manifest"])
    el<HTMLAnchorElement>(id).removeAttribute("href");
}
/** Reload only authorized active clips; buttons bind opaque server IDs rather than DOM HTML. */
async function library(): Promise<void> {
  const rows = await api<Clip[]>("/api/clips");
  const list = el("clip-list");
  list.replaceChildren();
  for (const row of rows) {
    const button = document.createElement("button");
    button.className = "clip-item";
    button.textContent = `${row.title} · v${row.version}`;
    button.onclick = () => {
      if (busy || logoutPending || frameLoading) return;
      epoch++;
      void task(async () => {
        show(await api<Clip>(`/api/clips/${row.id}`));
      });
    };
    list.append(button);
  }
}
/** Enter a role-aware view; authority is always checked again by the backend. */
async function signedIn(next: User): Promise<void> {
  user = next;
  el("login-panel").hidden = true;
  el("workspace").hidden = false;
  text("identity", `${next.name} · ${next.role}`);
  el("ingest").hidden = next.role === "reviewer";
  await library();
}
/** Update private clip selection and reset stale approval links/draft state. */
function show(next: Clip): void {
  clip = next;
  masks = structuredClone(next.revision?.plan.masks ?? []);
  el("empty").hidden = true;
  el("clip-panel").hidden = false;
  text("clip-title", next.title);
  el<HTMLVideoElement>("video").style.aspectRatio =
    `${next.info.width} / ${next.info.height}`;
  text("badge", reviewLabel(next.version, next.revision?.review?.decision));
  const metrics = el("metrics");
  metrics.replaceChildren();
  for (const [amount, label] of [
    [`${next.info.frames}`, "DECODED FRAMES"],
    [`${next.info.fps} fps`, "CONSTANT RATE"],
    [`${next.info.width} × ${next.info.height}`, "FRAME SIZE"],
    [new Date(next.expires * 1000).toLocaleDateString(), "RETENTION UNTIL"],
  ]) {
    const div = document.createElement("div");
    div.className = "metric";
    const strong = document.createElement("strong");
    strong.textContent = amount;
    const small = document.createElement("span");
    small.textContent = label;
    div.append(strong, small);
    metrics.append(div);
  }
  const kind = el<HTMLSelectElement>("media-kind");
  kind.options[1].disabled = !next.revision;
  kind.value = next.revision ? "redacted" : "preview";
  const frame = el<HTMLInputElement>("frame");
  frame.max = String(next.info.frames - 1);
  frame.value = "0";
  el<HTMLInputElement>("first").max = frame.max;
  el<HTMLInputElement>("last").max = frame.max;
  el<HTMLInputElement>("last").value = frame.max;
  el<HTMLTextAreaElement>("note").value = next.revision?.plan.note ?? "";
  el<HTMLTextAreaElement>("telemetry").value = JSON.stringify(
    next.revision?.plan.telemetry ?? [],
    null,
    2,
  );
  el<HTMLInputElement>("offset").value = String(
    next.revision?.plan.offset_ms ?? 0,
  );
  text("history-output", "");
  el("editor").hidden = user?.role === "reviewer";
  el("plan-controls").hidden = user?.role === "reviewer";
  el("review-form").hidden =
    user?.role !== "reviewer" || !next.revision || !!next.revision.review;
  el<HTMLInputElement>("full-check").checked = false;
  el<HTMLInputElement>("context-check").checked = false;
  el<HTMLTextAreaElement>("review-note").value = "";
  text(
    "review-state",
    next.revision?.review
      ? `${next.revision.review.decision} by ${next.revision.review.actor}: ${next.revision.review.note}`
      : "Independent review required. Inspect the complete processed video, not only the draft outlines.",
  );
  text(
    "alignment",
    next.revision
      ? `Telemetry: ${next.revision.alignment.status}. ${next.revision.alignment.warnings.join("; ")}`
      : "Telemetry is optional and never included in exports.",
  );
  el("exports").hidden = next.revision?.review?.decision !== "approve";
  el<HTMLAnchorElement>("export-video").href =
    `/api/clips/${next.id}/media/export?version=${next.version}`;
  el<HTMLAnchorElement>("export-manifest").href =
    `/api/clips/${next.id}/manifest`;
  loadVideo();
  drawMasks();
}
/** Load the authorized current preview/revision; no blob URL or public media directory exists. */
function loadVideo(): void {
  if (!clip) return;
  const generation = ++videoGeneration;
  frameMode = false;
  frameLoading = false;
  const image = el<HTMLImageElement>("review-image");
  image.onload = null;
  image.onerror = null;
  image.removeAttribute("src");
  el("review-image").hidden = true;
  el("load-frame").hidden = true;
  el("video").hidden = false;
  text(
    "playback-status",
    "Loading video; frame-by-frame inspection is also available",
  );
  const video = el<HTMLVideoElement>("video");
  video.pause();
  video.src = `/api/clips/${clip.id}/media/${mediaKind(value("media-kind"))}?version=${clip.version}`;
  video.load();
  window.setTimeout(() => {
    if (
      clip &&
      !frameMode &&
      generation === videoGeneration &&
      video.readyState < 2
    )
      useFrames();
  }, 3000);
  drawMasks();
}
/** Codec-independent fallback uses verified server-decoded PNGs, not a substitute test fixture. */
function useFrames(): void {
  if (!clip || frameMode) return;
  frameMode = true;
  el<HTMLVideoElement>("video").pause();
  el("video").hidden = true;
  el("review-image").hidden = false;
  el("load-frame").hidden = false;
  text(
    "playback-status",
    "Frame-by-frame mode · move the slider, then load the selected frame",
  );
  loadFrame();
}
/** Each frame is independently authenticated, version-bound and decoded; no image cache. */
function loadFrame(): void {
  if (!clip) return;
  const index = Number(value("frame"));
  if (!Number.isInteger(index) || index < 0 || index >= clip.info.frames) {
    text("message", "Choose a valid frame index");
    return;
  }
  const generation = videoGeneration;
  const image = el<HTMLImageElement>("review-image");
  frameLoading = true;
  buttons();
  image.onload = () => {
    if (generation === videoGeneration) {
      frameLoading = false;
      buttons();
    }
  };
  image.onerror = () => {
    if (clip && generation === videoGeneration) {
      frameLoading = false;
      buttons();
      text(
        "message",
        "Frame unavailable: refresh for expiry/version changes, or wait for the active job and load again",
      );
    }
  };
  image.src = `/api/clips/${clip.id}/frame/${mediaKind(value("media-kind"))}?version=${clip.version}&index=${index}`;
}
/** Draw review-only outlines for the unredacted preview, never claim them as processed redaction. */
function drawMasks(): void {
  const overlay = el<HTMLElement>("mask-overlay");
  overlay.replaceChildren();
  const list = el("masks");
  list.replaceChildren();
  if (!clip) return;
  overlay.setAttribute("viewBox", `0 0 ${clip.info.width} ${clip.info.height}`);
  overlay.setAttribute("preserveAspectRatio", "none");
  for (const mask of masks) {
    const item = document.createElement("li");
    item.textContent = `${mask.reason} · frames ${mask.first}–${mask.last} · [${mask.x}, ${mask.y}, ${mask.width}, ${mask.height}]`;
    list.append(item);
    if (
      value("media-kind") === "preview" &&
      mask.first <= Number(value("frame")) &&
      mask.last >= Number(value("frame"))
    ) {
      const rect = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "rect",
      );
      for (const [key, amount] of Object.entries({
        x: mask.x * clip.info.width,
        y: mask.y * clip.info.height,
        width: mask.width * clip.info.width,
        height: mask.height * clip.info.height,
      }))
        rect.setAttribute(key, String(amount));
      rect.setAttribute("fill", "none");
      rect.setAttribute("stroke", "#ffce75");
      rect.setAttribute("stroke-width", "3");
      overlay.append(rect);
    }
  }
  const frame = Number(value("frame"));
  text(
    "frame-label",
    `Frame ${frame} / ${clip.info.frames - 1} · ${(frame / clip.info.fps).toFixed(2)} s`,
  );
  text(
    "position",
    positionAt(
      clip.revision?.plan.telemetry ?? [],
      (frame * 1000) / clip.info.fps,
      clip.revision?.plan.offset_ms ?? 0,
    ),
  );
}
el<HTMLFormElement>("login-form").onsubmit = (event) => {
  event.preventDefault();
  void task(async () => {
    const next = await api<User>("/api/login", {
      username: value("username"),
      password: value("password"),
    });
    el<HTMLInputElement>("password").value = "";
    await signedIn(next);
  });
};
el("logout").onclick = () => {
  const csrf = user?.csrf ?? "";
  logoutPending = true;
  reset();
  buttons();
  text("message", "Signing out…");
  void fetch("/api/logout", {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-CSRF-Token": csrf },
    body: "{}",
  })
    .then((response) =>
      text(
        "message",
        response.ok
          ? "Signed out; private view cleared"
          : "View cleared; server sign-out failed. Close this browser session.",
      ),
    )
    .catch(() =>
      text(
        "message",
        "View cleared; server unavailable. Close this browser session.",
      ),
    )
    .finally(() => {
      logoutPending = false;
      buttons();
    });
};
el("refresh").onclick = () => void task(library);
el("example").onclick = () =>
  void task(async () => {
    show(await api<Clip>(`/api/examples/${value("scenario")}`, {}));
    await library();
  });
el<HTMLFormElement>("import-form").onsubmit = (event) => {
  event.preventDefault();
  void task(async () => {
    const file = el<HTMLInputElement>("file").files?.[0];
    if (!file || file.size > 20 * 1024 * 1024)
      throw new Error("Choose an MP4 no larger than 20 MiB");
    const params = new URLSearchParams({
      title: value("title"),
      purpose: value("purpose"),
      retention: value("retention"),
    });
    show(await api<Clip>(`/api/clips/import?${params}`, undefined, file));
    await library();
    el<HTMLInputElement>("file").value = "";
  });
};
el<HTMLFormElement>("mask-form").onsubmit = (event) => {
  event.preventDefault();
  if (!clip) return;
  const mask: Mask = {
    first: Number(value("first")),
    last: Number(value("last")),
    x: Number(value("x")),
    y: Number(value("y")),
    width: Number(value("width")),
    height: Number(value("height")),
    reason: value("reason") as Mask["reason"],
  };
  if (!validMask(mask, clip.info.frames) || masks.length >= 32) {
    text("message", "Check mask bounds, frame interval and 32-mask limit");
    return;
  }
  masks.push(mask);
  drawMasks();
  text("message", "Draft updated; process a new revision to apply these masks");
};
el("clear-masks").onclick = () => {
  masks = [];
  drawMasks();
  text(
    "message",
    "Draft masks cleared; saved revision unchanged until processing",
  );
};
el("sample-telemetry").onclick = () => {
  if (!clip) return;
  el<HTMLTextAreaElement>("telemetry").value = JSON.stringify(
    Array.from({ length: clip.info.frames }, (_, index) => ({
      ms: Math.round((index * 1000) / clip!.info.fps),
      east_m: index * 0.5,
      north_m: index * 0.2,
      altitude_m: 45,
    })),
    null,
    2,
  );
  el<HTMLInputElement>("offset").value = "0";
  text(
    "message",
    "Synthetic relative telemetry added to draft—not real navigation data",
  );
};
el("process").onclick = () =>
  void task(async () => {
    if (!clip) return;
    const body: Plan = {
      expected_version: clip.version,
      masks,
      note: value("note"),
      telemetry: JSON.parse(value("telemetry")),
      offset_ms: Number(value("offset")),
    };
    show(await api<Clip>(`/api/clips/${clip.id}/process`, body));
    await library();
  });
el<HTMLFormElement>("review-form").onsubmit = (event) => {
  event.preventDefault();
  void task(async () => {
    if (!clip) return;
    show(
      await api<Clip>(`/api/clips/${clip.id}/review`, {
        expected_version: clip.version,
        decision: value("decision"),
        full_clip_checked: el<HTMLInputElement>("full-check").checked,
        context_checked: el<HTMLInputElement>("context-check").checked,
        note: value("review-note"),
      }),
    );
  });
};
el("history").onclick = () =>
  void task(async () => {
    if (clip)
      text(
        "history-output",
        JSON.stringify(await api(`/api/clips/${clip.id}/history`), null, 2),
      );
  });
el("media-kind").onchange = loadVideo;
el<HTMLVideoElement>("video").onloadeddata = () => {
  if (clip && !frameMode)
    text(
      "playback-status",
      "Video playback available · masks are applied to actual server-decoded frames",
    );
};
el("frame-mode").onclick = useFrames;
el("load-frame").onclick = loadFrame;
el<HTMLVideoElement>("video").onerror = () => {
  if (clip && el<HTMLVideoElement>("video").src.includes(clip.id)) useFrames();
};
el<HTMLInputElement>("frame").oninput = () => {
  if (!clip) return;
  const video = el<HTMLVideoElement>("video");
  video.pause();
  if (!frameMode)
    video.currentTime = (Number(value("frame")) + 0.5) / clip.info.fps;
  drawMasks();
};
el<HTMLVideoElement>("video").ontimeupdate = () => {
  if (clip && !frameMode) {
    el<HTMLInputElement>("frame").value = String(
      Math.min(
        clip.info.frames - 1,
        Math.floor(el<HTMLVideoElement>("video").currentTime * clip.info.fps),
      ),
    );
    drawMasks();
  }
};
void task(async () => {
  try {
    await signedIn(await api<User>("/api/me"));
  } catch {
    reset();
    text("message", "Sign in with your locally provisioned account");
  }
});
