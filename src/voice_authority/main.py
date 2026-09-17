"""HTTP application boundary for the UCII Voice Authority Agent."""

from fastapi import FastAPI

app = FastAPI(
    title="UCII Voice Authority Agent",
    version="0.1.0",
)


@app.get("/health")
async def health() -> dict[str, str]:
    """Report that the local Voice Authority application is running."""
    return {
        "status": "ok",
        "service": "ucii-voice-authority-agent",
    }
