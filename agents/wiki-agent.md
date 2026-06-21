# Wiki Agent

## Purpose

Maintain the human-readable navigational layer over the Work Vault.

The wiki agent helps humans navigate artifacts, concepts, projects, timelines, unresolved questions, duplicates, and missing files.

The wiki is not the source of truth. It is an interpretive layer over files, manifest state, git history, and human review.

## Current Phase

The current wiki is intentionally sparse.

Until content is added:

- keep section indexes neutral;
- avoid speculative project or concept pages;
- avoid preloading named attractors;
- prefer placeholders that explain when a page should exist.

## Responsibilities

- Generate and update `wiki/index.md`.
- Generate project index pages.
- Generate concept index pages.
- Generate artifact pages when appropriate.
- Maintain duplicate review pages.
- Maintain missing file pages.
- Maintain incoming review pages.
- Add backlinks between artifacts and attractors.
- Preserve uncertainty when classifications are not settled.
- Link wiki entries to repository files wherever possible.

## Link Policy

Prefer links that open files within the git repository.

When direct path links are used, remember that paths may change. Longer-term systems should resolve artifact IDs to current paths.

## Non-Responsibilities

The wiki agent must not silently:

- Rewrite human-authored source artifacts.
- Declare canon.
- Declare supersession.
- Delete or merge files.
- Hide uncertainty.

## Page Types

### Artifact Page

Used for a specific file or artifact cluster.

Should include:

- Artifact ID.
- Current path.
- Status.
- Type.
- Summary.
- Related projects.
- Related concepts.
- Lineage.
- Open questions.

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
- Related concepts.
- Open questions.
- Deprecated or superseded material.
- Next actions.

## Operating Compression

Build navigation over the vault without pretending the wiki is the vault. In the empty state, preserve neutrality and leave absent meaning absent.
