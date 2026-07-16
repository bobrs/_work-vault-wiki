#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path
from typing import Any

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from jsonschema import Draft202012Validator

FAMILY_TO_SCHEMA = {
    "center-standing":"center-standing.schema.json",
    "source-projection-context":"source-projection-context.schema.json",
    "purpose-authority-role":"purpose-authority-role.schema.json",
    "route-gate-action-consequence":"route-gate-action-consequence.schema.json",
    "event-witness-contest-repair":"event-witness-contest-repair.schema.json",
    "lifecycle-transfer-residual":"lifecycle-transfer-residual.schema.json",
    "authorization-policy":"authorization-policy.schema.json",
    "verification-signature":"verification-signature.schema.json",
    "context-revision":"context-revision.schema.json",
    "disclosure-profile":"disclosure-profile.schema.json",
    "correction-reachability":"correction-reachability.schema.json",
    "tool-transaction":"tool-transaction.schema.json",
    "authenticated-role-session":"authenticated-role-session.schema.json",
    "threshold-approval":"threshold-approval.schema.json",
    "policy-migration":"policy-migration.schema.json",
    "queue-delivery":"queue-delivery.schema.json",
    "multi-party-correction":"multi-party-correction.schema.json",
    "external-review-finding":"external-review-finding.schema.json",
    "accessibility-test-run":"accessibility-test-run.schema.json",
    "privacy-review-finding":"privacy-review-finding.schema.json",
    "release-candidate-manifest":"release-candidate-manifest.schema.json",
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_extract(archive: zipfile.ZipFile, root: Path) -> None:
    base = root.resolve()
    for member in archive.infolist():
        target = (root / member.filename).resolve()
        if target != base and base not in target.parents:
            raise ValueError(f"Unsafe path in archive: {member.filename}")
    archive.extractall(root)


def verify_signature(public_key_pem: bytes, data: bytes, signature_b64: str) -> bool:
    try:
        key = serialization.load_pem_public_key(public_key_pem)
        if not isinstance(key, Ed25519PublicKey):
            return False
        key.verify(base64.b64decode(signature_b64), data)
        return True
    except Exception:
        return False


def verify(export_zip: Path) -> dict[str, Any]:
    errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix="telic-j2-independent-") as temp_name:
        root = Path(temp_name)
        with zipfile.ZipFile(export_zip) as archive:
            safe_extract(archive, root)

        checked = 0
        for line in (root / "checksums.txt").read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            expected, rel = line.split("  ", 1)
            path = root / rel
            if not path.exists():
                errors.append(f"Missing file: {rel}")
                continue
            checked += 1
            if file_sha256(path) != expected:
                errors.append(f"Checksum mismatch: {rel}")

        manifest_path = root / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        signature = json.loads((root / manifest["verification_signature"]).read_text(encoding="utf-8"))
        if signature["signed_digest"] != file_sha256(manifest_path):
            errors.append("Signed manifest digest mismatch")
        if not verify_signature((root / manifest["public_key"]).read_bytes(), manifest_path.read_bytes(), signature["signature"]):
            errors.append("Ed25519 signature verification failed")

        validators = {}
        for family, filename in FAMILY_TO_SCHEMA.items():
            schema = json.loads((root / "schemas" / filename).read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            validators[family] = Draft202012Validator(schema)

        validated = 0
        for family, validator in validators.items():
            path = root / "records" / f"{family}.json"
            if not path.exists():
                continue
            for record in json.loads(path.read_text(encoding="utf-8"))["records"]:
                for error in validator.iter_errors(record):
                    errors.append(f"{family}: {error.message}")
                validated += 1

        index = json.loads((root / "records" / "object-index.json").read_text(encoding="utf-8"))["objects"]
        commitments = {item["object_id"]:item["object_hash"] for item in index}
        for audience, rel in manifest["selective_views"].items():
            view = json.loads((root / rel).read_text(encoding="utf-8"))
            for omitted in view["omitted_commitments"]:
                if commitments.get(omitted["object_id"]) != omitted["commitment"]:
                    errors.append(f"{audience} commitment mismatch: {omitted['object_id']}")
            if audience == "public" and "daytime transit is inaccessible" in json.dumps(view):
                errors.append("Public view leaked protected source content")

        chain = json.loads((root / manifest["event_chain"]).read_text(encoding="utf-8"))["events"]
        previous = "0" * 64
        for item in chain:
            if item["prev_hash"] != previous:
                errors.append(f"Chain predecessor mismatch at {item['seq']}")
            expected = sha256_text(item["prev_hash"] + "\n" + canonical_json(item["event"]))
            if item["event_hash"] != expected:
                errors.append(f"Chain hash mismatch at {item['seq']}")
            previous = item["event_hash"]

        witness = json.loads((root / manifest["witness"]).read_text(encoding="utf-8"))
        required = [
            "failed_gate","valid_action","consequence_return","correction_propagation",
            "retirement_revocation","stale_context_rejection","policy_version_enforcement",
            "key_rotation","partial_failure_compensation","selective_disclosure",
        ]
        for proof in required:
            if witness.get("proofs", {}).get(proof) is not True:
                errors.append(f"Missing proof: {proof}")
        if manifest.get("provider_independent") is not True:
            errors.append("Provider-independent flag missing")

    return {
        "valid":not errors,
        "errors":errors,
        "checksums_verified":checked,
        "records_validated":validated,
        "events_verified":len(chain),
        "views_verified":len(manifest["selective_views"]),
        "signature_verified":not any("signature" in error.lower() or "digest" in error.lower() for error in errors),
        "verifier":"standalone-no-telic-j2-import",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Independent verifier for Telic Fields J.2 witness exports")
    parser.add_argument("export", type=Path)
    args = parser.parse_args()
    result = verify(args.export)
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
