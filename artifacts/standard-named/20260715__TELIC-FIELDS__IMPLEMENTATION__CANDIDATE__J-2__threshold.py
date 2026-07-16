from __future__ import annotations

import base64
from pathlib import Path
from typing import Any

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

from .canonical import canonical_json, utc_now
from .ids import urn


class ThresholdApprovalError(PermissionError):
    pass


class ThresholdCustody:
    """Independent-key M-of-N release approval.

    This avoids reconstructing one shared private key. Each custodian signs the
    exact release digest. A release is valid only when the configured threshold
    of distinct, active custodians approves the same digest.
    """

    def __init__(self, directory: Path, custodians: dict[str, str], threshold: int = 2):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.threshold = threshold
        self.roles = dict(custodians)
        self._private: dict[str, Ed25519PrivateKey] = {}
        self._public: dict[str, Ed25519PublicKey] = {}
        self._status: dict[str, str] = {}
        for custodian_id in sorted(custodians):
            self._load_or_create(custodian_id)

    def _load_or_create(self, custodian_id: str) -> None:
        safe = custodian_id.replace(":", "_").replace("/", "_")
        path = self.directory / f"{safe}.pem"
        if path.exists():
            key = serialization.load_pem_private_key(path.read_bytes(), password=None)
            if not isinstance(key, Ed25519PrivateKey):
                raise TypeError("Expected Ed25519 private key")
        else:
            key = Ed25519PrivateKey.generate()
            path.write_bytes(
                key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )
            path.chmod(0o600)
        self._private[custodian_id] = key
        self._public[custodian_id] = key.public_key()
        self._status[custodian_id] = "active"

    def revoke(self, custodian_id: str) -> None:
        self._status[custodian_id] = "revoked"

    def approve(self, *, custodian_id: str, release_id: str, manifest_digest: str, approved_at: str | None = None) -> dict[str, Any]:
        if self._status.get(custodian_id) != "active":
            raise ThresholdApprovalError("Custodian is not active")
        payload = {
            "approval_id": urn("release-approval", f"{release_id}:{custodian_id}:{manifest_digest}"),
            "release_id": release_id,
            "manifest_digest": manifest_digest,
            "custodian_id": custodian_id,
            "custodian_role": self.roles[custodian_id],
            "approved_at": approved_at or utc_now(),
            "status": "active",
        }
        signature = self._private[custodian_id].sign(canonical_json(payload).encode("utf-8"))
        return {
            "payload": payload,
            "signature": base64.b64encode(signature).decode("ascii"),
            "algorithm": "Ed25519",
        }

    def verify_threshold(self, approvals: list[dict[str, Any]], *, release_id: str, manifest_digest: str) -> dict[str, Any]:
        valid: list[str] = []
        errors: list[str] = []
        seen: set[str] = set()
        for approval in approvals:
            payload = approval.get("payload") or {}
            custodian_id = str(payload.get("custodian_id", ""))
            if custodian_id in seen:
                errors.append(f"duplicate custodian: {custodian_id}")
                continue
            seen.add(custodian_id)
            key = self._public.get(custodian_id)
            if key is None or self._status.get(custodian_id) != "active":
                errors.append(f"unknown or inactive custodian: {custodian_id}")
                continue
            if payload.get("release_id") != release_id or payload.get("manifest_digest") != manifest_digest:
                errors.append(f"scope mismatch: {custodian_id}")
                continue
            try:
                key.verify(
                    base64.b64decode(str(approval.get("signature", ""))),
                    canonical_json(payload).encode("utf-8"),
                )
                valid.append(custodian_id)
            except Exception:
                errors.append(f"invalid signature: {custodian_id}")
        return {
            "valid": len(valid) >= self.threshold,
            "threshold": self.threshold,
            "valid_custodians": sorted(valid),
            "errors": errors,
        }

    def public_bundle(self) -> dict[str, Any]:
        records = []
        for custodian_id in sorted(self._public):
            records.append({
                "custodian_id": custodian_id,
                "role": self.roles[custodian_id],
                "status": self._status[custodian_id],
                "public_key_pem": self._public[custodian_id].public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                ).decode("ascii"),
            })
        return {"threshold": self.threshold, "custodians": records}
