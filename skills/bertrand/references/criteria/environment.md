# (E) Environment: bertrand criteria

One entry per section: what it owes, where it goes wrong, and what I ask. These sharpen the
cross-cutting properties in `cross-cutting.md`; they do not replace them. "Where it goes wrong" is
my note to myself, not a line I deliver: I ask, I do not pronounce.

Boundaries with other sections are in `document-map.md`. I name the risk here and ask the question;
I do not recite the table.

## (E.1) Glossary

`parts/environment/E1.adoc` · milestone 1

**Owes.** Precise definitions of the project's vocabulary: domain terms, acronyms, and ordinary words used in a special sense. It covers the whole document, not just the Environment book.

**Where it goes wrong.** It defines the easy words and misses the dangerous ones. Or the definitions are dictionary entries that say nothing about how this project uses the term. At milestone 2 the revision asking for a domain model gets skipped.

- Pick any three domain terms used elsewhere in the document. Are they here?
- Which of these definitions would an outsider read and still not know how you use the word?
- Which ordinary English words does your project use in a special sense? Those are the ones that hurt. Are they here?
- From milestone 2: the revision asks for a domain model. What are the relationships between these terms, not just their definitions?

## (E.2) Components

`parts/environment/E2.adoc` · milestone 2

**Owes.** Elements of the environment that affect the system or are affected by it, including existing systems it must interface with. These are interfaces offered to the system from outside.

**Where it goes wrong.** Interfaces the system provides outward end up here instead of S.3. Development tooling ends up here instead of P.5.

- For each of these: does it exist whether or not you build this system?
- Which of these does the running system talk to, and which does your team need in order to build it?
- What happens to the system when one of these is unavailable?

## (E.3) Constraints

`parts/environment/E3.adoc` · milestone 2

**Owes.** Non-negotiable restrictions imposed by the environment: business rules, physical laws, externally imposed engineering decisions.

**Where it goes wrong.** Assumptions get filed here because they sound firmer that way. Or a decision the team made themselves is presented as though the world imposed it.

- Who imposed this, and could you negotiate it away? If you could, which section does it belong in?
- Is this a limit coming from the world, or a choice your team made?
- How would you know if you had violated it?

## (E.4) Assumptions

`parts/environment/E4.adoc` · milestone 2

**Owes.** Properties not imposed by the environment but assumed to hold, as an explicit decision to simplify the system.

**Where it goes wrong.** Constraints get mislabelled as assumptions. Or the assumptions the team actually relies on are never written down, which is the expensive kind.

- What happens if this turns out to be false? If the answer is nothing, why state it?
- Is this assumed, or imposed on you?
- What are you relying on elsewhere in the document that is not declared here?

## (E.5) Effects

`parts/environment/E5.adoc` · milestone 1

**Owes.** What the system's operation changes in the environment. Influence running from the system outward, the reverse of E.3 and E.4.

**Where it goes wrong.** The direction gets reversed and constraints appear here. Or the effects are a restatement of system features rather than changes to the world.

- Does this describe the system changing the world, or the world constraining the system?
- Who notices when this effect happens, and how would they notice?
- Which of these effects would somebody be unhappy about?

## (E.6) Invariants

`parts/environment/E6.adoc` · milestone 1

**Owes.** Properties of the environment that operations may assume when they start and must leave standing when they finish.

**Where it goes wrong.** It becomes a second copy of E.3, or it collects things the system deliberately changes, which are E.5. Or the invariants cannot be checked at all.

- State it as something true both before and after every operation. Can you?
- Is this preserved by the system, or imposed on it?
- What breaks if it stops holding halfway through an operation?

