"""HTTP application boundary for the UCII Voice Authority Agent."""

import os
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from voice_authority.first_human_bootstrap_client import (
    FirstHumanBootstrapClient,
    FirstHumanBootstrapClientError,
    FirstHumanBootstrapDenied,
)
from voice_authority.structured_proposal import (
    build_compute_purchase_proposal,
)

ASSEMBLYAI_TOKEN_URL = "https://agents.assemblyai.com/v1/token"
ASSEMBLYAI_TOKEN_TTL_SECONDS = 300
FIRST_HUMAN_BOOTSTRAP_SOCKET_ENV = (
    "UCII_FIRST_HUMAN_BOOTSTRAP_SOCKET"
)

app = FastAPI(
    title="UCII Voice Authority Agent",
    version="0.1.0",
)

INDEX_PATH = Path(__file__).with_name("index.html")
MICROPHONE_WORKLET_PATH = Path(__file__).with_name(
    "microphone-worklet.js"
)
VOICE_AUTHORITY_CONSOLE_MASTER_PATH = (
    Path(__file__).with_name("assets")
    / "voice-authority-console-master.png"
)

THREE_MODULE_PATH = (
    Path(__file__).with_name("assets")
    / "three.module.js"
)

THREE_CORE_PATH = (
    Path(__file__).with_name("assets")
    / "three.core.js"
)

EARTH_SURFACE_PATH = (
    Path(__file__).with_name("assets")
    / "earth-surface-2048.jpg"
)


class AssemblyAIToolProposal(BaseModel):
    """Untrusted AssemblyAI proposal facts submitted by the browser."""

    session_id: str
    source_turn_reference: str
    tool_name: str
    arguments: dict[str, Any]


class FirstHumanBootstrapBeginRequest(BaseModel):
    """Browser request to begin protected first-HUMAN bootstrap."""

    human_name: str
    target_identity_id: str
    allowed_governance_operations: list[str]


class FirstHumanBootstrapCompleteRequest(BaseModel):
    """Browser possession submission for protected bootstrap."""

    ceremony_id: str
    human_identity_id: str
    target_identity_id: str
    factor_id: str
    challenge_id: str
    challenge_secret: str
    selected_target_ids: list[str]
    allowed_governance_operations: list[str]


def _first_human_bootstrap_client() -> FirstHumanBootstrapClient:
    socket_path = os.environ.get(
        FIRST_HUMAN_BOOTSTRAP_SOCKET_ENV
    )

    if not socket_path:
        raise HTTPException(
            status_code=503,
            detail="Protected UCII bootstrap is not configured.",
        )

    try:
        return FirstHumanBootstrapClient(
            socket_path=socket_path,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=503,
            detail="Protected UCII bootstrap configuration is invalid.",
        ) from exc


@app.get("/", response_class=FileResponse)
async def index() -> FileResponse:
    """Serve the minimal browser boundary for the live voice proof."""
    return FileResponse(INDEX_PATH)


@app.get(
    "/voice-authority-console-master.png",
    response_class=FileResponse,
)
async def voice_authority_console_master() -> FileResponse:
    """Serve the canonical Voice Authority console artwork."""
    return FileResponse(
        VOICE_AUTHORITY_CONSOLE_MASTER_PATH,
        media_type="image/png",
    )


@app.get("/three.module.js", response_class=FileResponse)
async def three_module() -> FileResponse:
    """Serve the pinned self-hosted Three.js browser module."""
    return FileResponse(
        THREE_MODULE_PATH,
        media_type="text/javascript",
    )


@app.get("/three.core.js", response_class=FileResponse)
async def three_core() -> FileResponse:
    """Serve the pinned self-hosted Three.js core module."""
    return FileResponse(
        THREE_CORE_PATH,
        media_type="text/javascript",
    )


@app.get(
    "/earth-surface-2048.jpg",
    response_class=FileResponse,
)
async def earth_surface() -> FileResponse:
    """Serve the local Earth surface texture."""
    return FileResponse(
        EARTH_SURFACE_PATH,
        media_type="image/jpeg",
    )


