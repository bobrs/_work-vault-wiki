from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import Any

from .canonical import canonical_json, sha256_text, utc_now
from .crypto import ExportSigner, verify_ed25519_signature
from .disclosure import build_selective_view
from .event_store import EventStore
from .schemas import FAMILY_TO_SCHEMA, SchemaRegistry


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_extract(archive: zipfile.ZipFile, root: Path) -> None:
    root_resolved = root.resolve()
    for member in archive.infolist():
        target = (root / member.filename).resolve()
        if root_resolved not in target.parents and target != root_resolved:
            raise ValueError(f"Unsafe archive path: {member.filename}")
    archive.extractall(root)


def export_witness(
    *,
    store: EventStore,
    schema_dir: Path,
    output_zip: Path,
    witness_summary: dict[str, Any],
    disclosure_profiles: list[dict[str, Any]],
    signer: ExportSigner,
    participant_id: str,
) -> Path:
    output_zip = Path(output_zip)
    output_zip.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="telic-j2-export-") as temp_name:
        root = Path(temp_name)
        for rel in ["schemas","records","events","witness","database","views","verification"]:
            (root / rel).mkdir(parents=True, exist_ok=True)

        for schema_path in Path(schema_dir).glob("*.json"):
            shutil.copy2(schema_path, root / "schemas" / schema_path.name)

        objects = store.list_objects()
        by_family: dict[str, list[dict[str, Any]]] = {}
        object_index = []
        for item in objects:
            by_family.setdefault(item["family"], []).append(item["record"])
            object_index.append({
                "object_id":item["object_id"],
                "family":item["family"],
                "object_hash":item["object_hash"],
                "revision":item["revision"],
            })
        for family, records in sorted(by_family.items()):
            (root / "records" / f"{family}.json").write_text(
                json.dumps({"records":records}, indent=2) + "\n", encoding="utf-8"
            )
        (root / "records" / "object-index.json").write_text(
            json.dumps({"objects":object_index}, indent=2) + "\n", encoding="utf-8"
        )

        events = store.list_events()
        (root / "events" / "event-chain.json").write_text(
            json.dumps({"events":events}, indent=2) + "\n", encoding="utf-8"
        )
        (root / "witness" / "reference-witness.json").write_text(
            json.dumps(witness_summary, indent=2) + "\n", encoding="utf-8"
        )
        store.snapshot_database(root / "database" / "pilot.sqlite3")

        view_files: dict[str, str] = {}
        for profile in disclosure_profiles:
            view = build_selective_view(
                profile=profile,
                objects=objects,
                participant_id=participant_id if profile["audience"] == "participant" else None,
            )
            filename = f"{profile['audience']}-view.json"
            (root / "views" / filename).write_text(json.dumps(view, indent=2) + "\n", encoding="utf-8")
            view_files[profile["audience"]] = f"views/{filename}"

        manifest = {
            "export_format":"telic-field-witness",
            "export_version":"0.2",
            "created_at":utc_now(),
            "profile":witness_summary["conformance_claim"]["profile"],
            "bounded_extension":witness_summary["conformance_claim"]["bounded_extension"],
            "scope":witness_summary["scope"],
            "provider_independent":True,
            "event_chain":"events/event-chain.json",
            "witness":"witness/reference-witness.json",
            "database_snapshot":"database/pilot.sqlite3",
            "schemas":"schemas/",
            "records":"records/",
            "selective_views":view_files,
            "verification_signature":"verification/manifest-signature.json",
            "public_key":"verification/witness-public-key.pem",
            "production_claim":False,
        }
        manifest_path = root / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        public_key_rel = "verification/witness-public-key.pem"
        (root / public_key_rel).write_bytes(signer.public_pem())
        signature = signer.sign_file(manifest_path, public_key_rel)
        (root / "verification" / "manifest-signature.json").write_text(
            json.dumps(signature, indent=2) + "\n", encoding="utf-8"
        )

        files = [p for p in root.rglob("*") if p.is_file() and p.name != "checksums.txt"]
        (root / "checksums.txt").write_text(
            "\n".join(f"{file_sha256(path)}  {path.relative_to(root).as_posix()}" for path in sorted(files)) + "\n",
            encoding="utf-8",
        )
        if output_zip.exists():
            output_zip.unlink()
        with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(root.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(root).as_posix())
    return output_zip


