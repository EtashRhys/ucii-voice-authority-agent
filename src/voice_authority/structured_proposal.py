"""Deterministic structured-proposal boundary for Voice Authority requests."""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Any


class Operation(StrEnum):
    """Closed top-level Voice Authority operation vocabulary."""

    INSPECT = "INSPECT"
    GRANT = "GRANT"
    REVOKE = "REVOKE"
    EXECUTE = "EXECUTE"
    GOVERN = "GOVERN"


class ConsequenceClass(StrEnum):
    """Frozen consequence classes used by the ceremony contract."""

    LOW = "LOW"
    CONSEQUENTIAL = "CONSEQUENTIAL"
    SENSITIVE = "SENSITIVE"
    CRITICAL = "CRITICAL"


@dataclass(frozen=True, slots=True)
class StructuredProposal:
    """Canonical bounded proposal before any authority evaluation."""

    ceremony_id: str
    session_id: str
    operation: Operation
    consequence_class: ConsequenceClass
    source_turn_reference: str
    created_at: datetime
    principal_identity_id: str | None = None
    target_identity_id: str | None = None
    target_authority_id: str | None = None
    requested_scope: dict[str, Any] | None = None
    requested_parameters: dict[str, Any] | None = None

    def __post_init__(self) -> None:
        required_text = {
            "ceremony_id": self.ceremony_id,
            "session_id": self.session_id,
            "source_turn_reference": self.source_turn_reference,
        }

        for field_name, value in required_text.items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(
                    f"{field_name} must be a non-empty string"
                )

        optional_text = {
            "principal_identity_id": self.principal_identity_id,
            "target_identity_id": self.target_identity_id,
            "target_authority_id": self.target_authority_id,
        }

        for field_name, value in optional_text.items():
            if value is not None and (
                not isinstance(value, str) or not value.strip()
            ):
                raise ValueError(
                    f"{field_name} must be absent or a non-empty string"
                )

        if not isinstance(self.created_at, datetime):
            raise TypeError("created_at must be a datetime")

        if self.created_at.tzinfo is None:
            raise ValueError("created_at must be timezone-aware")

        for field_name, value in (
            ("requested_scope", self.requested_scope),
            ("requested_parameters", self.requested_parameters),
        ):
            if value is not None and not isinstance(value, dict):
                raise TypeError(
                    f"{field_name} must be absent or a dictionary"
                )