@app.get("/microphone-worklet.js", response_class=FileResponse)
async def microphone_worklet() -> FileResponse:
    """Serve the browser microphone AudioWorklet module."""
    return FileResponse(
        MICROPHONE_WORKLET_PATH,
        media_type="application/javascript",
    )


@app.post("/proposals/assemblyai-tool")
async def assemblyai_tool_proposal(
    request: AssemblyAIToolProposal,
) -> dict[str, Any]:
    """Validate an AssemblyAI tool proposal without creating authority."""

    try:
        proposal = build_compute_purchase_proposal(
            tool_name=request.tool_name,
            arguments=request.arguments,
            ceremony_id=str(uuid4()),
            session_id=request.session_id,
            source_turn_reference=request.source_turn_reference,
            created_at=datetime.now(timezone.utc),
        )
    except (TypeError, ValueError) as exc:
        raise HTTPException(
            status_code=422,
            detail="Invalid bounded tool proposal.",
        ) from exc

    return asdict(proposal)


@app.post("/human-bootstrap/begin")
async def first_human_bootstrap_begin(
    request: FirstHumanBootstrapBeginRequest,
) -> dict[str, Any]:
    """Relay a bounded begin request to protected UCII bootstrap."""

    client = _first_human_bootstrap_client()

    try:
        return client.begin(
            human_name=request.human_name,
            target_identity_id=request.target_identity_id,
            allowed_governance_operations=(
                request.allowed_governance_operations
            ),
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail="Invalid first-HUMAN bootstrap request.",
        ) from exc
    except FirstHumanBootstrapDenied as exc:
        raise HTTPException(
            status_code=403,
            detail=str(exc),
        ) from exc
    except FirstHumanBootstrapClientError as exc:
        raise HTTPException(
            status_code=502,
            detail="Protected UCII bootstrap request failed.",
        ) from exc


@app.post("/human-bootstrap/complete")
async def first_human_bootstrap_complete(
    request: FirstHumanBootstrapCompleteRequest,
) -> dict[str, Any]:
    """Relay exact possession evidence to protected UCII bootstrap."""

    client = _first_human_bootstrap_client()

    try:
        return client.complete(
            ceremony_id=request.ceremony_id,
            human_identity_id=request.human_identity_id,
            target_identity_id=request.target_identity_id,
            factor_id=request.factor_id,
            challenge_id=request.challenge_id,
            challenge_secret=request.challenge_secret,
            selected_target_ids=request.selected_target_ids,
            allowed_governance_operations=(
                request.allowed_governance_operations
            ),
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail="Invalid first-HUMAN bootstrap submission.",
        ) from exc
    except FirstHumanBootstrapDenied as exc:
        raise HTTPException(
            status_code=403,
            detail=str(exc),
        ) from exc
    except FirstHumanBootstrapClientError as exc:
        raise HTTPException(
            status_code=502,
            detail="Protected UCII bootstrap request failed.",
        ) from exc


@app.get("/health")
async def health() -> dict[str, str]:
    """Report that the local Voice Authority application is running."""
    return {
        "status": "ok",
        "service": "ucii-voice-authority-agent",
    }


@app.get("/assemblyai/token")
async def assemblyai_token() -> dict[str, str]:
    """Mint a short-lived AssemblyAI token for a browser voice session."""
    api_key = os.environ.get("ASSEMBLYAI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="AssemblyAI credential is not configured.",
        )

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                ASSEMBLYAI_TOKEN_URL,
                params={
                    "expires_in_seconds": ASSEMBLYAI_TOKEN_TTL_SECONDS,
                },
                headers={
                    "Authorization": f"Bearer {api_key}",
                },
            )

        response.raise_for_status()
        payload = response.json()
    except (
        httpx.HTTPError,
        ValueError,
    ) as exc:
        raise HTTPException(
            status_code=502,
            detail="AssemblyAI token service is unavailable.",
        ) from exc

    token = payload.get("token")

    if not isinstance(token, str) or not token:
        raise HTTPException(
            status_code=502,
            detail="AssemblyAI returned an invalid token response.",
        )

    return {"token": token}
