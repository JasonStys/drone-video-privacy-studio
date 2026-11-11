/** Jason Stys: actual extracted video application, file import, moving-mask processing and independent controlled export. Lines: docs/SOURCE_MAP.md. */
import assert from "node:assert/strict";
import fs from "node:fs/promises";
import path from "node:path";
import { chromium, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

const [base, output] = process.argv.slice(2);
assert(
  base &&
    output &&
    process.env.NATIVE_TEST_PASSWORD &&
    process.env.NATIVE_TEST_VIDEO_PATH,
);
const origin = new URL(base).origin;
const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 1000 },
  acceptDownloads: true,
  reducedMotion: "reduce",
});
const page = await context.newPage();
const errors = [],
  external = [],
  exchanges = [];
page.on("pageerror", (error) => errors.push(error.message));
page.on("request", (request) => {
  if (request.url().startsWith(origin))
    exchanges.push({
      event: "request",
      method: request.method(),
      path: new URL(request.url()).pathname,
      time: performance.now(),
    });
  if (
    /^https?:/.test(request.url()) &&
    new URL(request.url()).origin !== origin
  )
    external.push(request.url());
});
page.on("response", (response) => {
  if (response.url().startsWith(origin))
    exchanges.push({
      event: "response",
      method: response.request().method(),
      path: new URL(response.url()).pathname,
      status: response.status(),
      time: performance.now(),
    });
});

/** Actual account authentication waits for session startup rather than racing the initial reset. */
async function login(role) {
  await page.goto(base);
  await page.getByLabel("Username", { exact: true }).fill(role);
  await page
    .getByLabel("Password", { exact: true })
    .fill(process.env.NATIVE_TEST_PASSWORD);
  await page.getByRole("button", { name: "Sign in", exact: true }).click();
  await expect(page.locator("#identity")).toContainText(role);
  await expect(page.locator("#message")).toContainText("Ready");
}

/** Complete ordinary server revocation before changing roles or navigating. */
async function logout() {
  const pending = page.waitForResponse(
    (response) =>
      new URL(response.url()).pathname === "/api/logout" &&
      response.request().method() === "POST",
  );
  await page.getByRole("button", { name: "Sign out", exact: true }).click();
  assert.equal((await pending).status(), 200);
  await expect(page.locator("#message")).toContainText("Signed out");
}

/** Require genuine decoded media pixels, using the supported server PNG fallback when selected. */
async function loaded() {
  await expect
    .poll(
      () =>
        page.evaluate(() => {
          const video = document.getElementById("video"),
            image = document.getElementById("review-image");
          return (
            (!video.hidden && video.readyState >= 2) ||
            (!image.hidden && image.complete && image.naturalWidth === 640)
          );
        }),
      { timeout: 15000 },
    )
    .toBe(true);
}

/** Retain a real browser download under a fixed owned QA filename, never a caller-selected export path. */
async function download(link, filename) {
  const pending = page.waitForEvent("download");
  await link.click();
  const item = await pending;
  await item.saveAs(path.join(output, filename));
}

