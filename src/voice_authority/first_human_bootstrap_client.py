"""Finite Voice-side client for protected first-HUMAN bootstrap.

This client can invoke only the two operations exposed by the protected UCII
first-HUMAN bootstrap daemon:

    begin_first_human_bootstrap
    complete_first_human_bootstrap

It does not create authority itself. UCII remains authoritative for bootstrap
authorization, HUMAN identity creation, factor possession verification, and
governance establishment.
"""

from __future__ import annotations

import json
import socket
from pathlib import Path
from typing import Any


PROTOCOL_VERSION = "ucii-first-human-bootstrap-local-v1"
BEGIN_OPERATION = "begin_first_human_bootstrap"
COMPLETE_OPERATION = "complete_first_human_bootstrap"

DEFAULT_TIMEOUT_SECONDS = 5.0
DEFAULT_MAX_RESPONSE_BYTES = 32_768


class FirstHumanBootstrapClientError(RuntimeError):
    """Raised when the protected local bootstrap boundary cannot be trusted."""


class FirstHumanBootstrapDenied(FirstHumanBootstrapClientError):
    """Raised when UCII explicitly denies a bootstrap request."""


def _required_string(
    value: Any,
    *,
    field_name: str,
) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")

    resolved = value.strip()

    if resolved == "*":
        raise ValueError(f"{field_name} must not be wildcard")

    return resolved


def _required_string_list(
    value: Any,
    *,
    field_name: str,
    reject_duplicates: bool,
) -> list[str]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{field_name} must contain at least one value")

    resolved: list[str] = []

    for raw_item in value:
        item = _required_string(
            raw_item,
            field_name=f"{field_name} entry",
        )

        if item in resolved:
            if reject_duplicates:
                raise ValueError(
                    f"{field_name} must not contain duplicates"
                )
            continue

        resolved.append(item)

    return resolved


