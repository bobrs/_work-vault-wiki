# 📁 Artifact Spine Protocol (ASP-0.1)

## Canon Naming Standard v0.1

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

# Field Definitions (Canonical)

## 1. DATE — Birth of Artifact

Format:
```
YYYYMMDD
```

Represents first creation date, not last edit.  
Immutable.

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

CamelCase preferred for named initiatives.  
Hyphen allowed for case identifiers.

---

## 6. SLUG — Local Context Signal

Lowercase.  
Hyphen-separated.  
3–5 words max.  
No poetry. No metaphysics. Just signal.

Good examples:
```
idolatry-collapse-field
consent-loop-taxonomy
cardiac-followup
insolvency-declaration
```

The slug orients. It does not sermonize.

---

# Canon Principles

1. Artifact ≠ Attractor.
2. Filename encodes structure, not meaning.
3. Stable > clever.
4. Parsable > aesthetic.
5. Add fields only if necessary.

---

# Versioning Rule

Structural revisions increment protocol version:

```
ASP-0.2
```

Existing filenames remain valid unless structurally incompatible.

---

Witnessed. 🜹

