# Work Vault

A git-backed personal work vault, artifact wiki, and AI-managed continuity system.

This repository is prepared to hold a body of work in a form that can be inventoried, versioned, linked, classified, reconciled, and navigated over time.

The repository now contains active intake content, archived snapshots, and lineage-aware project pages. The structure, instructions, scripts, and review pages exist to keep that content legible over time.

The initial operating principle:

> Witness before mutation.

No file should be renamed, moved, deleted, merged, or overwritten until it has first been inventoried.

## Directory Map

```text
artifacts/   actual work files
wiki/        human-readable navigation layer
manifest/    machine-readable inventory, logs, and reconciliation state
scripts/     executable maintenance tools
agents/      instructions for AI management agents
docs/        repository operating instructions
.vault/      configuration and rules
```

## Current Phase

The wiki should stay evidence-led. Small durable branches get their own pages. HTML-published items keep HTML primary and may archive DOCX or MD companions when they are not needed for coherence. Keep auxiliary bundles separate from core source unless otherwise noted.

## First Content Intake

1. Add source files to `artifacts/incoming/`.
2. Run `python3 scripts/inventory.py`.
3. Run `python3 scripts/detect_duplicates.py` when needed.
4. Run `python3 scripts/build_wiki_index.py`.
5. Review the generated state before any move, rename, merge, or canon decision.

## Source Of Truth

```text
Files     = what exists.
Manifest  = what the system knows.
Git       = how things changed.
Wiki      = how humans navigate.
Agents    = how coherence is maintained.
```

## Operating Instructions

See:

- [`docs/README.md`](docs/README.md)
- [`docs/20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-3__lineage-aware-intake-operating-protocol.md`](docs/20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-3__lineage-aware-intake-operating-protocol.md)
- [`docs/20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-4__project-directives-addendum.md`](docs/20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-4__project-directives-addendum.md)

## Public Site

The wiki web layer is prepared as a Cloudflare Sites-compatible Worker wrapper around static HTML output.

- Build command: `npm run build`
- Worker entrypoint: `dist/index.js`
- Landing page output: `dist/index.html`
- Raw vault browser: `dist/vault/index.html`
- Public source repository: `https://github.com/bobrs/_work-vault-wiki`
