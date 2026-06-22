# Work Vault

A git-backed personal work vault, artifact wiki, and AI-managed continuity system.

This repository is prepared to hold a body of work in a form that can be inventoried, versioned, linked, classified, reconciled into stable standard-named source files, semantically processed, and navigated over time.

The repository now contains active intake content, archived snapshots, lineage-aware project pages, and instructions for separating inbound originals from standard-named source files. The structure, instructions, scripts, and review pages exist to keep that content legible over time.

The initial operating principle:

> Witness before mutation.

No file should be renamed, moved, deleted, merged, or overwritten until it has first been inventoried.

## Directory Map

```text
artifacts/   actual work files, intake archive, standard-named source files, auxiliary material
wiki/        human-readable semantic navigation layer
manifest/    machine-readable inventory, logs, and reconciliation state
scripts/     executable maintenance tools
agents/      instructions for AI management agents
docs/        repository operating instructions
.vault/      configuration and rules
```

## Current Phase

The wiki should stay evidence-led. Small durable branches get their own pages. Durable pages should increasingly contain semantic compression and deliberate cross-links, not only labels and source pointers. HTML-published items keep HTML primary and may archive DOCX or MD companions when they are not needed for coherence. Keep auxiliary bundles separate from core source unless otherwise noted.

The repository is also adopting a standard-named source layer:

```text
artifacts/intake-archive/  original inbound files preserved as received
artifacts/standard-named/   flat directory of standard-named source files
```

Inbound files are evidence. Standard-named files are named source copies under the Work Vault naming standard. The wiki should prefer standard-named source links once available, while preserving provenance back to inbound originals where useful.

## First Content Intake

1. Add received source files to a dated batch under `artifacts/intake-archive/`.
2. Run `python3 scripts/inventory.py`.
3. Run `python3 scripts/detect_duplicates.py` when needed.
4. Assign or propose standard filenames for meaningful artifacts.
5. Copy source files into the flat `artifacts/standard-named/` directory.
6. Run `python3 scripts/build_wiki_index.py`.
7. Review the generated state before any move, rename, merge, canon decision, or irreversible consolidation.

## Source Of Truth

```text
Inbound Archive       = what was received.
Standard-Named Files  = source files named under the Work Vault naming standard.
Manifest              = identity, provenance, roles, and relationships.
Git                   = witnessed state transitions.
Wiki                  = semantic navigation and interpretation.
Agents                = coherence, reconciliation, standard naming, and salience processing.
```

## Operating Instructions

See:

- [`docs/README.md`](docs/README.md)
- [`docs/20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-3__lineage-aware-intake-operating-protocol.md`](docs/20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-3__lineage-aware-intake-operating-protocol.md)
- [`docs/20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-4__project-directives-addendum.md`](docs/20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-4__project-directives-addendum.md)
- [`docs/20260622__WORKVAULT__INSTRUCTIONS__SEMANTIC-SALIENCE__v0-6__semantic-compression-and-link-seeding-addendum.md`](docs/20260622__WORKVAULT__INSTRUCTIONS__SEMANTIC-SALIENCE__v0-6__semantic-compression-and-link-seeding-addendum.md)
- [`docs/20260622__WORKVAULT__INSTRUCTIONS__STANDARD-NAMED-SOURCE__v0-7__flat-source-name-standard-addendum.md`](docs/20260622__WORKVAULT__INSTRUCTIONS__STANDARD-NAMED-SOURCE__v0-7__flat-source-name-standard-addendum.md)

## Public Site

The wiki web layer is a static HTML build generated from the markdown wiki sources.

- Build command: `npm run build`
- Worker entrypoint: `dist/index.js`
- Landing page output: `dist/index.html`
- Raw vault browser: `dist/vault/index.html`
- Public source repository: `https://github.com/bobrs/_work-vault-wiki`
