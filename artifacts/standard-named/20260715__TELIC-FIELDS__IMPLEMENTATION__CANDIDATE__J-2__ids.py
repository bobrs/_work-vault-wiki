from __future__ import annotations

import uuid


def urn(kind: str, seed: str) -> str:
    value = uuid.uuid5(uuid.NAMESPACE_URL, f"telic-j2:{kind}:{seed}")
    return f"urn:telic:j2:{kind}:{value}"
