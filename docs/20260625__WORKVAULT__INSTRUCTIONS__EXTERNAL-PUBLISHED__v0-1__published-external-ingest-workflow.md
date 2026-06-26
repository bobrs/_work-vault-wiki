# Work Vault External Published Ingest Workflow

## Status

Version: `0.1`
Scope: metadata-first ingestion of published external sources into the wiki layer.

External published sources are not inbound archive files and not standard-named source files. They should be fetched, validated, and indexed as `published_external` records, with wiki pages serving as the first semantic surface.

## Workflow

1. Add or update the source config in `manifest/external_sources.json`.
2. Run the ingest script.
3. Confirm the manifest snapshot and ingest log update.
4. Review the generated wiki index and essay pages.
5. Add salience notes later without overwriting human-authored sections below the marker.

```bash
python3 scripts/ingest_shimmerymemory_essays.py
git diff
git add manifest/external_sources.json manifest/external_published_index.jsonl manifest/external_ingest_log.jsonl wiki/external/shimmerymemory/essays scripts/ingest_shimmerymemory_essays.py
git commit -m "ingest: update Shimmery Memory essays"
```

## Guardrails

- Fail fast if the endpoint changes shape.
- Do not copy full essay bodies by default.
- Do not place these records in `artifacts/intake-archive/` or `artifacts/standard-named/`.
- Preserve any notes below `<!-- BEGIN HUMAN / AI SALIENCE NOTES -->`.
