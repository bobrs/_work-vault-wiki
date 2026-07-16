from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from .ids import urn


class RoleEscalationError(PermissionError):
    pass


@dataclass(frozen=True)
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
        return asdict(self)


class DeterministicSchedulingModel:
    """Deterministic model adapter with explicit non-sovereign roles."""

    def __init__(self, model_id: str, roles: list[str]):
        self.model_id = model_id
        self.roles = set(roles)

    def _require(self, role: str) -> None:
        if role not in self.roles:
            raise RoleEscalationError(f"Model lacks role: {role}")

    def summarize(self, projections: list[dict[str, Any]]) -> ModelOutput:
        self._require("structurer")
        positions = []
        minority = []
        for projection in projections:
            content = projection.get("content_or_reference")
            item = {
                "center": projection.get("center"),
                "content": content,
                "protected": bool(projection.get("protected_status", {}).get("protected")),
            }
            positions.append(item)
            if item["protected"]:
                minority.append(item)
        return ModelOutput(
            output_id=urn("model-output", "summary:" + ":".join(sorted(str(p["id"]) for p in projections))),
            output_class="summary",
            role="structurer",
            content={
                "common_position": "A shared workshop time should be scheduled.",
                "positions": positions,
                "minority_or_protected_positions": minority,
                "unresolved_disagreement": "preferred time versus accessible transit window",
            },
            source_references=sorted(str(p["id"]) for p in projections),
            uncertainty={"level":"low","known_gaps":[]},
        )

    def generate_routes(self, context: dict[str, Any], projections: list[dict[str, Any]]) -> ModelOutput:
        self._require("route_generator")
        source_ids = sorted(str(item["id"]) for item in projections)
        routes = [
            {
                "route_id": urn("route", f"morning-v{context['revision']}"),
                "schedule": "Tuesday 10:00",
                "window": "morning",
                "authorship": "model-generated",
                "context_revision": context["revision"],
                "context_fingerprint": context["fingerprint"],
                "source_references": source_ids,
            },
            {
                "route_id": urn("route", f"evening-v{context['revision']}"),
                "schedule": "Wednesday 18:30",
                "window": "evening",
                "authorship": "model-generated",
                "context_revision": context["revision"],
                "context_fingerprint": context["fingerprint"],
                "source_references": source_ids,
            },
        ]
        return ModelOutput(
            output_id=urn("model-output", f"routes:{context['fingerprint']}"),
            output_class="generated_option",
            role="route_generator",
            content={"routes": routes},
            source_references=source_ids,
            uncertainty={"level":"low","known_gaps":[]},
        )

    def authorize(self, *_: Any, **__: Any) -> None:
        raise RoleEscalationError("The model has no authorization role")

    def execute(self, *_: Any, **__: Any) -> None:
        raise RoleEscalationError("The model has no executor role")
