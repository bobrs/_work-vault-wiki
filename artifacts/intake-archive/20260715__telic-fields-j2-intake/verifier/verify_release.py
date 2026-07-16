#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from verify_witness import verify as verify_witness


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(Path(path).read_bytes())


def safe_extract(archive: zipfile.ZipFile, root: Path) -> None:
    base = root.resolve()
    for member in archive.infolist():
        target = (root / member.filename).resolve()
        if target != base and base not in target.parents:
            raise ValueError(f"Unsafe archive path: {member.filename}")
    archive.extractall(root)


def verify_signature(public_key_pem: str, payload: dict, signature_b64: str) -> bool:
    try:
        key = serialization.load_pem_public_key(public_key_pem.encode("ascii"))
        if not isinstance(key, Ed25519PublicKey):
            return False
        key.verify(base64.b64decode(signature_b64), canonical_json(payload).encode("utf-8"))
        return True
    except Exception:
        return False


def verify_release(path: Path) -> dict:
    errors = []
    with tempfile.TemporaryDirectory(prefix="telic-j2-release-verify-") as temp_name:
        root = Path(temp_name)
        with zipfile.ZipFile(path) as archive:
            safe_extract(archive, root)

        private_candidates = [
            item.relative_to(root).as_posix()
            for item in root.rglob("*")
            if item.is_file() and (
                item.suffix.lower() in {".key", ".p12", ".pfx"}
                or "private" in item.name.lower()
                or "private" in item.parent.name.lower()
            )
        ]
        if private_candidates:
            errors.append(f"Private-key-like files included: {private_candidates}")

        manifest_path = root / "release-manifest.json"
        approvals_path = root / "release-approvals.json"
        if not manifest_path.exists() or not approvals_path.exists():
            errors.append("Release manifest or approvals missing")
            return {"valid": False, "errors": errors}
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        approvals = json.loads(approvals_path.read_text(encoding="utf-8"))
        manifest_digest = sha256_file(manifest_path)
        if approvals.get("manifest_digest") != manifest_digest:
            errors.append("Approval manifest digest mismatch")
        if manifest.get("private_key_material_included") is not False:
            errors.append("Manifest does not explicitly exclude private key material")
        if manifest.get("production_claim") is not False:
            errors.append("Release candidate makes a production claim")
        if manifest.get("external_human_review_complete") is not False:
            errors.append("Release candidate incorrectly claims external human review complete")

        checked = 0
        for item in manifest.get("files", []):
            rel = str(item["path"])
            file_path = root / rel
            if not file_path.exists():
                errors.append(f"Manifest file missing: {rel}")
                continue
            checked += 1
            if sha256_file(file_path) != item.get("sha256"):
                errors.append(f"Manifest checksum mismatch: {rel}")
            if file_path.stat().st_size != item.get("size"):
                errors.append(f"Manifest size mismatch: {rel}")

        public = {
            item["custodian_id"]: item
            for item in approvals.get("public_custody", {}).get("custodians", [])
        }
        valid_custodians = set()
        for approval in approvals.get("approvals", []):
            payload = approval.get("payload") or {}
            custodian_id = str(payload.get("custodian_id", ""))
            public_record = public.get(custodian_id)
            if not public_record or public_record.get("status") != "active":
                errors.append(f"Unknown or inactive custodian approval: {custodian_id}")
                continue
            if payload.get("release_id") != manifest.get("release_id"):
                errors.append(f"Release scope mismatch: {custodian_id}")
                continue
            if payload.get("manifest_digest") != manifest_digest:
                errors.append(f"Approval digest mismatch: {custodian_id}")
                continue
            if not verify_signature(public_record["public_key_pem"], payload, approval.get("signature", "")):
                errors.append(f"Invalid approval signature: {custodian_id}")
                continue
            valid_custodians.add(custodian_id)
        threshold = int(approvals.get("threshold", 0))
        if len(valid_custodians) < threshold:
            errors.append(f"Release approval threshold not met: {len(valid_custodians)}/{threshold}")

        witness_path = root / "exports" / "tf-mvi-1-j2-witness.zip"
        witness_result = None
        if witness_path.exists():
            witness_result = verify_witness(witness_path)
            if not witness_result.get("valid"):
                errors.append("Nested witness verification failed")
        else:
            errors.append("Nested J.2 witness missing")

    return {
        "valid": not errors,
        "errors": errors,
        "manifest_files_verified": checked,
        "valid_release_custodians": sorted(valid_custodians),
        "threshold": threshold,
        "private_key_material_found": private_candidates,
        "nested_witness": witness_result,
        "verifier": "standalone-release-verifier-no-telic-j2-import",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Telic Fields J.2 release candidate")
    parser.add_argument("release", type=Path)
    args = parser.parse_args()
    result = verify_release(args.release)
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
