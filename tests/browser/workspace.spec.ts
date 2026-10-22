/** @file Jason Stys: real server/media browser workflows, downloads, accessibility and logout race regressions. Lines: docs/SOURCE_MAP.md. */
import { test, expect, type Page } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";
import fs from "node:fs";
import path from "node:path";
const directory = process.env.VIDEO_TEST_DIRECTORY!;
/** Read only random disposable sandbox credentials; never print them or operate real user accounts. */
async function signIn(page: Page, role = "operator"): Promise<void> {
  const account = JSON.parse(
    fs.readFileSync(path.join(directory, "credentials.json"), "utf8"),
  )[role];
  await page.getByLabel("Username", { exact: true }).fill(account.username);
  await page.getByLabel("Password", { exact: true }).fill(account.password);
  await page.getByRole("button", { name: "Sign in", exact: true }).click();
  await expect(page.locator("#identity")).toContainText(account.username);
  await expect(page.locator("#message")).toContainText("Ready");
}
/** Wait for actual H.264 or actual server-decoded PNG, not a rendered tag or mocked result. */
async function loaded(page: Page): Promise<void> {
  await expect
    .poll(
      () =>
        page.evaluate(() => {
          const video = document.getElementById("video") as HTMLVideoElement;
          const image = document.getElementById(
            "review-image",
          ) as HTMLImageElement;
          return (
            (!video.hidden && video.readyState >= 2) ||
            (!image.hidden && image.complete && image.naturalWidth > 0)
          );
        }),
      { timeout: 15000 },
    )
    .toBe(true);
}
test("solid-mask processing, real playback, independent review and controlled downloads", async ({
  page,
}) => {
  await page.goto("/");
  await signIn(page);
  await page.getByRole("button", { name: "Create synthetic clip" }).click();
  await expect(page.locator("#badge")).toHaveText("UNPROCESSED");
  await loaded(page);
  await page.getByRole("button", { name: "Add mask to draft" }).click();
  await page.getByLabel("X", { exact: true }).fill("0.62");
  await page.getByLabel("Y", { exact: true }).fill("0.67");
  await page.getByLabel("Width", { exact: true }).fill("0.18");
  await page.getByLabel("Height", { exact: true }).fill("0.13");
  await page
    .getByRole("combobox", { name: "Reason", exact: true })
    .selectOption("plate");
  await page.getByRole("button", { name: "Add mask to draft" }).click();
  await expect(page.locator("#masks li")).toHaveCount(2);
  await page
    .getByLabel("Private review notes")
    .fill(
      "Check all generated motion and mock plate; contextual review remains necessary.",
    );
  await page
    .getByText("Telemetry and synchronization", { exact: true })
    .click();
  await page
    .getByRole("button", { name: "Use synthetic aligned telemetry" })
    .click();
  await page.getByRole("button", { name: "Process new revision" }).click();
  await expect(page.locator("#badge")).toHaveText("V1 · REVIEW REQUIRED");
  await loaded(page);
  const black = await page.locator("#video").evaluate((node) => {
    const video = (node as HTMLVideoElement).hidden
      ? (document.getElementById("review-image") as HTMLImageElement)
      : (node as HTMLVideoElement);
    const canvas = document.createElement("canvas");
    canvas.width = 640;
    canvas.height = 360;
    const context = canvas.getContext("2d")!;
    context.drawImage(video, 0, 0, 640, 360);
    return [...context.getImageData(75, 80, 1, 1).data].slice(0, 3);
  });
  expect(Math.max(...black)).toBeLessThanOrEqual(24);
  await expect(page.locator("#exports")).toBeHidden();
  await page
    .getByRole("button", { name: "Show access & revision history" })
    .click();
  await expect(page.locator("#history-output")).toContainText(
    "revision_processed",
  );
  await page.getByRole("button", { name: "Sign out" }).click();
  await expect(page.locator("#message")).toContainText("Signed out");
  await signIn(page, "reviewer");
  await page.locator(".clip-item").first().click();
  await expect(page.locator("#editor")).toBeHidden();
  await page
    .getByLabel("I checked the full processed clip", { exact: false })
    .check();
  await page.getByLabel("I checked context", { exact: false }).check();
  await page
    .getByLabel("Independent review note")
    .fill(
      "Checked the complete synthetic clip and permitted purpose; no anonymity guarantee.",
    );
  await page.getByRole("button", { name: "Record independent review" }).click();
  await expect(page.locator("#badge")).toHaveText("V1 · APPROVED");
  const download = page.waitForEvent("download");
  await page.getByRole("link", { name: "Download reviewed MP4" }).click();
  const file = await download;
  expect(file.suggestedFilename()).toBe("reviewed-video.mp4");
  expect((await fs.promises.stat((await file.path())!)).size).toBeGreaterThan(
    1000,
  );
  const receiptDownload = page.waitForEvent("download");
  await page.getByRole("link", { name: "Download minimal receipt" }).click();
  const receipt = JSON.parse(
    await fs.promises.readFile((await (await receiptDownload).path())!, "utf8"),
  );
  expect(receipt.anonymity_guaranteed).toBe(false);
  expect(receipt.telemetry_included).toBe(false);
  expect(JSON.stringify(receipt)).not.toContain("east_m");
  await page.getByRole("button", { name: "Sign out" }).click();
  await expect(page.locator("#message")).toContainText("Signed out");
  await signIn(page);
  await page.locator(".clip-item").first().click();
  await page.getByRole("button", { name: "Process new revision" }).click();
  await expect(page.locator("#badge")).toHaveText("V2 · REVIEW REQUIRED");
  await expect(page.locator("#exports")).toBeHidden();
});
test("real file import escapes title text and synchronizes an explicit frame", async ({
  page,
}) => {
  await page.goto("/");
  await signIn(page);
  await page
    .getByRole("combobox", { name: "Scenario", exact: true })
    .selectOption("inspection");
  const created = page.waitForResponse(
    (response) =>
      response.url().endsWith("/api/examples/inspection") &&
      response.status() === 200,
  );
  await page.getByRole("button", { name: "Create synthetic clip" }).click();
  const original = await (await created).json();
  await expect(page.locator("#message")).toContainText("Ready");
  const title = "<img src=x onerror=alert(1)> synthetic";
  await page.getByLabel("Clip title", { exact: true }).fill(title);
  await page
    .getByLabel("Authorized purpose", { exact: true })
    .fill(
      "Browser upload of original generated geometry for authorized privacy testing",
    );
  await page
    .getByLabel("MP4 file", { exact: true })
    .setInputFiles(path.join(directory, "media", original.id, "source.mp4"));
  await page.getByRole("button", { name: "Import for private review" }).click();
  await expect(page.locator("#clip-title")).toHaveText(title);
  await loaded(page);
  await expect(page.locator("#clip-title img")).toHaveCount(0);
  await page
    .getByRole("button", { name: "Use frame-by-frame review", exact: true })
    .click();
  await loaded(page);
  await page.locator("#frame").fill("20");
  const frameResponse = page.waitForResponse(
    (response) =>
      response.url().includes("/frame/preview?") &&
      response.url().endsWith("index=20"),
  );
  await page
    .getByRole("button", { name: "Load selected frame", exact: true })
    .click();
  expect((await frameResponse).status()).toBe(200);
  await loaded(page);
  await expect(page.locator("#frame-label")).toContainText("Frame 20 / 39");
  await expect(page.locator("#position")).toContainText("Position unknown");
  await expect(page.locator("#exports")).toBeHidden();
});
test("logout clears private state even when an earlier real clip response arrives late", async ({
  page,
}) => {
  await page.goto("/");
  await signIn(page);
  let release!: () => void;
  let received!: () => void;
  const hold = new Promise<void>((resolve) => {
    release = resolve;
  });
  const responseReady = new Promise<void>((resolve) => {
    received = resolve;
  });
  await page.route(/\/api\/clips\/[0-9a-f]{32}$/, async (route) => {
    const response = await route.fetch();
    received();
    await hold;
    await route.fulfill({ response });
  });
  await page.locator(".clip-item").first().click();
  await responseReady;
  await page.getByRole("button", { name: "Sign out" }).click();
  await expect(page.locator("#login-panel")).toBeVisible();
  release();
  await expect(page.locator("#message")).toContainText("Signed out");
  await expect(page.locator("#clip-title")).toHaveText("");
  await expect(page.locator("#video")).not.toHaveAttribute("src");
  await expect(page.locator("#clip-list")).toBeEmpty();
  await expect(page.locator("#workspace")).toBeHidden();
});
test("keyboard, mobile layout, help and WCAG automated checks", async ({
  page,
}) => {
  await page.goto("/");
  await expect(page.locator("#message")).toContainText("Sign in");
  await page
    .getByText("Help · how this works and what it does not do", { exact: true })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "A review tool, not an anonymity certificate",
    }),
  ).toBeVisible();
  expect(
    (
      await new AxeBuilder({ page })
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
  await signIn(page);
  await page.locator(".clip-item").first().click();
  await expect(page.locator("#clip-panel")).toBeVisible();
  expect(
    (
      await new AxeBuilder({ page })
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= window.innerWidth + 1,
    ),
  ).toBe(true);
});
