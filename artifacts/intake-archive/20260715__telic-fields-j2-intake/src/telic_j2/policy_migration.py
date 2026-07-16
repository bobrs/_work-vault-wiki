from __future__ import annotations

from typing import Any, Callable

from .canonical import utc_now
from .ids import urn
from .policy import AuthorizationPolicyRegistry


class PolicyMigrationManager:
    def __init__(self, registry: AuthorizationPolicyRegistry):
        self.registry = registry
        self.history: list[dict[str, Any]] = []

    def attempt(
        self,
        *,
        version: int,
        purpose: str,
        allowed_operations: list[str],
        prohibited_operations: list[str],
        required_checks: list[str],
        validation: Callable[[dict[str, Any]], tuple[bool, list[str]]],
    ) -> dict[str, Any]:
        prior = self.registry.active()
        candidate = self.registry.publish(
            version=version,
            purpose=purpose,
            allowed_operations=allowed_operations,
            prohibited_operations=prohibited_operations,
            required_checks=required_checks,
            supersedes=prior["policy_id"],
        )
        passed, errors = validation(candidate)
        record = {
            "migration_id": urn("policy-migration", f"{prior['version']}:{version}"),
            "from_version": prior["version"],
            "to_version": version,
            "candidate_digest": candidate["digest"],
            "validation_passed": passed,
            "validation_errors": errors,
            "rollback_version": None,
            "created_at": utc_now(),
            "status": "active" if passed else "rolled_back",
        }
        if not passed:
            self.registry.activate(prior["version"])
            record["rollback_version"] = prior["version"]
        self.history.append(record)
        return record
