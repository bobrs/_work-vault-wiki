#!/usr/bin/env python3
"""Detect exact duplicate files by content hash from manifest/hash_index.json."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HASH_INDEX_PATH = ROOT / "manifest" / "hash_index.json"
DUPLICATES_PATH = ROOT / "manifest" / "duplicate_sets.json"


def main() -> None:
    if not HASH_INDEX_PATH.exists():
        raise SystemExit("Missing manifest/hash_index.json. Run scripts/inventory.py first.")

    hash_index = json.loads(HASH_INDEX_PATH.read_text(encoding="utf-8"))
    duplicates = {
        digest: paths for digest, paths in hash_index.items() if len(paths) > 1
    }

    DUPLICATES_PATH.write_text(
        json.dumps(duplicates, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print(f"Found {len(duplicates)} duplicate hash groups.")
    print(f"Wrote {DUPLICATES_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