try {
  await login("operator");
  await expect(page.locator("#application-version")).toContainText("v0.2.1");
  assert.deepEqual(
    await (await page.request.get(new URL("api/clips", base).href)).json(),
    [],
  );
  await page
    .getByLabel("Clip title", { exact: true })
    .fill("Fictional coastal privacy review");
  await page
    .getByLabel("Authorized purpose", { exact: true })
    .fill(
      "Synthetic controlled privacy workflow; no real people or locations.",
    );
  await page
    .getByLabel("MP4 file", { exact: true })
    .setInputFiles(process.env.NATIVE_TEST_VIDEO_PATH);
  const importResponse = page.waitForResponse(
    (response) =>
      new URL(response.url()).pathname === "/api/clips/import" &&
      response.request().method() === "POST",
  );
  await page
    .getByRole("button", { name: "Import for private review", exact: true })
    .click();
  assert.equal((await importResponse).status(), 200);
  await expect(page.locator("#badge")).toHaveText("UNPROCESSED");
  await loaded();
  const clips = await (
    await page.request.get(new URL("api/clips", base).href)
  ).json();
  assert.equal(clips.length, 1);
  const id = clips[0].id;
  assert.equal(
    (
      await page.request.get(new URL(`api/clips/${id}/original`, base).href)
    ).status(),
    404,
  );
  await page.getByLabel("First frame", { exact: true }).fill("0");
  await page.getByLabel("Last frame", { exact: true }).fill("39");
  for (const [field, value] of [
    ["X", "0.06"],
    ["Y", "0.15"],
    ["Width", "0.18"],
    ["Height", "0.18"],
    ["Last keyframe X", "0.18"],
    ["Last keyframe Y", "0.15"],
    ["Last keyframe width", "0.18"],
    ["Last keyframe height", "0.18"],
    ["Envelope segments (1–32)", "8"],
  ])
    await page.getByLabel(field, { exact: true }).fill(value);
  await page
    .getByRole("button", { name: "Add manual motion envelopes", exact: true })
    .click();
  await expect(page.locator("#masks li")).toHaveCount(8);
  await expect(page.locator("#badge")).toHaveText("UNPROCESSED");
  for (const [field, value] of [
    ["X", "0.62"],
    ["Y", "0.67"],
    ["Width", "0.18"],
    ["Height", "0.13"],
  ])
    await page.getByLabel(field, { exact: true }).fill(value);
  await page
    .getByRole("combobox", { name: "Reason", exact: true })
    .selectOption("plate");
  await page
    .getByRole("button", { name: "Add mask to draft", exact: true })
    .click();
  await expect(page.locator("#masks li")).toHaveCount(9);
  await page
    .getByLabel("Private review notes", { exact: true })
    .fill(
      "Inspect every synthetic frame; requested masks are not anonymity certification.",
    );
  const processResponse = page.waitForResponse(
    (response) =>
      new URL(response.url()).pathname === `/api/clips/${id}/process` &&
      response.request().method() === "POST",
  );
  await page
    .getByRole("button", { name: "Process new revision", exact: true })
    .click();
  assert.equal((await processResponse).status(), 200);
  await expect(page.locator("#badge")).toHaveText("V1 \u00b7 REVIEW REQUIRED");
  await loaded();
  await expect(page.locator("#exports")).toBeHidden();
  const premature = await page.request.get(
    new URL(`api/clips/${id}/media/export?version=1`, base).href,
  );
  assert.equal(premature.status(), 409);
  const frameResponse = page.waitForResponse(
    (response) =>
      new URL(response.url()).pathname === `/api/clips/${id}/frame/redacted`,
  );
  await page
    .getByRole("button", { name: "Use frame-by-frame review", exact: true })
    .click();
  assert.equal((await frameResponse).status(), 200);
  await expect(page.locator("#review-image")).toBeVisible();
  await loaded();
  await page.locator(".player-panel").screenshot({
    path: path.join(output, "01-processed-moving-mask-frame.png"),
  });
  await logout();
  await login("admin");
  await expect(page.locator(".clip-item")).toHaveCount(1);
  await page.locator(".clip-item").click();
  await expect(page.locator("#review-form")).toBeHidden();
  await logout();
  await login("reviewer");
  await page.locator(".clip-item").click();
  await expect(page.locator("#editor")).toBeHidden();
  await page
    .getByLabel("I checked the full processed clip", { exact: false })
    .check();
  await page.getByLabel("I checked context", { exact: false }).check();
  await page
    .getByLabel("Independent review note", { exact: true })
    .fill(
      "Full fictional clip and context reviewed; no guarantee of anonymity.",
    );
  await page
    .getByRole("button", { name: "Record independent review", exact: true })
    .click();
  await expect(page.locator("#badge")).toHaveText("V1 \u00b7 APPROVED");
  await download(
    page.getByRole("link", { name: "Download reviewed MP4", exact: true }),
    "downloaded-reviewed-video.mp4",
  );
  await download(
    page.getByRole("link", { name: "Download minimal receipt", exact: true }),
    "downloaded-receipt.json",
  );
  const receipt = JSON.parse(
    await fs.readFile(path.join(output, "downloaded-receipt.json"), "utf8"),
  );
  assert.equal(receipt.anonymity_guaranteed, false);
  assert.equal(receipt.audio_included, false);
  assert.equal(receipt.telemetry_included, false);
  assert.equal(receipt.video.frames, 40);
  assert.equal(receipt.video.fps, 10);
  assert(
    !JSON.stringify(receipt).includes("Fictional coastal") &&
      !JSON.stringify(receipt).includes("source_digest") &&
      !JSON.stringify(receipt).includes("Private review"),
  );
  await page
    .locator("#review-form")
    .locator("..")
    .screenshot({
      path: path.join(output, "02-independent-reviewed-export.png"),
    });
  await page.setViewportSize({ width: 390, height: 844 });
  assert.equal(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth,
    ),
    true,
  );
  assert.deepEqual(
    (
      await new AxeBuilder({ page })
        .withTags(["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"])
        .analyze()
    ).violations,
    [],
  );
  const cookies = await context.cookies();
  assert.equal(cookies.length, 1);
  assert.equal(cookies[0].name, process.env.NATIVE_TEST_COOKIE_NAME);
  assert.equal(cookies[0].httpOnly, true);
  assert.equal(cookies[0].sameSite, "Strict");
  assert.deepEqual(
    await page.evaluate(() => [localStorage.length, sessionStorage.length]),
    [0, 0],
  );
  assert.deepEqual(external, []);
  assert.deepEqual(errors, []);
  await fs.writeFile(
    path.join(output, "feature.json"),
    JSON.stringify(
      {
        passed: true,
        actual_roles: ["operator", "admin", "reviewer"],
        arbitrary_supported_mp4_import: true,
        actual_frames: 40,
        manual_motion_envelopes: 8,
        static_plate_masks: 1,
        review_required_before_export: true,
        independent_reviewer: "reviewer",
        actual_video_and_minimal_receipt_downloaded: true,
        anonymity_guaranteed: false,
        outside_requests: 0,
        mobile_width: 390,
      },
      null,
      2,
    ) + "\n",
  );
} finally {
  await fs.writeFile(
    path.join(output, "browser-exchanges.json"),
    JSON.stringify(
      {
        exchanges,
        errors,
        message: await page
          .locator("#message")
          .textContent()
          .catch(() => "Page closed"),
      },
      null,
      2,
    ),
  );
  await context.close();
  await browser.close();
}
