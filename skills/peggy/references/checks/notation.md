# Notation: peggy

**What I compare.** An artefact against the rules of the notation it is written in. The course
teaches each of these, so the rules below are the course's, not mine, and a team has already been
taught every one of them.

**Where the line with Bertrand falls.** The course draws it itself, in the warning attached to the
EARS templates:

> A template does not make a requirement good. `The system shall be user friendly` fits the
> ubiquitous pattern perfectly, and nobody can test it. EARS tells you where to put the words;
> whether those words are worth writing down is what *necessary* and *verifiable* decide.

So: **I check where the words go. Bertrand checks whether they were worth writing.** A requirement
can pass everything in this file and still be worthless, and saying so is his job, not mine. If I
find myself asking whether a requirement is any good, I have wandered out of my own lane.

**And I still only ask.** I quote the line and ask which rule it is following. I do not announce
that something is malformed.

## EARS, the five templates

Taught in T05 and examined twice. A requirement should fit one of these, and the team should be
able to say which.

| Template | Shape | For |
|---|---|---|
| Ubiquitous | `The <system> shall <response>.` | the system always does it |
| State-driven | `While <state>, the <system> shall <response>.` | true while something holds |
| Event-driven | `When <trigger>, the <system> shall <response>.` | triggered by something happening |
| Unwanted behaviour | `If <trigger>, then the <system> shall <response>.` | the case everyone forgets |
| Optional feature | `Where <feature is included>, the <system> shall <response>.` | only when built with it |

What I look at:

- Whether a requirement fits any template at all. Some genuinely do not, and the course says so
  outright: saying which and why is worth more than forcing it.
- Whether the chosen template matches the sentence. A trigger written as a state, a condition
  written as a trigger.
- Whether the system is named. `The system` where the project has a name is a template filled in
  carelessly.
- **The spread.** The course is explicit that all-ubiquitous means nobody has thought about the
  system failing. A document with no `If` requirement anywhere is worth one question.

Questions:

- Which of the five is this? If none, which did you try, and what would not fit?
- This reads as a state and uses the event-driven template. Which is it, a trigger or a condition?
- Which of these use the unwanted-behaviour template? If none do, has nothing got a failure case,
  or was it simply not written?

## Domain model, the class diagram in E.1

Taught in T07 and due as the milestone 2 revision to E.1. The course is emphatic that this is a
different activity from design modelling in the other courses, even though the language is the
same.

A domain model **does not** carry method signatures or private attributes. It reifies concepts and
relationships in the problem space, not software classes in the solution space.

The subset of UML the course uses:

- **Inheritance**, white-headed arrow, reads "is a".
- **Association**, plain arrow, a link between concepts, carrying multiplicities. Undirected means
  both concepts know each other.
- **Composition**, black diamond, ownership and containment: destroying the whole destroys the
  parts.
- **Enumeration**, a class box tagged `<<enumeration>>` with the values inside. The concept reaches
  it through a named relation **instead of** also carrying an attribute of that type. The course's
  reason is worth keeping: a model that states the same fact twice can end up contradicting itself.
- **Abstract** concepts, used to structure the model taxonomically.

Questions:

- What is this method signature doing here? Is this the domain model or a design model?
- How many of these are there at each end? The association does not say.
- Composition means destroying the whole destroys the parts. Is that true here?
- This concept has both an attribute and a relation to the enumeration. Which one does a reader
  believe?
- Is this concept in the problem space, or is it something you plan to build?

## Use case diagram

Taught in T07. The rule that matters most is where the actors come from.

- **Actors are not invented.** They are the stakeholders already identified, kept only where they
  actually interact with the system. Not every stakeholder is an actor: somebody who never touches
  the system stays a stakeholder and does not belong on the diagram.
- Primary stakeholders become primary actors, drawn on the left. Secondary actors go on the right.
  The system is a rectangle.
- Actors may be people or supporting systems.
- Actor inheritance reads "is a", and abstract actors carry commonality.
- The diagram stays simple: no detail inside the use cases, and **no ordering between them**.

Questions:

- This actor is not in G.7. Where did they come from?
- This G.7 category is on the diagram. Do they touch the system, or do they just care about it?
- These use cases are drawn in a sequence. Is that ordering meant to be read?

## Activity diagram

Taught in T07, for how one concept behaves.

- Activities are rounded rectangles, conditions are diamonds or hexagons.
- Start is a circle, end is two concentric circles, and a faulty termination is an X.
- Parallel paths are genuinely parallel.
- Partitions, or swimlanes, are one per actor or system, and answer "who does what?".

Questions:

- There is no faulty termination anywhere in this diagram. Can this process only end well?
- These two branches never rejoin. Is that intended?
- Which swimlane is this activity in, and does that match who does it in S.4?

## User stories, in S.4

Taught in T09, Connextra form: **"As a `[role]`, I want `[feature]`, so that `[benefit]`."** The
template's own guidance for S.4 says the scenarios there are expressed as user stories.

- The role is a role, not a person, and should be a category from G.7.
- The benefit is the part that gets dropped, and it is the part that ties the story to a goal.

Questions:

- This story has a role and a feature and no "so that". What is the benefit?
- This role is not one of your G.7 categories. Which one is it?
- Which goal does this benefit serve?

## Gherkin, in S.6 from milestone 3

Taught in T10. `Feature`, `Scenario`, then `Given` / `When` / `Then`, with `And` to extend any of
them. Runnable as acceptance tests.

- `Given` is state before, `When` is the single action, `Then` is the observable outcome.
- More than one `When` in a scenario usually means two scenarios.
- A `Then` that is not observable cannot be a test.

Questions:

- This scenario has three `When` steps. Is that one test or three?
- What would a tool observe to decide this `Then` passed?
- Which requirement does this scenario check? The milestone 3 revision asks for the matrix that
  says so.

## MoSCoW, in S.5

Taught in T09: **Must have**, **Should have**, **Could have**, **Won't have (this time)**. The
template asks S.5 to classify by criticality without mandating a scheme, so this applies if the
team has used one.

- Every item classified, using the scheme's own words.
- "Won't have (this time)" is a real category and its relationship to G.6 is worth a question:
  one is deferred, the other is out of scope.

Questions:

- Which scheme is this, and are these its categories?
- This is marked "Won't have". Is that this release, or never? G.6 is where never lives.
- What distinguishes your Must from your Should here?
