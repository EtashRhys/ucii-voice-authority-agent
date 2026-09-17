"""HTTP application boundary for the UCII Voice Authority Agent."""

import os
from pathlib import Path

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

ASSEMBLYAI_TOKEN_URL = "https://agents.assemblyai.com/v1/token"
ASSEMBLYAI_TOKEN_TTL_SECONDS = 300

app = FastAPI(
    title="UCII Voice Authority Agent",
    version="0.1.0",
)

INDEX_PATH = Path(__file__).with_name("index.html")


@app.get("/", response_class=FileResponse)
async def index() -> FileResponse:
    """Serve the minimal browser boundary for the live voice proof."""
    return FileResponse(INDEX_PATH)


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
