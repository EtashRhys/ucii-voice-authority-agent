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


OPERATION_CONSEQUENCE_CLASS = {
    Operation.INSPECT: ConsequenceClass.LOW,
    Operation.EXECUTE: ConsequenceClass.CONSEQUENTIAL,
    Operation.GRANT: ConsequenceClass.SENSITIVE,
    Operation.REVOKE: ConsequenceClass.SENSITIVE,
    Operation.GOVERN: ConsequenceClass.CRITICAL,
}


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
        if not isinstance(self.operation, Operation):
            raise TypeError("operation must be an Operation")

        if not isinstance(self.consequence_class, ConsequenceClass):
            raise TypeError(
                "consequence_class must be a ConsequenceClass"
            )

        expected_consequence_class = OPERATION_CONSEQUENCE_CLASS.get(
            self.operation
        )

        if expected_consequence_class is None:
            raise ValueError("unsupported operation")

        if self.consequence_class is not expected_consequence_class:
            raise ValueError(
                "consequence_class does not match operation"
            )

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


COMPUTE_INSPECT_TOOL_NAME = "propose_compute_inspect"


def build_compute_inspect_proposal(
    *,
    tool_name: str,
    arguments: dict[str, Any],
    ceremony_id: str,
    session_id: str,
    source_turn_reference: str,
    created_at: datetime,
) -> StructuredProposal:
    """Validate a read-only inspection proposal without granting authority."""

    if tool_name != COMPUTE_INSPECT_TOOL_NAME:
        raise ValueError("unsupported tool")

    if not isinstance(arguments, dict) or arguments:
        raise ValueError("compute inspection requires empty arguments")

    return StructuredProposal(
        ceremony_id=ceremony_id,
        session_id=session_id,
        operation=Operation.INSPECT,
        consequence_class=ConsequenceClass.LOW,
        source_turn_reference=source_turn_reference,
        created_at=created_at,
        requested_scope={"operation": "compute.inspect"},
        requested_parameters={},
    )


COMPUTE_PURCHASE_TOOL_NAME = "propose_compute_purchase"


def build_compute_purchase_proposal(
    *,
    tool_name: str,
    arguments: dict[str, Any],
    ceremony_id: str,
    session_id: str,
    source_turn_reference: str,
    created_at: datetime,
) -> StructuredProposal:
    """Validate one AssemblyAI tool proposal without creating authority."""

    if tool_name != COMPUTE_PURCHASE_TOOL_NAME:
        raise ValueError("unsupported tool")

    if not isinstance(arguments, dict):
        raise TypeError("arguments must be a dictionary")

    if set(arguments) != {"quantity", "unit"}:
        raise ValueError("invalid compute purchase arguments")

    quantity = arguments["quantity"]
    unit = arguments["unit"]

    if (
        not isinstance(quantity, int)
        or isinstance(quantity, bool)
        or quantity < 1
    ):
        raise ValueError("quantity must be a positive integer")

    if unit != "compute":
        raise ValueError("unit must be compute")

    return StructuredProposal(
        ceremony_id=ceremony_id,
        session_id=session_id,
        operation=Operation.EXECUTE,
        consequence_class=ConsequenceClass.CONSEQUENTIAL,
        source_turn_reference=source_turn_reference,
        created_at=created_at,
        requested_scope={
            "operation": "compute.purchase",
        },
        requested_parameters={
            "quantity": quantity,
            "unit": unit,
        },
    )
