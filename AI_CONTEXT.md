# AI Context for the Work Vault Wiki

This repository is a static, markdown-first knowledge base. The wiki pages are the primary semantic layer, the manifest files are the machine-readable metadata layer, and the artifacts tree holds source material, intake archives, and standard-named source copies.

## Read Order

1. [AI Entry Surface](/ai/index.html)
2. `llms.txt`
3. `llms-full.txt`
4. [Search](/search/index.html)
5. [Graph](/graph/index.html)
6. [Maintenance Hub](/wiki/maintenance/index.html)
7. [Reader Paths](./wiki/paths/index.md)
8. [AI Answer Contracts](./wiki/ai-answer-contracts/index.md)
9. [Status Vocabulary](./wiki/status-vocabulary/index.md)
10. [Work Vault Index](./wiki/index.md)
11. [Projects Index](./wiki/projects/index.md)
12. [Quantum Invariants AI](./wiki/projects/quantum-invariants/ai/index.md)
13. [Published Essays Index](./wiki/external/shimmerymemory/essays/index.md)

## Source Precedence

- Prefer local wiki pages when a semantic page already exists.
- Prefer standard-named source copies when a source file is needed.
- Preserve inbound originals in intake archive form.
- Treat `published_external` items as public external artifacts, not inbound files.
- Do not rewrite source content when the task is semantic extraction or linking.

## Working Rules

- Keep structure stable unless a durable seam appears.
- Expand existing pages before creating new branches.
- Preserve human notes and markers.
- Use manifests for routing, inventory, and published-external metadata.
- Use the graph surface when you need generated link structure or review edges.
- Use the maintenance hub when you need queue pressure before drilling into individual pages.
- Use attractors, concepts, and projects for deliberate cross-linking.

## Key Paths

- `CANON.md`
- `ATTRACTOR_MAP.md`
- `GLOSSARY.md`
- `CHANGELOG.md`
- `wiki/index.md`
- `wiki/projects/index.md`
- `wiki/concepts/index.md`
- `wiki/attractors/index.md`
- `wiki/paths/index.md`
- `wiki/ai-answer-contracts/index.md`
- `wiki/status-vocabulary/index.md`
- `wiki/external/shimmerymemory/essays/index.md`
- `search/index.html`
- `search.json`
- `sitemap.xml`
- `robots.txt`
- `manifest/inventory.jsonl`
- `manifest/standard_named_sources.jsonl`
- `manifest/external_published_index.jsonl`
- `artifacts/intake-archive/`
- `artifacts/standard-named/`
- `artifacts/incoming/`

## Notes

This page is an orientation layer, not a canon declaration. If a request is ambiguous, prefer a conservative edit and preserve the source trail.
