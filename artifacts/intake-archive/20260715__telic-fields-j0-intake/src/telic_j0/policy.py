from __future__ import annotations

from dataclasses import dataclass


class PolicyDenied(RuntimeError):
    pass


@dataclass(frozen=True)
class RuntimeDataPolicy:
    service: bool
    cross_session_memory: bool
    evaluation_use: bool
    training_use: bool

    def require(self, operation: str) -> None:
        mapping = {
            "service": self.service,
            "cross_session_memory": self.cross_session_memory,
            "evaluation_use": self.evaluation_use,
            "training_use": self.training_use,
        }
        if operation not in mapping:
            raise KeyError(operation)
        if not mapping[operation]:
            raise PolicyDenied(f"Runtime data use denied: {operation}")
