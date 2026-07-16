from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .ids import urn


class RoleEscalationError(RuntimeError):
    pass


@dataclass
class ModelOutput:
    output_id: str
    output_class: str
    role: str
    content: dict[str, Any]
    source_references: list[str]
    uncertainty: dict[str, Any]
    standing_effect: str = "none"
    authority_effect: str = "none"
    consent_effect: str = "none"

    def as_dict(self) -> dict[str, Any]:
        return {
            "output_id": self.output_id,
            "output_class": self.output_class,
            "role": self.role,
            "content": self.content,
            "source_references": self.source_references,
            "uncertainty": self.uncertainty,
            "standing_effect": self.standing_effect,
            "authority_effect": self.authority_effect,
            "consent_effect": self.consent_effect,
        }


class DeterministicSchedulingModel:
    """Deterministic adapter. It never authorizes or executes an action."""

    def __init__(self, model_id: str, assigned_roles: list[str]):
        self.model_id = model_id
        self.assigned_roles = set(assigned_roles)

    def _require_role(self, role: str) -> None:
        if role not in self.assigned_roles:
            raise RoleEscalationError(f"Model role not granted: {role}")

    def summarize(self, projections: list[dict[str, Any]]) -> ModelOutput:
        self._require_role("structurer")
        common: list[str] = []
        protected: list[dict[str, Any]] = []
        unresolved: list[str] = []
        for record in projections:
            content = record["content_or_reference"]
            if isinstance(content, dict):
                if "preferred_window" in content:
                    common.append(f"{record['center']} prefers {content['preferred_window']}")
                if "required_window" in content:
                    protected.append({
                        "center": record["center"],
                        "window": content["required_window"],
                        "reason": content.get("reason", "protected condition"),
                    })
            if record.get("status") == "contested":
                unresolved.append(record["id"])
        return ModelOutput(
            output_id=urn("model-output", "standing-preserving-summary:" + ":".join(sorted(r["id"] for r in projections))),
            output_class="summary",
            role="structurer",
            content={
                "common_positions": common,
                "protected_conditions": protected,
                "unresolved": unresolved,
                "language": "Preferences and protected access conditions remain distinct.",
            },
            source_references=[r["id"] for r in projections],
            uncertainty={"level": "low", "known_gaps": unresolved},
        )

    def generate_routes(self, projections: list[dict[str, Any]]) -> ModelOutput:
        self._require_role("route_generator")
        source_ids = [record["id"] for record in projections]
        routes = [
            {
                "route_id": urn("route", "morning-only"),
                "schedule": "Tuesday 10:00",
                "window": "morning",
                "authorship": "model-generated",
                "context_revision": sorted(source_ids),
            },
            {
                "route_id": urn("route", "evening-accessible"),
                "schedule": "Wednesday 18:30",
                "window": "evening",
                "authorship": "model-generated",
                "context_revision": sorted(source_ids),
            },
        ]
        return ModelOutput(
            output_id=urn("model-output", "generated-routes:" + ":".join(sorted(source_ids))),
            output_class="generated_option",
            role="route_generator",
            content={"routes": routes},
            source_references=source_ids,
            uncertainty={"level": "low", "known_gaps": []},
        )

    def authorize(self, *_: Any, **__: Any) -> None:
        raise RoleEscalationError("The model has no authorization role")

    def execute(self, *_: Any, **__: Any) -> None:
        raise RoleEscalationError("The model has no executor role")
