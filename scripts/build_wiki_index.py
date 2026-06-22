#!/usr/bin/env python3
"""Build a grouped wiki index from the current artifact inventory."""

from __future__ import annotations

import json
from collections import defaultdict
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_PATH = ROOT / "manifest" / "inventory.jsonl"
OUT_PATH = ROOT / "wiki" / "artifacts" / "index.md"


def make_node() -> dict:
    return {"dirs": defaultdict(make_node), "files": []}


def add_record(root: dict, record: dict) -> None:
    parts = Path(record["current_path"]).parts[1:]
    node = root
    for part in parts[:-1]:
        node = node["dirs"][part]
    node["files"].append(record)


def subtree_count(node: dict) -> int:
    return len(node["files"]) + sum(subtree_count(child) for child in node["dirs"].values())


def file_link(path: str) -> str:
    encoded = "/".join(quote(part, safe="") for part in Path(path).parts)
    return f"../../{encoded}"


def preferred_path(record: dict) -> str:
    standard_named_path = record.get("standard_named_path")
    if standard_named_path:
        return standard_named_path
    return record["current_path"]


def file_label(record: dict) -> str:
    current_path = record["current_path"]
    preferred = preferred_path(record)
    if preferred != current_path:
        return f"{current_path} -> {preferred}"
    return current_path


def render_node(name: str, node: dict, level: int, lines: list[str]) -> None:
    count = subtree_count(node)
    lines.append("")
    lines.append(f"{'#' * level} {name} ({count})")

    if node["files"]:
        lines.append("")
        lines.append(f"Direct files ({len(node['files'])})")
        for record in sorted(node["files"], key=lambda r: r["current_path"]):
            path = preferred_path(record)
            lines.append(f"- [{file_label(record)}]({file_link(path)})")

    for child_name in sorted(node["dirs"]):
        render_node(child_name, node["dirs"][child_name], min(level + 1, 6), lines)


def main() -> None:
    if not INVENTORY_PATH.exists():
        raise SystemExit("Missing manifest/inventory.jsonl. Run scripts/inventory.py first.")

    records = []
    for line in INVENTORY_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))

    artifact_records = [record for record in records if record["current_path"].startswith("artifacts/")]

    lines = [
        "# Artifact Index",
        "",
        "Generated from `manifest/inventory.jsonl`.",
        "",
        "Where available, links prefer standard-named source files while preserving the inbound path in the label.",
        "",
    ]
    if not artifact_records:
        lines.append("No artifact files have been added yet.")
    else:
        root = make_node()
        for record in artifact_records:
            add_record(root, record)
        for name in sorted(root["dirs"]):
            render_node(name, root["dirs"][name], 2, lines)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {OUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
