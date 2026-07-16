from __future__ import annotations

import base64
import json
import secrets
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

from .canonical import canonical_json, utc_now
from .ids import urn


class AuthenticationError(PermissionError):
    pass


class RoleIdentityRegistry:
    """Small local identity registry for authenticated pilot roles.

    Private keys live only in the run work directory. Public keys and signed role
    assertions may be exported. The registry rejects expired assertions, wrong
    roles, wrong operations, and consumed nonces.
    """

    def __init__(self, directory: Path):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self._private: dict[str, Ed25519PrivateKey] = {}
        self._public: dict[str, Ed25519PublicKey] = {}
        self._roles: dict[str, set[str]] = {}
        self._consumed_nonces: set[str] = set()

    def register(self, actor_id: str, roles: list[str]) -> None:
        safe = actor_id.replace(":", "_").replace("/", "_")
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
        self._private[actor_id] = key
        self._public[actor_id] = key.public_key()
        self._roles[actor_id] = set(roles)

    def issue(
        self,
        *,
        actor_id: str,
        role: str,
        operation: str,
        session_id: str,
        subject: str,
        ttl_seconds: int = 600,
        nonce: str | None = None,
    ) -> dict[str, Any]:
        if actor_id not in self._private:
            raise AuthenticationError("Unknown actor")
        if role not in self._roles.get(actor_id, set()):
            raise AuthenticationError("Actor does not hold requested role")
        issued = datetime.now(timezone.utc).replace(microsecond=0)
        expires = issued + timedelta(seconds=ttl_seconds)
        payload = {
            "assertion_id": urn("role-assertion", f"{actor_id}:{session_id}:{operation}:{nonce or ''}"),
            "actor_id": actor_id,
            "role": role,
            "operation": operation,
            "session_id": session_id,
            "subject": subject,
            "issued_at": issued.isoformat().replace("+00:00", "Z"),
            "expires_at": expires.isoformat().replace("+00:00", "Z"),
            "nonce": nonce or secrets.token_hex(16),
            "status": "active",
        }
        signature = self._private[actor_id].sign(canonical_json(payload).encode("utf-8"))
        return {
            "id": payload["assertion_id"],
            "payload": payload,
            "signature": base64.b64encode(signature).decode("ascii"),
            "algorithm": "Ed25519",
        }

    def verify(
        self,
        assertion: dict[str, Any],
        *,
        required_role: str,
        required_operation: str,
        session_id: str,
        consume_nonce: bool = False,
        now: str | None = None,
    ) -> dict[str, Any]:
        payload = assertion.get("payload") or {}
        actor_id = str(payload.get("actor_id", ""))
        key = self._public.get(actor_id)
        if key is None:
            raise AuthenticationError("Unknown assertion actor")
        try:
            key.verify(
                base64.b64decode(str(assertion.get("signature", ""))),
                canonical_json(payload).encode("utf-8"),
            )
        except Exception as exc:
            raise AuthenticationError("Role assertion signature invalid") from exc
        if payload.get("role") != required_role:
            raise AuthenticationError("Role assertion does not satisfy required role")
        if payload.get("operation") != required_operation:
            raise AuthenticationError("Role assertion does not satisfy required operation")
        if payload.get("session_id") != session_id:
            raise AuthenticationError("Role assertion belongs to another session")
        current = datetime.fromisoformat((now or utc_now()).replace("Z", "+00:00"))
        expiry = datetime.fromisoformat(str(payload.get("expires_at", "1970-01-01T00:00:00Z")).replace("Z", "+00:00"))
        if current > expiry:
            raise AuthenticationError("Role assertion expired")
        nonce = str(payload.get("nonce", ""))
        if not nonce:
            raise AuthenticationError("Role assertion missing nonce")
        if nonce in self._consumed_nonces:
            raise AuthenticationError("Role assertion replay detected")
        if consume_nonce:
            self._consumed_nonces.add(nonce)
        return dict(payload)

    def public_bundle(self) -> dict[str, Any]:
        identities = []
        for actor_id in sorted(self._public):
            pem = self._public[actor_id].public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            ).decode("ascii")
            identities.append({
                "actor_id": actor_id,
                "roles": sorted(self._roles[actor_id]),
                "public_key_pem": pem,
            })
        return {"identities": identities, "created_at": utc_now()}
