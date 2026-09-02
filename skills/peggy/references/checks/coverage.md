# Coverage: peggy

**What I compare.** What this milestone expects against what the document has, and what the
document claims to be about against what it bounds. Meyer's *Complete* and *Delimited*.

**How the mismatch shows.** Something expected and absent, or something claimed and unbounded.

**The rule that governs this file: I never count.** Not how many sections are empty, not how many
gaps there are, not a proportion. A count is a score with the arithmetic hidden. I name what
matters and say nothing about the size of what I do not.

## Milestone coverage

`milestones.md` says which sections each milestone expects. A section still holding `{emptysec}`
because its milestone has not arrived is not a finding and is not mentioned. A section this
milestone expects, still empty, is worth one question and no more.

The three revisions have their own milestones: E.1 gains a domain model at 2, S.6 gains tests and
a traceability matrix at 3, P.6 gains threats at 3. A first version that was fine at its own
milestone can still be short of what the revision asks.

## Internal completeness

- Every S.1 component with behaviour in S.2.
- Every S.2 behaviour reachable through S.3.
- Every G.7 category appearing somewhere after G.7.
- Every S.2, S.3 and S.4 element carrying a priority once S.5 exists.

## Delimited

- G.6 exists and bounds something a reader might otherwise have assumed.
- The scope in G.6 and the functionality in G.4 do not overlap.

## Questions

- Milestone 2 expects S.3 and it still holds `{emptysec}`. Is that where you are?
- Where does this S.1 component get its behaviour described? If nowhere, is that deliberate?
- E.1 was written at milestone 1 and the revision at milestone 2 asks for a domain model. Where is
  it?
- What does G.6 rule out that somebody reading G.4 would otherwise expect?
