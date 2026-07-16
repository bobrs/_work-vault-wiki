from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .canonical import canonical_json, sha256_text, utc_now
from .ids import urn


class PolicyDenied(PermissionError):
    pass


class PolicyVersionError(RuntimeError):
    pass


@dataclass(frozen=True)
class RuntimeDataPolicy:
    service: bool
    cross_session_memory: bool
    evaluation_use: bool
    training_use: bool
    export_private_content: bool = False

    def require(self, operation: str) -> None:
        if not hasattr(self, operation):
            raise KeyError(operation)
        if not bool(getattr(self, operation)):
            raise PolicyDenied(f"Runtime data use denied: {operation}")

    def as_dict(self) -> dict[str, bool]:
        return {
            "service": self.service,
            "cross_session_memory": self.cross_session_memory,
            "evaluation_use": self.evaluation_use,
            "training_use": self.training_use,
            "export_private_content": self.export_private_content,
        }


class AuthorizationPolicyRegistry:
    def __init__(self) -> None:
        self._policies: dict[int, dict[str, Any]] = {}
        self._active_version: int | None = None

    @staticmethod
    def _digest_payload(record: dict[str, Any]) -> dict[str, Any]:
        return {
            "policy_id": record["policy_id"],
            "version": record["version"],
            "purpose": record["purpose"],
            "allowed_operations": record["allowed_operations"],
            "prohibited_operations": record["prohibited_operations"],
            "required_checks": record["required_checks"],
            "supersedes": record.get("supersedes"),
        }

    def load(self, record: dict[str, Any]) -> None:
        version = int(record["version"])
        expected = sha256_text(canonical_json(self._digest_payload(record)))
        if record.get("digest") != expected:
            raise PolicyVersionError(f"Policy digest mismatch for version {version}")
        self._policies[version] = dict(record)
        active_versions = [v for v, item in self._policies.items() if item.get("status") == "active"]
        self._active_version = max(active_versions) if active_versions else None

    def publish(
        self,
        *,
        version: int,
        purpose: str,
        allowed_operations: list[str],
        prohibited_operations: list[str],
        required_checks: list[str],
        supersedes: str | None = None,
        status: str = "active",
    ) -> dict[str, Any]:
        if version in self._policies:
            raise PolicyVersionError(f"Policy version already exists: {version}")
        core = {
            "policy_id": urn("authorization-policy", f"v{version}"),
            "version": version,
            "purpose": purpose,
            "allowed_operations": list(allowed_operations),
            "prohibited_operations": list(prohibited_operations),
            "required_checks": list(required_checks),
            "valid_time": {"from": utc_now(), "to": None},
            "supersedes": supersedes,
            "status": status,
        }
        core["digest"] = sha256_text(canonical_json(self._digest_payload(core)))
        self._policies[version] = core
        if status == "active":
            if self._active_version is not None:
                prior = self._policies[self._active_version]
                prior["status"] = "superseded"
            self._active_version = version
        return dict(core)

    def active(self) -> dict[str, Any]:
        if self._active_version is None:
            raise PolicyVersionError("No active authorization policy")
        return dict(self._policies[self._active_version])

    def get(self, version: int) -> dict[str, Any]:
        if version not in self._policies:
            raise PolicyVersionError(f"Unknown policy version: {version}")
        return dict(self._policies[version])

    def require_active(self, version: int, digest: str) -> dict[str, Any]:
        active = self.active()
        if active["version"] != version or active["digest"] != digest:
            raise PolicyVersionError("Authorization policy is stale or mismatched")
        return active

    def all(self) -> list[dict[str, Any]]:
        return [dict(self._policies[v]) for v in sorted(self._policies)]
