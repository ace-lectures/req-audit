<!-- GENERATED from shared/document-map.md by scripts/sync.py. Do not edit. -->

# The document under review

The team's requirements document follows the `cas-handbook-req-template`, an AsciiDoc
implementation of the four "books" from Bertrand Meyer's *Handbook of Requirements and Business
Analysis* (Springer, 2022).

## Repository layout

| Path | What it holds |
|---|---|
| `index.adoc` | Root document; assembles everything. |
| `metadata.adoc` | Team-supplied settings: authors, project title, course number and term, revision, current milestone, draft flag. **Read this first**: it tells you who the team is and which milestone they are on. |
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

### (G) Goals, in `parts/goals/`

| Id | Title | File | Anchor | Milestone |
|---|---|---|---|---|
| G.1 | Context and Overall Objectives | `parts/goals/G1.adoc` | `<<g1>>` | 1 |
| G.2 | Current situation | `parts/goals/G2.adoc` | `<<g2>>` | 1 |
| G.3 | Expected Benefits | `parts/goals/G3.adoc` | `<<g3>>` | 1 |
| G.4 | Functionality overview | `parts/goals/G4.adoc` | `<<g4>>` | 1 |
| G.5 | High-level usage scenarios | `parts/goals/G5.adoc` | `<<g5>>` | 2 |
| G.6 | Limitations and Exclusions | `parts/goals/G6.adoc` | `<<g6>>` | 2 |
| G.7 | Stakeholders and requirements sources | `parts/goals/G7.adoc` | `<<g7>>` | 1 |

### (E) Environment, in `parts/environment/`

| Id | Title | File | Anchor | Milestone |
|---|---|---|---|---|
| E.1 | Glossary | `parts/environment/E1.adoc` | `<<e1>>` | 1 |
| E.2 | Components | `parts/environment/E2.adoc` | `<<e2>>` | 2 |
| E.3 | Constraints | `parts/environment/E3.adoc` | `<<e3>>` | 2 |
| E.4 | Assumptions | `parts/environment/E4.adoc` | `<<e4>>` | 2 |
| E.5 | Effects | `parts/environment/E5.adoc` | `<<e5>>` | 1 |
| E.6 | Invariants | `parts/environment/E6.adoc` | `<<e6>>` | 1 |

### (S) System, in `parts/system/`

| Id | Title | File | Anchor | Milestone |
|---|---|---|---|---|
| S.1 | Components | `parts/system/S1.adoc` | `<<s1>>` | 2 |
| S.2 | Functionality | `parts/system/S2.adoc` | `<<s2>>` | 2 |
| S.3 | Interfaces | `parts/system/S3.adoc` | `<<s3>>` | 2 |
| S.4 | Detailed usage scenarios | `parts/system/S4.adoc` | `<<s4>>` | 2 |
| S.5 | Prioritization | `parts/system/S5.adoc` | `<<s5>>` | 3 |
| S.6 | Verification and acceptance criteria | `parts/system/S6.adoc` | `<<s6>>` | 2 |

### (P) Project, in `parts/project/`

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

Material that belongs in one book routinely lands in another, and it is the single most common
thing a reviewer has to notice. The template draws these lines itself, in the `ifdef::env-draft[]`
guidance it quotes from the Handbook, and names most of the confusions below outright.

**†** marks a distinction the template states in its own guidance, naming the other section by
its anchor. The rest are read off that same guidance and are the instructor's to confirm.

The table says where the line falls. It does not say to announce that material is on the wrong
side of it: see rule 8 in `house-rules.md`.

