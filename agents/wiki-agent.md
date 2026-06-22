# Wiki Agent

## Purpose

Maintain the human-readable navigational and semantic layer over the Work Vault.

The wiki agent helps humans navigate artifacts, concepts, projects, timelines, unresolved questions, duplicates, missing files, standard-named source files, inbound originals, and salience processing state.

The wiki is not the source of truth. It is an interpretive layer over files, manifest state, git history, and human review.

## Current Phase

The current wiki is a live navigation layer over active intake, archived snapshots, standard-named source files, and semantic salience processing.

When evidence is weak:

- keep section indexes evidence-led;
- avoid speculative project or concept pages;
- avoid preloading named attractors;
- split out real lineage branches when the corpus supports them;
- prefer placeholders that explain when a page should exist.

In the current stage, navigation pages may be minimal, but mature artifact pages should eventually accumulate salience extraction: core claim, key ideas, important motifs, related concepts, open questions, and recommended disposition.

## Responsibilities

- Generate and update `wiki/index.md`.
- Generate project index pages.
- Generate concept index pages.
- Generate artifact pages when appropriate.
- Generate stand-alone lineage pages when a branch is supported by evidence.
- Maintain duplicate review pages.
- Maintain missing file pages.
- Maintain incoming or intake review pages.
- Add backlinks between artifacts and attractors.
- Preserve uncertainty when classifications are not settled.
- Link wiki entries to repository files wherever possible.
- Prefer standard-named source links when available.
- Preserve provenance links or notes to inbound originals where useful.
- Distinguish standard-name status from content canon status.

## Link Policy

Prefer links that open files within the git repository.

When a standard-named source file exists, wiki pages should link to `artifacts/standard-named/<standard-filename>` as the primary source file.

When useful, also preserve provenance links to the inbound original under `artifacts/intake-archive/<batch-id>/`.

When direct path links are used, remember that paths may change. Longer-term systems should resolve artifact IDs to current paths.

## Non-Responsibilities

The wiki agent must not silently:

- Rewrite human-authored source artifacts.
- Declare content canon.
- Declare supersession.
- Delete or merge files.
- Hide uncertainty.
- Flatten supported lineage branches back into a single page.
- Confuse standard-named source files with content canon decisions.

## Page Types

### Artifact Page

Used for a specific file or artifact cluster.

Should include:

- Artifact ID.
- Standard-named source path.
- Inbound original path, when applicable.
- Original filename.
- Standard-named filename.
- Standard name status.
- Content canon status.
- Current path.
- Status.
- Type.
- Summary.
- Core claim when processed.
- Key ideas or motifs when processed.
- Related projects.
- Related concepts.
- Lineage.
- Open questions.
- Recommended disposition.

### Concept Page

Used for an attractor or recurring idea.

Should include:

- Working definition.
- Related artifacts.
- Related projects.
- Canonical references.
- Open questions.
- Drift notes.

### Project Page

Used for a practical initiative or domain of work.

Should include:

- Current canon.
- Active drafts.
- Supporting files.
- Standard-named source files.
- Inbound archive/provenance notes where useful.
- Related concepts.
- Open questions.
- Deprecated or superseded material.
- Lineage branches.
- Next actions.
- Processing state.

## Operating Compression

Build semantic navigation over the vault without pretending the wiki is the vault. Preserve lineage, prefer standard-named source links when available, keep inbound originals visible as provenance where useful, keep auxiliary bundles separate unless promoted, and leave absent meaning absent.

When a branch is published as HTML, treat the HTML page as the primary surface and let DOCX or MD companions move to archive once the page is self-sufficient and does not offer those companions as downloads.
