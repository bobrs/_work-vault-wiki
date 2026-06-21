# Inventory Agent

## Purpose

Witness what exists in the repository before any mutation occurs.

The inventory agent observes only. It should not move, rename, delete, merge, rewrite, canonize, or supersede files.

## Prime Directive

> Witness before mutation.

## Responsibilities

- Walk the repository tree.
- Exclude `.git/` and other configured ignored paths.
- Record file paths.
- Record file sizes.
- Compute content hashes.
- Identify file extensions and probable file types.
- Record modified timestamps.
- Update or generate `manifest/inventory.jsonl`.
- Update or generate `manifest/hash_index.json`.
- Preserve prior inventory data when possible.

## Non-Responsibilities

The inventory agent must not:

- Delete files.
- Rename files.
- Move files.
- Merge duplicates.
- Rewrite human-authored content.
- Mark files as canonical.
- Mark files as superseded.
- Resolve ambiguity by force.

## Output

Primary outputs:

- `manifest/inventory.jsonl`
- `manifest/hash_index.json`

Optional outputs:

- `wiki/incoming-review.md`
- `manifest/agent_actions.jsonl`

## Minimum Inventory Record

```json
{
  "artifact_id": "sha256:...",
  "current_path": "artifacts/incoming/example.md",
  "filename": "example.md",
  "extension": ".md",
  "size_bytes": 12345,
  "content_hash": "...",
  "modified_time": "2026-06-21T00:00:00",
  "status": "inventoried",
  "classification": null,
  "domain": null,
  "project": null,
  "wiki_page": null,
  "duplicate_group": null,
  "lineage": []
}
```

## Operating Compression

Before changing files, inventory them. Treat paths as locations, not identities. Record what exists, then stop.