def verify_export(export_zip: Path) -> dict[str, Any]:
    errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix="telic-j2-verify-") as temp_name:
        root = Path(temp_name)
        with zipfile.ZipFile(export_zip) as archive:
            _safe_extract(archive, root)

        checked = 0
        for line in (root / "checksums.txt").read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            expected, rel = line.split("  ", 1)
            path = root / rel
            if not path.exists():
                errors.append(f"Missing checksummed file: {rel}")
                continue
            checked += 1
            if file_sha256(path) != expected:
                errors.append(f"Checksum mismatch: {rel}")

        manifest_path = root / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        signature = json.loads((root / manifest["verification_signature"]).read_text(encoding="utf-8"))
        public_key = (root / manifest["public_key"]).read_bytes()
        if signature.get("signed_digest") != file_sha256(manifest_path):
            errors.append("Manifest digest does not match signature record")
        if not verify_ed25519_signature(public_key, manifest_path.read_bytes(), signature.get("signature", "")):
            errors.append("Manifest Ed25519 signature invalid")

        registry = SchemaRegistry(root / "schemas")
        validated_records = 0
        full_objects: dict[str, dict[str, Any]] = {}
        for family in FAMILY_TO_SCHEMA:
            path = root / "records" / f"{family}.json"
            if not path.exists():
                continue
            for record in json.loads(path.read_text(encoding="utf-8"))["records"]:
                try:
                    registry.validate(family, record)
                    validated_records += 1
                    object_id = (
                        record.get("id") or record.get("event_id") or record.get("context_id")
                        or record.get("profile_id") or record.get("report_id") or record.get("transaction_id")
                        or record.get("policy_id") or record.get("signature_id") or record.get("correction_id")
                        or record.get("migration_id") or record.get("delivery_id") or record.get("finding_id")
                        or record.get("review_id") or record.get("run_id") or record.get("release_id")
                    )
                    if object_id:
                        full_objects[str(object_id)] = {"family":family,"record":record}
                except Exception as exc:
                    errors.append(str(exc))

        index = json.loads((root / "records" / "object-index.json").read_text(encoding="utf-8"))["objects"]
        index_hashes = {item["object_id"]:item["object_hash"] for item in index}
        for object_id, item in full_objects.items():
            actual = sha256_text(canonical_json(item["record"]))
            if index_hashes.get(object_id) != actual:
                errors.append(f"Object commitment mismatch: {object_id}")

        chain = json.loads((root / "events" / "event-chain.json").read_text(encoding="utf-8"))["events"]
        expected_prev = "0" * 64
        for item in chain:
            if item["prev_hash"] != expected_prev:
                errors.append(f"Event chain prev_hash mismatch at seq {item['seq']}")
            expected_hash = sha256_text(item["prev_hash"] + "\n" + canonical_json(item["event"]))
            if item["event_hash"] != expected_hash:
                errors.append(f"Event chain hash mismatch at seq {item['seq']}")
            expected_prev = item["event_hash"]

        for audience, rel in manifest.get("selective_views", {}).items():
            view = json.loads((root / rel).read_text(encoding="utf-8"))
            for omitted in view["omitted_commitments"]:
                if index_hashes.get(omitted["object_id"]) != omitted["commitment"]:
                    errors.append(f"Selective-view commitment mismatch in {audience}: {omitted['object_id']}")
            if audience == "public":
                serialized = json.dumps(view, sort_keys=True)
                if "daytime transit is inaccessible" in serialized:
                    errors.append("Public view leaked direct protected source content")
                if '"training_use": false' in serialized.lower():
                    errors.append("Public view leaked participant-specific consent detail")

        witness = json.loads((root / manifest["witness"]).read_text(encoding="utf-8"))
        proofs = witness.get("proofs", {})
        required_proofs = [
            "failed_gate","valid_action","consequence_return","correction_propagation",
            "retirement_revocation","stale_context_rejection","policy_version_enforcement",
            "key_rotation","partial_failure_compensation","selective_disclosure",
        ]
        for proof in required_proofs:
            if proofs.get(proof) is not True:
                errors.append(f"Missing proof: {proof}")
        if manifest.get("provider_independent") is not True:
            errors.append("Export not marked provider independent")

    return {
        "valid":not errors,
        "errors":errors,
        "checksums_verified":checked,
        "records_validated":validated_records,
        "events_verified":len(chain),
        "views_verified":len(manifest.get("selective_views", {})),
        "manifest_signature_valid":not any("signature" in e.lower() or "digest" in e.lower() for e in errors),
        "proofs":proofs,
    }
