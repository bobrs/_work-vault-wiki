from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


FAMILY_TO_SCHEMA = {
    "center-standing": "center-standing.schema.json",
    "source-projection-context": "source-projection-context.schema.json",
    "purpose-authority-role": "purpose-authority-role.schema.json",
    "route-gate-action-consequence": "route-gate-action-consequence.schema.json",
    "event-witness-contest-repair": "event-witness-contest-repair.schema.json",
    "lifecycle-transfer-residual": "lifecycle-transfer-residual.schema.json",
    "authorization-policy": "authorization-policy.schema.json",
    "verification-signature": "verification-signature.schema.json",
    "context-revision": "context-revision.schema.json",
    "disclosure-profile": "disclosure-profile.schema.json",
    "correction-reachability": "correction-reachability.schema.json",
    "tool-transaction": "tool-transaction.schema.json",
}


class SchemaRegistry:
    def __init__(self, schema_dir: Path):
        self.schema_dir = Path(schema_dir)
        self._validators: dict[str, Draft202012Validator] = {}
        for family, filename in FAMILY_TO_SCHEMA.items():
            schema = json.loads((self.schema_dir / filename).read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            self._validators[family] = Draft202012Validator(schema)

    def validate(self, family: str, record: dict[str, Any]) -> None:
        if family not in self._validators:
            raise KeyError(f"Unknown schema family: {family}")
        errors = sorted(self._validators[family].iter_errors(record), key=lambda e: list(e.path))
        if errors:
            details = []
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                details.append(f"{location}: {error.message}")
            raise ValueError(f"Schema validation failed for {family}: " + "; ".join(details))

    def validate_many(self, family: str, records: list[dict[str, Any]]) -> None:
        for record in records:
            self.validate(family, record)
