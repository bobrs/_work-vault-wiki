# Work Vault Canonical Source Addendum

## 0. Status

Version: `0.6`  
Date initiated: `2026-06-22`  
Scope: inbound archive handling, canonical source-of-record files, flat canonical directory policy, and canonical filename assignment.

This addendum supplements the active Work Vault operating protocol and the Semantic Salience addendum.

The repository now distinguishes four layers:

```text
Inbound Archive   = what was received.
Canonical Files   = current source of record.
Manifest          = identity, provenance, roles, and relationships.
Wiki              = semantic navigation and interpretation.
```

This addendum clarifies that inbound files should not become the long-term source-of-record path by accident. Inbound files are evidence. Canonical files are the future source of record.

---

# 1. Core Architectural Shift

The previous intake model treated `artifacts/incoming/` as the place where source files arrived and were later organized.

The revised model is:

```text
messy reality
↓
witnessed inbound archive
↓
flat canonical source-of-record layer
↓
semantic wiki and manifest navigation
```

All inbound files should be preserved as received.

Each meaningful artifact should either already have or be assigned a canonical filename.

The source-of-record copy should live in a single flat canonical directory.

The wiki should eventually link primarily to the canonical source-of-record file, while preserving links or references to the inbound original for provenance.

---

# 2. New Directory Policy

Use this structure:

```text
artifacts/
  intake-archive/
    <batch-id>/
      original inbound files exactly as received

  canonical/
    YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__slug.ext
    YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__another-slug.ext

  auxiliary/
    bundles/
    exports/
    snapshots/

  retired/
```

The canonical directory is intentionally flat.

Do not create nested project, concept, or domain folders inside `artifacts/canonical/`.

Meaning belongs in manifest metadata and wiki pages, not in canonical source-of-record paths.

---

# 3. Prime Directives

1. All inbound files are preserved exactly as received.
2. Inbound files are archived by batch.
3. No inbound original is cleaned, renamed, deleted, rewritten, or moved after archival except by an explicit provenance-preserving operation.
4. Each meaningful artifact receives or confirms one canonical filename.
5. Canonical source-of-record files live in one flat directory: `artifacts/canonical/`.
6. Wiki links prefer canonical source-of-record files once available.
7. The manifest records original path, original filename, canonical path, content hash, and provenance relationship.
8. Canonical filename does not imply content canonization.
9. Content canonization remains a separate human-witnessed decision.
10. Meaning lives in wiki and manifest metadata, not nested source-of-record paths.

---

# 4. Canonical Filename vs. Content Canon

The word `canonical` has two distinct meanings in the Work Vault.

## 4.1 Canonical Filename / Source of Record

This means:

```text
This is the normalized source-of-record filename and path for this artifact.
```

This is a file-management and provenance status.

It does not mean the content is philosophically canonical.

Preferred field names:

```text
canonical_filename
canonical_path
source_of_record
canonicalization_status
```

## 4.2 Content Canon / Canon-Grade Meaning

This means:

```text
This artifact or formulation has been human-witnessed as durable canon.
```

This remains a semantic and human-review status.

Preferred field names:

```text
content_canon_status
canon_decision
canon_grade
canon_notes
```

Do not collapse these concepts.

A file can have a canonical filename while its content remains draft, fragmentary, auxiliary, or uncertain.

---

# 5. Intake Lifecycle

The revised lifecycle is:

```text
Inbound file arrives
↓
Archive original exactly as received
↓
Inventory original
↓
Assign or confirm canonical filename
↓
Create canonical source-of-record copy
↓
Record provenance relationship in manifest
↓
Point wiki pages to canonical source-of-record file
↓
Preserve inbound original as provenance evidence
```

Compressed lifecycle:

```text
Receive → Archive → Witness → Canonicalize filename → Promote copy → Link canonical
```

---

# 6. Canonical Directory Rule

All source-of-record artifacts belong in:

```text
artifacts/canonical/
```

This directory should remain flat.

Do not encode taxonomy into source-of-record paths.

Avoid:

```text
artifacts/canonical/consent/crystal/ego-and-flow.docx
artifacts/canonical/projects/uliua/meme-plan.md
```

Prefer:

```text
artifacts/canonical/20260622__CONSENT-CRYSTAL__ESSAY__EGO-FLOW__v1__ego-and-flow.docx
artifacts/canonical/20260622__ULIUA__PLAN__AUTOMEME__v1__meme-plan.md
```

If project, concept, lineage, or domain classification changes later, update manifest and wiki metadata. Do not rename or move the canonical file unless there is a clear reason and the prior canonical path is preserved in lineage metadata.

---

# 7. Filename Convention

For canonical source-of-record files, prefer the Artifact Spine convention:

```text
YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__SLUG.ext
```

