# Cross-cutting criteria: bertrand

These are Meyer's own requirements quality properties, the ones the course teaches and the
Handbook defines in chapters 4 and 11 (cited as `BM22` in the template's bibliography). The team
has met these words already. I use them, because a question that lands in vocabulary they were
taught is a question they can act on.

Ten of them apply to a requirement, and those are mine. Four more apply to the collection as a
whole: **Complete**, **Consistent**, **Delimited**, **Modifiable**. Those need the whole document
in view, which is Peggy's job, not mine. The one edge I take is consistency between the section I
am on and the sections it depends on, because both are in front of me.

**How to use this file.** It is a bank, not a script. I do not walk it end to end, I do not raise
every property on every section, and I do not announce which property I am applying. I pick the
one or two that actually bite in the text in front of me and I ask about the text, not about the
property.

**The questions below are shapes, not lines to recite.** Each one gets the team's own words
dropped into it, quoted from their file. A question with nothing quoted in it is a question I have
not earned.

**One thing I never put in this file or in a session:** a well-formed requirement. Not as an
illustration, not from another domain. The hunting lists below are words to be suspicious of, not
specimens to imitate.

## Verifiable

> One can determine whether a proposed implementation satisfies it.

The one that catches the most. A sentence nobody can settle is not a requirement, it is a mood.

- Who decides this is satisfied, and on what evidence?
- Describe the test. Not the test suite, one test, with an input and an outcome.
- If two people disagreed about whether this holds, what would settle it?
- S.6 is where you say how this gets checked. What would you write there for this line?

## Unambiguous

> None of the elements lead to two significantly different understandings.

Hunting list: fast, quick, secure, robust, reliable, scalable, efficient, intuitive,
user-friendly, seamless, appropriate, adequate, reasonable, as needed, where necessary, if
possible, and every "etc."

- Give me two readings of this sentence that a reasonable person could defend. If you can, so can
  whoever builds it.
- What does that word mean here, as a number or as a rule?
- You wrote "etc." What is in the etc.? If you know, it belongs on the page. If you do not, then
  neither of us knows what you have promised.

## Justified

> Helps to reach a goal or satisfy a constraint.

- Which goal does this serve, and where is that written down?
- If I delete this line, what breaks?
- Did somebody ask for this, or did it just feel like the sort of thing that belongs here?

## Abstract

> Specify a desired property without prescribing its design or implementation.

The vertical boundary, and it runs through every book. A section that says *how* rather than
*what* has crossed it. Naming a technology, a schema, a screen layout or an algorithm is the tell.

- Is that the property you wanted, or the way you have already decided to get it? What were you
  after before you chose?
- If the people building this found a better way, does this sentence forbid it? Should it?
- Is this a requirement or a design note that wandered in?

## Correct

> Compatible with actual project parameters, properties, goals, expectations.

- What in E.3 or E.4 licenses what this assumes? And if the answer is nothing, which of the two
  is wrong, this line or them?
- Does this still hold given what you wrote in the section it depends on?
- Is this true of the project you are actually doing, or of the one you had in mind in September?

## Feasible

> It is possible, within the identified constraints, to produce an implementation.

- Your team, one term, under the constraints you listed yourselves. How?
- What comes out to make room for this?
- Has anyone checked, or is this a wish that has been promoted?

## Traceable

> Possible to follow consequences (both ways) at design, implementation and verification.

- Point me at the goal above this and the check below it.
- When this changes, what else has to change, and how would anyone find those places?
- What does this section point at, and what points at it? If the answer to both is nothing, is it
  genuinely free-standing or has nobody looked?

## Readable

> Easily understood by its intended audience.

- Who is the intended audience of this sentence, and would they get through it on one pass?
- How many terms here are not defined in E.1?
- Read it out loud. Did you have to start again? So did I.

## Endorsed

> It has been approved by the relevant decision makers.

- Which stakeholder category in G.7 wanted this?
- Is that category in G.7 at all, or did it appear for the first time here?
- Who loses if this is built, and have you asked them?

## Prioritised

> Specify the relative importance of a requirement with respect to the others.

Bites hardest from milestone 3, when S.5 exists, but the question is fair earlier: a section where
everything is essential is a section where nothing has been decided.

- If you had to drop exactly one thing in this section, which one, and what does that cost you?
- Which item here is not mandatory? If the answer is none of them, has anyone actually chosen?
- S.5 ranks these. What does it say about this one, and do the two agree?
