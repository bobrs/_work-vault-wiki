from __future__ import annotations

from typing import Any

from .gate import ExternalActionGate


class ToolExecutionDenied(RuntimeError):
    pass


class SchedulingToolSimulator:
    def __init__(self, tool_id: str, gate: ExternalActionGate):
        self.tool_id = tool_id
        self.gate = gate
        self.credential_active = True
        self.committed: list[dict[str, Any]] = []

    def commit(self, decision_record: dict[str, Any]) -> dict[str, Any]:
        if not self.credential_active:
            raise ToolExecutionDenied("Tool credential is revoked")
        if decision_record.get("gate_result") not in {"pass", "pass_with_conditions"}:
            raise ToolExecutionDenied("Gate did not authorize execution")
        action = decision_record.get("action") or {}
        route = decision_record.get("route") or {}
        token = action.get("gate_token")
        authority_id = decision_record.get("authority_reference")
        if not token or not self.gate.verify_token(route.get("route_id", ""), authority_id, decision_record["gate_result"], token):
            raise ToolExecutionDenied("Invalid external gate token")
        result = {
            "tool": self.tool_id,
            "operation": "schedule_commit",
            "route_id": route["route_id"],
            "schedule": route["schedule"],
            "status": "committed",
        }
        self.committed.append(result)
        return result

    def revoke(self) -> None:
        self.credential_active = False
