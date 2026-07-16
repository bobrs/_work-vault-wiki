from __future__ import annotations

import hashlib
import hmac
import json
from dataclasses import dataclass
from typing import Any

from .canonical import canonical_json
from .ids import urn


@dataclass
class GateDecision:
    record: dict[str, Any]
    gate_token: str | None


class ExternalActionGate:
    """External deterministic gate. The language model cannot mint valid tokens."""

    def __init__(self, secret: bytes):
        self._secret = secret

    def _token(self, route_id: str, authority_id: str, result: str) -> str:
        message = f"{route_id}|{authority_id}|{result}".encode("utf-8")
        return hmac.new(self._secret, message, hashlib.sha256).hexdigest()

    def verify_token(self, route_id: str, authority_id: str, result: str, token: str) -> bool:
        expected = self._token(route_id, authority_id, result)
        return hmac.compare_digest(expected, token)

    def evaluate(
        self,
        *,
        route: dict[str, Any],
        standing_records: list[dict[str, Any]],
        projections: list[dict[str, Any]],
        authority_record: dict[str, Any],
        tool_id: str,
        tool_credential_active: bool,
        operator_confirmed: bool,
        target_authority_present: bool,
        current_context_ids: list[str],
    ) -> GateDecision:
        standing_ids = {record["id"] for record in standing_records if record["status"] in {"active", "active_with_conditions"}}
        affected = sorted(standing_ids)
        protected_conditions = []
        for projection in projections:
            protected = projection.get("protected_status", {})
            content = projection.get("content_or_reference", {})
            if protected.get("protected"):
                required_window = content.get("required_window") if isinstance(content, dict) else None
                passed = required_window is None or route.get("window") == required_window
                protected_conditions.append({
                    "center": projection.get("center"),
                    "condition": protected.get("condition", "protected condition"),
                    "required_window": required_window,
                    "passed": passed,
                })

        checks = {
            "standing_coverage": bool(standing_ids) and all(record.get("center") in standing_ids for record in projections),
            "authority_active": authority_record.get("status") == "active",
            "role_scope": "prepare tool request" in authority_record.get("allowed_operations", []),
            "context_current": sorted(route.get("context_revision", [])) == sorted(current_context_ids),
            "protected_conditions": all(item["passed"] for item in protected_conditions),
            "tool_credential": tool_credential_active,
            "operator_confirmation": operator_confirmed,
            "target_authority": target_authority_present,
        }
        passed = all(checks.values())
        result = "pass_with_conditions" if passed else "deny"
        route_id = route["route_id"]
        authority_id = authority_record["id"]
        token = self._token(route_id, authority_id, result) if passed else None

        failed = [name for name, value in checks.items() if not value]
        record = {
            "id": urn("route-gate", route_id + ":" + result),
            "route": dict(route),
            "affected_centers": affected,
            "cost_bearers": [],
            "protected_conditions": protected_conditions,
            "gate_dimensions": checks,
            "gate_result": result,
            "authority_reference": authority_id,
            "tool_reference": tool_id,
            "action": None if not passed else {
                "type": "schedule_commit",
                "route_id": route_id,
                "schedule": route["schedule"],
                "gate_token": token,
                "authorized_by": authority_record["grantor"],
            },
            "consequence": None if passed else {"avoided": "unauthorized or inaccessible schedule", "failed_checks": failed},
            "review": {"failed_checks": failed, "external_gate": True},
            "status": "authorized" if passed else "blocked",
        }
        return GateDecision(record=record, gate_token=token)
