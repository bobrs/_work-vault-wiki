from __future__ import annotations

import base64
import hashlib
import hmac
import json
import secrets
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

from .canonical import canonical_json, sha256_bytes, utc_now
from .ids import urn


@dataclass(frozen=True)
class GateKey:
    key_id: str
    secret: bytes
    status: str = "active"


class GateKeyRing:
    """Rotatable HMAC keyring for external action-gate tokens."""

    def __init__(self, keys: list[GateKey], active_key_id: str):
        self._keys = {key.key_id: key for key in keys}
        if active_key_id not in self._keys:
            raise ValueError("active key missing")
        self.active_key_id = active_key_id

    @classmethod
    def deterministic_demo(cls) -> "GateKeyRing":
        return cls(
            [
                GateKey("gate-k1", hashlib.sha256(b"telic-j2-gate-key-one").digest(), "revoked"),
                GateKey("gate-k2", hashlib.sha256(b"telic-j2-gate-key-two").digest(), "active"),
            ],
            "gate-k2",
        )

    def rotate(self, key_id: str, secret: bytes | None = None) -> None:
        if self.active_key_id in self._keys:
            prior = self._keys[self.active_key_id]
            self._keys[self.active_key_id] = GateKey(prior.key_id, prior.secret, "superseded")
        self._keys[key_id] = GateKey(key_id, secret or secrets.token_bytes(32), "active")
        self.active_key_id = key_id

    def revoke(self, key_id: str) -> None:
        key = self._keys[key_id]
        self._keys[key_id] = GateKey(key.key_id, key.secret, "revoked")

    def sign(self, payload: dict[str, Any]) -> dict[str, Any]:
        key = self._keys[self.active_key_id]
        if key.status != "active":
            raise ValueError("active signing key is not active")
        encoded = canonical_json(payload).encode("utf-8")
        signature = hmac.new(key.secret, encoded, hashlib.sha256).hexdigest()
        return {"key_id": key.key_id, "payload": payload, "signature": signature}

    def verify(self, token: dict[str, Any]) -> bool:
        key_id = str(token.get("key_id", ""))
        key = self._keys.get(key_id)
        if key is None or key.status == "revoked":
            return False
        encoded = canonical_json(token.get("payload", {})).encode("utf-8")
        expected = hmac.new(key.secret, encoded, hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, str(token.get("signature", "")))

    def public_status(self) -> dict[str, str]:
        return {key_id: key.status for key_id, key in sorted(self._keys.items())}

    def to_private_dict(self) -> dict[str, Any]:
        return {
            "active_key_id": self.active_key_id,
            "keys": [
                {"key_id": key.key_id, "secret": base64.b64encode(key.secret).decode("ascii"), "status": key.status}
                for key in self._keys.values()
            ],
        }

    @classmethod
    def from_private_dict(cls, value: dict[str, Any]) -> "GateKeyRing":
        keys = [
            GateKey(str(item["key_id"]), base64.b64decode(item["secret"]), str(item["status"]))
            for item in value["keys"]
        ]
        return cls(keys, str(value["active_key_id"]))

    @classmethod
    def load_or_create(cls, path: Path) -> "GateKeyRing":
        path = Path(path)
        if path.exists():
            return cls.from_private_dict(json.loads(path.read_text(encoding="utf-8")))
        keyring = cls.deterministic_demo()
        keyring.save(path)
        return keyring

    def save(self, path: Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_private_dict(), indent=2) + "\n", encoding="utf-8")
        path.chmod(0o600)


class ExportSigner:
    """Ed25519 signing for provider-independent witness verification."""

    def __init__(self, private_key: Ed25519PrivateKey, key_id: str):
        self.private_key = private_key
        self.key_id = key_id

    @classmethod
    def generate(cls, key_id: str = "witness-signing-k1") -> "ExportSigner":
        return cls(Ed25519PrivateKey.generate(), key_id)

    @classmethod
    def load_or_create(cls, private_key_path: Path, key_id: str = "witness-signing-k1") -> "ExportSigner":
        private_key_path = Path(private_key_path)
        if private_key_path.exists():
            key = serialization.load_pem_private_key(private_key_path.read_bytes(), password=None)
            if not isinstance(key, Ed25519PrivateKey):
                raise TypeError("Expected Ed25519 private key")
            return cls(key, key_id)
        private_key_path.parent.mkdir(parents=True, exist_ok=True)
        key = Ed25519PrivateKey.generate()
        private_key_path.write_bytes(
            key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )
        private_key_path.chmod(0o600)
        return cls(key, key_id)

    def public_pem(self) -> bytes:
        return self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

    def sign_file(self, file_path: Path, public_key_file: str) -> dict[str, Any]:
        data = Path(file_path).read_bytes()
        digest = sha256_bytes(data)
        signature = self.private_key.sign(data)
        return {
            "signature_id": urn("signature", f"{self.key_id}:{digest}"),
            "algorithm": "Ed25519",
            "key_id": self.key_id,
            "signed_file": Path(file_path).name,
            "signed_digest": digest,
            "signature": base64.b64encode(signature).decode("ascii"),
            "public_key_file": public_key_file,
            "created_at": utc_now(),
            "status": "active",
        }


def verify_ed25519_signature(public_key_pem: bytes, data: bytes, signature_b64: str) -> bool:
    try:
        key = serialization.load_pem_public_key(public_key_pem)
        if not isinstance(key, Ed25519PublicKey):
            return False
        key.verify(base64.b64decode(signature_b64), data)
        return True
    except Exception:
        return False
