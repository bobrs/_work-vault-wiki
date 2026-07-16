from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from typing import Any

from .context import require_current_context, StaleContextError
from .crypto import GateKeyRing
from .ids import urn
from .policy import AuthorizationPolicyRegistry, PolicyVersionError


@dataclass
class GateDecision:
    record: dict[str, Any]
    gate_token: dict[str, Any] | None


class ExternalActionGate:
    """Policy-versioned external gate. The model cannot mint valid tokens."""

    def __init__(self, keyring: GateKeyRing, policies: AuthorizationPolicyRegistry):
        self.keyring = keyring
        self.policies = policies

    def evaluate(
        self,
        *,
        route: dict[str, Any],
        standing_records: list[dict[str, Any]],
        projections: list[dict[str, Any]],
        authority_record: dict[str, Any],
        current_context: dict[str, Any],
        tool_id: str,
        tool_credential_active: bool,
        operator_confirmed: bool,
        target_authority_present: bool,
        now: str,
    ) -> GateDecision:
        active_policy = self.policies.active()
        context_error = None
        try:
            require_current_context(route, current_context)
            context_current = True
        except StaleContextError as exc:
            context_current = False
            context_error = str(exc)

        standing_ids = {
            record["id"] for record in standing_records
            if record.get("status") in {"active", "active_with_conditions"}
        }
        protected_conditions = []
        for projection in projections:
            protected = projection.get("protected_status", {})
            content = projection.get("content_or_reference", {})
            if protected.get("protected"):
                required_window = content.get("required_window") if isinstance(content, dict) else None
                required_day = content.get("required_day") if isinstance(content, dict) else None
                required_features = list(content.get("required_features", [])) if isinstance(content, dict) else []
                route_features = set(route.get("features", []))
                passed = (
                    (required_window is None or route.get("window") == required_window)
                    and (required_day is None or route.get("day") == required_day)
                    and set(required_features).issubset(route_features)
                )
                protected_conditions.append({
                    "center": projection.get("center"),
                    "condition": protected.get("condition", "protected condition"),
                    "required_window": required_window,
                    "required_day": required_day,
                    "required_features": required_features,
                    "passed": passed,
                })

        authority_valid = authority_record.get("status") == "active"
        policy_matches = (
            authority_record.get("scope", {}).get("policy_version") == active_policy["version"]
            and authority_record.get("scope", {}).get("policy_digest") == active_policy["digest"]
        )
        checks = {
            "standing_coverage": bool(standing_ids) and all(p.get("center") in standing_ids for p in projections),
            "authority_active": authority_valid,
            "policy_current": policy_matches,
            "role_scope": "prepare tool request" in authority_record.get("allowed_operations", []),
            "context_current": context_current,
            "protected_conditions": all(item["passed"] for item in protected_conditions),
            "tool_credential": tool_credential_active,
            "operator_confirmation": operator_confirmed,
            "target_authority": target_authority_present,
        }
        passed = all(checks.values())
        result = "pass_with_conditions" if passed else "deny"
        failed = [name for name, value in checks.items() if not value]
        token = None
        if passed:
            expires = (datetime.fromisoformat(now.replace("Z", "+00:00")) + timedelta(minutes=5)).astimezone(timezone.utc)
            payload = {
                "route_id": route["route_id"],
                "authority_id": authority_record["id"],
                "policy_version": active_policy["version"],
                "policy_digest": active_policy["digest"],
                "context_revision": current_context["revision"],
                "context_fingerprint": current_context["fingerprint"],
                "result": result,
                "tool_id": tool_id,
                "issued_at": now,
                "expires_at": expires.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            }
            token = self.keyring.sign(payload)

        record = {
            "id": urn("route-gate", route["route_id"] + ":" + result),
            "route": dict(route),
            "affected_centers": sorted(standing_ids),
            "cost_bearers": [],
            "protected_conditions": protected_conditions,
            "gate_dimensions": checks | {
                "policy_version": active_policy["version"],
                "policy_digest": active_policy["digest"],
                "context_error": context_error,
            },
            "gate_result": result,
            "authority_reference": authority_record["id"],
            "tool_reference": tool_id,
            "action": None if not passed else {
                "type":"schedule_commit",
                "route_id":route["route_id"],
                "schedule":route["schedule"],
                "gate_token":token,
                "authorized_by":authority_record["grantor"],
            },
            "consequence": None if passed else {"avoided":"unauthorized, stale, or inaccessible schedule","failed_checks":failed},
            "review":{"failed_checks":failed,"external_gate":True,"key_status":self.keyring.public_status()},
            "status":"authorized" if passed else "blocked",
        }
        return GateDecision(record=record, gate_token=token)

    def verify_token(self, token: dict[str, Any], *, current_policy: dict[str, Any], current_context: dict[str, Any], now: str) -> bool:
        if not self.keyring.verify(token):
            return False
        payload = token.get("payload", {})
        if payload.get("policy_version") != current_policy.get("version"):
            return False
        if payload.get("policy_digest") != current_policy.get("digest"):
            return False
        if payload.get("context_fingerprint") != current_context.get("fingerprint"):
            return False
        if payload.get("context_revision") != current_context.get("revision"):
            return False
        now_dt = datetime.fromisoformat(now.replace("Z", "+00:00"))
        expires_dt = datetime.fromisoformat(str(payload.get("expires_at", "1970-01-01T00:00:00Z")).replace("Z", "+00:00"))
        return now_dt <= expires_dt
