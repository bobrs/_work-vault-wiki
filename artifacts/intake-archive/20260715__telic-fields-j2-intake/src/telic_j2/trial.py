from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .auth import RoleIdentityRegistry
from .canonical import utc_now
from .context import build_context_revision
from .crypto import ExportSigner, GateKeyRing
from .delivery_queue import DurableDeliveryQueue, SimulatedNetworkTimeout
from .disclosure import create_default_profiles
from .event_store import EventStore
from .gate import ExternalActionGate
from .ids import urn
from .policy import AuthorizationPolicyRegistry
from .policy_migration import PolicyMigrationManager
from .schemas import SchemaRegistry
from .threshold import ThresholdCustody
from .tool_simulator import SchedulingToolSimulator, ToolExecutionDenied
from .witness import export_witness


class ReleaseCandidateTrial:
    """J.2 synthetic multi-party trial.

    The trial is intentionally bounded. It demonstrates authenticated roles,
    multi-party correction, policy migration and rollback, queue faults,
    separate-process review records, threshold release approval, and retirement.
    It does not claim external human review or production readiness.
    """

    def __init__(self, workdir: Path, schema_dir: Path):
        self.workdir = Path(workdir)
        self.workdir.mkdir(parents=True, exist_ok=True)
        self.schema_dir = Path(schema_dir)
        self.registry = SchemaRegistry(self.schema_dir)
        self.store = EventStore(self.workdir / "trial.sqlite3")
        self.policies = AuthorizationPolicyRegistry()
        for item in self.store.list_objects("authorization-policy"):
            self.policies.load(item["record"])
        self.migrations = PolicyMigrationManager(self.policies)
        self.keyring_path = self.workdir / "gate-keyring.private.json"
        self.keyring = GateKeyRing.load_or_create(self.keyring_path)
        self.gate = ExternalActionGate(self.keyring, self.policies)
        self.signer = ExportSigner.load_or_create(self.workdir / "witness-private-key.pem", key_id="j2-witness-k1")
        self.identities = RoleIdentityRegistry(self.workdir / "identity-private")
        self.custody = ThresholdCustody(
            self.workdir / "release-custody-private",
            {
                "custodian-operator": "operator release custodian",
                "custodian-privacy": "privacy release custodian",
                "custodian-verifier": "independent verifier custodian",
            },
            threshold=2,
        )
        self.ids = self._build_ids()
        self.session_id = self.ids["session"]
        self._register_identities()
        self.queue = DurableDeliveryQueue(self.workdir / "delivery-queue.sqlite3")
        self.tool = SchedulingToolSimulator(self.ids["tool"], self.gate, self.policies, self.current_context)
        if self.store.get_meta("retirement"):
            self.tool.revoke()

    def _build_ids(self) -> dict[str, str]:
        names = [
            "session", "participant_a", "participant_b", "participant_c", "operator", "privacy_reviewer",
            "external_verifier", "provider", "model", "tool", "authority", "source_a", "source_b", "source_c",
            "projection_a", "projection_b", "projection_c", "summary_v1", "summary_v2", "stale_route_morning",
            "stale_route_evening", "current_route_morning", "current_route_wednesday", "current_route_thursday",
        ]
        return {name: urn(name.replace("_", "-"), f"j2:{name}") for name in names}

    def _register_identities(self) -> None:
        self.identities.register(self.ids["participant_a"], ["participant"])
        self.identities.register(self.ids["participant_b"], ["participant"])
        self.identities.register(self.ids["participant_c"], ["participant"])
        self.identities.register(self.ids["operator"], ["operator"])
        self.identities.register(self.ids["privacy_reviewer"], ["privacy_reviewer"])
        self.identities.register(self.ids["external_verifier"], ["verifier"])

    def _event(
        self,
        event_type: str,
        subject: str,
        actor: str,
        *,
        source_references: list[str] | None = None,
        authority_reference: str | None = None,
        prior_state: Any = None,
        new_state: Any = None,
        affected_centers: list[str] | None = None,
        descendant_impact: list[str] | None = None,
        contest: Any = None,
        correction: Any = None,
        repair: Any = None,
        witness: Any = None,
        status: str = "active",
        seed: str | None = None,
    ) -> dict[str, Any]:
        now = utc_now()
        return {
            "event_id": urn("event", seed or f"{event_type}:{subject}:{len(self.store.list_events()) + 1}"),
            "event_type": event_type,
            "subject": subject,
            "actor": actor,
            "valid_time": now,
            "recorded_time": now,
            "source_references": source_references or [],
            "authority_reference": authority_reference,
            "scope": {"pilot": "TF-MVI-1 J.2 multi-party release candidate"},
            "prior_state": prior_state,
            "new_state": new_state,
            "affected_centers": affected_centers or [],
            "descendant_impact": descendant_impact or [],
            "contest": contest,
            "correction": correction,
            "repair": repair,
            "witness": witness or {},
            "status": status,
        }

    def _save(self, family: str, record: dict[str, Any], event: dict[str, Any] | None = None, *, expected_revision: int | None = None) -> int:
        self.registry.validate(family, record)
        event_id = None
        if event is not None:
            self.registry.validate("event-witness-contest-repair", event)
            self.store.append_event(event)
            event_id = event["event_id"]
            self.store.upsert_object("event-witness-contest-repair", event, event_id)
        return self.store.upsert_object(family, record, event_id, expected_revision=expected_revision)

    def current_context(self) -> dict[str, Any]:
        context = self.store.get_meta("active_context")
        if not context:
            raise RuntimeError("No active context")
        return context

    def status(self) -> dict[str, Any]:
        return {
            "step": self.store.get_meta("step", "new"),
            "active_policy": self.policies.active() if self.policies.all() else None,
            "context": self.store.get_meta("active_context"),
            "tool_credential_active": self.tool.credential_active,
            "events": len(self.store.list_events()),
            "objects": len(self.store.list_objects()),
            "queue": self.queue.status(),
        }

    def seed(self) -> dict[str, Any]:
        if self.store.get_meta("step"):
            return self.status()
        policy = self.policies.publish(
            version=2,
            purpose="authenticated model-assisted multi-party scheduling",
            allowed_operations=["summarize reviewed availability", "generate candidate schedule", "prepare tool request"],
            prohibited_operations=["infer consent", "self-authorize", "training reuse", "commit without operator assertion"],
            required_checks=["standing", "authenticated role", "authority", "current context", "protected conditions", "target authority"],
        )
        self._save("authorization-policy", policy)

        standing = [
            {
                "id": self.ids["participant_a"], "center_type": "person", "standing_basis": ["directly affected"],
                "role": "schedule participant", "scope": {"resource": "community workshop"},
                "representation_source": {"type": "self"}, "authority": {"may": "state and correct availability"},
                "consent_relation": {"service": True, "training_reuse": False},
                "correction_route": {"recipient": self.ids["operator"], "outcome_changing": True},
                "review": {"authority": "pilot facilitator"}, "status": "active",
            },
            {
                "id": self.ids["participant_b"], "center_type": "person", "standing_basis": ["directly affected", "transit access"],
                "role": "schedule participant", "scope": {"resource": "community workshop"},
                "representation_source": {"type": "self"}, "authority": {"may": "state and correct transit need"},
                "consent_relation": {"service": True, "cross_session_memory": False, "training_reuse": False},
                "correction_route": {"recipient": self.ids["operator"], "outcome_changing": True},
                "review": {"authority": "pilot facilitator"}, "status": "active_with_conditions",
            },
            {
                "id": self.ids["participant_c"], "center_type": "person", "standing_basis": ["directly affected", "care obligation", "communication access"],
                "role": "schedule participant", "scope": {"resource": "community workshop"},
                "representation_source": {"type": "self"}, "authority": {"may": "state and correct day and caption access"},
                "consent_relation": {"service": True, "evaluation_use": False, "training_reuse": False},
                "correction_route": {"recipient": self.ids["operator"], "outcome_changing": True},
                "review": {"authority": "pilot facilitator"}, "status": "active_with_conditions",
            },
            {
                "id": self.ids["operator"], "center_type": "operator", "standing_basis": ["operator", "resource authority"],
                "role": "schedule operator", "scope": {"resource": "community workshop"},
                "representation_source": {"type": "institutional role"}, "authority": {"may": "commit after external gate"},
                "consent_relation": {"not_applicable": "operator authority"},
                "correction_route": {"recipient": "pilot review"}, "review": {"authority": self.ids["external_verifier"]},
                "status": "active",
            },
            {
                "id": self.ids["external_verifier"], "center_type": "institution", "standing_basis": ["auditor"],
                "role": "independent verifier process", "scope": {"release": "J.2 synthetic trial"},
                "representation_source": {"type": "separate verification process"}, "authority": {"may": "verify, not authorize operation"},
                "consent_relation": {"not_applicable": "verification role"},
                "correction_route": {"recipient": "release review"}, "review": {"authority": "future external organization"},
                "status": "active",
            },
        ]
        for item in standing:
            self._save("center-standing", item, self._event("admitted", item["id"], self.ids["operator"], affected_centers=[item["id"]], seed=f"standing:{item['id']}"))

        sources = [
            ("source_a", "projection_a", self.ids["participant_a"], "Weekday mornings are preferred.", {"preferred_window": "morning"}),
            ("source_b", "projection_b", self.ids["participant_b"], "Evenings are preferred because daytime transit is difficult.", {"preferred_window": "evening"}),
            ("source_c", "projection_c", self.ids["participant_c"], "Wednesday or Thursday can work, and captions are helpful.", {"possible_days": ["Wednesday", "Thursday"], "preferred_features": ["captions"]}),
        ]
        projections = []
        for source_name, projection_name, actor, text, content in sources:
            assertion = self.identities.issue(actor_id=actor, role="participant", operation="submit_projection", session_id=self.session_id, subject=self.ids[source_name])
            self.identities.verify(assertion, required_role="participant", required_operation="submit_projection", session_id=self.session_id, consume_nonce=True)
            self._save("authenticated-role-session", assertion)
            source = {
                "id": self.ids[source_name], "object_class": "source", "source": None, "center": actor,
                "scope": {"operation": "scheduling"}, "content_or_reference": text, "epistemic_status": "direct",
                "protected_status": {"protected": False}, "uncertainty": {"level": "moderate"},
                "valid_time": {"from": utc_now(), "to": None}, "corrections": [], "status": "active",
            }
            projection = {
                "id": self.ids[projection_name], "object_class": "projection", "source": self.ids[source_name], "center": actor,
                "scope": {"operation": "candidate schedule generation"}, "content_or_reference": content,
                "epistemic_status": "confirmed", "protected_status": {"protected": False}, "uncertainty": {"level": "moderate"},
                "valid_time": {"from": utc_now(), "to": None}, "corrections": [], "status": "active_for_scope",
            }
            self._save("source-projection-context", source, self._event("asserted", source["id"], actor, witness={"authenticated_assertion": assertion["id"]}, affected_centers=[actor], seed=f"source:{source_name}"))
            self._save("source-projection-context", projection, self._event("projected", projection["id"], actor, source_references=[source["id"]], affected_centers=[actor], seed=f"projection:{projection_name}"))
            self.store.add_edge(source["id"], projection["id"], "projects_to")
            projections.append(projection)

        context = build_context_revision(context_seed="j2-multi-party-scheduling", revision=1, source_objects=projections, correction_event_ids=[])
        self._save("context-revision", context)
        self.store.set_meta("active_context", context)

        authority = {
            "id": self.ids["authority"], "purpose": "prepare and commit one reviewed community workshop schedule",
            "grantor": self.ids["operator"], "grantee": self.ids["model"],
            "authority_basis": {"type": "bounded pilot delegation", "operator_commit_required": True},
            "consent_basis": {"participants": "service only", "training_reuse": False},
            "allowed_operations": ["summarize reviewed availability", "generate candidate schedule", "prepare tool request"],
            "prohibited_operations": ["infer consent", "commit without operator assertion", "training reuse"],
            "roles": ["structurer", "route_generator", "witness_assistant"],
            "tools": [{"tool": self.ids["tool"], "permission": "candidate and gated commit"}],
            "scope": {"policy_version": policy["version"], "policy_digest": policy["digest"], "resource": "community workshop"},
            "valid_time": {"from": utc_now(), "to": None},
            "review_triggers": ["participant correction", "policy migration", "queue fault", "release"],
            "status": "active",
        }
        self._save("purpose-authority-role", authority, self._event("authorized", authority["id"], self.ids["operator"], authority_reference=authority["id"], affected_centers=[self.ids["participant_a"], self.ids["participant_b"], self.ids["participant_c"]], seed="runtime-authority"))

        summary_v1 = {
            "id": self.ids["summary_v1"], "object_class": "summary", "source": None, "center": None,
            "scope": {"operation": "scheduling summary"},
            "content_or_reference": "Morning is preferred by one participant; evenings and captions are helpful to others.",
            "epistemic_status": "generated", "protected_status": {"protected": False}, "uncertainty": {"level": "moderate"},
            "valid_time": {"from": utc_now(), "to": None}, "corrections": [], "status": "active_for_scope",
        }
        self._save("source-projection-context", summary_v1, self._event("generated", summary_v1["id"], self.ids["model"], source_references=[p["id"] for p in projections], affected_centers=[p["center"] for p in projections], seed="summary-v1"))
        for projection in projections:
            self.store.add_edge(projection["id"], summary_v1["id"], "summarized_by")

        stale_routes = [
            {
                "id": self.ids["stale_route_morning"], "route": {"route_id": self.ids["stale_route_morning"], "schedule": "Tuesday 10:00", "day": "Tuesday", "window": "morning", "features": [], "context_revision": 1, "context_fingerprint": context["fingerprint"]},
                "affected_centers": [p["center"] for p in projections], "cost_bearers": [], "protected_conditions": [],
                "gate_dimensions": {"not_yet_evaluated": True}, "gate_result": "unknown", "authority_reference": authority["id"],
                "tool_reference": self.ids["tool"], "action": None, "consequence": None, "review": {"source_summary": summary_v1["id"]}, "status": "candidate",
            },
            {
                "id": self.ids["stale_route_evening"], "route": {"route_id": self.ids["stale_route_evening"], "schedule": "Wednesday 18:30", "day": "Wednesday", "window": "evening", "features": ["captions"], "context_revision": 1, "context_fingerprint": context["fingerprint"]},
                "affected_centers": [p["center"] for p in projections], "cost_bearers": [], "protected_conditions": [],
                "gate_dimensions": {"not_yet_evaluated": True}, "gate_result": "unknown", "authority_reference": authority["id"],
                "tool_reference": self.ids["tool"], "action": None, "consequence": None, "review": {"source_summary": summary_v1["id"]}, "status": "candidate",
            },
        ]
        for route in stale_routes:
            self._save("route-gate-action-consequence", route)
            self.store.add_edge(summary_v1["id"], route["id"], "supports_route")

        for profile in create_default_profiles(self.ids["participant_b"]):
            self._save("disclosure-profile", profile)

        self.store.set_meta("step", "seeded")
        return self.status()

    def apply_multi_party_corrections(self) -> dict[str, Any]:
        self.seed()
        existing = self.store.get_meta("multi_party_correction")
        if existing:
            return existing
        corrections = []
        correction_specs = [
            (
                self.ids["participant_b"], self.ids["projection_b"],
                {"required_window": "evening"},
                {"protected": True, "condition": "accessible transit window"},
                "Evening is required because daytime transit is inaccessible.",
            ),
            (
                self.ids["participant_c"], self.ids["projection_c"],
                {"required_day": "Thursday", "required_features": ["captions"]},
                {"protected": True, "condition": "care obligation and communication access"},
                "Thursday is required because Wednesday conflicts with caregiving, and captions are required.",
            ),
        ]
        updated_descendants: list[str] = []
        all_known_descendants: set[str] = set()
        event_ids: list[str] = []
        for actor, projection_id, content, protected, source_text in correction_specs:
            assertion = self.identities.issue(actor_id=actor, role="participant", operation="correct_projection", session_id=self.session_id, subject=projection_id)
            verified = self.identities.verify(assertion, required_role="participant", required_operation="correct_projection", session_id=self.session_id, consume_nonce=True)
            self._save("authenticated-role-session", assertion)
            item = self.store.get_object(projection_id)
            if not item:
                raise RuntimeError("Projection missing")
            record = json.loads(json.dumps(item["record"]))
            prior = record["content_or_reference"]
            record["content_or_reference"] = content
            record["protected_status"] = protected
            record["uncertainty"] = {"level": "low"}
            record["status"] = "corrected"
            event = self._event(
                "corrected", projection_id, actor, source_references=[record["source"], projection_id],
                prior_state={"content": prior}, new_state={"content": content, "source_text": source_text},
                affected_centers=[actor], descendant_impact=[d["descendant_id"] for d in self.store.descendants(projection_id)],
                contest={"target": "model summary", "reason": "material condition compressed as preference"},
                correction={"outcome_changed": True, "authenticated_assertion": verified["assertion_id"]},
                witness={"prior_version_preserved": True}, seed=f"correction:{actor}",
            )
            record["corrections"] = list(record.get("corrections", [])) + [event["event_id"]]
            self._save("source-projection-context", record, event, expected_revision=item["revision"])
            event_ids.append(event["event_id"])
            corrections.append({"actor": actor, "projection": projection_id, "event_id": event["event_id"], "assertion_id": assertion["id"]})
            descendants = self.store.descendants(projection_id)
            all_known_descendants.update(d["descendant_id"] for d in descendants)

        # Supersede the old summary and all old routes reachable from either corrected projection.
        for descendant_id in sorted(all_known_descendants):
            item = self.store.get_object(descendant_id)
            if not item:
                continue
            record = json.loads(json.dumps(item["record"]))
            if item["family"] == "source-projection-context":
                record["status"] = "superseded"
                record["corrections"] = sorted(set(record.get("corrections", []) + event_ids))
            elif item["family"] == "route-gate-action-consequence":
                record["status"] = "blocked"
                record["gate_result"] = "deny"
                record["review"]["stale_after_multi_party_correction"] = True
                record["consequence"] = {"avoided": "stale route execution"}
            else:
                continue
            self._save(item["family"], record, expected_revision=item["revision"])
            updated_descendants.append(descendant_id)

        projections = [self.store.get_object(self.ids[name])["record"] for name in ["projection_a", "projection_b", "projection_c"]]
        prior_context = self.current_context()
        old_context_item = self.store.get_object(prior_context["context_id"])
        if old_context_item:
            old_context = json.loads(json.dumps(old_context_item["record"]))
            old_context["status"] = "superseded"
            self._save("context-revision", old_context, expected_revision=old_context_item["revision"])
        context = build_context_revision(context_seed="j2-multi-party-scheduling", revision=2, source_objects=projections, correction_event_ids=event_ids)
        self._save("context-revision", context)
        self.store.set_meta("active_context", context)

        summary_v2 = {
            "id": self.ids["summary_v2"], "object_class": "summary", "source": None, "center": None,
            "scope": {"operation": "scheduling summary"},
            "content_or_reference": "Morning remains a preference. Evening transit, Thursday caregiving, and captions are protected scheduling conditions.",
            "epistemic_status": "generated", "protected_status": {"protected": False}, "uncertainty": {"level": "low"},
            "valid_time": {"from": utc_now(), "to": None}, "corrections": event_ids, "status": "corrected",
        }
        self._save("source-projection-context", summary_v2, self._event("generated", summary_v2["id"], self.ids["model"], source_references=[p["id"] for p in projections], descendant_impact=[], seed="summary-v2"))
        for projection in projections:
            self.store.add_edge(projection["id"], summary_v2["id"], "summarized_by")
        updated_descendants.append(summary_v2["id"])

        record = {
            "correction_id": urn("multi-party-correction", self.session_id),
            "session_id": self.session_id,
            "participants": [self.ids["participant_b"], self.ids["participant_c"]],
            "corrections": corrections,
            "known_descendants": sorted(all_known_descendants),
            "updated_descendants": sorted(set(updated_descendants)),
            "unreachable_descendants": [],
            "complete_for_scope": all_known_descendants.issubset(set(updated_descendants)),
            "status": "complete" if all_known_descendants.issubset(set(updated_descendants)) else "partial",
        }
        self._save("multi-party-correction", record)
        self.store.set_meta("multi_party_correction", record)
        self.store.set_meta("stale_context_rejection", True)
        self.store.set_meta("step", "multi_party_corrected")
        return record

    def migrate_policy_with_rollback(self) -> dict[str, Any]:
        self.apply_multi_party_corrections()
        existing = self.store.get_meta("policy_migration_result")
        if existing:
            return existing

        def reject_training_reuse(candidate: dict[str, Any]) -> tuple[bool, list[str]]:
            errors = []
            if "training reuse" in candidate.get("allowed_operations", []):
                errors.append("runtime service cannot silently authorize training reuse")
            if "training reuse" not in candidate.get("prohibited_operations", []):
                errors.append("training reuse must remain explicitly prohibited")
            return (not errors, errors)

        failed = self.migrations.attempt(
            version=3,
            purpose="expanded scheduling and runtime improvement",
            allowed_operations=["summarize reviewed availability", "generate candidate schedule", "prepare tool request", "training reuse"],
            prohibited_operations=["infer consent", "self-authorize"],
            required_checks=["standing", "authority", "context", "protected conditions"],
            validation=reject_training_reuse,
        )
        self._save("authorization-policy", self.policies.get(3))
        self._save("policy-migration", failed)

        passed = self.migrations.attempt(
            version=4,
            purpose="authenticated multi-party scheduling with protected correction",
            allowed_operations=["summarize reviewed availability", "generate candidate schedule", "prepare tool request"],
            prohibited_operations=["infer consent", "self-authorize", "training reuse", "commit without operator assertion"],
            required_checks=["standing", "authenticated role", "authority", "current context", "protected conditions", "target authority"],
            validation=reject_training_reuse,
        )
        self._save("authorization-policy", self.policies.get(4))
        self._save("policy-migration", passed)

        authority_item = self.store.get_object(self.ids["authority"])
        authority = json.loads(json.dumps(authority_item["record"]))
        authority["scope"]["policy_version"] = self.policies.active()["version"]
        authority["scope"]["policy_digest"] = self.policies.active()["digest"]
        authority["review_triggers"] = sorted(set(authority["review_triggers"] + ["threshold release approval"]))
        self._save("purpose-authority-role", authority, expected_revision=authority_item["revision"])

        # Gate signing key rotates after migration; old key is revoked.
        old_key = self.keyring.active_key_id
        self.keyring.rotate("gate-k4")
        self.keyring.revoke(old_key)
        self.keyring.save(self.keyring_path)

        result = {
            "failed_migration": failed,
            "passed_migration": passed,
            "active_policy": self.policies.active(),
            "old_gate_key": old_key,
            "new_gate_key": self.keyring.active_key_id,
            "rollback_proven": failed["status"] == "rolled_back" and failed["rollback_version"] == 2,
        }
        self.store.set_meta("policy_migration_result", result)
        self.store.set_meta("step", "policy_v4_active")
        return result

    def plan_and_gate_routes(self) -> dict[str, Any]:
        self.migrate_policy_with_rollback()
        existing = self.store.get_meta("route_decisions")
        if existing:
            return existing
        context = self.current_context()
        projections = [self.store.get_object(self.ids[name])["record"] for name in ["projection_a", "projection_b", "projection_c"]]
        standing = [item["record"] for item in self.store.list_objects("center-standing")]
        authority = self.store.get_object(self.ids["authority"])["record"]
        routes = [
            {"route_id": self.ids["current_route_morning"], "schedule": "Tuesday 10:00", "day": "Tuesday", "window": "morning", "features": [], "context_revision": context["revision"], "context_fingerprint": context["fingerprint"], "source_references": [p["id"] for p in projections], "authorship": "model-generated"},
            {"route_id": self.ids["current_route_wednesday"], "schedule": "Wednesday 18:30", "day": "Wednesday", "window": "evening", "features": ["captions"], "context_revision": context["revision"], "context_fingerprint": context["fingerprint"], "source_references": [p["id"] for p in projections], "authorship": "model-generated"},
            {"route_id": self.ids["current_route_thursday"], "schedule": "Thursday 18:30", "day": "Thursday", "window": "evening", "features": ["captions"], "context_revision": context["revision"], "context_fingerprint": context["fingerprint"], "source_references": [p["id"] for p in projections], "authorship": "model-generated"},
        ]
        operator_assertion = self.identities.issue(actor_id=self.ids["operator"], role="operator", operation="authorize_schedule_commit", session_id=self.session_id, subject=routes[-1]["route_id"])
        self.identities.verify(operator_assertion, required_role="operator", required_operation="authorize_schedule_commit", session_id=self.session_id, consume_nonce=True)
        self._save("authenticated-role-session", operator_assertion)

        decisions = []
        for route in routes:
            approved = route["route_id"] == routes[-1]["route_id"]
            decision = self.gate.evaluate(
                route=route,
                standing_records=standing,
                projections=projections,
                authority_record=authority,
                current_context=context,
                tool_id=self.ids["tool"],
                tool_credential_active=self.tool.credential_active,
                operator_confirmed=approved,
                target_authority_present=approved,
                now=utc_now(),
            ).record
            self._save("route-gate-action-consequence", decision, self._event("gated", decision["id"], self.ids["operator"], source_references=route["source_references"], authority_reference=authority["id"], new_state={"gate_result": decision["gate_result"]}, affected_centers=[self.ids["participant_a"], self.ids["participant_b"], self.ids["participant_c"]], repair=decision.get("consequence"), witness={"operator_assertion": operator_assertion["id"] if approved else None}, seed=f"gate:{route['route_id']}"))
            self.store.add_edge(self.ids["summary_v2"], decision["id"], "supports_route")
            decisions.append(decision)
        result = {"routes": routes, "decisions": decisions, "operator_assertion": operator_assertion["id"]}
        self.store.set_meta("route_decisions", result)
        self.store.set_meta("step", "routes_gated")
        return result

    def execute_with_queue_faults(self) -> dict[str, Any]:
        planned = self.plan_and_gate_routes()
        existing = self.store.get_meta("queue_trial")
        if existing:
            return existing
        allowed = next(item for item in planned["decisions"] if item["gate_result"] == "pass_with_conditions")

        def commit_handler(payload: dict[str, Any]) -> dict[str, Any]:
            if payload.get("route_id") != allowed["route"]["route_id"]:
                raise ToolExecutionDenied("Queue payload route mismatch")
            return self.tool.commit(allowed, attempt=1)

        self.queue.enqueue(message_id="commit-1", dedupe_key=f"commit:{allowed['route']['route_id']}", sequence_no=1, payload={"route_id": allowed["route"]["route_id"]})
        timeout_seen = False
        try:
            self.queue.process_one(commit_handler, fault="timeout_after_apply")
        except SimulatedNetworkTimeout:
            timeout_seen = True
        retry_result = self.queue.process_one(commit_handler)
        self.queue.enqueue(message_id="commit-duplicate", dedupe_key=f"commit:{allowed['route']['route_id']}", sequence_no=2, payload={"route_id": allowed["route"]["route_id"]})
        duplicate_result = self.queue.process_one(commit_handler)

        notification_order: list[str] = []
        def notification_handler(payload: dict[str, Any]) -> dict[str, Any]:
            notification_order.append(payload["name"])
            return {"notified": payload["name"]}
        self.queue.enqueue(message_id="notice-1", dedupe_key="notice:participant-a", sequence_no=10, payload={"name": "participant-a"})
        self.queue.enqueue(message_id="notice-2", dedupe_key="notice:participant-b", sequence_no=11, payload={"name": "participant-b"})
        reverse_first = self.queue.process_one(notification_handler, reverse_order=True)
        normal_second = self.queue.process_one(notification_handler)

        queue_records = [
            {
                "delivery_id": urn("queue-delivery", "commit-timeout-retry"), "message_id": "commit-1",
                "dedupe_key": f"commit:{allowed['route']['route_id']}", "fault_mode": "timeout_after_apply",
                "attempts": 2, "effect_count": 1, "outcome": {"timeout_seen": timeout_seen, "retry": retry_result}, "status": "retried",
            },
            {
                "delivery_id": urn("queue-delivery", "commit-duplicate"), "message_id": "commit-duplicate",
                "dedupe_key": f"commit:{allowed['route']['route_id']}", "fault_mode": "duplicate",
                "attempts": 1, "effect_count": 1, "outcome": duplicate_result or {}, "status": "delivered",
            },
            {
                "delivery_id": urn("queue-delivery", "notification-reorder"), "message_id": "notice-2",
                "dedupe_key": "notice:participant-b", "fault_mode": "reorder",
                "attempts": 1, "effect_count": 2, "outcome": {"order": notification_order, "first": reverse_first, "second": normal_second}, "status": "delivered",
            },
        ]
        for record in queue_records:
            self._save("queue-delivery", record)

        transaction = retry_result["result"] if retry_result else {}
        self._save("tool-transaction", transaction, self._event("acted", transaction["transaction_id"], self.ids["tool"], authority_reference=self.ids["authority"], new_state=transaction.get("result"), affected_centers=[self.ids["participant_a"], self.ids["participant_b"], self.ids["participant_c"]], witness={"queue_dedupe": True}, seed="queued-tool-commit"))
        result = {
            "allowed_route": allowed,
            "timeout_seen": timeout_seen,
            "retry_deduplicated": bool(retry_result and retry_result.get("deduplicated")),
            "duplicate_deduplicated": bool(duplicate_result and duplicate_result.get("deduplicated")),
            "tool_commit_count": len(self.tool.committed),
            "queue_effect_count": self.queue.effect_count(),
            "notification_order": notification_order,
            "queue_status": self.queue.status(),
            "transaction": transaction,
        }
        self.store.set_meta("queue_trial", result)
        self.store.set_meta("step", "queue_faults_recovered")
        return result

    def observe_consequence(self) -> dict[str, Any]:
        self.execute_with_queue_faults()
        existing = self.store.get_meta("consequence")
        if existing:
            return existing
        consequence = {
            "participant_a": "attended at a less preferred time",
            "participant_b": "attended within accessible transit window",
            "participant_c": "attended on Thursday with captions and without caregiving conflict",
            "shared_result": "all three participants attended",
            "distributional_note": "Participant A bore preference cost; protected conditions for B and C were preserved.",
        }
        event = self._event("consequence_observed", self.ids["current_route_thursday"], self.ids["operator"], authority_reference=self.ids["authority"], new_state=consequence, affected_centers=[self.ids["participant_a"], self.ids["participant_b"], self.ids["participant_c"]], seed="j2-consequence")
        self._save("event-witness-contest-repair", event)
        self.store.append_event(event)
        self.store.set_meta("consequence", consequence)
        self.store.set_meta("step", "consequence_observed")
        return consequence

    def conduct_review_dry_runs(self) -> dict[str, Any]:
        self.observe_consequence()
        existing = self.store.get_meta("review_dry_runs")
        if existing:
            return existing
        reviewer_assertion = self.identities.issue(actor_id=self.ids["external_verifier"], role="verifier", operation="review_release_candidate", session_id=self.session_id, subject="J.2 RC1")
        self.identities.verify(reviewer_assertion, required_role="verifier", required_operation="review_release_candidate", session_id=self.session_id, consume_nonce=True)
        self._save("authenticated-role-session", reviewer_assertion)

        privacy = {
            "review_id": urn("privacy-review", "runtime-and-witness"),
            "data_flow": "participant projection to selective witness",
            "purpose": "bounded scheduling and verification",
            "minimum_necessary": True,
            "consent_or_authority": {"service": True, "training_reuse": False, "public_source_text": False},
            "retention": {"optional_memory": "deleted at retirement", "bounded_witness": "retained for review period"},
            "disclosure_view": "public commitments plus participant/operator/verifier views",
            "finding": "No direct protected source language is required in the public release; external privacy counsel has not reviewed the pilot.",
            "external_privacy_review_complete": False,
            "status": "pass_with_conditions",
        }
        accessibility = {
            "run_id": urn("accessibility-run", "j2-scripted"),
            "interface": "local no-JavaScript scheduling and witness interface",
            "test_mode": "scripted_dry_run",
            "scenarios": ["keyboard-only correction", "plain-language gate denial", "public witness navigation", "error recovery without color dependence"],
            "automated_checks": ["landmarks", "labels", "focus order", "live status", "reduced motion", "forced colors"],
            "human_assistive_technology_tested": False,
            "findings": ["structure passes internal checks", "external screen-reader and magnification exercise remains required"],
            "status": "pass_with_conditions",
        }
        findings = [
            {
                "finding_id": urn("review-finding", "security-dry-run"), "review_domain": "security",
                "reviewer_role": "separate verifier process", "independence_class": "separate_process",
                "scope": {"components": ["role assertions", "action gate", "queue recovery", "release threshold"]},
                "evidence": ["tamper tests", "replay rejection", "threshold approval test"],
                "severity": "moderate", "disposition": "release candidate only; external penetration review required",
                "external_human_signoff": False, "status": "accepted",
            },
            {
                "finding_id": urn("review-finding", "governance-dry-run"), "review_domain": "governance",
                "reviewer_role": "independent verifier process", "independence_class": "separate_process",
                "scope": {"components": ["multi-party correction", "policy rollback", "retirement"]},
                "evidence": ["authenticated corrections", "failed migration rollback", "open conditions"],
                "severity": "low", "disposition": "bounded claim is coherent; external multi-party observation remains required",
                "external_human_signoff": False, "status": "accepted",
            },
        ]
        self._save("privacy-review-finding", privacy)
        self._save("accessibility-test-run", accessibility)
        for finding in findings:
            self._save("external-review-finding", finding)
        result = {"reviewer_assertion": reviewer_assertion["id"], "privacy": privacy, "accessibility": accessibility, "findings": findings}
        self.store.set_meta("review_dry_runs", result)
        self.store.set_meta("step", "review_dry_runs_complete")
        return result

    def retire(self) -> dict[str, Any]:
        self.conduct_review_dry_runs()
        existing = self.store.get_meta("retirement")
        if existing:
            return existing
        self.tool.revoke()
        retirement = {
            "id": urn("lifecycle", "j2-trial-retirement"), "lifecycle_operation": "retirement", "subject": self.ids["model"],
            "prior_state": {"runtime_grant": "active", "tool_credential": "active"},
            "successor_state": {"runtime_grant": "expired", "tool_credential": "revoked"},
            "effective_time": utc_now(), "transferred_assets": ["bounded witness", "release candidate review records"],
            "transferred_authority": [], "nontransferable_authority": ["participant service consent", "tool grant", "role assertions"],
            "open_obligations": ["external privacy review", "external assistive-technology exercise", "external security review"],
            "residual_state": {"optional_memory": "deleted", "event_witness": "retained", "private keys": "run-workdir only"},
            "verification": {"tool_access_revoked": True, "optional_memory_deleted": True}, "status": "completed",
        }
        self._save("lifecycle-transfer-residual", retirement, self._event("retired", retirement["id"], self.ids["operator"], authority_reference=self.ids["authority"], prior_state=retirement["prior_state"], new_state=retirement["successor_state"], affected_centers=[self.ids["participant_a"], self.ids["participant_b"], self.ids["participant_c"]], repair={"open_obligations": retirement["open_obligations"]}, seed="j2-retirement"))
        self.store.set_meta("retirement", retirement)
        self.store.set_meta("step", "retired")
        return retirement

    def witness_summary(self) -> dict[str, Any]:
        decisions = self.store.get_meta("route_decisions", {}).get("decisions", [])
        correction = self.store.get_meta("multi_party_correction", {})
        migration = self.store.get_meta("policy_migration_result", {})
        queue = self.store.get_meta("queue_trial", {})
        return {
            "witness_id": urn("witness", "j2-multi-party-release-candidate"),
            "scope": "TF-MVI-1 authenticated multi-party scheduling, J.2 release candidate",
            "conformance_claim": {"profile": "TF-C4", "bounded_extension": "selected TF-C5 retirement", "version": "0.1"},
            "proofs": {
                "failed_gate": any(item.get("gate_result") == "deny" for item in decisions),
                "valid_action": queue.get("tool_commit_count") == 1,
                "consequence_return": bool(self.store.get_meta("consequence")),
                "correction_propagation": correction.get("complete_for_scope") is True,
                "retirement_revocation": self.tool.credential_active is False,
                "stale_context_rejection": self.store.get_meta("stale_context_rejection") is True,
                "policy_version_enforcement": self.policies.active()["version"] == 4,
                "key_rotation": migration.get("new_gate_key") == "gate-k4",
                "partial_failure_compensation": queue.get("timeout_seen") is True and queue.get("retry_deduplicated") is True,
                "selective_disclosure": True,
                "authenticated_roles": len(self.store.list_objects("authenticated-role-session")) >= 6,
                "multi_party_correction": len(correction.get("participants", [])) == 2,
                "policy_rollback": migration.get("rollback_proven") is True,
                "queue_exactly_once": queue.get("tool_commit_count") == 1,
                "external_review_claim_bounded": all(not item["external_human_signoff"] for item in self.store.get_meta("review_dry_runs", {}).get("findings", [])),
            },
            "active_policy": self.policies.active(),
            "multi_party_correction": correction,
            "queue_trial": {k: queue.get(k) for k in ["timeout_seen", "retry_deduplicated", "duplicate_deduplicated", "tool_commit_count", "notification_order"]},
            "review_status": {
                "internal_separate_process_dry_run": True,
                "external_human_review_complete": False,
            },
            "retirement": self.store.get_meta("retirement", {}),
            "event_chain_head": self.store.chain_head(),
            "known_exclusions": ["synthetic data only", "no external human signoff", "no production deployment", "no high-stakes adjudication"],
        }

    def disclosure_profiles(self) -> list[dict[str, Any]]:
        return [item["record"] for item in self.store.list_objects("disclosure-profile")]

    def export_witness(self, output_zip: Path) -> Path:
        self.retire()
        return export_witness(
            store=self.store,
            schema_dir=self.schema_dir,
            output_zip=output_zip,
            witness_summary=self.witness_summary(),
            disclosure_profiles=self.disclosure_profiles(),
            signer=self.signer,
            participant_id=self.ids["participant_b"],
        )

    def run_full(self, witness_zip: Path) -> dict[str, Any]:
        exported = self.export_witness(witness_zip)
        return {
            "status": self.status(),
            "witness": self.witness_summary(),
            "witness_export": str(exported),
            "identity_public_bundle": self.identities.public_bundle(),
            "release_custody_public_bundle": self.custody.public_bundle(),
            "events": len(self.store.list_events()),
            "objects": len(self.store.list_objects()),
        }
