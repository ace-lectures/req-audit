# (S) System: frida criteria

One entry per section: what gets decided here, where teams close early, and what I ask. These
sharpen the three lenses in `cross-cutting.md`; they do not replace them. "Where teams close
early" is my note to myself, not a line I deliver.

Every question names an axis. None of them names what the answer should be. If the team could
paste my words into their document as a requirement, I wrote the question wrong.

## (S.1) Components

`parts/system/S1.adoc` · milestone 2

**What gets decided here.** The decomposition: what counts as a part, and along which principle the system is cut up.

**Where teams close early.** The first architecture anyone drew, which usually mirrors how the team divided the work rather than anything about the system.

- Why this split? Does it mirror the system, or your team?
- Which two of these would you merge if forced? Which one would you split?
- What does this look like decomposed along a different principle entirely?
- Which component here is quietly doing the work of two?

## (S.2) Functionality

`parts/system/S2.adoc` · milestone 2

**What gets decided here.** What the system does rather than a person, and how much judgement is handed to it.

**Where teams close early.** The current process gets automated rather than reconsidered, so behaviours exist because the old paper form had a box for them.

- For each of these: who does it today, and why is the system doing it now?
- Which could a person do instead, and what would that cost?
- What does the system decide here, and what does it merely record?
- Which behaviour exists because the process you are replacing had it?

## (S.3) Interfaces

`parts/system/S3.adoc` · milestone 2

**What gets decided here.** How much of the system is exposed, to whom, and in what form.

**Where teams close early.** One interface for one kind of user, almost always a screen, because that is what the team pictured when they started.

- Who or what talks to this system that is not a person looking at a screen?
- What did you decide to expose, and what did you decide to keep inside?
- If this had no interface at all and simply ran, what would break?
- Which of these would you regret having exposed in two years?

## (S.4) Detailed usage scenarios

`parts/system/S4.adoc` · milestone 2

**What gets decided here.** Which interactions are worth writing down, and how much of the world around them counts as part of the scenario.

**Where teams close early.** One happy path per feature. Nothing between scenarios, nothing repeated, nothing abandoned halfway through.

- Which of these end badly? Where is the abandoned one, the interrupted one, the one done wrong?
- What happens between two of these? Who does the waiting, and what are they doing meanwhile?
- What does this look like for somebody doing it for the hundredth time today?
- Which scenario did you leave out because it was awkward to write?

## (S.5) Prioritization

`parts/system/S5.adoc` · milestone 3

**What gets decided here.** What matters most, and whose judgement of importance the ranking encodes.

**Where teams close early.** Priority tracks effort or enthusiasm rather than value, and the ranking is the team's view with nobody else consulted.

- Who decided this ranking? Would the categories in G.7 rank it the same way?
- What sits at the bottom, and why is it in the document at all?
- Rank these instead by who complains loudest when it is missing. Does the order change?
- Which of these is high because it is interesting to build?

## (S.6) Verification and acceptance criteria

`parts/system/S6.adoc` · milestone 2

**What gets decided here.** What counts as evidence, and who has to be satisfied by it.

**Where teams close early.** The team tests what is easy to test, and acceptance means the team agreeing among themselves.

- Who has to be convinced by this, and would it convince them?
- Which behaviour in S.2 is hardest to check? Is it anywhere in this section?
- What would you accept as evidence from somebody you did not trust?
- What are you checking because it is easy rather than because it matters?

