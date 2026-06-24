# Implementation and Runtime

This seam holds the complete app runtime seed for `Abracadoo`: the browser shell, HumanKey contact flow, local vault adapters, backup path, and PWA packaging that makes the app a usable local-first surface instead of a static mockup.

## Current Shape

- 3 app runtime bundles.

## Representative Files

- [Abracadoo HumanKey seed scaffold v2.zip](<../../../../artifacts/standard-named/20260624__ABRACADOO__CODE__HUMANKEY-SEED__v2__abracadoo-humankey-seed.zip>) · [archive copy](<../../../../artifacts/intake-archive/20260624__abracadoo-implementation-lineage-intake/20260624__ABRACADOO__CODE__HUMANKEY-SEED__v2__abracadoo-humankey-seed.zip>)
- [Abracadoo HumanKey seed browser shell v4.zip](<../../../../artifacts/standard-named/20260624__ABRACADOO__CODE__HUMANKEY-SEED__v4__abracadoo-humankey-seed.zip>) · [archive copy](<../../../../artifacts/intake-archive/20260624__abracadoo-implementation-lineage-intake/20260624__ABRACADOO__CODE__HUMANKEY-SEED__v4__abracadoo-humankey-seed.zip>)
- [Abracadoo HumanKey seed runtime bundle v9.zip](<../../../../artifacts/standard-named/20260624__ABRACADOO__CODE__HUMANKEY-SEED__v9__abracadoo-humankey-seed.zip>) · [archive copy](<../../../../artifacts/intake-archive/20260624__abracadoo-implementation-intake/20260624__ABRACADOO__CODE__HUMANKEY-SEED__v9__abracadoo-humankey-seed.zip>)

## Working Read

The earlier seeds show the runtime becoming real in stages: first the scaffold, then the browser shell, then the finished runtime bundle. The current seed wires a browser UI around contact creation, QR-code generation, code verification, local backup import/export, and IndexedDB-backed storage. The app surface is therefore more than a mock landing page: it is a runnable HumanKey-first runtime with a visible local state boundary.

This page stays separate from the public site-variant rail so that code lineage, copy lineage, and design lineage can move independently.

## Related Links

- [Abracadoo](../index.md)
- [Architecture and Trust](../architecture-and-trust/index.md)
- [Brand and Overview](../brand-and-overview/index.md)
- [Site Variants](../site-variants/index.md)
- [Abracadabracadoo](../../abracadabracadoo/index.md)

## Next Actions

1. Keep the runtime seed separate from the public-facing site bundles.
2. Add future code bundles here only if they remain part of the same implementation seam.
3. Split again only if a second durable runtime branch appears.