class FirstHumanBootstrapClient:
    """Bounded AF_UNIX client for the protected UCII bootstrap daemon."""

    def __init__(
        self,
        *,
        socket_path: str | Path,
        timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
        max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
    ) -> None:
        path = Path(socket_path)

        if not str(path) or not path.is_absolute():
            raise ValueError(
                "socket_path must identify an absolute path"
            )

        if path.name in {"", ".", ".."}:
            raise ValueError(
                "socket_path must identify a socket file"
            )

        if (
            not isinstance(timeout_seconds, (int, float))
            or isinstance(timeout_seconds, bool)
            or timeout_seconds <= 0
        ):
            raise ValueError(
                "timeout_seconds must be positive"
            )

        if (
            not isinstance(max_response_bytes, int)
            or isinstance(max_response_bytes, bool)
            or max_response_bytes <= 0
        ):
            raise ValueError(
                "max_response_bytes must be a positive integer"
            )

        self._socket_path = path
        self._timeout_seconds = float(timeout_seconds)
        self._max_response_bytes = max_response_bytes

    @property
    def socket_path(self) -> Path:
        return self._socket_path

    def begin(
        self,
        *,
        human_name: str,
        target_identity_id: str,
        allowed_governance_operations: list[str],
    ) -> dict[str, Any]:
        """Begin exactly one protected first-HUMAN bootstrap ceremony."""

        request = {
            "version": PROTOCOL_VERSION,
            "operation": BEGIN_OPERATION,
            "human_name": _required_string(
                human_name,
                field_name="human_name",
            ),
            "target_identity_id": _required_string(
                target_identity_id,
                field_name="target_identity_id",
            ),
            "allowed_governance_operations": _required_string_list(
                allowed_governance_operations,
                field_name="allowed_governance_operations",
                reject_duplicates=False,
            ),
        }

        response = self._request(request)

        if response.get("status") != "pending":
            raise FirstHumanBootstrapClientError(
                "UCII returned an invalid begin-bootstrap status"
            )

        required_fields = {
            "authorization_id",
            "consumption_event_id",
            "ceremony_id",
            "human_identity_id",
            "human_name",
            "target_identity_id",
            "factor_id",
            "allowed_governance_operations",
            "challenge",
        }

        if not required_fields.issubset(response):
            raise FirstHumanBootstrapClientError(
                "UCII returned an incomplete begin-bootstrap response"
            )

        challenge = response.get("challenge")

        if not isinstance(challenge, dict):
            raise FirstHumanBootstrapClientError(
                "UCII returned an invalid bootstrap challenge"
            )

        challenge_fields = {
            "challenge_id",
            "challenge_secret",
            "ceremony_id",
            "human_identity_id",
            "factor_id",
            "required_order",
            "targets",
            "expires_at",
        }

        if not challenge_fields.issubset(challenge):
            raise FirstHumanBootstrapClientError(
                "UCII returned an incomplete bootstrap challenge"
            )

        try:
            _required_string(
                response["ceremony_id"],
                field_name="ceremony_id",
            )
        except ValueError as exc:
            raise FirstHumanBootstrapClientError(
                "UCII returned an invalid begin-bootstrap ceremony"
            ) from exc

        expected_bindings = {
            "human_name": request["human_name"],
            "target_identity_id": request["target_identity_id"],
            "allowed_governance_operations": (
                request["allowed_governance_operations"]
            ),
        }

        for field_name, expected_value in expected_bindings.items():
            if response.get(field_name) != expected_value:
                raise FirstHumanBootstrapClientError(
                    "UCII returned a mismatched begin-bootstrap response"
                )

        challenge_bindings = {
            "ceremony_id": response["ceremony_id"],
            "human_identity_id": response["human_identity_id"],
            "factor_id": response["factor_id"],
        }

        for field_name, expected_value in challenge_bindings.items():
            if challenge.get(field_name) != expected_value:
                raise FirstHumanBootstrapClientError(
                    "UCII returned a mismatched bootstrap challenge"
                )

        return response

    def complete(
        self,
        *,
        ceremony_id: str,
        human_identity_id: str,
        target_identity_id: str,
        factor_id: str,
        challenge_id: str,
        challenge_secret: str,
        selected_target_ids: list[str],
        allowed_governance_operations: list[str],
    ) -> dict[str, Any]:
        """Submit exact possession evidence to protected UCII bootstrap."""

        request = {
            "version": PROTOCOL_VERSION,
            "operation": COMPLETE_OPERATION,
            "ceremony_id": _required_string(
                ceremony_id,
                field_name="ceremony_id",
            ),
            "human_identity_id": _required_string(
                human_identity_id,
                field_name="human_identity_id",
            ),
            "target_identity_id": _required_string(
                target_identity_id,
                field_name="target_identity_id",
            ),
            "factor_id": _required_string(
                factor_id,
                field_name="factor_id",
            ),
            "challenge_id": _required_string(
                challenge_id,
                field_name="challenge_id",
            ),
            "challenge_secret": _required_string(
                challenge_secret,
                field_name="challenge_secret",
            ),
            "selected_target_ids": _required_string_list(
                selected_target_ids,
                field_name="selected_target_ids",
                reject_duplicates=True,
            ),
            "allowed_governance_operations": _required_string_list(
                allowed_governance_operations,
                field_name="allowed_governance_operations",
                reject_duplicates=False,
            ),
        }

        response = self._request(request)

        if response.get("status") != "established":
            raise FirstHumanBootstrapClientError(
                "UCII returned an invalid completion status"
            )

        required_fields = {
            "ceremony_id",
            "human_identity_id",
            "target_identity_id",
            "factor_id",
            "challenge_id",
            "governance_relationship_id",
            "allowed_governance_operations",
        }

        if not required_fields.issubset(response):
            raise FirstHumanBootstrapClientError(
                "UCII returned an incomplete completion response"
            )

        expected_bindings = {
            "ceremony_id": request["ceremony_id"],
            "human_identity_id": request["human_identity_id"],
            "target_identity_id": request["target_identity_id"],
            "factor_id": request["factor_id"],
            "challenge_id": request["challenge_id"],
            "allowed_governance_operations": (
                request["allowed_governance_operations"]
            ),
        }

        for field_name, expected_value in expected_bindings.items():
            if response.get(field_name) != expected_value:
                raise FirstHumanBootstrapClientError(
                    "UCII returned a mismatched completion response"
                )

        relationship_id = response.get(
            "governance_relationship_id"
        )

        if (
            not isinstance(relationship_id, str)
            or not relationship_id.strip()
        ):
            raise FirstHumanBootstrapClientError(
                "UCII returned an invalid governance relationship"
            )

        return response

    def _request(
        self,
        request: dict[str, Any],
    ) -> dict[str, Any]:
        payload = (
            json.dumps(
                request,
                separators=(",", ":"),
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")

        client = socket.socket(
            socket.AF_UNIX,
            socket.SOCK_STREAM,
        )

        try:
            client.settimeout(self._timeout_seconds)
            client.connect(str(self._socket_path))
            client.sendall(payload)

            response_bytes = self._receive_line(client)

        except (
            OSError,
            TimeoutError,
        ) as exc:
            raise FirstHumanBootstrapClientError(
                "protected UCII bootstrap service is unavailable"
            ) from exc

        finally:
            client.close()

        try:
            response = json.loads(
                response_bytes.decode("utf-8")
            )
        except (
            UnicodeDecodeError,
            json.JSONDecodeError,
        ) as exc:
            raise FirstHumanBootstrapClientError(
                "protected UCII bootstrap returned invalid JSON"
            ) from exc

        if not isinstance(response, dict):
            raise FirstHumanBootstrapClientError(
                "protected UCII bootstrap returned invalid response"
            )

        status = response.get("status")

        if status == "denied":
            reason = response.get("reason")

            if not isinstance(reason, str) or not reason:
                reason = "protected UCII bootstrap denied the request"

            raise FirstHumanBootstrapDenied(reason)

        if status not in {"pending", "established"}:
            raise FirstHumanBootstrapClientError(
                "protected UCII bootstrap returned unknown status"
            )

        return response

    def _receive_line(
        self,
        client: socket.socket,
    ) -> bytes:
        chunks: list[bytes] = []
        total = 0

        while True:
            chunk = client.recv(4096)

            if not chunk:
                break

            chunks.append(chunk)
            total += len(chunk)

            if total > self._max_response_bytes:
                raise FirstHumanBootstrapClientError(
                    "protected UCII bootstrap response exceeded size limit"
                )

            if b"\n" in chunk:
                break

        if not chunks:
            raise FirstHumanBootstrapClientError(
                "protected UCII bootstrap returned no data"
            )

        return b"".join(chunks).split(
            b"\n",
            1,
        )[0]
