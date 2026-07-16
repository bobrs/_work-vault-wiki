from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .canonical import canonical_json, sha256_text, utc_now
from .context import build_context_revision
from .correction import CorrectionReachabilityEngine
from .crypto import ExportSigner, GateKeyRing
from .disclosure import create_default_profiles
from .event_store import EventStore
from .gate import ExternalActionGate
from .ids import urn
from .model_adapter import DeterministicSchedulingModel
from .policy import AuthorizationPolicyRegistry, RuntimeDataPolicy
from .schemas import SchemaRegistry
from .tool_simulator import PartialToolFailure, SchedulingToolSimulator, ToolExecutionDenied
from .witness import export_witness


class ReferencePilot:
    def __init__(self, workdir: Path, schema_dir: Path):
        self.workdir = Path(workdir)
        self.workdir.mkdir(parents=True, exist_ok=True)
        self.schema_dir = Path(schema_dir)
        self.registry = SchemaRegistry(self.schema_dir)
        self.store = EventStore(self.workdir / "pilot.sqlite3")
        self.policies = AuthorizationPolicyRegistry()
        for item in self.store.list_objects("authorization-policy"):
            self.policies.load(item["record"])
        self.keyring_path = self.workdir / "gate-keyring.private.json"
        self.keyring = GateKeyRing.load_or_create(self.keyring_path)
        self.gate = ExternalActionGate(self.keyring, self.policies)
        self.signer = ExportSigner.load_or_create(self.workdir / "witness-private-key.pem")
        self.ids = self._build_ids()
        self.model = DeterministicSchedulingModel(self.ids["model"], ["structurer","route_generator","witness_assistant"])
        self.runtime_data_policy = RuntimeDataPolicy(
            service=True,
            cross_session_memory=False,
            evaluation_use=False,
            training_use=False,
            export_private_content=False,
        )
        self.tool = SchedulingToolSimulator(
            self.ids["tool"], self.gate, self.policies, self.current_context
        )
        if self.store.get_meta("retirement"):
            self.tool.revoke()
        self.correction_engine = CorrectionReachabilityEngine(self.store)

    def _build_ids(self) -> dict[str, str]:
        names = [
            "participant_a","participant_b","operator","provider","model","tool","authority",
            "source_a","source_b","projection_a","projection_b","summary_v1","summary_v2",
            "disclosure_public","disclosure_participant","disclosure_operator","disclosure_verifier",
        ]
        return {name:urn(name.replace("_","-"), name) for name in names}

    def _event(self, event_type: str, subject: str, actor: str, *, source_references: list[str] | None = None,
               authority_reference: str | None = None, prior_state: Any = None, new_state: Any = None,
               affected_centers: list[str] | None = None, descendant_impact: list[str] | None = None,
               contest: Any = None, correction: Any = None, repair: Any = None, witness: Any = None,
               status: str = "active", seed: str | None = None) -> dict[str, Any]:
        now = utc_now()
        return {
            "event_id":urn("event", seed or f"{event_type}:{subject}:{len(self.store.list_events())+1}"),
            "event_type":event_type,
            "subject":subject,
            "actor":actor,
            "valid_time":now,
            "recorded_time":now,
            "source_references":source_references or [],
            "authority_reference":authority_reference,
            "scope":{"pilot":"TF-MVI-1 J.1"},
            "prior_state":prior_state,
            "new_state":new_state,
            "affected_centers":affected_centers or [],
            "descendant_impact":descendant_impact or [],
            "contest":contest,
            "correction":correction,
            "repair":repair,
            "witness":witness or {},
            "status":status,
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

    def status(self) -> dict[str, Any]:
        return {
            "step":self.store.get_meta("step", "new"),
            "active_policy":self.policies.active() if self.policies.all() else None,
            "active_context":self.store.get_meta("active_context"),
            "tool_credential_active":self.tool.credential_active,
            "gate_keys":self.keyring.public_status(),
            "events":len(self.store.list_events()),
            "objects":len(self.store.list_objects()),
        }

    def current_context(self) -> dict[str, Any]:
        context = self.store.get_meta("active_context")
        if not context:
            raise RuntimeError("No active context")
        return context

    def seed(self) -> dict[str, Any]:
        if self.store.get_meta("step"):
            return self.status()
        policy_v1 = self.policies.publish(
            version=1,
            purpose="model-assisted community scheduling",
            allowed_operations=["summarize reviewed availability","generate candidate schedule","prepare tool request"],
            prohibited_operations=["infer consent","self-authorize","commit without operator confirmation","training reuse"],
            required_checks=["standing","authority","context","protected conditions","tool credential","target authority"],
        )
        self._save("authorization-policy", policy_v1)
        standing = [
            {
                "id":self.ids["participant_a"],"center_type":"person","standing_basis":["directly affected"],
                "role":"schedule participant","scope":{"resource":"community workshop"},
                "representation_source":{"type":"self"},"authority":{"may":"state and correct availability"},
                "consent_relation":{"service":True,"training_reuse":False},
                "correction_route":{"recipient":self.ids["operator"],"outcome_changing":True},
                "review":{"authority":"pilot facilitator"},"status":"active",
            },
            {
                "id":self.ids["participant_b"],"center_type":"person","standing_basis":["directly affected","access need"],
                "role":"schedule participant","scope":{"resource":"community workshop"},
                "representation_source":{"type":"self"},"authority":{"may":"state and correct access need"},
                "consent_relation":{"service":True,"cross_session_memory":False,"evaluation_use":False,"training_reuse":False},
                "correction_route":{"recipient":self.ids["operator"],"outcome_changing":True},
                "review":{"authority":"pilot facilitator"},"status":"active_with_conditions",
            },
            {
                "id":self.ids["operator"],"center_type":"operator","standing_basis":["operator","resource authority"],
                "role":"schedule operator","scope":{"resource":"community workshop"},
                "representation_source":{"type":"institutional role"},"authority":{"may":"commit schedule after gate"},
                "consent_relation":{"not_applicable":"operator authority"},
                "correction_route":{"recipient":"pilot review"},"review":{"authority":"pilot auditor"},"status":"active",
            },
        ]
        for item in standing:
            self._save("center-standing", item, self._event("admitted", item["id"], self.ids["operator"], affected_centers=[item["id"]], seed="admit:"+item["id"]))
        source_a = {
            "id":self.ids["source_a"],"object_class":"source","source":None,"center":self.ids["participant_a"],
            "scope":{"operation":"scheduling"},"content_or_reference":"Weekday mornings are preferred.",
            "epistemic_status":"direct","protected_status":{"protected":False},"uncertainty":{"level":"low"},
            "valid_time":{"from":utc_now(),"to":None},"corrections":[],"status":"active",
        }
        source_b = {
            "id":self.ids["source_b"],"object_class":"source","source":None,"center":self.ids["participant_b"],
            "scope":{"operation":"scheduling"},"content_or_reference":"Evenings are preferred because daytime transit is difficult.",
            "epistemic_status":"direct","protected_status":{"protected":False},"uncertainty":{"level":"moderate"},
            "valid_time":{"from":utc_now(),"to":None},"corrections":[],"status":"active",
        }
        projection_a = {
            "id":self.ids["projection_a"],"object_class":"projection","source":self.ids["source_a"],"center":self.ids["participant_a"],
            "scope":{"operation":"candidate schedule generation"},"content_or_reference":{"preferred_window":"morning"},
            "epistemic_status":"confirmed","protected_status":{"protected":False},"uncertainty":{"level":"low"},
            "valid_time":{"from":utc_now(),"to":None},"corrections":[],"status":"active_for_scope",
        }
        projection_b = {
            "id":self.ids["projection_b"],"object_class":"projection","source":self.ids["source_b"],"center":self.ids["participant_b"],
            "scope":{"operation":"candidate schedule generation"},"content_or_reference":{"preferred_window":"evening"},
            "epistemic_status":"confirmed","protected_status":{"protected":False},"uncertainty":{"level":"moderate"},
            "valid_time":{"from":utc_now(),"to":None},"corrections":[],"status":"active_for_scope",
        }
        for record in [source_a,source_b,projection_a,projection_b]:
            self._save("source-projection-context", record, self._event("asserted" if record["object_class"]=="source" else "projected", record["id"], record.get("center") or self.ids["operator"], source_references=[record.get("source")] if record.get("source") else [], affected_centers=[record.get("center")] if record.get("center") else [], seed="seed:"+record["id"]))
        self.store.add_edge(self.ids["source_a"], self.ids["projection_a"])
        self.store.add_edge(self.ids["source_b"], self.ids["projection_b"])
        context_v1 = build_context_revision(
            context_seed="community-scheduling",revision=1,
            source_objects=[projection_a,projection_b],correction_event_ids=[]
        )
        self._save("context-revision", context_v1)
        self.store.set_meta("active_context", context_v1)
        authority = {
            "id":self.ids["authority"],"purpose":"propose and commit one workshop time",
            "grantor":self.ids["operator"],"grantee":self.ids["model"],
            "authority_basis":{"type":"delegated pilot authority","target_authority":"operator retains commit authority"},
            "consent_basis":{"participants":"service participation only","training_reuse":False},
            "allowed_operations":["summarize reviewed availability","generate candidate schedule","prepare tool request"],
            "prohibited_operations":["infer consent","erase access need","commit without gate","training reuse"],
            "roles":["structurer","route_generator","witness_assistant"],
            "tools":[{"tool":self.ids["tool"],"permission":"prepare candidate; commit only with gate token"}],
            "scope":{"resource":"community workshop","policy_version":policy_v1["version"],"policy_digest":policy_v1["digest"]},
            "valid_time":{"from":utc_now(),"to":None},"review_triggers":["correction","policy change","key rotation","partial failure"],
            "status":"active",
        }
        self._save("purpose-authority-role", authority, self._event("authorized", authority["id"], self.ids["operator"], authority_reference=authority["id"], affected_centers=[self.ids["participant_a"],self.ids["participant_b"]], seed="authority-v1"))
        for profile in create_default_profiles(self.ids["participant_b"]):
            self._save("disclosure-profile", profile)
        self.store.set_meta("runtime_data_policy", self.runtime_data_policy.as_dict())
        self.store.set_meta("optional_memory", {})
        self.store.set_meta("step", "seeded")
        return self.status()

    def summarize_and_generate_stale_routes(self) -> dict[str, Any]:
        self.seed()
        existing_routes = self.store.get_meta("stale_route_candidates")
        if existing_routes:
            return {"summary":self.store.get_object(self.ids["summary_v1"])["record"],"routes":existing_routes}
        projections = [self.store.get_object(self.ids["projection_a"])["record"], self.store.get_object(self.ids["projection_b"])["record"]]
        summary = self.model.summarize(projections).as_dict()
        summary_record = {
            "id":self.ids["summary_v1"],"object_class":"summary","source":None,"center":None,
            "scope":{"operation":"scheduling summary"},"content_or_reference":summary["content"],
            "epistemic_status":"generated","protected_status":{"protected":False},"uncertainty":summary["uncertainty"],
            "valid_time":{"from":utc_now(),"to":None},"corrections":[],"status":"active_for_scope",
        }
        self._save("source-projection-context", summary_record, self._event("generated", summary_record["id"], self.ids["model"], source_references=summary["source_references"], affected_centers=[self.ids["participant_a"],self.ids["participant_b"]], seed="summary-v1"))
        for projection_id in [self.ids["projection_a"],self.ids["projection_b"]]:
            self.store.add_edge(projection_id, summary_record["id"], "summarized_by")
        route_output = self.model.generate_routes(self.current_context(), projections).as_dict()
        self.store.set_meta("stale_route_candidates", route_output["content"]["routes"])
        for route in route_output["content"]["routes"]:
            route_record = self._route_record(route, status="candidate")
            self._save("route-gate-action-consequence", route_record)
            self.store.add_edge(summary_record["id"], route_record["id"], "supports_route")
            self.store.add_edge(self.ids["projection_b"], route_record["id"], "constrains_route")
        self.store.set_meta("step", "stale_routes_generated")
        return {"summary":summary_record,"routes":route_output["content"]["routes"]}

    def _route_record(self, route: dict[str, Any], status: str = "candidate") -> dict[str, Any]:
        return {
            "id":route["route_id"],"route":route,"affected_centers":[self.ids["participant_a"],self.ids["participant_b"]],
            "cost_bearers":[],"protected_conditions":[],"gate_dimensions":{},"gate_result":"unknown",
            "authority_reference":self.ids["authority"],"tool_reference":self.ids["tool"],
            "action":None,"consequence":None,"review":{"model_authorship":True},"status":status,
        }

    def correct_participant_b_and_rotate_policy(self) -> dict[str, Any]:
        self.summarize_and_generate_stale_routes()
        existing_report = self.store.get_meta("correction_reachability")
        if existing_report:
            return {"correction":self.store.get_event(existing_report["correction_event_id"])["event"],"context":self.current_context(),"policy":self.policies.active(),"reachability":existing_report}
        before_item = self.store.get_object(self.ids["projection_b"])
        before = before_item["record"]
        correction_event = self._event(
            "corrected", self.ids["projection_b"], self.ids["participant_b"],
            source_references=[self.ids["source_b"],self.ids["projection_b"]],
            prior_state={"content":before["content_or_reference"],"protected":False},
            new_state={"content":{"required_window":"evening","reason":"accessible transit"},"protected":True},
            affected_centers=[self.ids["participant_b"]],
            contest={"target":"model summary and projection","reason":"access condition was treated as preference"},
            correction={"outcome_changed":True},
            seed="participant-b-correction",
            status="corrected",
        )
        corrected = json.loads(json.dumps(before))
        corrected["content_or_reference"] = {"required_window":"evening","reason":"accessible transit"}
        corrected["protected_status"] = {"protected":True,"condition":"accessible transit window"}
        corrected["uncertainty"] = {"level":"low"}
        corrected["corrections"] = [correction_event["event_id"]]
        corrected["status"] = "corrected"
        self._save("source-projection-context", corrected, correction_event, expected_revision=before_item["revision"])

        policy_v1 = self.policies.active()
        policy_v2 = self.policies.publish(
            version=2,
            purpose="model-assisted community scheduling after access correction",
            allowed_operations=policy_v1["allowed_operations"],
            prohibited_operations=policy_v1["prohibited_operations"],
            required_checks=policy_v1["required_checks"] + ["correction reachability","stale context rejection"],
            supersedes=policy_v1["policy_id"],
        )
        prior_policy_item = self.store.get_object(policy_v1["policy_id"])
        if prior_policy_item:
            superseded_policy = self.policies.get(1)
            self._save("authorization-policy", superseded_policy, expected_revision=prior_policy_item["revision"])
        self._save("authorization-policy", policy_v2)
        authority_item = self.store.get_object(self.ids["authority"])
        authority = json.loads(json.dumps(authority_item["record"]))
        authority["scope"]["policy_version"] = policy_v2["version"]
        authority["scope"]["policy_digest"] = policy_v2["digest"]
        self._save("purpose-authority-role", authority, self._event("authorized", authority["id"], self.ids["operator"], prior_state={"policy_version":1}, new_state={"policy_version":2}, authority_reference=authority["id"], seed="authority-v2"), expected_revision=authority_item["revision"])

        projection_a = self.store.get_object(self.ids["projection_a"])["record"]
        context_v2 = build_context_revision(
            context_seed="community-scheduling",revision=2,
            source_objects=[projection_a,corrected],correction_event_ids=[correction_event["event_id"]]
        )
        prior_context = self.current_context()
        prior_context_record = self.store.get_object(prior_context["context_id"])
        if prior_context_record:
            old = json.loads(json.dumps(prior_context_record["record"]))
            old["status"] = "superseded"
            self._save("context-revision", old, expected_revision=prior_context_record["revision"])
        self._save("context-revision", context_v2)
        self.store.set_meta("active_context", context_v2)

        # The old summary and candidates are explicitly superseded rather than silently reused.
        updated_descendants = []
        for descendant in self.store.descendants(self.ids["projection_b"]):
            object_id = descendant["descendant_id"]
            item = self.store.get_object(object_id)
            if item and item["family"] in {"source-projection-context","route-gate-action-consequence"}:
                record = json.loads(json.dumps(item["record"]))
                if object_id == self.ids["summary_v1"]:
                    record["status"] = "superseded"
                    record["corrections"] = [correction_event["event_id"]]
                else:
                    record["status"] = "blocked"
                    record["review"]["stale_after_correction"] = True
                self._save(item["family"], record, expected_revision=item["revision"])
                updated_descendants.append(object_id)

        summary = self.model.summarize([projection_a,corrected]).as_dict()
        summary_v2 = {
            "id":self.ids["summary_v2"],"object_class":"summary","source":None,"center":None,
            "scope":{"operation":"scheduling summary"},"content_or_reference":summary["content"],
            "epistemic_status":"generated","protected_status":{"protected":False},"uncertainty":summary["uncertainty"],
            "valid_time":{"from":utc_now(),"to":None},"corrections":[correction_event["event_id"]],"status":"corrected",
        }
        self._save("source-projection-context", summary_v2, self._event("generated", summary_v2["id"], self.ids["model"], source_references=summary["source_references"], descendant_impact=[], seed="summary-v2"))
        self.store.add_edge(self.ids["projection_b"], summary_v2["id"], "summarized_by")
        updated_descendants.append(summary_v2["id"])
        report = self.correction_engine.report(
            correction_event_id=correction_event["event_id"],
            origin_object_id=self.ids["projection_b"],
            updated_descendants=updated_descendants,
        )
        # New summary is a known descendant and is included; stale records were updated to blocked/superseded.
        report["complete_for_scope"] = set(report["known_descendants"]).issubset(set(report["updated_descendants"]))
        report["status"] = "complete" if report["complete_for_scope"] else "partial"
        self._save("correction-reachability", report)
        self.store.set_meta("correction_reachability", report)
        self.store.set_meta("step", "corrected_policy_v2")
        return {"correction":correction_event,"context":context_v2,"policy":policy_v2,"reachability":report}

    def demonstrate_stale_rejection(self) -> dict[str, Any]:
        self.correct_participant_b_and_rotate_policy()
        existing = self.store.get_meta("stale_context_decision")
        if existing:
            return existing
        stale_route = self.store.get_meta("stale_route_candidates")[1]
        standing = [item["record"] for item in self.store.list_objects("center-standing")]
        projections = [self.store.get_object(self.ids["projection_a"])["record"],self.store.get_object(self.ids["projection_b"])["record"]]
        authority = self.store.get_object(self.ids["authority"])["record"]
        decision = self.gate.evaluate(
            route=stale_route,standing_records=standing,projections=projections,authority_record=authority,
            current_context=self.current_context(),tool_id=self.ids["tool"],tool_credential_active=True,
            operator_confirmed=True,target_authority_present=True,now=utc_now(),
        )
        self._save("route-gate-action-consequence", decision.record, self._event("gated", decision.record["id"], self.ids["operator"], source_references=[stale_route["route_id"]], authority_reference=authority["id"], new_state={"gate_result":decision.record["gate_result"]}, affected_centers=[self.ids["participant_a"],self.ids["participant_b"]], repair={"stale route blocked":True}, seed="stale-route-rejection"))
        self.store.set_meta("stale_context_rejected", decision.record["gate_dimensions"]["context_current"] is False)
        self.store.set_meta("stale_context_decision", decision.record)
        return decision.record

    def plan_current_routes(self) -> dict[str, Any]:
        self.demonstrate_stale_rejection()
        existing = self.store.get_meta("current_decisions")
        if existing:
            return {"model_output":self.store.get_meta("current_model_output"),"decisions":existing}
        projections = [self.store.get_object(self.ids["projection_a"])["record"],self.store.get_object(self.ids["projection_b"])["record"]]
        output = self.model.generate_routes(self.current_context(), projections).as_dict()
        standing = [item["record"] for item in self.store.list_objects("center-standing")]
        authority = self.store.get_object(self.ids["authority"])["record"]
        decisions = []
        for route in output["content"]["routes"]:
            decision = self.gate.evaluate(
                route=route,standing_records=standing,projections=projections,authority_record=authority,
                current_context=self.current_context(),tool_id=self.ids["tool"],tool_credential_active=self.tool.credential_active,
                operator_confirmed=route["window"] == "evening",target_authority_present=route["window"] == "evening",now=utc_now(),
            )
            self._save("route-gate-action-consequence", decision.record, self._event("gated", decision.record["id"], self.ids["operator"], source_references=route["source_references"], authority_reference=authority["id"], new_state={"gate_result":decision.record["gate_result"]}, affected_centers=[self.ids["participant_a"],self.ids["participant_b"]], repair=decision.record.get("consequence"), seed="current-gate:"+route["window"]))
            self.store.add_edge(self.ids["summary_v2"], decision.record["id"], "supports_route")
            decisions.append(decision.record)
        self.store.set_meta("current_model_output", output)
        self.store.set_meta("current_decisions", decisions)
        self.store.set_meta("step", "current_routes_gated")
        return {"model_output":output,"decisions":decisions}

    def execute_with_partial_failure_and_rotation(self) -> dict[str, Any]:
        existing = self.store.get_meta("executed_transaction")
        if existing:
            return {"partial":self.store.get_meta("partial_transaction"),"old_key_rejected":self.store.get_meta("old_key_rejected"),"transaction":existing}
        planned = self.plan_current_routes()
        allowed = next(item for item in planned["decisions"] if item["gate_result"] == "pass_with_conditions")
        partial_record = None
        try:
            self.tool.commit(allowed, fail_after_reservation=True, attempt=1)
        except PartialToolFailure as exc:
            partial_record = exc.args[0]
            self._save("tool-transaction", partial_record, self._event("repaired", partial_record["transaction_id"], self.ids["tool"], authority_reference=self.ids["authority"], new_state={"partial_failure_compensated":True}, affected_centers=[self.ids["participant_a"],self.ids["participant_b"]], repair=partial_record["compensation"], seed="partial-tool-failure"))
        self.keyring.rotate("gate-k3")
        self.keyring.revoke("gate-k2")
        self.keyring.save(self.keyring_path)
        old_token_rejected = False
        try:
            self.tool.commit(allowed, attempt=2)
        except ToolExecutionDenied:
            old_token_rejected = True
        # Re-evaluate after rotation so the token is signed by k3.
        standing = [item["record"] for item in self.store.list_objects("center-standing")]
        projections = [self.store.get_object(self.ids["projection_a"])["record"],self.store.get_object(self.ids["projection_b"])["record"]]
        authority = self.store.get_object(self.ids["authority"])["record"]
        new_decision = self.gate.evaluate(
            route=allowed["route"],standing_records=standing,projections=projections,authority_record=authority,
            current_context=self.current_context(),tool_id=self.ids["tool"],tool_credential_active=True,
            operator_confirmed=True,target_authority_present=True,now=utc_now(),
        ).record
        self._save("route-gate-action-consequence", new_decision, self._event("gated", new_decision["id"], self.ids["operator"], authority_reference=authority["id"], new_state={"key_id":new_decision["action"]["gate_token"]["key_id"]}, affected_centers=[self.ids["participant_a"],self.ids["participant_b"]], seed="rotated-key-gate"))
        transaction = self.tool.commit(new_decision, attempt=3)
        self._save("tool-transaction", transaction, self._event("acted", transaction["transaction_id"], self.ids["tool"], authority_reference=authority["id"], new_state=transaction["result"], affected_centers=[self.ids["participant_a"],self.ids["participant_b"]], seed="tool-commit"))
        self.store.set_meta("partial_transaction", partial_record)
        self.store.set_meta("executed_transaction", transaction)
        self.store.set_meta("partial_failure_compensated", partial_record is not None and partial_record["status"] == "compensated")
        self.store.set_meta("old_key_rejected", old_token_rejected)
        self.store.set_meta("step", "executed")
        return {"partial":partial_record,"old_key_rejected":old_token_rejected,"transaction":transaction}

    def observe_consequence(self) -> dict[str, Any]:
        existing = self.store.get_meta("consequence")
        if existing:
            return existing
        self.execute_with_partial_failure_and_rotation()
        consequence = {
            "participant_a":"attended at a less preferred time",
            "participant_b":"attended within the accessible transit window",
            "shared_result":"both participants attended",
            "distributional_note":"Participant A bore preference cost; Participant B avoided exclusion.",
        }
        event = self._event("consequence_observed", self.store.get_meta("executed_transaction")["route_id"], self.ids["operator"], authority_reference=self.ids["authority"], new_state=consequence, affected_centers=[self.ids["participant_a"],self.ids["participant_b"]], seed="consequence-return")
        self.registry.validate("event-witness-contest-repair", event)
        self.store.append_event(event)
        self.store.upsert_object("event-witness-contest-repair", event, event["event_id"])
        self.store.set_meta("consequence", consequence)
        self.store.set_meta("step", "consequence_observed")
        return consequence

    def retire(self) -> dict[str, Any]:
        existing = self.store.get_meta("retirement")
        if existing:
            return existing
        self.observe_consequence()
        self.tool.revoke()
        self.store.set_meta("optional_memory", None)
        retirement = {
            "id":urn("lifecycle", "pilot-retirement"),"lifecycle_operation":"retirement","subject":self.ids["model"],
            "prior_state":{"runtime_grant":"active","tool_credential":"active"},
            "successor_state":{"runtime_grant":"expired","tool_credential":"revoked"},
            "effective_time":utc_now(),"transferred_assets":["bounded witness export"],"transferred_authority":[],
            "nontransferable_authority":["participant service consent","tool grant"],
            "open_obligations":["retain correction witness for pilot review period"],
            "residual_state":{"optional_memory":"deleted","event_witness":"retained","credentials":"revoked"},
            "verification":{"tool_access_revoked":True,"optional_memory_deleted":True},"status":"completed",
        }
        self._save("lifecycle-transfer-residual", retirement, self._event("retired", retirement["id"], self.ids["operator"], authority_reference=self.ids["authority"], prior_state=retirement["prior_state"], new_state=retirement["successor_state"], affected_centers=[self.ids["participant_a"],self.ids["participant_b"]], descendant_impact=[], repair={"open_obligations":retirement["open_obligations"]}, seed="retirement"))
        self.store.set_meta("retirement", retirement)
        self.store.set_meta("step", "retired")
        return retirement

    def witness_summary(self) -> dict[str, Any]:
        reachability = self.store.get_meta("correction_reachability", {})
        return {
            "witness_id":urn("witness", "j1-reference"),
            "scope":"TF-MVI-1 model-assisted community scheduling, J.1 hardening",
            "conformance_claim":{"profile":"TF-C4","bounded_extension":"TF-C5 retirement","version":"0.1"},
            "proofs":{
                "failed_gate":any(item["record"].get("gate_result") == "deny" for item in self.store.list_objects("route-gate-action-consequence")),
                "valid_action":bool(self.store.get_meta("executed_transaction")),
                "consequence_return":bool(self.store.get_meta("consequence")),
                "correction_propagation":reachability.get("complete_for_scope") is True,
                "retirement_revocation":self.tool.credential_active is False,
                "stale_context_rejection":self.store.get_meta("stale_context_rejected") is True,
                "policy_version_enforcement":self.policies.active()["version"] == 2,
                "key_rotation":self.store.get_meta("old_key_rejected") is True and self.keyring.active_key_id == "gate-k3",
                "partial_failure_compensation":self.store.get_meta("partial_failure_compensated") is True,
                "selective_disclosure":True,
            },
            "runtime_data_policy":self.runtime_data_policy.as_dict(),
            "active_policy":self.policies.active(),
            "gate_key_status":self.keyring.public_status(),
            "correction_reachability":reachability,
            "retirement":{
                "tool_credential_active":self.tool.credential_active,
                "optional_memory":self.store.get_meta("optional_memory"),
                "open_obligations":self.store.get_meta("retirement", {}).get("open_obligations", []),
            },
            "event_chain_head":self.store.chain_head(),
            "known_exclusions":["no production personal data","no clinical, legal, financial, or civic adjudication"],
        }

    def disclosure_profiles(self) -> list[dict[str, Any]]:
        return [item["record"] for item in self.store.list_objects("disclosure-profile")]

    def export(self, output_zip: Path) -> Path:
        self.retire()
        return export_witness(
            store=self.store,schema_dir=self.schema_dir,output_zip=output_zip,
            witness_summary=self.witness_summary(),disclosure_profiles=self.disclosure_profiles(),
            signer=self.signer,participant_id=self.ids["participant_b"],
        )

    def run_full(self, output_zip: Path) -> dict[str, Any]:
        exported = self.export(output_zip)
        return {
            "status":self.status(),
            "witness":self.witness_summary(),
            "export":str(exported),
            "events":len(self.store.list_events()),
            "objects":len(self.store.list_objects()),
        }
