# Work Vault Standard-Named Source Addendum

## 0. Status

Version: `0.7`
Date initiated: `2026-06-22`
Scope: inbound archive handling, standard-named source files, flat source directory policy, manifest source fields, and wiki link preference.

This addendum supersedes the prior file-naming language that used `canonical` for source-file names. From this point forward, use `standard-named` for files that have received a name under the Work Vault naming standard.

The word `canonical` is reserved for content-level meaning decisions, such as content-canonical artifacts approved by human review. Do not use it for file naming status.

The repository distinguishes four layers:

```text
Inbound Archive       = what was received.
Standard-Named Files  = source files named under the Work Vault naming standard.
Manifest              = identity, provenance, roles, and relationships.
Wiki                  = semantic navigation and interpretation.
```

## 1. Core Rule

Inbound files are evidence. Preserve them exactly as received.

Files that have or receive a name under the source naming standard live in one flat directory:

```text
artifacts/standard-named/
```

The wiki should prefer standard-named source links once available, while preserving inbound archive links or provenance notes where useful.

Standard-named files are not content-canonical by default. A standard-named file can still be draft, fragmentary, auxiliary, ambiguous, superseded, or awaiting human review.

## 2. Directory Policy

Use this structure:

```text
artifacts/
  intake-archive/
    <batch-id>/
      original inbound files exactly as received

  standard-named/
    YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__slug.ext

  auxiliary/
    bundles/
    exports/
    snapshots/

  retired/
```

Keep `artifacts/standard-named/` flat. Do not create nested project, concept, lineage, or domain folders inside it.

Meaning belongs in manifest metadata and wiki pages, not in source path nesting.

## 3. Prime Directives

1. All inbound files are preserved exactly as received.
2. Inbound files are archived by batch.
3. No inbound original is cleaned, renamed, deleted, rewritten, or moved after archival except by an explicit provenance-preserving operation.
4. Each meaningful artifact may receive or confirm one standard filename.
5. Standard-named source files live in one flat directory: `artifacts/standard-named/`.
6. Wiki links prefer standard-named source files once available.
7. The manifest records original path, original filename, standard-named path, content hash, and provenance relationship.
8. Standard naming does not imply content-canonical status.
9. Content-canonical status remains a separate human-witnessed decision.
10. Ambiguous naming decisions should be proposed for review instead of guessed.

## 4. Naming Standard vs. Content Canon

The naming layer and the meaning layer are separate.

Standard-named source means:

```text
This file has a normalized source filename and path under the Work Vault naming standard.
```

Preferred fields:

```text
standard_named_filename
standard_named_path
standard_name_status
source_role
```

Content-canonical means:

```text
This artifact or formulation has been human-witnessed as durable content.
```

Preferred fields:

```text
content_canon_status
canon_decision
canon_grade
canon_notes
```

Do not collapse these concepts.

## 5. Intake Lifecycle

Use this lifecycle:

```text
Receive -> Archive inbound original -> Inventory -> Assign or confirm standard filename -> Promote copy -> Link standard-named source
```

Expanded:

1. Inbound file arrives.
2. Archive original exactly as received.
3. Inventory original.
4. Assign or confirm standard filename.
5. Create standard-named source copy.
6. Record provenance relationship in manifest.
7. Point wiki pages to the standard-named source file.
8. Preserve inbound original as evidence.

## 6. Filename Convention

For standard-named source files, prefer the Artifact Spine convention:

```text
YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__SLUG.ext
```

The date should usually represent the best known artifact date or intake/standard-naming date, depending on evidence. If the original date is uncertain, use the intake date and record uncertainty in metadata.

Do not rename inbound originals merely to fit this convention. Create or assign a standard-named source copy instead.

## 7. Manifest Fields

Manifest records should support source-role and provenance fields:

```json
{
  "artifact_id": "sha256:abc123",
  "record_kind": "artifact",
  "source_role": "inbound_original | standard_named_source | auxiliary | retired",
  "original_filename": "Ego and Flow.docx",
  "inbound_path": "artifacts/intake-archive/20260622__initial-batch/Ego and Flow.docx",
  "standard_named_filename": "20260622__CONSENT-CRYSTAL__ESSAY__EGO-FLOW__v1__ego-and-flow.docx",
  "standard_named_path": "artifacts/standard-named/20260622__CONSENT-CRYSTAL__ESSAY__EGO-FLOW__v1__ego-and-flow.docx",
  "standard_name_status": "unassigned | proposed | assigned | confirmed | ambiguous",
  "content_canon_status": "unset | candidate | canonical | superseded",
  "received_batch": "20260622__initial-batch",
  "derived_from": "artifacts/intake-archive/20260622__initial-batch/Ego and Flow.docx",
  "content_hash": "abc123",
  "lineage": []
}
```

The same content hash may appear in inbound archive and standard-named directories when the source copy is byte-identical. That is expected. The difference is role, not content.

## 8. Wiki Link Policy

Once standard naming has occurred, wiki pages should prefer links to the standard-named source file.

A mature artifact page should distinguish:

```markdown
## Source Artifact

- Standard-named source: [filename](../../../../artifacts/standard-named/...)
- Inbound original: [original filename](../../../../artifacts/intake-archive/<batch-id>/...)
- Original filename: `...`
- Standard-named filename: `...`
- Standard name status: `assigned | confirmed | ambiguous`
- Content canon status: `unset | candidate | canonical | superseded`
```

The inbound archive link preserves provenance. The standard-named source link supports stable future navigation.

## 9. Updated File States

Use or support these states as the system matures:

```text
received
archived_inbound
inventoried
standard_name_unassigned
standard_name_proposed
standard_name_assigned
standard_name_confirmed
standard_named_source_created
salience_pending
salience_extracted
concept_integrated
content_canon_candidate
content_canonical
retired
```

## 10. Refactoring Existing Work

When refactoring an existing Work Vault repository into this model:

1. Create `artifacts/intake-archive/` if absent.
2. Create `artifacts/standard-named/` if absent.
3. Treat existing `artifacts/incoming/` contents as inbound originals unless already clearly handled.
4. Move or copy existing inbound material into a dated batch under `artifacts/intake-archive/` only after inventory has witnessed the pre-refactor state.
5. For each meaningful artifact, propose or assign a standard filename.
6. Copy the source artifact into `artifacts/standard-named/` using the standard filename.
7. Update manifest records to distinguish inbound originals from standard-named source files.
8. Update wiki source links to point to standard-named files where available.
9. Preserve inbound links or provenance notes where useful.
10. Commit the refactor as a witnessed state transition.

The refactor should be reversible through git. Do not delete or rewrite source content.

## 11. Operating Compression

Inbound files are evidence. Preserve them exactly as received. Assign or confirm one standard filename for each meaningful artifact. Store standard-named source copies in one flat `artifacts/standard-named/` directory. Record `inbound_path` and `standard_named_path` in the manifest. Link the wiki to standard-named files once available. Do not confuse standard-named files with content-canonical artifacts.
