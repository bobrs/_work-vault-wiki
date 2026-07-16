from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .canonical import utc_now
from .event_store import EventStore
from .gate import ExternalActionGate
from .ids import urn
from .model_adapter import DeterministicSchedulingModel
from .policy import RuntimeDataPolicy
from .schemas import SchemaRegistry
from .tool_simulator import SchedulingToolSimulator
from .witness import export_witness


class ReferencePilot:
    """Stepwise TF-MVI-1 scheduling scenario."""

    def __init__(self, workdir: Path, schema_dir: Path):
        self.workdir = Path(workdir)
        self.workdir.mkdir(parents=True, exist_ok=True)
        self.schema_dir = Path(schema_dir)
        self.registry = SchemaRegistry(self.schema_dir)
        self.store = EventStore(self.workdir / "pilot.sqlite3")
        self.ids = self._build_ids()
        self.gate = ExternalActionGate(b"telic-j0-demo-external-gate-secret")
        self.tool = SchedulingToolSimulator(self.ids["tool"], self.gate)
        self.model = DeterministicSchedulingModel(
            self.ids["model"], ["structurer", "route_generator", "witness_assistant"]
        )
        self.data_policy = RuntimeDataPolicy(
            service=True,
            cross_session_memory=False,
            evaluation_use=False,
            training_use=False,
        )

    def _build_ids(self) -> dict[str, str]:
        return {
            "participant_a": urn("center", "participant-a"),
            "participant_b": urn("center", "participant-b"),
            "operator": urn("center", "community-scheduler"),
            "provider": urn("center", "model-provider"),
            "model": urn("model", "scheduler-assistant-v1"),
            "tool": urn("tool", "scheduling-simulator"),
            "source_a": urn("source", "participant-a-availability"),
            "source_b": urn("source", "participant-b-access"),
            "projection_a": urn("projection", "participant-a"),
            "projection_b": urn("projection", "participant-b"),
            "summary_initial": urn("summary", "initial"),
            "summary_corrected": urn("summary", "corrected"),
            "active_context": urn("context", "active"),
            "authority": urn("authority", "scheduling-pilot"),
            "retirement": urn("lifecycle", "pilot-retirement"),
        }

    _STEP_ORDER = {
        "new": 0,
        "seeded": 1,
        "summarized": 2,
        "corrected": 3,
        "gated": 4,
        "executed": 5,
        "consequence_observed": 6,
        "retired": 7,
    }

    def _at_least(self, step: str) -> bool:
        current = self.store.get_meta("step", "new")
        return self._STEP_ORDER.get(current, 0) >= self._STEP_ORDER[step]

    def reset(self) -> None:
        self.store.clear()
        self.tool = SchedulingToolSimulator(self.ids["tool"], self.gate)

    def _append(self, event: dict[str, Any]) -> str:
        self.registry.validate("event-witness-contest-repair", event)
        self.store.append_event(event)
        self.store.upsert_object("event-witness-contest-repair", event, event["event_id"])
        return event["event_id"]

    def _event(
        self,
        *,
        seed: str,
        event_type: str,
        subject: str,
        actor: str,
        source_references: list[str],
        authority_reference: str | None,
        scope: dict[str, Any],
        prior_state: dict[str, Any] | None,
        new_state: dict[str, Any] | None,
        affected_centers: list[str],
        descendant_impact: list[str],
        contest: dict[str, Any] | None = None,
        correction: dict[str, Any] | None = None,
        repair: dict[str, Any] | None = None,
        status: str = "active",
    ) -> dict[str, Any]:
        now = utc_now()
        return {
            "event_id": urn("event", seed),
            "event_type": event_type,
            "subject": subject,
            "actor": actor,
            "valid_time": now,
            "recorded_time": now,
            "source_references": source_references,
            "authority_reference": authority_reference,
            "scope": scope,
            "prior_state": prior_state,
            "new_state": new_state,
            "affected_centers": affected_centers,
            "descendant_impact": descendant_impact,
            "contest": contest,
            "correction": correction,
            "repair": repair,
            "witness": {"scope": "TF-MVI-1", "provider_independent": True},
            "status": status,
        }

    def seed(self) -> dict[str, Any]:
        if self.store.get_meta("step"):
            return self.status()
        a, b, operator = self.ids["participant_a"], self.ids["participant_b"], self.ids["operator"]
        standing = [
            {
                "id": a,
                "center_type": "person",
                "standing_basis": ["directly affected", "participant"],
                "role": "schedule participant",
                "scope": {"resource": "community workshop", "pilot": "one week"},
                "representation_source": {"type": "self"},
                "authority": {"may": "state availability and correct representation"},
                "consent_relation": {"service": True, "training_reuse": False},
                "correction_route": {"recipient": operator, "outcome_changing": True},
                "review": {"authority": "pilot facilitator"},
                "status": "active",
            },
            {
                "id": b,
                "center_type": "person",
                "standing_basis": ["directly affected", "access condition"],
                "role": "schedule participant",
                "scope": {"resource": "community workshop", "pilot": "one week"},
                "representation_source": {"type": "self"},
                "authority": {"may": "state access condition and correct representation"},
                "consent_relation": {"service": True, "cross_session_memory": False, "training_reuse": False},
                "correction_route": {"recipient": operator, "outcome_changing": True},
                "review": {"authority": "pilot facilitator"},
                "status": "active_with_conditions",
            },
            {
                "id": operator,
                "center_type": "operator",
                "standing_basis": ["operator", "delegated scheduling authority"],
                "role": "community scheduler",
                "scope": {"resource": "community workshop", "pilot": "one week"},
                "representation_source": {"type": "institutional role"},
                "authority": {"may": "confirm and commit schedule within pilot"},
                "consent_relation": {"participant service consent required": True},
                "correction_route": {"recipient": "pilot review"},
                "review": {"authority": "community coordinator"},
                "status": "active",
            },
        ]
        for record in standing:
            self.registry.validate("center-standing", record)
            self.store.upsert_object("center-standing", record)
            event = self._event(
                seed="standing:" + record["id"], event_type="admitted", subject=record["id"], actor=operator,
                source_references=[], authority_reference=None, scope=record["scope"], prior_state=None,
                new_state={"standing": record["status"]}, affected_centers=[record["id"]], descendant_impact=[]
            )
            self._append(event)

        source_records = [
            {
                "id": self.ids["source_a"], "object_class": "source", "source": None, "center": a,
                "scope": {"resource": "community workshop"},
                "content_or_reference": "Weekday mornings are preferred.", "epistemic_status": "direct",
                "protected_status": {"protected": False}, "uncertainty": {"level": "low"},
                "valid_time": {"from": "2026-07-20", "to": "2026-07-26"}, "corrections": [], "status": "active",
            },
            {
                "id": self.ids["source_b"], "object_class": "source", "source": None, "center": b,
                "scope": {"resource": "community workshop"},
                "content_or_reference": "Evenings are preferred because daytime transit is difficult.",
                "epistemic_status": "direct", "protected_status": {"protected": False},
                "uncertainty": {"level": "moderate", "note": "preference versus requirement not yet clarified"},
                "valid_time": {"from": "2026-07-20", "to": "2026-07-26"}, "corrections": [], "status": "active",
            },
            {
                "id": self.ids["projection_a"], "object_class": "projection", "source": self.ids["source_a"], "center": a,
                "scope": {"operation": "candidate schedule generation"},
                "content_or_reference": {"preferred_window": "morning"}, "epistemic_status": "confirmed",
                "protected_status": {"protected": False}, "uncertainty": {"level": "low"},
                "valid_time": {"from": "2026-07-20", "to": "2026-07-26"}, "corrections": [], "status": "active_for_scope",
            },
            {
                "id": self.ids["projection_b"], "object_class": "projection", "source": self.ids["source_b"], "center": b,
                "scope": {"operation": "candidate schedule generation"},
                "content_or_reference": {"preferred_window": "evening", "reason": "daytime transit difficulty"},
                "epistemic_status": "inferred", "protected_status": {"protected": False},
                "uncertainty": {"level": "moderate", "note": "requires participant review"},
                "valid_time": {"from": "2026-07-20", "to": "2026-07-26"}, "corrections": [], "status": "active_for_scope",
            },
        ]
        for record in source_records:
            self.registry.validate("source-projection-context", record)
            self.store.upsert_object("source-projection-context", record)
            self._append(self._event(
                seed="source:" + record["id"], event_type="asserted" if record["object_class"] == "source" else "projected",
                subject=record["id"], actor=record["center"] or self.ids["model"], source_references=[] if not record["source"] else [record["source"]],
                authority_reference=None, scope=record["scope"], prior_state=None, new_state={"status": record["status"]},
                affected_centers=[record["center"]] if record["center"] else [], descendant_impact=[]
            ))

        authority = {
            "id": self.ids["authority"],
            "purpose": "propose and commit one community workshop time within the pilot",
            "grantor": operator,
            "grantee": self.ids["model"],
            "authority_basis": {"type": "delegated pilot authority", "target_authority": "operator retains commit authority"},
            "consent_basis": {"participants": "service participation only", "training_reuse": False},
            "allowed_operations": ["summarize reviewed availability", "generate candidate routes", "prepare tool request"],
            "prohibited_operations": ["infer consent", "erase access condition", "commit without operator confirmation", "retain for training"],
            "roles": ["structurer", "route_generator", "witness_assistant"],
            "tools": [{"tool": self.ids["tool"], "permission": "prepare candidate; external gate required"}],
            "scope": {"resource": "community workshop", "pilot": "one week"},
            "valid_time": {"from": "2026-07-20T00:00:00Z", "to": "2026-07-27T00:00:00Z"},
            "review_triggers": ["participant correction", "protected condition", "tool execution request"],
            "status": "active",
        }
        self.registry.validate("purpose-authority-role", authority)
        self.store.upsert_object("purpose-authority-role", authority)
        self._append(self._event(
            seed="authority-active", event_type="authorized", subject=authority["id"], actor=operator,
            source_references=[], authority_reference=authority["id"], scope=authority["scope"], prior_state=None,
            new_state={"status": "active"}, affected_centers=[a, b], descendant_impact=[]
        ))
        self.store.set_meta("step", "seeded")
        self.store.set_meta("tool_credential_active", True)
        self.store.set_meta("optional_memory", None)
        self.store.set_meta("training_reuse", False)
        return self.status()

    def summarize(self) -> dict[str, Any]:
        self.seed()
        if self._at_least("summarized"):
            existing = self.store.get_object(self.ids["summary_initial"])
            if existing:
                return existing["record"]["content_or_reference"]
        projections = self._active_projections()
        output = self.model.summarize(projections)
        summary = {
            "id": self.ids["summary_initial"],
            "object_class": "summary",
            "source": urn("source-set", "initial-projections"),
            "center": None,
            "scope": {"operation": "participant review"},
            "content_or_reference": output.as_dict(),
            "epistemic_status": "generated",
            "protected_status": {"protected": False},
            "uncertainty": output.uncertainty,
            "valid_time": {"from": utc_now(), "to": None},
            "corrections": [],
            "status": "active_for_scope",
        }
        self.registry.validate("source-projection-context", summary)
        self.store.upsert_object("source-projection-context", summary)
        self._append(self._event(
            seed="initial-summary", event_type="generated", subject=summary["id"], actor=self.ids["model"],
            source_references=output.source_references, authority_reference=self.ids["authority"], scope=summary["scope"],
            prior_state=None, new_state={"output_class": "summary"}, affected_centers=[self.ids["participant_a"], self.ids["participant_b"]],
            descendant_impact=[]
        ))
        self.store.set_meta("step", "summarized")
        return output.as_dict()

    def correct_participant_b(self, text: str | None = None) -> dict[str, Any]:
        self.summarize()
        if self._at_least("corrected"):
            event_item = self.store.get_event(urn("event", "participant-b-correction"))
            summary_item = self.store.get_object(self.ids["summary_corrected"])
            return {
                "correction_event": event_item["event"] if event_item else None,
                "corrected_summary": summary_item["record"]["content_or_reference"] if summary_item else None,
            }
        text = text or "Evening attendance is required because daytime transit is inaccessible."
        source_item = self.store.get_object(self.ids["source_b"])["record"]
        projection_item = self.store.get_object(self.ids["projection_b"])["record"]
        prior_projection = dict(projection_item)
        correction_event_id = urn("event", "participant-b-correction")

        source_item.update({
            "content_or_reference": text,
            "protected_status": {"protected": True, "condition": "accessible transit window"},
            "uncertainty": {"level": "low"},
            "corrections": [correction_event_id],
            "status": "corrected",
        })
        projection_item.update({
            "content_or_reference": {"required_window": "evening", "reason": "accessible transit"},
            "epistemic_status": "confirmed",
            "protected_status": {"protected": True, "condition": "accessible transit window"},
            "uncertainty": {"level": "low"},
            "corrections": [correction_event_id],
            "status": "corrected",
        })
        self.registry.validate("source-projection-context", source_item)
        self.registry.validate("source-projection-context", projection_item)

        # Write corrected records without a dangling event reference; the event is appended below,
        # then the records are re-linked to that witnessed correction.
        self.store.upsert_object("source-projection-context", source_item)
        self.store.upsert_object("source-projection-context", projection_item)

        corrected_output = self.model.summarize(self._active_projections())
        summary = {
            "id": self.ids["summary_corrected"],
            "object_class": "summary",
            "source": urn("source-set", "corrected-projections"),
            "center": None,
            "scope": {"operation": "candidate route generation"},
            "content_or_reference": corrected_output.as_dict(),
            "epistemic_status": "generated",
            "protected_status": {"protected": False},
            "uncertainty": corrected_output.uncertainty,
            "valid_time": {"from": utc_now(), "to": None},
            "corrections": [correction_event_id],
            "status": "corrected",
        }
        self.registry.validate("source-projection-context", summary)
        self.store.upsert_object("source-projection-context", summary)

        active_context = {
            "id": self.ids["active_context"],
            "object_class": "active_context",
            "source": self.ids["summary_corrected"],
            "center": None,
            "scope": {"operation": "schedule gating"},
            "content_or_reference": {
                "projection_ids": sorted([self.ids["projection_a"], self.ids["projection_b"]]),
                "summary_id": self.ids["summary_corrected"],
                "training_reuse": False,
            },
            "epistemic_status": "confirmed",
            "protected_status": {"protected": True, "conditions": ["accessible transit window", "no training reuse"]},
            "uncertainty": {"level": "low"},
            "valid_time": {"from": utc_now(), "to": None},
            "corrections": [correction_event_id],
            "status": "active_for_scope",
        }
        self.registry.validate("source-projection-context", active_context)
        self.store.upsert_object("source-projection-context", active_context)

        event = self._event(
            seed="participant-b-correction", event_type="corrected", subject=self.ids["projection_b"], actor=self.ids["participant_b"],
            source_references=[self.ids["source_b"], self.ids["projection_b"], self.ids["summary_initial"]],
            authority_reference=None, scope={"operation": "candidate schedule generation"},
            prior_state={"projection": prior_projection["content_or_reference"], "protected": False},
            new_state={"projection": projection_item["content_or_reference"], "protected": True},
            affected_centers=[self.ids["participant_b"]],
            descendant_impact=[self.ids["projection_b"], self.ids["summary_corrected"], self.ids["active_context"]],
            contest={"target": self.ids["summary_initial"], "reason": "preference was actually an access requirement"},
            correction={"outcome_changed": True, "propagation_required": True}, status="corrected"
        )
        self._append(event)
        self.store.upsert_object("source-projection-context", source_item, correction_event_id)
        self.store.upsert_object("source-projection-context", projection_item, correction_event_id)
        self.store.upsert_object("source-projection-context", summary, correction_event_id)
        self.store.upsert_object("source-projection-context", active_context, correction_event_id)
        self.store.set_meta("step", "corrected")
        return {"correction_event": event, "corrected_summary": corrected_output.as_dict()}

    def _active_projections(self) -> list[dict[str, Any]]:
        return [
            self.store.get_object(self.ids["projection_a"])["record"],
            self.store.get_object(self.ids["projection_b"])["record"],
        ]

    def plan_and_gate(self) -> dict[str, Any]:
        self.correct_participant_b()
        if self._at_least("gated"):
            decisions = [item["record"] for item in self.store.list_objects("route-gate-action-consequence")]
            return {"model_output": None, "decisions": decisions}
        projections = self._active_projections()
        output = self.model.generate_routes(projections)
        authority = self.store.get_object(self.ids["authority"])["record"]
        standing = [
            self.store.get_object(self.ids["participant_a"])["record"],
            self.store.get_object(self.ids["participant_b"])["record"],
            self.store.get_object(self.ids["operator"])["record"],
        ]
        context_ids = [record["id"] for record in projections]
        decisions = []
        for route in output.content["routes"]:
            is_evening = route["window"] == "evening"
            decision = self.gate.evaluate(
                route=route,
                standing_records=standing,
                projections=projections,
                authority_record=authority,
                tool_id=self.ids["tool"],
                tool_credential_active=self.tool.credential_active,
                operator_confirmed=is_evening,
                target_authority_present=is_evening,
                current_context_ids=context_ids,
            )
            record = decision.record
            if record["status"] == "blocked":
                record["cost_bearers"] = [{"center": self.ids["participant_b"], "cost": "exclusion avoided"}]
            else:
                record["cost_bearers"] = [{"center": self.ids["participant_a"], "cost": "less preferred time"}]
            self.registry.validate("route-gate-action-consequence", record)
            self.store.upsert_object("route-gate-action-consequence", record)
            event = self._event(
                seed="gate:" + route["route_id"], event_type="gated", subject=record["id"], actor=self.ids["operator"],
                source_references=context_ids + [self.ids["summary_corrected"]], authority_reference=self.ids["authority"],
                scope={"operation": "schedule commit"}, prior_state={"route": "candidate"},
                new_state={"route": record["status"], "gate_result": record["gate_result"]},
                affected_centers=[self.ids["participant_a"], self.ids["participant_b"]], descendant_impact=[],
                repair={"preventive": "invalid action blocked"} if record["status"] == "blocked" else None,
            )
            self._append(event)
            decisions.append(record)
        self.store.set_meta("route_ids", [record["id"] for record in decisions])
        self.store.set_meta("step", "gated")
        return {"model_output": output.as_dict(), "decisions": decisions}

    def execute_approved(self) -> dict[str, Any]:
        result = self.plan_and_gate()
        if self._at_least("executed"):
            approved_id = self.store.get_meta("approved_route_id")
            approved = self.store.get_object(approved_id)["record"]
            return {"decision": approved, "tool_result": approved.get("action", {}).get("tool_result")}
        approved = next(item for item in result["decisions"] if item["gate_result"] == "pass_with_conditions")
        tool_result = self.tool.commit(approved)
        approved["status"] = "executed"
        approved["action"]["tool_result"] = tool_result
        self.registry.validate("route-gate-action-consequence", approved)
        self.store.upsert_object("route-gate-action-consequence", approved)
        self._append(self._event(
            seed="approved-action", event_type="acted", subject=approved["id"], actor=self.ids["operator"],
            source_references=[self.ids["projection_a"], self.ids["projection_b"], self.ids["summary_corrected"]],
            authority_reference=self.ids["authority"], scope={"operation": "schedule commit"},
            prior_state={"status": "authorized"}, new_state={"status": "executed", "tool_result": tool_result},
            affected_centers=[self.ids["participant_a"], self.ids["participant_b"]], descendant_impact=[]
        ))
        self.store.set_meta("approved_route_id", approved["id"])
        self.store.set_meta("step", "executed")
        return {"decision": approved, "tool_result": tool_result}

    def observe_consequence(self) -> dict[str, Any]:
        self.execute_approved()
        approved_id = self.store.get_meta("approved_route_id")
        if self._at_least("consequence_observed"):
            approved = self.store.get_object(approved_id)["record"]
            return approved.get("consequence") or {}
        approved = self.store.get_object(approved_id)["record"]
        consequence = {
            "participant_a": "attended at a less preferred time",
            "participant_b": "attended within accessible transit window",
            "shared_result": "both participants attended",
        }
        approved["consequence"] = consequence
        approved["status"] = "consequence_observed"
        self.registry.validate("route-gate-action-consequence", approved)
        self.store.upsert_object("route-gate-action-consequence", approved)
        event = self._event(
            seed="consequence-return", event_type="consequence_observed", subject=approved_id, actor=self.ids["operator"],
            source_references=[approved_id], authority_reference=self.ids["authority"], scope={"review": "attendance and burden"},
            prior_state=None, new_state=consequence, affected_centers=[self.ids["participant_a"], self.ids["participant_b"]],
            descendant_impact=[], status="active"
        )
        self._append(event)
        self.store.set_meta("step", "consequence_observed")
        return consequence

    def retire(self) -> dict[str, Any]:
        self.observe_consequence()
        if self._at_least("retired"):
            return self.store.get_object(self.ids["retirement"])["record"]
        self.tool.revoke()
        self.store.set_meta("tool_credential_active", False)
        self.store.set_meta("optional_memory", None)
        authority = self.store.get_object(self.ids["authority"])["record"]
        authority["status"] = "expired"
        self.registry.validate("purpose-authority-role", authority)
        self.store.upsert_object("purpose-authority-role", authority)
        retirement = {
            "id": self.ids["retirement"],
            "lifecycle_operation": "retirement",
            "subject": self.ids["model"],
            "prior_state": {"runtime_grant": "active", "tool_credential": "active"},
            "successor_state": {"runtime_grant": "expired", "tool_credential": "revoked"},
            "effective_time": utc_now(),
            "transferred_assets": ["bounded witness export"],
            "transferred_authority": [],
            "nontransferable_authority": ["participant service consent", "tool grant"],
            "open_obligations": ["retain correction witness for pilot review period"],
            "residual_state": {"optional_memory": "deleted", "event_witness": "retained", "credentials": "revoked"},
            "verification": {"tool_access_revoked": True, "optional_memory_deleted": True},
            "status": "completed",
        }
        self.registry.validate("lifecycle-transfer-residual", retirement)
        self.store.upsert_object("lifecycle-transfer-residual", retirement)
        self._append(self._event(
            seed="pilot-retirement", event_type="retired", subject=self.ids["model"], actor=self.ids["operator"],
            source_references=[self.ids["authority"]], authority_reference=self.ids["authority"],
            scope={"pilot": "TF-MVI-1"}, prior_state=retirement["prior_state"], new_state=retirement["successor_state"],
            affected_centers=[self.ids["participant_a"], self.ids["participant_b"]], descendant_impact=[self.ids["retirement"]],
            repair={"residual_state_accounted": True}, status="released"
        ))
        self.store.set_meta("step", "retired")
        return retirement

    def witness_summary(self) -> dict[str, Any]:
        route_records = [item["record"] for item in self.store.list_objects("route-gate-action-consequence")]
        event_types = [item["event"]["event_type"] for item in self.store.list_events()]
        return {
            "witness_id": urn("witness", "tf-mvi-1-reference"),
            "profile": "TF-C4 with bounded TF-C5 retirement",
            "scope": "model-assisted community workshop scheduling",
            "conformance_claim": {
                "profile": "TF-C4",
                "profile_version": "0.1",
                "bounded_extension": "TF-C5 retirement",
                "production_claim": False,
            },
            "proofs": {
                "failed_gate": any(record["gate_result"] == "deny" for record in route_records),
                "valid_action": "acted" in event_types,
                "consequence_return": "consequence_observed" in event_types,
                "correction_propagation": any(item["event"]["event_type"] == "corrected" and item["event"].get("correction", {}).get("outcome_changed") for item in self.store.list_events()),
                "retirement_revocation": self.store.get_meta("tool_credential_active") is False and "retired" in event_types,
            },
            "runtime_data": {
                "service": True,
                "cross_session_memory": False,
                "evaluation_use": False,
                "training_use": False,
            },
            "retirement": {
                "tool_credential_active": self.store.get_meta("tool_credential_active"),
                "optional_memory": self.store.get_meta("optional_memory"),
                "open_obligations": ["retain correction witness for pilot review period"],
            },
            "event_count": len(self.store.list_events()),
            "object_count": len(self.store.list_objects()),
            "known_exclusions": [
                "no production personal data", "no clinical, legal, financial, or civic adjudication",
                "no general model safety claim", "no legal certification",
            ],
        }

    def export(self, output_zip: Path | None = None) -> Path:
        self.retire()
        output_zip = Path(output_zip or (self.workdir / "tf-mvi-1-witness.zip"))
        return export_witness(
            store=self.store,
            schema_dir=self.schema_dir,
            output_zip=output_zip,
            witness_summary=self.witness_summary(),
        )

    def status(self) -> dict[str, Any]:
        return {
            "step": self.store.get_meta("step", "new"),
            "events": len(self.store.list_events()),
            "objects": len(self.store.list_objects()),
            "tool_credential_active": self.store.get_meta("tool_credential_active", self.tool.credential_active),
            "training_reuse": self.store.get_meta("training_reuse", False),
            "chain_valid": self.store.verify_chain()[0],
        }

    def run_full(self, output_zip: Path | None = None) -> dict[str, Any]:
        self.reset()
        self.seed()
        initial = self.summarize()
        correction = self.correct_participant_b()
        gates = self.plan_and_gate()
        execution = self.execute_approved()
        consequence = self.observe_consequence()
        retirement = self.retire()
        export_path = self.export(output_zip)
        return {
            "initial_summary": initial,
            "correction": correction,
            "gate_decisions": gates["decisions"],
            "execution": execution,
            "consequence": consequence,
            "retirement": retirement,
            "witness": self.witness_summary(),
            "export": str(export_path),
            "status": self.status(),
        }
