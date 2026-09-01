# The document under review

The team's requirements document follows the `cas-handbook-req-template`, an AsciiDoc
implementation of the four "books" from Bertrand Meyer's *Handbook of Requirements and Business
Analysis* (Springer, 2022).

## Repository layout

| Path | What it holds |
|---|---|
| `index.adoc` | Root document; assembles everything. |
| `metadata.adoc` | Team-supplied settings: authors, project title, course number and term, revision, current milestone, draft flag. **Read this first** — it tells you who the team is and which milestone they are on. |
| `parts/core.adoc` | Assembly order of the four books. |
| `parts/control.adoc` | Document-level version and feedback tracking table. |
| `parts/integrity.adoc` | Per-author academic-integrity affirmation. |
| `parts/goals/`, `parts/environment/`, `parts/system/`, `parts/project/` | One file per section, plus an `index.adoc` and a `control.adoc` per book. |
| `appendix/`, `models/`, `mockups/` | Appendices, PlantUML sources, and interface mockups. |

## Reading a section file

Every section file has the same shape:

```asciidoc
[#g3,reftext=G.3]
=== (G.3) Expected Benefits

ifdef::env-draft[]
TIP: _New processes, or improvement to existing processes, ..._  <<BM22>>
endif::[]

{emptysec}
```

- The **anchor** (`[#g3,...]`) is what cross-references point at, as `<<g3>>`.
- The `ifdef::env-draft[]` block is the *template's own* guidance, quoted from the Handbook. It is
  not the team's writing. Do not review it, and do not count it as content.
- **`{emptysec}` means the section is unwritten.** It expands to "Nothing available at this
  point." Its presence, and nothing else, is what tells you a section is still empty.
- Draft mode is toggled by `:env-draft:` in `metadata.adoc`; teams comment it out for final
  delivery, which hides the guidance blocks in the built PDF but leaves them in the source.

## Section inventory

26 sections across four books. Anchors are the lowercase id without the dot.

### (G) Goals — `parts/goals/`

| Id | Title | File | Anchor | Milestone |
|---|---|---|---|---|
| G.1 | Context and Overall Objectives | `parts/goals/G1.adoc` | `<<g1>>` | 1 |
| G.2 | Current situation | `parts/goals/G2.adoc` | `<<g2>>` | 1 |
| G.3 | Expected Benefits | `parts/goals/G3.adoc` | `<<g3>>` | 1 |
| G.4 | Functionality overview | `parts/goals/G4.adoc` | `<<g4>>` | 1 |
| G.5 | High-level usage scenarios | `parts/goals/G5.adoc` | `<<g5>>` | 2 |
| G.6 | Limitations and Exclusions | `parts/goals/G6.adoc` | `<<g6>>` | 2 |
| G.7 | Stakeholders and requirements sources | `parts/goals/G7.adoc` | `<<g7>>` | 1 |

### (E) Environment — `parts/environment/`

| Id | Title | File | Anchor | Milestone |
|---|---|---|---|---|
| E.1 | Glossary | `parts/environment/E1.adoc` | `<<e1>>` | 1 |
| E.2 | Components | `parts/environment/E2.adoc` | `<<e2>>` | 2 |
| E.3 | Constraints | `parts/environment/E3.adoc` | `<<e3>>` | 2 |
| E.4 | Assumptions | `parts/environment/E4.adoc` | `<<e4>>` | 2 |
| E.5 | Effects | `parts/environment/E5.adoc` | `<<e5>>` | 1 |
| E.6 | Invariants | `parts/environment/E6.adoc` | `<<e6>>` | 1 |

### (S) System — `parts/system/`

| Id | Title | File | Anchor | Milestone |
|---|---|---|---|---|
| S.1 | Components | `parts/system/S1.adoc` | `<<s1>>` | 2 |
| S.2 | Functionality | `parts/system/S2.adoc` | `<<s2>>` | 2 |
| S.3 | Interfaces | `parts/system/S3.adoc` | `<<s3>>` | 2 |
| S.4 | Detailed usage scenarios | `parts/system/S4.adoc` | `<<s4>>` | 2 |
| S.5 | Prioritization | `parts/system/S5.adoc` | `<<s5>>` | 3 |
| S.6 | Verification and acceptance criteria | `parts/system/S6.adoc` | `<<s6>>` | 2 |

### (P) Project — `parts/project/`

| Id | Title | File | Anchor | Milestone |
|---|---|---|---|---|
| P.1 | Roles and personnel | `parts/project/P1.adoc` | `<<p1>>` | 3 |
| P.2 | Imposed technical choices | `parts/project/P2.adoc` | `<<p2>>` | 3 |
| P.3 | Schedule and milestones | `parts/project/P3.adoc` | `<<p3>>` | 3 |
| P.4 | Tasks and deliverables | `parts/project/P4.adoc` | `<<p4>>` | 3 |
| P.5 | Required technology elements | `parts/project/P5.adoc` | `<<p5>>` | 3 |
| P.6 | Risk and mitigation analysis | `parts/project/P6.adoc` | `<<p6>>` | 1 |
| P.7 | Requirements process and report | `parts/project/P7.adoc` | `<<p7>>` | 1 |

## Section boundaries

The template deliberately separates concerns across its four books, and its own `ifdef::env-draft[]`
guidance states where each concern belongs. Misplaced material is a common finding, so the pairs
that look alike belong here.

_TODO: the boundary table — which pairs of sections teams confuse, and the distinction the
template draws between them. Source it from the guidance blocks in the section files rather than
from memory._
