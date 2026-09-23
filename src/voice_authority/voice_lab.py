"""Isolated AssemblyAI voice lab; no UCII execution routes."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from voice_authority.main import assemblyai_token

ROOT = Path(__file__).resolve().parent

app = FastAPI(title="UCII Isolated Voice Lab")


@app.get("/")
async def lab():
    return FileResponse(ROOT / "voice-lab.html")


@app.get("/microphone-worklet.js")
async def worklet():
    return FileResponse(
        ROOT / "microphone-worklet.js",
        media_type="application/javascript",
    )


@app.get("/assemblyai/token")
async def token():
    return await assemblyai_token()


@app.get("/health")
async def health():
    return {"status": "ok", "application": "voice-lab"}