| These get confused | Where the line falls |
|---|---|
| **G.4 vs S.2** † | Depth. G.4 is "a kind of capsule version of book S, skipping details", principal properties only. S.2 is "the bulk of the System book", one subsection per component from S.1. If a reader has to go to G.4 to learn how something works, G.4 has taken S.2's job. |
| **G.5 vs S.4** † | Vocabulary and coverage. G.5 holds main usage patterns "stated in user terms only, independently of the system's structure", with no special or erroneous cases. S.4 may name system components and covers the special and erroneous cases. A G.5 scenario that mentions a screen or a component belongs in S.4. |
| **G.6 vs P.6** † | What is scoped out versus what might go wrong. G.6 states what the system will not do. The guidance is blunt that G.6 "is not the place for an analysis of risks and obstacles, which pertain to the project rather than the goals". |
| **E.2 vs S.3** † | Direction. E.2 is interfaces provided *to* the system from the outside world. S.3 is interfaces provided *by* the system to the outside. |
| **E.2 vs P.5** † | Running versus building. E.2 is what the operating system interacts with. P.5 is "technology elements that the system's development will require". A library the team compiles against is P.5; a service the running system calls is E.2. |
| **E.3 vs E.4** † | Imposed versus chosen. E.3 is "non-negotiable restrictions coming from the environment". E.4 is properties "not imposed by the environment but assumed to hold, as an explicit decision". If the team could have decided otherwise, it is E.4. |
| **E.3 and E.4 vs E.5** † | Direction again. E.3 and E.4 are the environment acting on the system. E.5 is the reverse: "effects are influences in the reverse direction". |
| **E.5 vs E.6** | The same properties, opposite obligation. E.5 is what the system's operations change in the environment. E.6 is what they may assume on entry and must leave standing. Altered versus preserved. |
| **S.1 vs E.2** | Ownership. S.1 lists the major parts of the system being built. E.2 lists elements of the environment. A component nobody on the team can change is E.2. |
| **S.2 vs S.4** † | Description versus illustration. S.2 describes behaviour precisely. S.4 gives examples of interaction as user stories, which "are not by themselves a substitute for precise descriptions of functionality" but specify cases those descriptions must support. |
| **S.5 vs P.3 and P.4** | Criticality versus schedule. S.5 ranks what the system does, so functions can be dropped under pressure. P.3 and P.4 order the work. Criticality is a property of the system; sequence is a property of the project. |
| **P.2 vs E.3** | Both are imposed, by different parties. E.3 comes from the environment: business rules, physical laws. P.2 is bound on the project a priori, and the guidance is candid that some such choices "result from company policies" rather than technical analysis. |
| **P.3 vs P.4** † | List versus detail. P.3 is the list of tasks and their scheduling, "the project's key dates". P.4 "details the individual tasks listed under P.3 and their expected outcomes". |

### The boundary that runs through every book

Above all the pairs sits the line between requirements and design. P.5 states it outright:

> Although the actual use of such products belongs to design and implementation rather than
> requirements, it is part of the requirements task to identify elements whose availability is
> critical to the success of the project.

A section that says *how* rather than *what* has crossed it, wherever it sits. This is the one
boundary worth checking in every section rather than only in the pairs above.

### One cross-reference worth verifying

S.4's guidance reads "not by themselves a substitute for precise descriptions of functionality
(`<<s3>>`)", but functionality is S.2 in this template and S.3 is Interfaces. The sentence and the
anchor appear to disagree. It may be faithful to <<BM22>> and it may be a slip carried into the
template; settling it needs the Handbook itself, which ships as `plan.pdf` in the template
repository. Until it is settled, read the sentence rather than the anchor, and do not treat a team
that followed one or the other as having made an error.

## Section dependencies

A section-scoped reviewer works on one section **and the sections it depends on**, the ones whose
content it builds upon or must stay consistent with. This is the map that says which those are.

### The four books

PEGS books are not written in sequence, but they do refer to each other in one prevailing
direction:

```
Environment  ──────┐          the world, which exists whether or not the project does
                   ↓
Goals  ────────────┼───────→  why the system is wanted, in business terms
                   ↓
System ────────────┼───────→  what the system does, given those goals in that world
                   ↓
Project ───────────┘          how it gets built, given all of the above
```

- **Environment** is the most self-standing book. It describes what is true of the world
  regardless of this project, so it borrows least from the others.
- **Goals** builds on Environment (it describes a situation *in* that world) and on nothing in
  System or Project. A goal expressed in terms of the system's own structure is a goal that has
  leaked downward.
- **System** builds on Goals (what the system is for) and Environment (what it must live with).
- **Project** builds on all three, and on System most of all: you cannot schedule what you have
  not specified.

A reference pointing *up* this order is the strongest signal that material is in the wrong book.

### Two dependencies that hold everywhere

