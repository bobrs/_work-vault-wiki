# Attention-Weighted Block Persistence (Dev-Forward Spec)

You are implementing a **block persistence system** where *player attention* is the resource that keeps player-made blocks from decaying.

## Core invariant
**Player-altered blocks only persist while they are being collectively attended to by active players.** Server uptime alone does nothing.

---

# 1) The Mechanic (Direct, Implementable)

## 1.1 Block State Model (minimal)
Only **player-altered blocks** carry metadata.

```text
BlockState {
  intrinsic_mass        // effort-to-obtain proxy
  attention_mass        // accumulated attention
  last_updated_at       // last decay tick time
}
```

Storage note: keep this sparse (only for placed/modified blocks), not for seed blocks.

---

## 1.2 Attention Accumulation (“Seen” Events)
A block gains attention when it is *seen*.

### Seen Event (simple first pass)
Fire a Seen Event if:
- A player is online
- The block is in a loaded chunk
- The player is within radius **R** (e.g., 16–32 blocks)

Rate limit:
- At most once per **block per player** every **N seconds** (e.g., 5s)

### Attention gain
```text
attention_mass += seen_value
```
Start with:
```text
seen_value = 1
```
(You can later scale by player count, LoS, rarity, etc.)

---

## 1.3 Intrinsic Mass (labor encoding)
Intrinsic mass is an **effort-to-acquire proxy**, not market value.

Example mapping:

| Block | intrinsic_mass |
|---|---:|
| Dirt | 1 |
| Cobblestone | 2 |
| Stone brick | 3 |
| Iron block | 8 |
| Diamond block | 50 |

This is the foundation of “diamond anchors stabilize builds.”

---

## 1.4 Decay (half-life)
Decay only runs while **≥ 1 player online**.

Every decay tick (e.g., every 10–30 seconds):

```text
effective_mass = intrinsic_mass + attention_mass

decay_amount = decay_constant / effective_mass

attention_mass -= decay_amount * delta_time
```

When:
```text
attention_mass <= 0
```
The block decays.

---

## 1.5 Decay Outcome (choose one)

### Option A — Revert (fastest)
- Block reverts to the original seed-generated block

### Option B — Metabolize (recommended)
- Block breaks into ingredients
- Ingredients inherit persistence based on acquisition effort

Example concept:
```text
item_persistence = mining_time * tool_factor
```
Dropped items themselves can decay if ignored.

---

## 1.6 Attention Leakage (second layer, optional)
Blocks share attention with adjacent **player-altered** blocks.

At decay time:

```text
effective_mass =
  block.mass +
  Σ(neighbor.mass × leakage_factor)
```

Leakage rules (start simple):
- Only through player-placed adjacency
- Distance-1 only (no graph traversals yet)
- leakage_factor ≈ 0.05–0.15

Result:
- One high-mass anchor can stabilize a whole build
- Isolated builds rot naturally

---

## 1.7 Player Power Limiting (anti-hoard)
Don’t limit building directly—limit **how much attention a player can inject**.

### Option 1 — Distance from Spawn (simplest)
```text
attention_given = base / (1 + distance_from_spawn)
```

### Option 2 — Bed-Relative Load
```text
attention_given ∝ 1 / (# blocks placed since last bed set)
```

Both discourage infinite empire building.

---

# 2) What This Buys You (System Effects)
- World self-prunes abandoned builds
- Cities persist, noise disappears
- Ruins emerge naturally
- Grief heals without rollback
- Storage bloat drops over time
- “Soft governance” without admin rules

---

# 3) Implementation Strategy (Minimal → Rich)

## Suggested architecture
- Store metadata in **chunk-attached storage** or a **sparse map keyed by BlockPos**
- Run decay in **batches** (not per-block per-tick)
- Tick interval: 10–30 seconds
- Keep Seen events **rate-limited and coarse** for performance

---

# 4) Next-Step Options (Pick One)

## Option A — Minimal Working Prototype (fastest insight)
Goal: prove the loop works.

Implement:
- Seen events
- Intrinsic mass
- Attention decay
- Revert-on-decay

Ignore for now:
- Leakage
- Ingredient persistence
- Player power limits

Deliverable:
- Test server
- Logging: block lifetime histograms

---

## Option B — Leakage-First Prototype
Goal: test the “anchor stabilizes structure” intuition.

Implement:
- Everything in Option A
- Adjacency leakage
- Visual decay cues (cracks/shimmer/ghosting)

Deliverable:
- Side-by-side builds with and without anchors

---

## Option C — Paper-Track Prototype
Goal: research-grade evaluation.

Implement:
- Core mechanics
- Metrics logging:
  - block half-life distribution
  - chunk modification density over time
  - grief recovery time
- Two conditions:
  - vanilla
  - attention-based

Deliverable:
- Dataset + graphs
- Reproducible config

---

## Option D — Design-Forward Alpha
Goal: make it *feel* good.

Implement:
- Visual/audio feedback for decay
- Item ghosts / fading ruins
- Lore hooks (“the world remembers what is held”)

Deliverable:
- Playtest-ready server
- Player feedback

---

# 5) Recommended Path
Start with **Option A**, but structure the code so **leakage slots in cleanly**.

The moment you see a build slowly un-holding itself when players stop visiting, you’ll know exactly what to tune next.

---

# Fabric vs Forge (quick take)

## Fabric
- **Pros:** lightweight, fast iteration, modern ecosystem, great for performance-sensitive server mods, tends to be cleaner to maintain.
- **Cons:** some mod compatibility expectations differ from Forge; certain APIs/solutions may require extra libraries.
- **Choose Fabric if:** you want **a tight custom mechanic**, minimal overhead, and you’re comfortable living in a more “developer-first” ecosystem.

## Forge / NeoForge
- **Pros:** huge modding ecosystem, lots of examples, broad compatibility with larger modpacks; more batteries-included patterns.
- **Cons:** heavier, more boilerplate, sometimes slower iteration; version churn can be more painful.
- **Choose Forge/NeoForge if:** you want **maximum compatibility** with existing modpacks and you expect players to combine your mechanic with many other heavy mods.

## Default recommendation
If this is primarily a **server-side world-physics mechanic** you want to tune aggressively: **Fabric**.
If your primary goal is **modpack adoption and broad compatibility**: **Forge/NeoForge**.

