"""Jason Stys: authenticated loopback video-review API and same-origin static interface.

Exact endpoint/variable lines: docs/SOURCE_MAP.md. No public original-file or registration route.
"""

import asyncio
import threading
from pathlib import Path
from typing import Annotated, Literal

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles

from workbench import auth, service
from workbench.media import MAX_BYTES
from workbench.models import Login, Plan, Review
from workbench.store import Store

HEADERS = {
    "Content-Security-Policy": "default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; media-src 'self'; connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
    "Cache-Control": "no-store",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
}
BODY_GATE = threading.BoundedSemaphore(2)


def create_app(database: Path, port=8891):
    """Bind one local organization to an exact authority; not hardened public SaaS hosting."""
    if not 1024 <= port <= 65535:
        raise ValueError("Port outside supported range")
    origin, authority = f"http://127.0.0.1:{port}", f"127.0.0.1:{port}"
    app = FastAPI(
        title="Drone Video Privacy Studio", docs_url=None, redoc_url=None, openapi_url=None
    )
    app.state.store = Store(database)

    @app.middleware("http")
    async def boundary(request: Request, call_next):
        """Exact Host/Origin, early auth, two bounded body readers, deadlines and security headers."""
        response, acquired = None, False
        try:
            if request.headers.get("host") != authority:
                raise HTTPException(400, "Untrusted Host")
            if request.method not in {"GET", "HEAD", "POST"}:
                raise HTTPException(405, "Method not allowed")
            if request.url.path.startswith("/api/") and (
                request.headers.get("sec-fetch-site") == "cross-site"
                or request.headers.get("origin", origin) != origin
            ):
                raise HTTPException(403, "Exact same-origin required")
            if request.method == "POST":
                if request.headers.get("origin") != origin:
                    raise HTTPException(403, "Exact same-origin required")
                if request.url.path != "/api/login":
                    auth.authorize(request)
                media = request.url.path == "/api/clips/import"
                expected = "video/mp4" if media else "application/json"
                if request.headers.get("content-type", "").split(";")[0] != expected:
                    raise HTTPException(415, f"{expected} required")
                if not BODY_GATE.acquire(blocking=False):
                    raise HTTPException(429, "Request body capacity reached")
                acquired = True
                data = bytearray()
                async with asyncio.timeout(20 if media else 5):
                    async for chunk in request.stream():
                        if len(data) + len(chunk) > (MAX_BYTES if media else 65536):
                            raise HTTPException(413, "Body exceeds endpoint size limit")
                        data.extend(chunk)
                request._body = bytes(data)
            response = await call_next(request)
        except HTTPException as error:
            response = JSONResponse({"detail": error.detail}, status_code=error.status_code)
        except TimeoutError:
            response = JSONResponse({"detail": "Body timeout"}, status_code=408)
        finally:
            if acquired:
                BODY_GATE.release()
        response.headers.update(HEADERS)
        return response

    @app.exception_handler(RequestValidationError)
    async def invalid(_request, error):
        """Report field paths/types without reflecting passwords, video contents or private notes."""
        return JSONResponse(
            {
                "detail": "Invalid field types, bounds or contradictory values",
                "fields": [{"location": list(e["loc"]), "type": e["type"]} for e in error.errors()],
            },
            status_code=422,
        )

    @app.get("/healthz")
    def health():
        """Liveness only; no account, filesystem or media details."""
        return {"status": "ok", "mode": "local-private-video-review"}

    @app.post("/api/login")
    def login(body: Login, request: Request):
        """Issue an HttpOnly opaque session, hashed server-side, with separate same-origin CSRF token."""
        token, user = auth.sign_in(request, body.username, body.password)
        response = JSONResponse(user)
        response.set_cookie("video_session", token, httponly=True, samesite="strict", max_age=3600)
        return response

    @app.get("/api/me")
    def me(request: Request):
        """Resolve live role and expiry from SQLite, never trust client role claims."""
        return auth.identity(request)

    @app.post("/api/logout")
    def logout(request: Request):
        """Revoke immediately, then clear the same local cookie."""
        auth.sign_out(request)
        response = JSONResponse({"signed_out": True})
        response.delete_cookie("video_session")
        return response

    @app.get("/api/clips")
    def clips(request: Request):
        """Authorized bounded active-clip history; operators cannot see another operator's clips."""
        return app.state.store.list(auth.identity(request))

    @app.post("/api/clips/import")
    async def upload(
        request: Request,
        title: Annotated[str, Query(min_length=3, max_length=80)],
        purpose: Annotated[str, Query(min_length=10, max_length=300)],
        retention: Annotated[int, Query(ge=1, le=30)] = 7,
    ):
        """Read bounded raw MP4 bytes, no filenames/URLs; offload native job wait from event loop."""
        user = auth.authorize(request)
        data = await request.body()
        return await asyncio.to_thread(
            service.import_clip, app.state.store, user, title, purpose, retention, data
        )

    @app.post("/api/examples/{scenario}")
    def example(scenario: Literal["flood", "inspection", "training"], request: Request):
        """Generate original synthetic pixels in a worker; never fetch third-party footage."""
        return service.import_clip(
            app.state.store,
            auth.authorize(request),
            f"Synthetic {scenario} assessment",
            "Original generated geometry for authorized privacy review training",
            7,
            scenario=scenario,
        )

    @app.get("/api/clips/{identifier}")
    def clip(identifier: str, request: Request):
        """Private source metadata, current masks, alignment and review status."""
        return app.state.store.get(identifier, auth.identity(request))

    @app.get("/api/clips/{identifier}/history")
    def history(identifier: str, request: Request):
        """Clip-scoped revision hashes and access history, not public analytics."""
        return app.state.store.history(identifier, auth.identity(request))

    @app.post("/api/clips/{identifier}/process")
    def process(identifier: str, body: Plan, request: Request):
        """Operator/admin creates a fully verified immutable revision; earlier approvals become stale."""
        return service.process(app.state.store, identifier, auth.authorize(request), body)

    @app.post("/api/clips/{identifier}/review")
    def review(identifier: str, body: Review, request: Request):
        """Reviewer-only independent attestation; cannot override missing review or telemetry drift."""
        user = auth.authorize(request, "reviewer")
        app.state.store.review(identifier, user, body)
        return app.state.store.get(identifier, user)

    @app.get("/api/clips/{identifier}/media/{kind}")
    def media(
        identifier: str,
        kind: Literal["preview", "redacted", "export"],
        request: Request,
        version: Annotated[int, Query(ge=0)],
    ):
        """Reauthorize every video range request; safe generated names; no raw original endpoint."""
        path = app.state.store.file(identifier, auth.identity(request), kind, version=version)
        return FileResponse(
            path,
            media_type="video/mp4",
            filename="reviewed-video.mp4" if kind == "export" else None,
        )

    @app.get("/api/clips/{identifier}/manifest")
    def manifest(identifier: str, request: Request):
        """Download only minimal approved receipt, not the private report/telemetry/notes."""
        return JSONResponse(
            app.state.store.manifest(identifier, auth.identity(request)),
            headers={"Content-Disposition": 'attachment; filename="reviewed-video-receipt.json"'},
        )

    @app.get("/api/clips/{identifier}/frame/{kind}")
    def frame(
        identifier: str,
        kind: Literal["preview", "redacted"],
        request: Request,
        version: Annotated[int, Query(ge=0)],
        index: Annotated[int, Query(ge=0, le=599)],
    ):
        """Codec-independent authorized frame inspection; no raw original and no persistent PNG cache."""
        return Response(
            service.render_frame(
                app.state.store, identifier, auth.identity(request), kind, version, index
            ),
            media_type="image/png",
        )

    @app.get("/")
    def index():
        """Fixed built UI, never serve the database/media directory through a static mount."""
        if not (service.ROOT / "dist/index.html").is_file():
            raise HTTPException(503, "Build UI with npm run build")
        return FileResponse(service.ROOT / "dist/index.html")

    if (service.ROOT / "dist/assets").is_dir():
        app.mount("/assets", StaticFiles(directory=service.ROOT / "dist/assets"), name="assets")
    return app
