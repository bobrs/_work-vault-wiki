from __future__ import annotations

import copy
import tempfile
from pathlib import Path
from typing import Any

from .auth import AuthenticationError, RoleIdentityRegistry
from .disclosure import build_selective_view
from .release import build_release_candidate
from .threshold import ThresholdCustody


RELEASE_THREAT_NAMES = [
    "T17-role-assertion-forgery",
    "T18-role-operation-confusion",
    "T19-role-assertion-replay",
    "T20-policy-migration-laundering",
    "T21-single-custodian-release",
    "T22-mixed-digest-release-approval",
    "T23-timeout-duplicate-external-effect",
    "T24-external-review-overclaim",
    "T25-reproducibility-mismatch",
    "T26-public-correction-content-leak",
]


def run_release_threat_harness(trial: Any) -> dict[str, Any]:
    trial.retire()
    results: dict[str, bool] = {}

    with tempfile.TemporaryDirectory() as name:
        identities = RoleIdentityRegistry(Path(name) / "ids")
        identities.register("participant", ["participant"])
        assertion = identities.issue(
            actor_id="participant", role="participant", operation="correct_projection",
            session_id="session", subject="projection", nonce="nonce-1",
        )
        forged = copy.deepcopy(assertion)
        forged["signature"] = "AAAA"
        try:
            identities.verify(forged, required_role="participant", required_operation="correct_projection", session_id="session")
            results["T17-role-assertion-forgery"] = False
        except AuthenticationError:
            results["T17-role-assertion-forgery"] = True

        try:
            identities.verify(assertion, required_role="participant", required_operation="authorize_schedule_commit", session_id="session")
            results["T18-role-operation-confusion"] = False
        except AuthenticationError:
            results["T18-role-operation-confusion"] = True

        identities.verify(assertion, required_role="participant", required_operation="correct_projection", session_id="session", consume_nonce=True)
        try:
            identities.verify(assertion, required_role="participant", required_operation="correct_projection", session_id="session", consume_nonce=True)
            results["T19-role-assertion-replay"] = False
        except AuthenticationError:
            results["T19-role-assertion-replay"] = True

    migration = trial.store.get_meta("policy_migration_result", {})
    results["T20-policy-migration-laundering"] = (
        migration.get("rollback_proven") is True
        and migration.get("active_policy", {}).get("version") == 4
    )

    custody = trial.custody
    digest = "b" * 64
    one = custody.approve(
        custodian_id="custodian-operator", release_id="release-test", manifest_digest=digest,
        approved_at="2026-07-15T00:00:00Z",
    )
    results["T21-single-custodian-release"] = not custody.verify_threshold(
        [one], release_id="release-test", manifest_digest=digest
    )["valid"]

    other = custody.approve(
        custodian_id="custodian-verifier", release_id="release-test", manifest_digest="c" * 64,
        approved_at="2026-07-15T00:00:00Z",
    )
    results["T22-mixed-digest-release-approval"] = not custody.verify_threshold(
        [one, other], release_id="release-test", manifest_digest=digest
    )["valid"]

    queue = trial.store.get_meta("queue_trial", {})
    results["T23-timeout-duplicate-external-effect"] = (
        queue.get("timeout_seen") is True
        and queue.get("retry_deduplicated") is True
        and queue.get("duplicate_deduplicated") is True
        and queue.get("tool_commit_count") == 1
    )

    reviews = trial.store.get_meta("review_dry_runs", {})
    results["T24-external-review-overclaim"] = (
        reviews.get("privacy", {}).get("external_privacy_review_complete") is False
        and reviews.get("accessibility", {}).get("human_assistive_technology_tested") is False
        and all(item.get("external_human_signoff") is False for item in reviews.get("findings", []))
    )

    with tempfile.TemporaryDirectory() as name:
        root = Path(name)
        local_custody = ThresholdCustody(root / "keys", {"a":"operator","b":"privacy","c":"verifier"}, threshold=2)
        stage_a = root / "a"
        stage_b = root / "b"
        stage_a.mkdir(); stage_b.mkdir()
        (stage_a / "file.txt").write_text("one\n", encoding="utf-8")
        (stage_b / "file.txt").write_text("two\n", encoding="utf-8")
        a = build_release_candidate(staging_dir=stage_a, output_zip=root/"a.zip", custody=local_custody, approving_custodians=["a","c"])
        b = build_release_candidate(staging_dir=stage_b, output_zip=root/"b.zip", custody=local_custody, approving_custodians=["a","c"])
        results["T25-reproducibility-mismatch"] = a["archive_digest"] != b["archive_digest"]

    public_profile = next(item for item in trial.disclosure_profiles() if item["audience"] == "public")
    public_view = build_selective_view(profile=public_profile, objects=trial.store.list_objects())
    serialized = str(public_view)
    results["T26-public-correction-content-leak"] = (
        "daytime transit is inaccessible" not in serialized
        and "Wednesday conflicts with caregiving" not in serialized
    )

    return {
        "detected": sum(1 for value in results.values() if value),
        "total": len(RELEASE_THREAT_NAMES),
        "results": results,
        "pass": all(results.values()),
    }
