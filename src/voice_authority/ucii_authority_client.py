"""Read-only UCII delegated-authority evaluation for the Voice agent.

The protected signer supplies credential proof. UCII independently verifies
that proof and evaluates persisted authority for the exact operation.
"""

from __future__ import annotations

import asyncio
import base64
from dataclasses import dataclass
from uuid import uuid4

import httpx

from .protected_signer_client import (
    ProtectedSignerError,
    sign_message,
)


ALLOWED_OPERATIONS = frozenset({
    "compute.purchase",
    "compute.inspect",
})


class AuthorityCheckError(RuntimeError):
    """A trustworthy UCII authority decision could not be obtained."""


@dataclass(frozen=True)
class VoiceIdentityBinding:
    identity_id: str
    credential_id: str
    credential_fingerprint: str
    signing_purpose: str

    def __post_init__(self) -> None:
        for name in (
            "identity_id",
            "credential_id",
            "credential_fingerprint",
            "signing_purpose",
        ):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} is required")


@dataclass(frozen=True)
class AuthorityDecision:
    authorized: bool
    operation: str
    source: str = "UCII_LIVE"


async def check_purchase_authority(
    *,
    ucii_base_url: str,
    binding: VoiceIdentityBinding,
    timeout_seconds: float = 5.0,
    operation: str = "compute.purchase",
) -> AuthorityDecision:
    """Obtain a fresh, read-only UCII delegated-authority decision.

    This function never grants authority or executes an operation.
    A transport, signer or response failure raises AuthorityCheckError,
    rather than being misrepresented as an actual UCII denial.
    """

    if not isinstance(ucii_base_url, str) or not (
        ucii_base_url.startswith("http://")
        or ucii_base_url.startswith("https://")
    ):
        raise ValueError("an HTTP(S) UCII base URL is required")

    if not 0 < timeout_seconds <= 30:
        raise ValueError("invalid UCII timeout")

    if operation not in ALLOWED_OPERATIONS:
        raise ValueError("unsupported delegated operation")

    # A fresh message prevents accidental reuse of an earlier proof.
    # The UCII endpoint independently verifies the signed message.
    message = f"ucii-voice-authority:{operation}:{uuid4()}"

    try:
        signature = await asyncio.to_thread(
            sign_message,
            credential_id=binding.credential_id,
            purpose=binding.signing_purpose,
            message=message.encode("utf-8"),
        )
    except ProtectedSignerError as exc:
        raise AuthorityCheckError(
            "protected signing failed"
        ) from exc

    request = {
        "identity_id": binding.identity_id,
        "credential_fingerprint": binding.credential_fingerprint,
        "operation": operation,
        "message": message,
        "signature": base64.b64encode(signature).decode("ascii"),
    }

    url = (
        ucii_base_url.rstrip("/")
        + "/v1/authorization/delegated/check"
    )

    try:
        async with httpx.AsyncClient(
            timeout=timeout_seconds,
            follow_redirects=False,
        ) as client:
            response = await client.post(url, json=request)
            response.raise_for_status()
            payload = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise AuthorityCheckError(
            "UCII authority check unavailable or invalid"
        ) from exc

    if not isinstance(payload, dict):
        raise AuthorityCheckError(
            "UCII returned an invalid authority response"
        )

    authorized = payload.get("authorized")

    if type(authorized) is not bool:
        raise AuthorityCheckError(
            "UCII response lacks an explicit authority decision"
        )

    return AuthorityDecision(
        authorized=authorized,
        operation=operation,
    )
