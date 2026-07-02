# Work Vault Markdown-First Migration Plan

## Status

Version: `0.1`
Date initiated: `2026-07-01`
Scope: phased migration from DOCX/PDF working files to markdown source copies where conversion is clean enough to preserve meaning.

This plan does not replace the existing source-preservation rules. Inbound originals remain evidence. The goal is to make markdown the preferred working and wiki-facing form for active material without losing provenance or flattening layout-dependent meaning.

## Goal

Move the repository toward a markdown-first working layer for documents that can be converted reliably, while keeping original DOCX/PDF files in intake archive as preserved originals.

## Core Policy

1. Preserve inbound originals exactly as received.
2. Do not rewrite or delete source content in place.
3. Convert documents into markdown as derived working copies when conversion is structurally faithful.
4. Keep archive originals as the provenance anchor.
5. Prefer markdown links in the wiki once a clean markdown source exists.
6. Leave ambiguous, layout-heavy, or lossy conversions in the archive until they can be reviewed manually.

## Recommended Order

1. High-value active branches already receiving semantic work.
2. Pages with dense backlinks or many child pages.
3. Project roots that are already structurally stable.
4. Smaller durable branches that are easy to validate.
5. Long-tail archival material only after the active corpus is stable.

Initial conversion candidates should include:

- CICP
- Semantic Collapse Theory
- Quantum Invariants
- Semantic Integrity
- Consentful Cybernetics
- WitnessKey
- Trust Interoperability Standard
- Other active side-projects-desktop branches with clear markdown-friendly structure

## Conversion Triage

Convert first when the source is:

- Mostly prose
- Already split into stable wiki pages
- Light on tables or image-dependent layout
- Actively linked from the wiki
- Likely to benefit from search and semantic extraction

Defer or keep archival when the source is:

- Form-heavy
- Image-heavy
- Table-heavy in a meaning-bearing way
- A scanned PDF without reliable text extraction
- A companion export that exists only because the original tool could not emit markdown

## Working Model

Use a three-stage handling model for each source document:

1. Inbound original stays in `artifacts/intake-archive/`.
2. Derived markdown is created as the working source layer.
3. Wiki pages are updated to point to the markdown source where available.

If a source must remain DOCX or PDF for now, keep it as archival source and add a markdown companion later rather than forcing a lossy rewrite.

## Manifest Expectations

Track the migration as provenance, not as a hidden rewrite.

Preferred fields to record or extend:

- `inbound_path`
- `standard_named_path`
- `derived_from`
- `source_role`
- `standard_name_status`
- `content_canon_status`
- `conversion_method`
- `conversion_status`
- `wiki_page`

If a markdown file replaces a DOCX source in the standard-named layer, keep the original file path in the archive and update the manifest so the lineage remains visible.

## QA Checklist

1. Compare headings, sections, and list structure.
2. Check that links survive or are rewritten intentionally.
3. Verify that tables, callouts, and images were not silently lost.
4. Confirm that wiki pages still build and render.
5. Review any page where the markdown conversion changes meaning.
6. Preserve any human-added notes or review markers.

## Migration Sequence

1. Inventory the current DOCX/PDF corpus by project and activity level.
2. Tag likely markdown-convertible documents.
3. Convert a pilot batch.
4. Validate the pilot batch in the wiki.
5. Expand by cluster.
6. Rewrite links to the markdown sources.
7. Keep archive originals untouched.
8. Reassess the remaining PDF/DOCX population for edge cases.

## Exit Criteria For A Batch

A batch is ready to move forward when:

- The markdown render is structurally faithful.
- The wiki points at the markdown source where appropriate.
- The original archive path is still preserved.
- No meaningful content was lost in conversion.

## Notes

This is a migration of the working surface, not a purge of the record. The archive remains the record. Markdown becomes the preferred editable form once the conversion has been witnessed as faithful.
