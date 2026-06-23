# Bridge and Transport

This seam holds the HumanKey transport, invite, and encrypted-backup material that sits around the core protocol drafts.

The documents here are operational companions rather than the protocol spine itself. They show how the trust-authentication family moves through manual messages, path invites, lane invites, and encrypted local backups, including the Abracadoo-adjacent variants that support the same transport story.

## Current Shape

- 9 auxiliary transport and bridge records.

## Representative Files

- [ABRACADOO_HUMANKEY_ENCRYPTED_BACKUP.json](<../../../../artifacts/intake-archive/20260623__humankey-protocol-bridge-intake/20260610__ABRACADOO__BACKUP__HUMANKEY-LOCAL__V0-5__encrypted.json>)
- [ABRACADOO_HUMANKEY_MANUAL_MESSAGE bob.json](<../../../../artifacts/intake-archive/20260623__humankey-protocol-bridge-intake/20260610__ABRACADOO__MESSAGE__HUMANKEY-MANUAL__V0-7__bob.json>)
- [ABRACADOO_HUMANKEY_MANUAL_MESSAGE alice.json](<../../../../artifacts/intake-archive/20260623__humankey-protocol-bridge-intake/20260610__ABRACADOO__MESSAGE__HUMANKEY-MANUAL__V0-7__alice.json>)
- [ABRACADOO_HUMANKEY_PATH_INVITE bob.json](<../../../../artifacts/intake-archive/20260623__humankey-protocol-bridge-intake/20260610__ABRACADOO__INVITE__HUMANKEY-PATH__V0-8__bob (1).json>)
- [ABRACADOO_HUMANKEY_LANE_INVITE bobby.json](<../../../../artifacts/intake-archive/20260623__humankey-protocol-bridge-intake/20260610__ABRACADOO__INVITE__HUMANKEY-LANE__V0-6__bobby.json>)

## Working Read

This is the transport edge of HumanKey: the place where encrypted state, manual delivery, and path invitations show up around the protocol core.

The page stays intentionally compact because these files are support evidence rather than the primary protocol drafts. They matter because they preserve the connective tissue between the app-side Abracadoo naming, the HumanKey message flow, and the trust-authentication lineage.

## Related Links

- [HumanKey Protocol](../index.md)
- [Protocol Drafts and Submission](../protocol-drafts-and-submission/index.md)
- [Presentation Materials](../presentation-materials/index.md)
- [Abracadoo](../../abracadoo/index.md)

## Next Actions

1. Keep the core protocol and presentation tracks separate from the bridge records.
2. Add only the bridge material that clearly belongs to transport, invites, or encrypted local state.
3. Split again only if the transport layer develops a second durable seam.