- **E.1 (Glossary)** underpins every section in every book. It is deliberately left out of the
  table below, which would otherwise list it 25 times. Any section using a domain term depends on
  E.1 defining it, and on using it in that sense.
- **G.7 (Stakeholders and requirements sources)** is where the content of the Goals book comes
  from. It is listed only where the dependency is direct, but a claim anywhere in G with no
  traceable source in G.7 is worth a question.

### Dependencies are context, not preconditions

The sections a section depends on are there to **give the reviewer context and to expose
inconsistency**. They are not requirements that must be satisfied before the section can be
judged.

- **A dependency that is empty, thin or absent is not a finding.** It may be due at a later
  milestone, or the team may simply not have written it yet. Do not raise it, do not treat it as a
  gap in the section under review, and do not ask the team to go write it first.
- **Read the dependencies to check the section against them**, not to audit the dependencies
  themselves. The question is whether this section contradicts, silently duplicates, or drifts
  from what it builds on, and whether a term or claim it leans on is actually established there.
- **When a dependency is empty, ask the question anyway and carry on.** The check that could not be
  made is still a question worth putting: "Which components do these behaviours belong to?" works
  whether or not S.1 has been written. Do not announce the emptiness, and do not make it the
  subject. Then review the section on its own terms.
- **The same goes for `Feeds`.** Downstream sections that do not exist yet are not omissions. The
  column is there so a question can be weighed: one that three later sections will inherit is
  worth more of the team's attention than one that stops where it is.

A section is reviewed on what it says, in the light of whatever context happens to exist.

### The table

`Depends on` is what to read before judging a section. `Feeds` is the exact inverse: the sections
that will inherit the problem if this one is wrong, which is what makes a finding worth raising.

**†** marks a dependency stated outright in the template's own `ifdef::env-draft[]` guidance. The
rest are read off the PEGS structure and are the instructor's to confirm or correct.

| Section | Depends on | Feeds |
|---|---|---|
| **G.1** | none | G.2, G.3, G.7, P.2 |
| **G.2** | G.1 | G.3 |
| **G.3** | G.1, G.2 | G.4, G.6, S.5, S.6 |
| **G.4** | G.3 | G.5, G.6, S.1, S.2 |
| **G.5** | G.4, G.7 | S.4 |
| **G.6** | G.3, G.4 | P.6 |
| **G.7** | G.1 | G.5, P.1, P.7 |
| **E.1** | none | none |
| **E.2** | none | E.3, S.1, S.3, P.5 |
| **E.3** | E.2 | E.4, E.5, E.6, S.2, P.2 |
| **E.4** | E.3† | E.5, E.6, S.2 |
| **E.5** | E.3†, E.4† | E.6, S.2 |
| **E.6** | E.3, E.4, E.5 | S.2 |
| **S.1** | G.4, E.2 | S.2, P.5 |
| **S.2** | G.4, E.3, E.4, E.5, E.6, S.1† | S.3, S.4, S.5, S.6, P.5 |
| **S.3** | E.2†, S.2† | S.4, S.5 |
| **S.4** | G.5†, S.2, S.3† | S.5, S.6 |
| **S.5** | G.3, S.2†, S.3†, S.4† | P.3 |
| **S.6** | G.3, S.2, S.4 | none |
| **P.1** | G.7, P.4 | none |
| **P.2** | G.1, E.3 | none |
| **P.3** | S.5 | P.4, P.6 |
| **P.4** | P.3† | P.1, P.6 |
| **P.5** | E.2†, S.1, S.2 | P.6 |
| **P.6** | G.6†, P.3, P.4†, P.5† | none |
| **P.7** | G.7 | none |

### Where the table and the milestones disagree

The milestone split does not follow the dependency order everywhere, and two cases are worth
knowing about because they look like errors in a team's document when they are not:

- **E.5 and E.6 are due at milestone 1, but depend on E.3 and E.4, due at milestone 2.** A team
  writing effects and invariants before constraints and assumptions is following the schedule, not
  making a mistake. Expect E.5 and E.6 to need revisiting once E.3 and E.4 exist.
- **G.4 is due at milestone 1 and S.2 at milestone 2.** That is the intended direction,
  the capsule overview first and the specification after, but it means S.2 arriving without changing
  G.4 deserves a question, since elaborating functionality usually reveals the overview was
  wrong.
