# Whole-document checks: peggy

I work across the entire document, so my material is not filed per section. Each dimension gets
its own file here. A pass covers one of them, chosen by the team, not all seven at once.

| File | Covers |
|---|---|
| `consistency.md` | Two sections that cannot both be true. Meyer's Consistent, at document level. |
| `terminology.md` | E.1 against the words the document actually uses. One thing named twice, one name covering two things. |
| `traceability.md` | Chains that should connect and do not: a goal, the behaviour serving it, the check catching it. |
| `coverage.md` | What the current milestone expects, and what is delimited as out of scope. Meyer's Complete and Delimited. |
| `placement.md` | Material on the wrong side of a boundary the template draws. Both sides read together. |
| `conformance.md` | The template's own mechanics: anchors, cross-references, control tables, draft mode. |
| `notation.md` | Whether an artefact follows the notation the course teaches: EARS, the domain model, UML diagrams, user stories, Gherkin, MoSCoW. |

Two of Meyer's four collection-level properties have a home above: Complete and Delimited in
`coverage.md`, Consistent in `consistency.md`. The fourth, **Modifiable**, is not a dimension of
its own. It is what `terminology.md` and `traceability.md` are protecting: a document where one
thing is said in one place can absorb a change, and one where it is said in four cannot.

`notation.md` is the largest and the one with the sharpest boundary against Bertrand. It checks
where the words go. Whether they were worth writing is his. The course states that division itself,
in the warning attached to the EARS templates, and the file quotes it.
