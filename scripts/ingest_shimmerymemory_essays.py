#!/usr/bin/env python3
"""Ingest the published Shimmery Memory essay index as external wiki metadata.

This script treats the feed as `published_external` material, not intake archive
material and not standard-named source material.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "manifest" / "external_sources.json"
INDEX_PATH = ROOT / "manifest" / "external_published_index.jsonl"
LOG_PATH = ROOT / "manifest" / "external_ingest_log.jsonl"
WIKI_ROOT = ROOT / "wiki" / "external" / "shimmerymemory" / "essays"
WORK_VAULT_INDEX = ROOT / "wiki" / "index.md"
PAGE_MARKER = "<!-- BEGIN HUMAN / AI SALIENCE NOTES -->"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def fail(message: str) -> "NoReturn":
    raise SystemExit(f"Shimmery Memory ingest failed: {message}")


def load_config(source_id: str) -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        fail(f"missing config file at {CONFIG_PATH.relative_to(ROOT)}")
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    sources = config.get("sources")
    if not isinstance(sources, list):
        fail("manifest/external_sources.json must contain a top-level `sources` array")
    for source in sources:
        if isinstance(source, dict) and source.get("source_id") == source_id:
            return source
    fail(f"no source config found for {source_id!r}")


def fetch_json(endpoint: str) -> dict[str, Any]:
    request = urllib.request.Request(
        endpoint,
        headers={
            "Accept": "application/json",
            "Cache-Control": "no-cache",
            "User-Agent": "Work Vault External Ingest/1.0 (+https://github.com/bobrs/_work-vault-wiki)",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        fail(f"unable to fetch {endpoint}: {exc}")
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        fail(f"endpoint returned invalid JSON: {exc}")
    if not isinstance(data, dict):
        fail("top-level response must be a JSON object")
    return data


def ensure(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def validate_date(value: Any, field: str, item_id: str | None = None) -> None:
    ensure(isinstance(value, str), f"{field} must be a string{f' for {item_id}' if item_id else ''}")
    ensure(
        re.fullmatch(r"\d{4}-\d{2}-\d{2}", value) is not None,
        f"{field} must use YYYY-MM-DD format{f' for {item_id}' if item_id else ''}",
    )


def validate_glyphs(value: Any, item_id: str) -> None:
    ensure(isinstance(value, list), f"canonical_glyphs must be a list for {item_id}")
    for idx, glyph in enumerate(value):
        ensure(isinstance(glyph, dict), f"canonical_glyphs[{idx}] must be an object for {item_id}")
        ensure(set(glyph.keys()) == {"name", "glyph"}, f"canonical_glyphs[{idx}] must contain only name/glyph for {item_id}")
        ensure(isinstance(glyph["name"], str) and glyph["name"], f"canonical_glyphs[{idx}].name must be a non-empty string for {item_id}")
        ensure(isinstance(glyph["glyph"], str) and glyph["glyph"], f"canonical_glyphs[{idx}].glyph must be a non-empty string for {item_id}")


def validate_invariants(value: Any, item_id: str) -> None:
    ensure(isinstance(value, list), f"related_invariants must be a list for {item_id}")
    for idx, invariant in enumerate(value):
        ensure(isinstance(invariant, dict), f"related_invariants[{idx}] must be an object for {item_id}")
        ensure(
            set(invariant.keys()) == {"label", "url", "site", "type"},
            f"related_invariants[{idx}] must contain only label/url/site/type for {item_id}",
        )
        ensure(isinstance(invariant["label"], str) and invariant["label"], f"related_invariants[{idx}].label must be a non-empty string for {item_id}")
        ensure(isinstance(invariant["url"], str) and invariant["url"].startswith("https://"), f"related_invariants[{idx}].url must be an https URL for {item_id}")
        ensure(isinstance(invariant["site"], str) and invariant["site"], f"related_invariants[{idx}].site must be a non-empty string for {item_id}")
        ensure(isinstance(invariant["type"], str) and invariant["type"], f"related_invariants[{idx}].type must be a non-empty string for {item_id}")


def validate_feed(data: dict[str, Any], config: dict[str, Any]) -> None:
    expected_top_level = set(config["expected_top_level_keys"])
    ensure(set(data.keys()) == expected_top_level, f"top-level keys changed: expected {sorted(expected_top_level)}")
    ensure(data["site"] == config["name"], f"site must be {config['name']!r}")
    ensure(data["base_url"] == config["base_url"], f"base_url must be {config['base_url']!r}")
    ensure(data["endpoint"] == config["endpoint"], f"endpoint must be {config['endpoint']!r}")
    ensure(data["schema_version"] == config["schema_version"], f"schema_version must be {config['schema_version']!r}")
    ensure(data["machine_invitation"] is True, "machine_invitation must be true")
    ensure(isinstance(data["item_count"], int), "item_count must be an integer")
    ensure(isinstance(data["items"], list), "items must be a list")
    ensure(data["item_count"] == len(data["items"]), "item_count must match len(items)")
    ensure(data["item_count"] > 0, "items must not be empty")
    expected_item_keys = set(config["required_item_keys"])
    for index, item in enumerate(data["items"]):
        item_id = f"items[{index}]"
        ensure(isinstance(item, dict), f"{item_id} must be an object")
        ensure(set(item.keys()) == expected_item_keys, f"{item_id} keys changed")
        ensure(isinstance(item["id"], str) and item["id"], f"{item_id}.id must be a non-empty string")
        ensure(isinstance(item["type"], str) and item["type"] == "essay", f"{item_id}.type must be 'essay'")
        ensure(isinstance(item["title"], str) and item["title"], f"{item_id}.title must be a non-empty string")
        ensure(item["subtitle"] is None or isinstance(item["subtitle"], str), f"{item_id}.subtitle must be null or a string")
        ensure(isinstance(item["description"], str), f"{item_id}.description must be a string")
        ensure(isinstance(item["excerpt"], str), f"{item_id}.excerpt must be a string")
        ensure(isinstance(item["url"], str) and item["url"].startswith("https://"), f"{item_id}.url must be an https URL")
        ensure(isinstance(item["canonical_url"], str) and item["canonical_url"].startswith("https://"), f"{item_id}.canonical_url must be an https URL")
        ensure(isinstance(item["slug"], str) and item["slug"], f"{item_id}.slug must be a non-empty string")
        ensure(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", item["slug"]) is not None, f"{item_id}.slug contains unsupported path characters")
        validate_date(item["published_date"], f"{item_id}.published_date", item["slug"])
        validate_date(item["updated_date"], f"{item_id}.updated_date", item["slug"])
        ensure(isinstance(item["author"], str) and item["author"], f"{item_id}.author must be a non-empty string")
        ensure(isinstance(item["source"], str) and item["source"] == config["name"], f"{item_id}.source must be {config['name']!r}")
        ensure(isinstance(item["tags"], list) and all(isinstance(tag, str) and tag for tag in item["tags"]), f"{item_id}.tags must be a list of non-empty strings")
        validate_glyphs(item["canonical_glyphs"], item["slug"])
        validate_invariants(item["related_invariants"], item["slug"])
        ensure(
            item["artifact_spine_filename"] is None or isinstance(item["artifact_spine_filename"], str),
            f"{item_id}.artifact_spine_filename must be null or a string",
        )
        ensure(
            item["content_hash"] is None or isinstance(item["content_hash"], str),
            f"{item_id}.content_hash must be null or a string",
        )
        ensure(isinstance(item["language"], str) and item["language"], f"{item_id}.language must be a non-empty string")
        ensure(isinstance(item["license"], str) and item["license"], f"{item_id}.license must be a non-empty string")
        ensure(isinstance(item["machine_invitation"], bool) and item["machine_invitation"] is True, f"{item_id}.machine_invitation must be true")
        ensure(isinstance(item["status"], str) and item["status"], f"{item_id}.status must be a non-empty string")
        ensure(item["source_path"] is None or isinstance(item["source_path"], str), f"{item_id}.source_path must be null or a string")
        ensure(isinstance(item["visibility"], str) and item["visibility"], f"{item_id}.visibility must be a non-empty string")
        ensure(isinstance(item["word_count"], int) and item["word_count"] >= 0, f"{item_id}.word_count must be a non-negative integer")


def load_existing_index() -> dict[str, dict[str, Any]]:
    if not INDEX_PATH.exists():
        return {}
    records: dict[str, dict[str, Any]] = {}
    for line in INDEX_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        item_id = record.get("item_id")
        if isinstance(item_id, str):
            records[item_id] = record
    return records


def relpath(from_path: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, start=from_path.parent).replace(os.sep, "/")


def split_preserved_notes(existing: str | None) -> str:
    if not existing or PAGE_MARKER not in existing:
        return ""
    return existing.split(PAGE_MARKER, 1)[1]


def format_tags(tags: list[str]) -> str:
    return ", ".join(f"`{tag}`" for tag in tags) if tags else "None listed"


def format_glyphs(glyphs: list[dict[str, str]]) -> list[str]:
    if not glyphs:
        return ["- None listed"]
    return [f"- `{glyph['name']}`: {glyph['glyph']}" for glyph in glyphs]


def format_invariants(invariants: list[dict[str, str]]) -> list[str]:
    if not invariants:
        return ["- None listed"]
    lines = []
    for invariant in invariants:
        label = invariant["label"]
        url = invariant["url"]
        site = invariant["site"]
        inv_type = invariant["type"]
        lines.append(f"- [{label}]({url}) · {site} · {inv_type}")
    return lines


def display_optional(value: Any) -> str:
    if value is None:
        return "None listed"
    return str(value)


def format_item_page(item: dict[str, Any], record: dict[str, Any], existing_notes: str = "") -> str:
    page_path = WIKI_ROOT / item["slug"] / "index.md"
    index_link = relpath(page_path, WIKI_ROOT / "index.md")
    wiki_root_link = relpath(page_path, WORK_VAULT_INDEX)
    canonical_glyph_lines = format_glyphs(item["canonical_glyphs"])
    invariant_lines = format_invariants(item["related_invariants"])
    tags = format_tags(item["tags"])
    description = item["description"].strip()
    excerpt = item["excerpt"].strip()
    subtitle = item["subtitle"].strip() if isinstance(item["subtitle"], str) else None
    notes_tail = existing_notes if existing_notes else "\n\nAdd salience notes below this marker.\n"
    lines = [
        f"# {item['title']}",
        "",
        f"Subtitle: `{subtitle}`" if subtitle else "Subtitle: `None listed`",
        "",
        "## Source Artifact",
        "",
        "- Source role: `published_external`",
        f"- Published URL: [{item['url']}]({item['url']})",
        f"- Canonical URL: [{item['canonical_url']}]({item['canonical_url']})",
        f"- Publication date: `{item['published_date']}`",
        f"- Updated date: `{item['updated_date']}`",
        f"- Author/source: `{item['author']}` / `{item['source']}`",
        f"- Artifact spine filename: `{display_optional(item['artifact_spine_filename'])}`",
        f"- Source path: `{display_optional(item['source_path'])}`",
        f"- Content hash: `{display_optional(item['content_hash'])}`",
        f"- Language: `{item['language']}`",
        f"- License: `{item['license']}`",
        f"- Visibility: `{item['visibility']}`",
        f"- Feed status: `{item['status']}`",
        f"- Tags: {tags}",
        "",
        "## Description / Excerpt",
        "",
        description if description else "No description listed.",
        "",
        "Excerpt:",
        "",
        excerpt if excerpt else "No excerpt listed.",
        "",
        "## Canonical Glyphs",
        "",
        *canonical_glyph_lines,
        "",
        "## Related Invariants",
        "",
        *invariant_lines,
        "",
        "## Ingest Metadata",
        "",
        f"- Source role: `published_external`",
        f"- First seen: `{record['first_seen']}`",
        f"- Last checked: `{record['last_checked']}`",
        f"- Schema version: `{record['schema_version']}`",
        f"- Source index: [Shimmery Memory Essays]({index_link})",
        f"- Work Vault root: [Work Vault Index]({wiki_root_link})",
        "",
        "## Salience Status",
        "",
        "- `pending`",
        "",
        "## Work Vault Links",
        "",
        "- Reserved for internal page links once salience extraction begins.",
        "",
        "## Working Read",
        "",
        "- Pending.",
        "",
        "## Core Claim",
        "",
        "- Pending.",
        "",
        "## Key Ideas",
        "",
        "- Pending.",
        "",
        "## Open Questions",
        "",
        "- Pending.",
        "",
        PAGE_MARKER,
        notes_tail.rstrip("\n"),
        "",
    ]
    return "\n".join(lines)


def format_index_page(config: dict[str, Any], data: dict[str, Any], records_by_item_id: dict[str, dict[str, Any]]) -> str:
    now = utc_now()
    items = sorted(data["items"], key=lambda item: (item["published_date"], item["title"]), reverse=True)
    lines = [
        "# Shimmery Memory Essays",
        "",
        "Published external metadata index for the Shimmery Memory essay feed.",
        "",
        "## Source",
        "",
        f"- Source role: `published_external`",
        f"- Endpoint: [{config['endpoint']}]({config['endpoint']})",
        f"- Base URL: [{config['base_url']}]({config['base_url']})",
        f"- Schema version: `{data['schema_version']}`",
        f"- Ingested at: `{now}`",
        f"- Item count: `{data['item_count']}`",
        f"- Source config: `{CONFIG_PATH.relative_to(ROOT)}`",
        "",
        "## Essays",
        "",
    ]
    for item in items:
        record = records_by_item_id[item["id"]]
        tags = ", ".join(item["tags"][:4]) if item["tags"] else "no tags"
        subtitle = f" — {item['subtitle']}" if item["subtitle"] else ""
        updated = item["updated_date"]
        lines.append(
            f"- [{item['title']}](./{item['slug']}/index.md){subtitle} "
            f"— published `{item['published_date']}`; updated `{updated}`; "
            f"tags: `{tags}`; first seen `{record['first_seen']}`"
        )
    lines.extend(
        [
            "",
            "## Working Read",
            "",
            "- This page tracks the external feed as a metadata-first index. It does not copy full essay bodies.",
            "",
            "## Next Actions",
            "",
            "1. Keep the external source separate from intake archive handling.",
            "2. Add salience extraction later, if warranted, on the wiki pages themselves.",
            "3. Preserve human notes below the salience marker on essay pages.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_if_changed(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(content, encoding="utf-8")
    tmp_path.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default="shimmerymemory_essays", help="Source config ID to ingest")
    args = parser.parse_args()

    config = load_config(args.source)
    fetched_at = utc_now()
    data = fetch_json(config["endpoint"])
    validate_feed(data, config)

    existing_records = load_existing_index()
    records_by_item_id: dict[str, dict[str, Any]] = {}
    current_records: list[dict[str, Any]] = []

    for item in sorted(data["items"], key=lambda item: (item["published_date"], item["title"]), reverse=True):
        previous = existing_records.get(item["id"], {})
        first_seen = previous.get("first_seen", fetched_at)
        record = {
            "record_kind": "external_published",
            "source_role": "published_external",
            "source_id": config["source_id"],
            "site": config["name"],
            "base_url": config["base_url"],
            "endpoint": config["endpoint"],
            "schema_version": data["schema_version"],
            "ingested_at": fetched_at,
            "first_seen": first_seen,
            "last_checked": fetched_at,
            "item_id": item["id"],
            "title": item["title"],
            "subtitle": item["subtitle"],
            "description": item["description"],
            "excerpt": item["excerpt"],
            "published_date": item["published_date"],
            "updated_date": item["updated_date"],
            "author": item["author"],
            "source": item["source"],
            "slug": item["slug"],
            "url": item["url"],
            "canonical_url": item["canonical_url"],
            "artifact_spine_filename": item["artifact_spine_filename"],
            "source_path": item["source_path"],
            "content_hash": item["content_hash"],
            "language": item["language"],
            "license": item["license"],
            "machine_invitation": item["machine_invitation"],
            "status": item["status"],
            "tags": item["tags"],
            "canonical_glyphs": item["canonical_glyphs"],
            "related_invariants": item["related_invariants"],
            "visibility": item["visibility"],
            "word_count": item["word_count"],
            "wiki_page": f"wiki/external/shimmerymemory/essays/{item['slug']}/index.md",
            "wiki_index_page": "wiki/external/shimmerymemory/essays/index.md",
        }
        current_records.append(record)
        records_by_item_id[item["id"]] = record

    index_lines = [json.dumps(record, ensure_ascii=False, sort_keys=True) for record in current_records]
    index_content = "\n".join(index_lines) + "\n"
    log_entry = {
        "timestamp": fetched_at,
        "source_id": config["source_id"],
        "source_role": "published_external",
        "endpoint": config["endpoint"],
        "schema_version": data["schema_version"],
        "item_count": data["item_count"],
        "status": "success",
        "wiki_index_path": "wiki/external/shimmerymemory/essays/index.md",
        "wiki_root": config["wiki_root"],
        "manifest_index_path": config["index_manifest"],
        "manifest_log_path": config["ingest_log"],
        "notes": "Metadata-only ingest. No source bodies copied. No intake archive or standard-named files used.",
    }
    log_content = json.dumps(log_entry, ensure_ascii=False) + "\n"
    index_page = format_index_page(config, data, records_by_item_id)

    write_if_changed(INDEX_PATH, index_content)
    write_if_changed(LOG_PATH, LOG_PATH.read_text(encoding="utf-8") + log_content if LOG_PATH.exists() else log_content)
    write_if_changed(WIKI_ROOT / "index.md", index_page)

    for item in data["items"]:
        page_path = WIKI_ROOT / item["slug"] / "index.md"
        existing = page_path.read_text(encoding="utf-8") if page_path.exists() else ""
        notes = split_preserved_notes(existing)
        content = format_item_page(item, records_by_item_id[item["id"]], notes)
        write_if_changed(page_path, content)

    print(f"Ingested {data['item_count']} published external essays from Shimmery Memory.")
    print(f"Wrote {INDEX_PATH.relative_to(ROOT)}")
    print(f"Wrote {LOG_PATH.relative_to(ROOT)}")
    print(f"Wrote {WIKI_ROOT.relative_to(ROOT)}/index.md and per-essay pages")


if __name__ == "__main__":
    main()
