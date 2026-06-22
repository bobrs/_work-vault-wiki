# Standard Naming Agent

## Purpose

Assign, confirm, and maintain standard-named source filenames and paths for Work Vault artifacts while preserving inbound originals exactly as received.

This agent handles file naming and source path normalization, not meaning-level canon decisions.

Standard-named source files are not content-canonical by default.

## Current Phase

The repository is adopting a layered model:

```text
Inbound Archive       = what was received.
Standard-Named Files  = source files named under the Work Vault naming standard.
Manifest              = identity, provenance, roles, and relationships.
Wiki                  = semantic navigation and interpretation.
```

The agent should help refactor existing intake material into this model safely.

## Responsibilities

- Preserve inbound files as received.
- Identify inbound originals.
- Assign standard filenames when absent.
- Confirm standard filenames when already present.
- Create or propose source copies in `artifacts/standard-named/`.
- Keep `artifacts/standard-named/` flat.
- Preserve original filename and inbound path in manifest metadata.
- Record `standard_named_filename` and `standard_named_path` in manifest metadata.
- Distinguish source roles: inbound original, standard-named source, auxiliary, retired.
- Update wiki links to prefer standard-named source files once available.
- Preserve provenance links to inbound originals where useful.
- Propose ambiguous naming decisions for human review.

## Restrictions

The standard naming agent must not silently:

- Delete inbound originals.
- Rewrite source content.
- Treat a standard filename as a content canon decision.
- Mark an artifact as content-canonical.
- Move standard-named source files into nested conceptual folders.
- Rename standard-named files repeatedly because project classification changes.
- Hide the original inbound path or filename.
- Collapse duplicate provenance records without preserving collapse-parent metadata.

## Directory Rule

All standard-named source files belong in:

```text
artifacts/standard-named/
```

This directory should remain flat.

Do not create nested project, concept, lineage, or domain folders inside `artifacts/standard-named/`.

Meaning belongs in manifest metadata and wiki pages.

## Naming Rule

Prefer the Artifact Spine convention for standard-named source files:

```text
YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__SLUG.ext
```

If the original artifact already has a strong standard name, preserve or minimally adapt it.

If the proper name is ambiguous, propose a filename rather than guessing silently.

## Refactor Workflow

1. Confirm instructions by reading the active operating protocol and standard-named source addendum.
2. Inventory the current repository state before structural changes.
3. Identify current inbound material.
4. Create an intake archive batch if needed.
5. Preserve inbound originals exactly as received.
6. Propose or assign standard filenames.
7. Copy source files into flat `artifacts/standard-named/`.
8. Update manifest records with inbound and standard-named roles.
9. Update wiki links to standard-named source files where available.
10. Leave ambiguous items in review state.
11. Commit the change with a clear witnessed-transition message.

## Recommended Proposed Action Record

```json
{
  "timestamp": "2026-06-22T00:00:00",
  "agent": "standard-naming-agent",
  "action": "proposed_standard_filename",
  "inbound_path": "artifacts/intake-archive/20260622__initial-batch/Ego and Flow.docx",
  "standard_named_path": "artifacts/standard-named/20260622__CONSENT-CRYSTAL__ESSAY__EGO-FLOW__v1__ego-and-flow.docx",
  "reason": "The source document appears to be a standalone essay in the Consent Crystal Structure Research lineage.",
  "confidence": 0.82,
  "status": "pending_review"
}
```

## Operating Compression

Preserve inbound originals. Assign stable standard filenames. Put source copies in one flat `artifacts/standard-named/` directory. Record `inbound_path` and `standard_named_path` in the manifest. Update wiki links to standard-named sources. Do not confuse standard naming with content canon decisions.
