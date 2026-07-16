from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import Any

from .canonical import canonical_json, sha256_bytes, sha256_text, utc_now
from .event_store import EventStore
from .schemas import FAMILY_TO_SCHEMA, SchemaRegistry


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def export_witness(
    *,
    store: EventStore,
    schema_dir: Path,
    output_zip: Path,
    witness_summary: dict[str, Any],
) -> Path:
    output_zip = Path(output_zip)
    output_zip.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="telic-j0-export-") as temp_name:
        root = Path(temp_name)
        for rel in ["schemas", "records", "events", "witness", "database"]:
            (root / rel).mkdir(parents=True, exist_ok=True)

        for schema_path in Path(schema_dir).glob("*.json"):
            shutil.copy2(schema_path, root / "schemas" / schema_path.name)

        by_family: dict[str, list[dict[str, Any]]] = {}
        for item in store.list_objects():
            by_family.setdefault(item["family"], []).append(item["record"])
        for family, records in sorted(by_family.items()):
            (root / "records" / f"{family}.json").write_text(
                json.dumps({"records": records}, indent=2) + "\n", encoding="utf-8"
            )

        events = store.list_events()
        (root / "events" / "event-chain.json").write_text(
            json.dumps({"events": events}, indent=2) + "\n", encoding="utf-8"
        )
        (root / "witness" / "reference-witness.json").write_text(
            json.dumps(witness_summary, indent=2) + "\n", encoding="utf-8"
        )
        store.snapshot_database(root / "database" / "pilot.sqlite3")

        manifest = {
            "export_format": "telic-field-witness",
            "export_version": "0.1",
            "created_at": utc_now(),
            "profile": witness_summary["profile"],
            "scope": witness_summary["scope"],
            "provider_independent": True,
            "event_chain": "events/event-chain.json",
            "witness": "witness/reference-witness.json",
            "database_snapshot": "database/pilot.sqlite3",
            "schemas": "schemas/",
            "records": "records/",
            "production_claim": False,
        }
        (root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

        files = [p for p in root.rglob("*") if p.is_file() and p.name != "checksums.txt"]
        (root / "checksums.txt").write_text(
            "\n".join(f"{file_sha256(path)}  {path.relative_to(root).as_posix()}" for path in sorted(files)) + "\n",
            encoding="utf-8",
        )

        with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(root.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(root).as_posix())
    return output_zip


def verify_export(export_zip: Path) -> dict[str, Any]:
    export_zip = Path(export_zip)
    errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix="telic-j0-verify-") as temp_name:
        root = Path(temp_name)
        with zipfile.ZipFile(export_zip) as archive:
            archive.extractall(root)

        checksum_lines = (root / "checksums.txt").read_text(encoding="utf-8").splitlines()
        checked = 0
        for line in checksum_lines:
            if not line.strip():
                continue
            expected, rel = line.split("  ", 1)
            path = root / rel
            if not path.exists():
                errors.append(f"Missing checksummed file: {rel}")
                continue
            actual = file_sha256(path)
            checked += 1
            if actual != expected:
                errors.append(f"Checksum mismatch: {rel}")

        registry = SchemaRegistry(root / "schemas")
        validated_records = 0
        for family in FAMILY_TO_SCHEMA:
            path = root / "records" / f"{family}.json"
            if not path.exists():
                errors.append(f"Missing record family: {family}")
                continue
            records = json.loads(path.read_text(encoding="utf-8"))["records"]
            for record in records:
                try:
                    registry.validate(family, record)
                    validated_records += 1
                except Exception as exc:  # noqa: BLE001
                    errors.append(str(exc))

        chain = json.loads((root / "events" / "event-chain.json").read_text(encoding="utf-8"))["events"]
        expected_prev = "0" * 64
        for item in chain:
            if item["prev_hash"] != expected_prev:
                errors.append(f"Event chain prev_hash mismatch at seq {item['seq']}")
            expected_hash = sha256_text(item["prev_hash"] + "\n" + canonical_json(item["event"]))
            if item["event_hash"] != expected_hash:
                errors.append(f"Event chain hash mismatch at seq {item['seq']}")
            expected_prev = item["event_hash"]

        witness = json.loads((root / "witness" / "reference-witness.json").read_text(encoding="utf-8"))
        proofs = witness.get("proofs", {})
        for proof in ["failed_gate", "valid_action", "consequence_return", "correction_propagation", "retirement_revocation"]:
            if proofs.get(proof) is not True:
                errors.append(f"Missing proof: {proof}")
        if witness.get("conformance_claim", {}).get("profile") != "TF-C4":
            errors.append("Unexpected conformance profile")
        if witness.get("retirement", {}).get("tool_credential_active") is not False:
            errors.append("Retirement did not revoke tool credential")

        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        if manifest.get("provider_independent") is not True:
            errors.append("Export is not marked provider independent")

    return {
        "valid": not errors,
        "errors": errors,
        "checksums_verified": checked,
        "records_validated": validated_records,
        "events_verified": len(chain),
        "proofs": proofs,
    }
