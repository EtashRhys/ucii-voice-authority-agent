"""Client for the existing self-hosted UCII Voice signing daemon.

This module never loads or handles private signing material.
"""

from __future__ import annotations

import base64
import binascii
import json
import socket
from pathlib import Path


VOICE_SIGNER_SOCKET = Path(
    "/run/ucii-voice-authority-signer/signer.sock"
)
PROTOCOL_VERSION = "ucii-local-signer-v1"
MAX_RESPONSE_BYTES = 65536


class ProtectedSignerError(RuntimeError):
    """A protected signing request failed or was rejected."""


def sign_message(
    *,
    credential_id: str,
    purpose: str,
    message: bytes,
    socket_path: Path = VOICE_SIGNER_SOCKET,
    timeout_seconds: float = 3.0,
) -> bytes:
    """Request one ML-DSA-65 signature from the protected Voice signer."""

    if not isinstance(credential_id, str) or not credential_id.strip():
        raise ValueError("credential_id is required")

    if not isinstance(purpose, str) or not purpose.strip():
        raise ValueError("signing purpose is required")

    if not isinstance(message, bytes) or not message:
        raise ValueError("message must be nonempty bytes")

    if not 0 < timeout_seconds <= 30:
        raise ValueError("invalid signing timeout")

    request = {
        "version": PROTOCOL_VERSION,
        "operation": "sign",
        "credential_id": credential_id,
        "algorithm": "ML-DSA-65",
        "purpose": purpose,
        "message_b64": base64.b64encode(message).decode("ascii"),
    }

    encoded = (
        json.dumps(request, separators=(",", ":")) + "\n"
    ).encode("utf-8")

    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as conn:
            conn.settimeout(timeout_seconds)
            conn.connect(str(socket_path))
            conn.sendall(encoded)

            response = bytearray()

            while b"\n" not in response:
                chunk = conn.recv(4096)

                if not chunk:
                    raise ProtectedSignerError(
                        "signer closed connection without a complete response"
                    )

                response.extend(chunk)

                if len(response) > MAX_RESPONSE_BYTES:
                    raise ProtectedSignerError(
                        "signer response exceeded size limit"
                    )

    except (OSError, TimeoutError) as exc:
        raise ProtectedSignerError(
            "protected signer unavailable"
        ) from exc

    try:
        payload = json.loads(response.split(b"\n", 1)[0])
    except (ValueError, UnicodeDecodeError) as exc:
        raise ProtectedSignerError(
            "invalid protected signer response"
        ) from exc

    if not isinstance(payload, dict):
        raise ProtectedSignerError(
            "invalid protected signer response"
        )

    if payload.get("status") != "signed":
        raise ProtectedSignerError(
            "protected signer denied the request"
        )

    signature_b64 = payload.get("signature_b64")

    if not isinstance(signature_b64, str) or not signature_b64:
        raise ProtectedSignerError(
            "protected signer returned no signature"
        )

    try:
        signature = base64.b64decode(
            signature_b64, validate=True
        )
    except (ValueError, binascii.Error) as exc:
        raise ProtectedSignerError(
            "protected signer returned an invalid signature"
        ) from exc

    if not signature:
        raise ProtectedSignerError(
            "protected signer returned an empty signature"
        )

    return signature
