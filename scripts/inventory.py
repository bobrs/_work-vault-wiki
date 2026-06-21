#!/usr/bin/env python3
"""Minimal Work Vault inventory script.

Observes files and writes manifest/inventory.jsonl plus manifest/hash_index.json.
Does not move, rename, delete, merge, or rewrite artifacts.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORE_PREFIXES = (".git", ".DS_Store", "__pycache__", ".vault/cache")
INVENTORY_PATH = ROOT / "manifest" / "inventory.jsonl"
HASH_INDEX_PATH = ROOT / "manifest" / "hash_index.json"


def should_skip(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return any(rel == prefix or rel.startswith(f"{prefix}/") for prefix in IGNORE_PREFIXES)


def record_kind_for(rel: str) -> str:
    if rel.startswith("artifacts/"):
        return "artifact"
    if rel.startswith("wiki/"):
        return "wiki"
    if rel.startswith("manifest/"):
        return "manifest"
    if rel.startswith("scripts/"):
        return "script"
    if rel.startswith("agents/"):
        return "agent_instruction"
    if rel.startswith(".vault/"):
        return "vault_config"
    if rel.startswith("docs/") or rel in {"README.md", "WIKI.md"}:
        return "documentation"
    return "other"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iso_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat()


def main() -> None:
    records = []
    hash_index = {}

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or should_skip(path):
            continue
        rel = path.relative_to(ROOT).as_posix()
        content_hash = sha256_file(path)
        artifact_id = f"sha256:{content_hash}"
        record = {
            "artifact_id": artifact_id,
            "current_path": rel,
            "record_kind": record_kind_for(rel),
            "filename": path.name,
            "extension": path.suffix,
            "size_bytes": path.stat().st_size,
            "content_hash": content_hash,
            "modified_time": iso_mtime(path),
            "status": "inventoried",
            "classification": None,
            "domain": None,
            "project": None,
            "wiki_page": None,
            "duplicate_group": None,
            "lineage": [],
        }
        records.append(record)
        hash_index.setdefault(content_hash, []).append(rel)

    INVENTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with INVENTORY_PATH.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

    with HASH_INDEX_PATH.open("w", encoding="utf-8") as f:
        json.dump(hash_index, f, ensure_ascii=False, indent=2, sort_keys=True)

    print(f"Inventoried {len(records)} files.")
    print(f"Wrote {INVENTORY_PATH.relative_to(ROOT)}")
    print(f"Wrote {HASH_INDEX_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
