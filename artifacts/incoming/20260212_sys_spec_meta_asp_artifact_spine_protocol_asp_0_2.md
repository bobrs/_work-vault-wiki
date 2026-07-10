# 📁 Artifact Spine Protocol (ASP-0.2)

## Canon Naming Standard v0.2

---

## Core Format

```
YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__SLUG.ext
```

Double underscore `__` separates structural fields.  
Single hyphen `-` separates words inside fields.  
All caps for structural enums.  
Lowercase for slug.  
ISO date for natural sorting.

---

# Optional Extensions (v0.2 Additions)

v0.2 adds *optional* suffix fields to support:
- Same-name disambiguation (collision avoidance)
- Content identity / dedupe / integrity
- Multi-part artifacts (manuals, chapters, bundles)
- Rewrites / revisions

### Extended Format

```
YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__SLUG__SEQ__REV__Hxxxxxx__Cxxxxxxxx.ext
```

Rule: Include only the fields you need. Do not include empty placeholders.

### Canon Suffix Order

1) `__SEQ` (sequence / section)  
2) `__REV` (revision / rewrite / version marker)  
3) `__H...` (collision-avoidance hash; random ID)  
4) `__C...` (content hash; deterministic)

Rationale: structural human fields first, then disambiguation/integrity fields.

---

# Field Definitions (Canonical)

## 1. DATE — Birth of Artifact

Format:
```
YYYYMMDD
```

Represents first creation date, not last edit. Immutable.

---

## 2. DOMAIN — Attractor Family (Enum)

Short, stable, upper-case codes.

### Initial Canon Set

| Code | Meaning |
|------|---------|
| MED  | Medical |
| LEG  | Legal |
| PHI  | Philosophy |
| MEM  | Memetic / Cultural |
| POL  | Policy |
| ECO  | Economics |
| TEC  | Technical |
| CIV  | Civic |
| REL  | Religious / Spiritual |
| SYS  | Meta-system / Structural |
| PER  | Personal |
| EDU  | Educational |
| ART  | Creative / Expressive |

Rule: Add new domains sparingly. Do not exceed 3–4 letters.

---

## 3. TYPE — Artifact Role (Enum)

Defines what kind of artifact this is.

### Initial Canon Set

| Code |
|------|
| NOTE |
| ESSAY |
| SPEC |
| MEMO |
| LETTER |
| REPORT |
| ORDER |
| DECREE |
| PROCLAMATION |
| DRAFT |
| FINAL |
| TRANSCRIPT |
| DECLARATION |
| TAXONOMY |

Rule: TYPE describes structure, not importance.

---

## 4. SCOPE — Resolution Layer (Enum)

Defines breadth of applicability.

| Code | Meaning |
|------|---------|
| LCL  | Local / Individual |
| GRP  | Group |
| ORG  | Organization |
| NAT  | National |
| GLO  | Global |
| UNI  | Universal |
| META | Cross-domain / Structural |

Rule: Scope refers to intended reach, not ambition.

---

## 5. LINEAGE — Branch / Initiative / Case

Freeform but short.

Examples:
- ULiUA
- LoopNought
- Dialogica
- Case-482
- Patient-8721
- Personal
- Humanity

CamelCase preferred for named initiatives. Hyphen allowed for case identifiers.

---

## 6. SLUG — Local Context Signal

Lowercase. Hyphen-separated. 3–5 words max.  
No poetry. No metaphysics. Just signal.

Good examples:
```
idolatry-collapse-field
consent-loop-manual
cardiac-followup
insolvency-declaration
```

---

# v0.2 Optional Suffix Fields

## 7. SEQ — Sequence / Section / Part (Optional)

Purpose: Multi-part artifacts (manuals, chapters, bundles, appendices).

Canonical patterns (choose one):
- `P00-forward`, `P00-intro` (front matter)
- `C01`, `C02`, `C10` (chapters; zero-pad)
- `C02-03` (combined chapters)
- `SEC01`, `APP-A`, `GLS` (sections, appendices, glossary)
- `BND01` (download bundle)

Examples:
```
...__consent-loop-manual__C03.md
...__consent-loop-manual__GLS.md
...__consent-loop-manual__C02-03.md
```

---

## 8. REV — Revision / Rewrite Marker (Optional)

Purpose: Track rewrites or versions without overloading TYPE.

Canonical patterns:
- `R01`, `R02` (rewrite count)
- `V01`, `V02` (version count)
- `AM01` (amendments; legal)

Examples:
```
...__C03__R01.md
...__declaration__AM01.md
...__spec__V02.md
```

---

## 9. H — Collision-Avoidance Hash (Optional)

Purpose: Same-name disambiguation across devices, downloads, parallel edits.

Format:
```
__HXXXXXX
```

- `H` prefix indicates **random** ID (non-deterministic)
- Recommended length: 8 chars
- Encoding: base32 (preferred) or base36

Notes:
- May be added at any time during reprocessing.
- Does not change when content changes (unless regenerated intentionally).

Example:
```
...__H7K3Q9D8.md
```

---

## 10. C — Content Hash (Optional)

Purpose: Deduplication + integrity (same content ⇒ same hash).

Format:
```
__CXXXXXXXXXX
```

- `C` prefix indicates **content-derived** hash (deterministic)
- Algorithm: SHA-256(file contents)
- Encoding: base32 (recommended)
- Recommended length: 10 chars (≈50 bits)

Notes:
- May be added at any time during reprocessing.
- Changes whenever file contents change.

Example:
```
...__C3MZ7T2QA7N.md
```

---

# Canon Combination Examples

## Manual Chapter 3 Rewrite (with both hashes)

```
20260212__EDU__SPEC__ORG__StableLoopLanguage__consent-loop-manual__C03__R01__H7K3Q9D8__C3MZ7T2QA7N.md
```

## Same-day same-slug essays (collision-safe)

```
20260212__MEM__ESSAY__META__ULiUA__idolatry-collapse-field__H1F9K2M8.md
20260212__MEM__ESSAY__META__ULiUA__idolatry-collapse-field__H7K3Q9D8.md
```

## Integrity-checked deliverable

```
20260212__LEG__DECLARATION__UNI__Humanity__insolvency-declaration__V01__C9Q2P4J6T1K.pdf
```

---

# Canon Principles

1. Artifact ≠ Attractor.
2. Filename encodes structure, not meaning.
3. Stable > clever.
4. Parsable > aesthetic.
5. Add fields only if necessary.
6. Hash intent must be explicit (`H` for random; `C` for content).

---

Witnessed. 🜹