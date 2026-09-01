# Milestones

The document is delivered three times. Each delivery is a full document; the milestone only says
which sections are expected to have content by then. Sections outside the current milestone are
legitimately still empty. Do not treat them as omissions.

**Ask which milestone the team is on before reviewing anything.** `metadata.adoc` carries a
`:milestone:` attribute, but it is often stale; confirm it with the team.

## Milestone 1: 10 sections

Establish why the project exists and who cares about it.

| Book | Sections |
|---|---|
| Goals | G.1, G.2, G.3, G.4, G.7 |
| Environment | E.1, E.5, E.6 |
| System | none |
| Project | P.6, P.7 |

## Milestone 2: 10 sections, plus one revision

Specify the system and the environment it sits in.

| Book | Sections |
|---|---|
| Goals | G.5, G.6 |
| Environment | E.2, E.3, E.4 |
| System | S.1, S.2, S.3, S.4, S.6 |
| Project | none |

**Revision due:** E.1, extend the glossary with a domain model (a class diagram) so the
terminology has structure, not just definitions.

## Milestone 3: 6 sections, plus two revisions

Plan the work and commit to what matters most.

| Book | Sections |
|---|---|
| Goals | none |
| Environment | none |
| System | S.5 |
| Project | P.1, P.2, P.3, P.4, P.5 |

**Revisions due:**

- S.6: take the single most important scenario from S.4 and propose five tests for it, in any
  formalism, plus a traceability matrix linking the tests back to the requirements.
- P.6: identify up to two security threats and describe mitigation mechanisms.

## What a milestone review means

A milestone says which sections are expected to have content by then. It does not say which
sections may be asked about.

**Every written section is in scope, whatever milestone it was due at.** Each delivery is the
whole document, and a section does not become settled because its milestone has passed. G.3, due
at milestone 1, is as open to questions in December as it was in October.

What is not in scope is a section that is still empty because its milestone has not arrived. That
is not an omission and not a finding. See rule 7 in `house-rules.md`.

### Later work puts pressure on earlier work

The dependency direction in `document-map.md` says which sections press on which, and the
milestone split makes two of those routine rather than exceptional. Both are set out under "Where
the table and the milestones disagree" in that file:

- E.5 and E.6 are written at milestone 1 but depend on E.3 and E.4, which arrive at milestone 2.
- G.4 is written at milestone 1 and S.2 elaborates it at milestone 2, which usually reveals that
  the overview needs to move.

A section that its dependencies have overtaken is the most productive thing to look at during a
later milestone, because the team has learned something since they wrote it.

### A section unchanged since the last milestone

Rule 3 allows reading the git history. A section untouched since an earlier milestone was either
right the first time or stopped being thought about, and those are very different situations.

Ask which one it is. Do not assume the second: a section that needed no edits is a good outcome,
and a team that can say why it still holds has answered well. The question is what makes that
visible, not an accusation of neglect, and like everything else it is asked rather than asserted.

### Revisions carry their own milestone

Three sections are revisited on a schedule rather than written once: E.1 at milestone 2, S.6 and
P.6 at milestone 3. Those revisions are listed with their milestones above. A first version that
was fine at its own milestone can still be short of what the revision asks for.

### Draft mode at milestone 3

`metadata.adoc` carries `:env-draft:`, which shows the template's guidance blocks in the built
document. The template's README says to comment it out for the final delivery.

If it is still on at milestone 3, that is worth asking about. Note that commenting it out only
hides the guidance in the built PDF; the `ifdef::env-draft[]` blocks stay in the source either
way, so their presence in a section file says nothing about whether the team did this.

### Control tables

The template keeps two review-process records.

Each book's `control.adoc` holds a per-section grid: `Section | Version | Lead | Delivered |
Reviewer | Approved`. This is where the lead author and lead reviewer of each section are recorded.

`parts/control.adoc` holds one row per delivery, V1 to V3, against a Version column, a Delivery
pair of Deadline and Delivered, and a Feedback pair of Received and Integrated. The same file
carries a biography stub for each author.

These belong to a **whole-document sweep only**. A persona scoped to one section leaves them
alone: they record the team's process across the document, and a single section gives no useful
view of them.
