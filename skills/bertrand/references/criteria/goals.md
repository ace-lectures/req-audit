# (G) Goals: bertrand criteria

One entry per section: what it owes, where it goes wrong, and what I ask. These sharpen the
cross-cutting properties in `cross-cutting.md`; they do not replace them. "Where it goes wrong" is
my note to myself, not a line I deliver: I ask, I do not pronounce.

Boundaries with other sections are in `document-map.md`. I name the risk here and ask the question;
I do not recite the table.

## (G.1) Context and Overall Objectives

`parts/goals/G1.adoc` · milestone 1

**Owes.** Why this project exists, in business terms, and the organisational context around it.

**Where it goes wrong.** It slides into what the system does or how it will be built. Or the objectives are activities rather than outcomes, which reads as busy and commits to nothing.

- What business objective does this serve, put so that somebody outside your team could repeat it back?
- Would this objective still stand if the system were built in a completely different way? If not, what is it doing in the Goals book?
- Cross out every sentence here that describes the system. Read what is left. Does it still justify the project?

## (G.2) Current situation

`parts/goals/G2.adoc` · milestone 1

**Owes.** The as-is baseline, factually: what happens today, and what it costs.

**Where it goes wrong.** It describes the future instead of the present, or it complains about today without measuring it, which leaves G.3 with nothing to improve on.

- What is the current situation costing, in time, money, errors, or anything else countable?
- Without that number, how will anyone show later that G.3 was achieved?
- Which sentences here describe today, and which describe your plans?
- Who does this work today, and how do you know? Did you ask them, or is this what you assume happens?

## (G.3) Expected Benefits

`parts/goals/G3.adoc` · milestone 1

**Owes.** The business benefits the organisation expects. The template calls this the core of the Goals book and the guard against creeping featurism.

**Where it goes wrong.** Features get listed instead of benefits, or the benefits are unmeasurable, or they do not connect to anything in G.2.

- Take each benefit in turn. Against what in G.2 would you show it happened?
- Which of these are gains to the organisation, and which are things the system does?
- Six months in, someone proposes a feature nobody asked for. Which line here tells you to say no?
- If none of them does, what is this section for?

## (G.4) Functionality overview

`parts/goals/G4.adoc` · milestone 1

**Owes.** A capsule of what the system does. Principal properties only.

**Where it goes wrong.** It turns into S.2 with the details half done, or it is so vague that it says nothing a reader could hold you to.

- Could a stakeholder read this alone and say what the system does? Have you tried it on somebody who has not read the rest?
- How much of this will S.2 repeat? If you deleted the overlap, what would a reader lose?
- Which sentence here would have to change if S.2 changed?

## (G.5) High-level usage scenarios

`parts/goals/G5.adoc` · milestone 2

**Owes.** The main usage paths, in user terms, independent of the system's structure. No special or erroneous cases: those are S.4.

**Where it goes wrong.** Screens, buttons and components appear. Or error handling creeps in. Or the scenarios are feature lists with a user glued to the front.

- Which of these mention a screen, a component, or a system response?
- Read one aloud, replacing every system noun with the word 'somehow'. Does the user's goal survive that?
- Which benefit in G.3 does this path deliver? If none, what makes it a main path?

## (G.6) Limitations and Exclusions

`parts/goals/G6.adoc` · milestone 2

**Owes.** What the system will not do. This is the section that makes the requirements delimited.

**Where it goes wrong.** Project risks land here instead of in P.6. Or the exclusions are things nobody would have expected anyway, which costs nothing and settles nothing.

- Which of these would a stakeholder have assumed was in scope, and which would nobody ever have expected?
- Is any of this an obstacle to the project rather than a limit on the system?
- Someone asks for something in month three. Which line here settles it?

## (G.7) Stakeholders and requirements sources

`parts/goals/G7.adoc` · milestone 1

**Owes.** Categories of people who affect the project or are affected by it, plus the non-human sources: documents, standards, existing systems.

**Where it goes wrong.** Individuals get named where the template asks for categories. Or the list is users and nobody else. Or the non-human sources are missing entirely.

- Are these categories of people, or individuals? The template is explicit about which it wants.
- Who is affected by this system and is not on this list? Start with whoever loses something.
- Which of these have you actually consulted, and which are aspirational?
- Where are the documents, standards and existing systems? Or did requirements only come from people?

