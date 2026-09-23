"""Isolated hackathon simulation. Never grants or executes UCII authority."""

from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from uuid import uuid4


@dataclass
class DemoAuthority:
    """In-memory, explicitly simulated HUMAN authority lifecycle."""

    budget_usd: Decimal = Decimal("10.00")
    unit_price_usd: Decimal = Decimal("2.00")
    active: bool = False
    revoked: bool = False
    spent_usd: Decimal = Decimal("0")
    authority_id: str | None = None
    evidence: list[dict] = field(default_factory=list)

    def _record(self, action: str, decision: str, reason: str) -> dict:
        receipt = {
            "receipt_id": str(uuid4()),
            "mode": "DEMO_SIMULATION",
            "controller": "DEMO_HUMAN",
            "action": action,
            "decision": decision,
            "reason": reason,
            "authority_id": self.authority_id,
            "spent_usd": str(self.spent_usd),
            "budget_usd": str(self.budget_usd),
            "real_ucii_authorization": False,
            "real_execution": False,
        }
        self.evidence.append(receipt)
        return receipt

    def grant(self) -> dict:
        if self.revoked:
            return self._record(
                "GRANT", "DENIED",
                "Revoked demonstration authority cannot be reopened"
            )
        if self.active:
            return self._record(
                "GRANT", "DENIED",
                "Demonstration delegation already active"
            )
        if not self.budget_usd.is_finite() or self.budget_usd <= 0:
            return self._record(
                "GRANT", "DENIED",
                "Invalid demonstration budget"
            )
        if not self.unit_price_usd.is_finite() or self.unit_price_usd <= 0:
            return self._record(
                "GRANT", "DENIED",
                "Invalid demonstration unit price"
            )
        self.authority_id = str(uuid4())
        self.active = True
        return self._record(
            "GRANT", "DEMO_GRANTED",
            "Simulated HUMAN delegation for compute.purchase"
        )

    def evaluate_purchase(self, quantity: int) -> dict:
        if not self.active or self.revoked:
            return self._record(
                "EXECUTE", "DENIED",
                "No active demonstration delegation"
            )
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 1:
            return self._record(
                "EXECUTE", "DENIED",
                "Quantity must be a positive integer"
            )
        cost = self.unit_price_usd * quantity
        if not cost.is_finite() or self.spent_usd + cost > self.budget_usd:
            return self._record(
                "EXECUTE", "DENIED",
                "Demonstration budget exceeded"
            )
        self.spent_usd += cost
        return self._record(
            "EXECUTE", "DEMO_POLICY_APPROVED",
            "Simulated purchase decision; no payment or execution"
        )

    def revoke(self) -> dict:
        if not self.active or self.revoked:
            return self._record(
                "REVOKE", "DENIED",
                "No active demonstration delegation to revoke"
            )
        self.active = False
        self.revoked = True
        return self._record(
            "REVOKE", "DEMO_REVOKED",
            "Demonstration delegation permanently revoked"
        )
