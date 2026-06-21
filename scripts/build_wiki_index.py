#!/usr/bin/env python3
"""Build a simple wiki index from the current inventory."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_PATH = ROOT / "manifest" / "inventory.jsonl"
OUT_PATH = ROOT / "wiki" / "artifacts" / "index.md"


def main() -> None:
    if not INVENTORY_PATH.exists():
        raise SystemExit("Missing manifest/inventory.jsonl. Run scripts/inventory.py first.")

    records = []
    for line in INVENTORY_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))

    lines = ["# Artifact Index", "", "Generated from `manifest/inventory.jsonl`.", ""]
    for record in sorted(records, key=lambda r: r["current_path"]):
        path = record["current_path"]
        lines.append(f"- [{path}](../../{path})")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {OUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
