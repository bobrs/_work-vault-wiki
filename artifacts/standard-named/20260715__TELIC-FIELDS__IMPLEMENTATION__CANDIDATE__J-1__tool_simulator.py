from __future__ import annotations

from typing import Any

from .canonical import utc_now
from .ids import urn


class ToolExecutionDenied(PermissionError):
    pass


class PartialToolFailure(RuntimeError):
    pass


class SchedulingToolSimulator:
    def __init__(self, tool_id: str, gate: Any, policies: Any, context_provider: Any):
        self.tool_id = tool_id
        self.gate = gate
        self.policies = policies
        self.context_provider = context_provider
        self.credential_active = True
        self.committed: dict[str, dict[str, Any]] = {}
        self.reservations: dict[str, dict[str, Any]] = {}

    def revoke(self) -> None:
        self.credential_active = False

    def commit(self, decision: dict[str, Any], *, fail_after_reservation: bool = False, attempt: int = 1) -> dict[str, Any]:
        if not self.credential_active:
            raise ToolExecutionDenied("Tool credential revoked")
        if decision.get("gate_result") != "pass_with_conditions":
            raise ToolExecutionDenied("Gate decision does not permit execution")
        action = decision.get("action") or {}
        token = action.get("gate_token")
        if not isinstance(token, dict):
            raise ToolExecutionDenied("Missing gate token")
        now = utc_now()
        if not self.gate.verify_token(
            token,
            current_policy=self.policies.active(),
            current_context=self.context_provider(),
            now=now,
        ):
            raise ToolExecutionDenied("Gate token invalid, stale, expired, or revoked")
        route = decision["route"]
        reservation_id = urn("reservation", f"{route['route_id']}:{attempt}")
        transaction_id = urn("tool-transaction", f"{route['route_id']}:{attempt}")
        self.reservations[reservation_id] = {"route_id":route["route_id"],"status":"reserved"}
        base = {
            "transaction_id":transaction_id,
            "route_id":route["route_id"],
            "tool_id":self.tool_id,
            "policy_version":token["payload"]["policy_version"],
            "key_id":token["key_id"],
            "reservation_id":reservation_id,
            "attempt":attempt,
            "events":["reservation_created"],
        }
        if fail_after_reservation:
            self.reservations[reservation_id]["status"] = "released"
            record = base | {
                "phase":"compensated",
                "result":{"committed":False,"failure":"simulated partial failure after reservation"},
                "compensation":{"reservation_released":True,"external_state_restored":True},
                "events":["reservation_created","commit_failed","reservation_released"],
                "status":"compensated",
            }
            raise PartialToolFailure(record)
        result = {
            "tool_result_id":urn("tool-result", route["route_id"]),
            "route_id":route["route_id"],
            "schedule":route["schedule"],
            "committed_at":now,
            "authorized_by":decision["authority_reference"],
            "gate_token_key_id":token["key_id"],
        }
        self.committed[route["route_id"]] = result
        self.reservations[reservation_id]["status"] = "committed"
        return base | {
            "phase":"committed",
            "result":result,
            "compensation":{"required":False},
            "events":["reservation_created","schedule_committed"],
            "status":"complete",
        }