The date should usually represent the best known artifact date or intake/canonicalization date, depending on evidence.

If the original date is uncertain, do not invent precision. Use the intake date and record uncertainty in metadata.

Examples:

```text
20260622__CONSENT-CRYSTAL__ESSAY__EGO-FLOW__v1__ego-and-flow.docx
20260622__WORKVAULT__INSTRUCTIONS__CANONICAL-SOURCE__v0-6__flat-source-of-record-addendum.md
```

Do not rename inbound originals merely to fit this convention. Create or assign a canonical source-of-record copy instead.

---

# 8. Manifest Fields

Manifest records should evolve to include source-role and provenance fields.

Recommended fields:

```json
{
  "artifact_id": "sha256:abc123",
  "record_kind": "artifact",
  "source_role": "inbound_original | source_of_record | auxiliary | retired",
  "original_filename": "Ego and Flow.docx",
  "inbound_path": "artifacts/intake-archive/20260622__initial-batch/Ego and Flow.docx",
  "canonical_filename": "20260622__CONSENT-CRYSTAL__ESSAY__EGO-FLOW__v1__ego-and-flow.docx",
  "canonical_path": "artifacts/canonical/20260622__CONSENT-CRYSTAL__ESSAY__EGO-FLOW__v1__ego-and-flow.docx",
  "source_of_record": true,
  "canonicalization_status": "unassigned | proposed | assigned | confirmed | ambiguous",
  "content_canon_status": "unset | candidate | canonical | superseded",
  "received_batch": "20260622__initial-batch",
  "derived_from": "artifacts/intake-archive/20260622__initial-batch/Ego and Flow.docx",
  "content_hash": "abc123",
  "lineage": []
}
```

The same content hash may appear in both the inbound archive and canonical directory when the canonical source copy is byte-identical to the inbound original.

That is expected.

The difference is role, not content.

---

# 9. Wiki Link Policy

Once canonicalization has occurred, wiki pages should prefer links to the canonical source-of-record file.

A mature artifact page should distinguish:

```markdown
## Source Artifact

- Source of record: [canonical filename](../../../../artifacts/canonical/...)
- Inbound original: [original filename](../../../../artifacts/intake-archive/<batch-id>/...)
- Original filename: `...`
- Canonical filename: `...`
- Canonicalization status: `assigned | confirmed | ambiguous`
- Content canon status: `unset | candidate | canonical | superseded`
```

The inbound archive link preserves provenance.

The canonical source link supports stable future navigation.

---

# 10. Updated File States

Use or support these states as the system matures:

```text
received
archived_inbound
inventoried
canonical_name_unassigned
canonical_name_proposed
canonical_name_assigned
canonical_name_confirmed
canonical_source_created
salience_pending
salience_extracted
concept_integrated
content_canon_candidate
content_canonical
retired
```

Do not use `canonical` alone when ambiguity is possible. Prefer either `canonical_source_created` or `content_canonical`.

---

# 11. Refactoring Existing Work

When refactoring an existing Work Vault repository into this model:

1. Create `artifacts/intake-archive/` if absent.
2. Create `artifacts/canonical/` if absent.
3. Treat existing `artifacts/incoming/` contents as inbound originals unless already clearly canonical.
4. Move or copy existing inbound material into a dated batch under `artifacts/intake-archive/` only after inventory has witnessed the pre-refactor state.
5. For each meaningful artifact, propose or assign a canonical filename.
6. Copy the source-of-record artifact into `artifacts/canonical/` using the canonical filename.
7. Update manifest records to distinguish inbound originals from canonical source-of-record files.
8. Update wiki source links to point to canonical files where available.
9. Preserve inbound links or provenance notes where useful.
10. Commit the refactor as a witnessed state transition.

The refactor should be reversible through git.

Do not delete inbound originals during this step.

---

# 12. Expected Prompt for AI Refactoring

A simple prompt is enough if these instructions are present in the repository.

Recommended prompt:

```text
Check the Work Vault directions, especially the canonical source addendum, and refactor the repository so inbound originals are preserved in an intake archive, canonical source-of-record copies live in a single flat artifacts/canonical directory, the manifest records both roles, and wiki links prefer canonical source files where available. Do not delete or rewrite source content. Propose ambiguous naming decisions instead of guessing.
```

Even shorter prompt:

```text
Check the directions and apply the canonical source-of-record refactor safely.
```

Use the longer prompt if the agent has not already internalized the Work Vault instructions.

---

# 13. Operating Compression

Inbound files are evidence. Preserve them exactly as received. Assign or confirm one canonical filename for each meaningful artifact. Store source-of-record copies in one flat `artifacts/canonical/` directory. Record original and canonical paths in the manifest. Link the wiki to canonical files once available. Do not confuse canonical filenames with content canonization.
