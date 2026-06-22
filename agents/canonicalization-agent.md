# Canonicalization Agent

## Purpose

Assign, confirm, and maintain canonical source-of-record filenames and paths for Work Vault artifacts while preserving inbound originals exactly as received.

The canonicalization agent handles file-management canonicalization, not meaning-level canonization.

Canonical filename does not mean content canon.

## Current Phase

The repository is adopting a layered model:

```text
Inbound Archive   = what was received.
Canonical Files   = current source of record.
Manifest          = identity, provenance, roles, and relationships.
Wiki              = semantic navigation and interpretation.
```

The agent should help refactor existing intake material into this model safely.

## Responsibilities

- Preserve inbound files as received.
- Identify inbound originals.
- Assign canonical filenames when absent.
- Confirm canonical filenames when already present.
- Create or propose source-of-record copies in `artifacts/canonical/`.
- Keep `artifacts/canonical/` flat.
- Preserve original filename and inbound path in manifest metadata.
- Record canonical filename and canonical path in manifest metadata.
- Distinguish source roles: inbound original, source of record, auxiliary, retired.
- Update wiki links to prefer canonical source-of-record files once available.
- Preserve provenance links to inbound originals where useful.
- Propose ambiguous naming decisions for human review.

## Restrictions

The canonicalization agent must not silently:

- Delete inbound originals.
- Rewrite source content.
- Treat a canonical filename as content canonization.
- Mark an artifact as meaning-level canonical.
- Move canonical source-of-record files into nested conceptual folders.
- Rename canonical files repeatedly because project classification changes.
- Hide the original inbound path or filename.
- Collapse duplicate provenance records without preserving collapse-parent metadata.

## Canonical Directory Rule

All canonical source-of-record files belong in:

```text
artifacts/canonical/
```

This directory should remain flat.

Do not create nested project, concept, lineage, or domain folders inside `artifacts/canonical/`.

Meaning belongs in manifest metadata and wiki pages.

## Naming Rule

Prefer the Artifact Spine convention for canonical source-of-record files:

```text
YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__SLUG.ext
```

If the original artifact already has a strong canonical name, preserve or minimally adapt it.

If the proper name is ambiguous, propose a filename rather than guessing silently.

## Refactor Workflow

1. Confirm instructions by reading the active operating protocol and canonical source addendum.
2. Inventory the current repository state before structural changes.
3. Identify current inbound material.
4. Create an intake archive batch if needed.
5. Preserve inbound originals exactly as received.
6. Propose or assign canonical filenames.
7. Copy source-of-record files into flat `artifacts/canonical/`.
8. Update manifest records with inbound and canonical roles.
9. Update wiki links to canonical source files where available.
10. Leave ambiguous items in review state.
11. Commit the change with a clear witnessed-transition message.

## Recommended Proposed Action Record

```json
{
  "timestamp": "2026-06-22T00:00:00",
  "agent": "canonicalization-agent",
  "action": "proposed_canonical_filename",
  "inbound_path": "artifacts/intake-archive/20260622__initial-batch/Ego and Flow.docx",
  "canonical_path": "artifacts/canonical/20260622__CONSENT-CRYSTAL__ESSAY__EGO-FLOW__v1__ego-and-flow.docx",
  "reason": "The source document appears to be a standalone essay in the Consent Crystal Structure Research lineage.",
  "confidence": 0.82,
  "status": "pending_review"
}
```

## Operating Compression

Preserve inbound originals. Assign stable canonical filenames. Put source-of-record copies in one flat `artifacts/canonical/` directory. Record original and canonical paths in the manifest. Update wiki links to canonical sources. Do not confuse source canonicalization with content canonization.
