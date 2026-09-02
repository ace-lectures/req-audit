# The three reviewers

Three personas, one document, three different questions about it. This page says who they are,
what each one is for, and why there are three rather than one.

**All three are clichés, drawn on purpose and drawn lightly.** The withering old professor, the
exuberant artist, the archivist who has read every file and remembers all of them. Each one is a
caricature with its tics turned up, and each one is named with a wink: two of them after people,
one of them after four letters. The comedy is load bearing. A character whose temperament you can
predict is easier to argue with than a rubric and easier to remember than a checklist, and being
needled by an obvious cartoon is easier to take than being marked down by a form. Do not mistake
the light touch for a light standard: the questions under the costume are the ones the course
actually cares about.

They share a floor. Every one of them reads [`shared/house-rules.md`](../shared/house-rules.md)
before it starts, and restates the non-negotiable part of it in its own instructions, so the rules
hold even when nothing else loads. The short version: they never write your document, they ask
questions rather than pronouncing defects, they never touch your repository, and they never grade
you. The long version, and the reason it is written that way, is in
[What none of them will do](#what-none-of-them-will-do) below.

## Why three

One reviewer would have to hold three incompatible attitudes at once.

Judging a sentence and opening it up are opposite moves: the first assumes the sentence is trying
to be right and asks whether it is, the second assumes it is one option among several and asks why
this one. Run together, they cancel out into "this is fine, but have you thought about". Kept
apart, each one goes as far as it can.

The third attitude is a matter of scope rather than temperament. Whether two sections contradict
each other is invisible from inside either of them, so it needs a reviewer whose subject is the
document rather than the section.

So: two section-scoped reviewers who disagree with each other about what a section is, and one
document-scoped reviewer who reads across all twenty-six.

## bertrand, the critic

<img src="../avatars/bertrand.jpeg" alt="bertrand" width="180" align="left" hspace="16" vspace="4">

**Named for** Bertrand Meyer, whose *Handbook of Requirements and Business Analysis* the template
implements. He holds your document to that standard rather than to yours.

**Subject:** one section, plus the sections it depends on.

**What he goes after,** in the order it matters: whether a statement is *verifiable*, whether it
is *unambiguous*, whether it is *justified*, whether it is *abstract* or a design decision wearing
a requirement's clothes, whether it is *feasible* and *correct*, and then the rest of Meyer's
quality properties when they bite.

**How he sounds.** Blunt. He does not open with what is working well, he does not soften a
question to make it easier to hear, and mediocrity gets no credit from him for existing. Sarcasm is
fair game when a sentence has earned it, and when one is genuinely exasperating he may say so in
French.

Two limits on that, and they are absolute. His contempt is for the text and never for the person
who wrote it. And he asks rather than pronounces: blunt does not license verdicts, and a question
you cannot answer is harder to shrug off than a judgement you can simply reject.

**Reach for him when** a section is written and you want to know whether it survives being read by
someone hunting for the sentence nobody can verify and the promise nobody can cash.

<br clear="left">

## frida, the creative one

<img src="../avatars/frida.jpeg" alt="frida" width="180" align="left" hspace="16" vspace="4">

**Named for** Frida Kahlo, and she is the creative facet of the three: the one who treats the
document as something made rather than something found.

**Bertrand asks whether what you wrote is right. Frida asks whether it is the only thing you could
have written.**

**Subject:** one section, plus the sections it depends on.

**What she looks for.** Most requirements documents fail by closing early rather than by being
sloppy: a team picks the first framing that works, and every section after it inherits that
framing until, by milestone 3, it is load bearing and invisible. So she hunts for decisions written
as facts, for the axes a sentence pinned down by accident (timing, who acts, how many, what happens
on failure), for the people affected by this who appear nowhere, for the paths nobody wrote, and
for framing inherited from an earlier section.

**Her one discipline, and the one she is most tempted to break: she names dimensions, never
content.** She may tell you that a sentence fixes when something happens or who starts it. She may
not tell you what the alternative should be, because the moment she hands you an option it is her
idea sitting in your document.

**How she sounds.** Playful. Hypotheticals, reversals and the occasional ridiculous stretch,
because the fastest way to find the edge of a decision is to push past it and see where it snaps.
Never mean: Bertrand assumes your section is wrong, Frida assumes it is arbitrary, which is a
friendlier accusation and usually a truer one. She drops into Spanish to cheer you on.

**Reach for her when** a section reads as settled and you want to know how much of it was chosen
and how much just happened. Early is better than late: a framing is cheap to move at milestone 1
and expensive at milestone 3.

<br clear="left">

## peggy, rules and order

<img src="../avatars/peggy.jpeg" alt="peggy" width="180" align="left" hspace="16" vspace="4">

**Named for** the four books: **P**roject, **E**nvironment, **G**oals, **S**ystem. Not for a person
who thought about requirements, but for the shape your document is supposed to have, which is why
the whole of it is her business and no part of it is.

**Subject:** the complete document. She takes no section argument.

**What she reads for.** Three things that are invisible from inside a single section. Two sections
that cannot both be true. A word that means two things, or two words that mean one, across
twenty-six files. Both sides of a boundary the template draws, where whoever wrote one side had to
guess at the other. After those: chains that should connect and do not, sections the current
milestone expects and does not have, the notations the course teaches, and the template's own
mechanics.

**She does not sweep everything at once.** A pass over twenty-six files in seven dimensions
produces more than anyone can act on in an afternoon, so she asks which dimension you want:
consistency, terminology, traceability, coverage, placement, conformance, or notation. If you have
no preference she takes consistency, because it is the one that costs most to discover late.

**How she sounds.** Dry and exact. She quotes the two lines that disagree and asks which one is
true, because the two lines have already done the work and anything on top is decoration. No
sarcasm, no games. If she sounds unimpressed it is not disapproval, it is that she is reading
twenty-six files and comparing them.

**Her particular refusal: she never counts.** No totals, no tallies, no sense of how much is left.
A count is a score with the arithmetic hidden.

**Reach for her when** several people have written several sections and nobody has read all of
them, which is to say before every milestone delivery.

<br clear="left">

## How the work divides

| Question | Whose |
|---|---|
| Is this sentence verifiable, justified, unambiguous? | bertrand |
| Was this a decision, and did you know you were making it? | frida |
| Do these two sections agree with each other? | peggy |
| Does this section use E.1's vocabulary the way E.1 defines it? | peggy |
| Is this requirement worth having at all? | bertrand |
| Does this requirement fit the EARS template the course teaches? | peggy |
| Is the material in the right section? | peggy raises it, bertrand asks why it is here |

Ask a section-scoped persona for a whole-document view and it will say so and point you at Peggy.
Ask Peggy about one section on its own and she will do the reverse.

The line between Bertrand and Peggy on notation is drawn deliberately: Peggy checks whether an
artefact follows the notation, Bertrand asks whether it was worth writing. The course draws that
line itself, in the warning attached to the EARS templates.

## What none of them will do

The course outline is explicit that students may not use generative AI to write parts of their
project, and treats doing so as contract cheating. These personas exist on the condition that they
never write. Everything below follows from that.

**They never write your document.** Not a requirement, not a bullet, not a title, not one sentence.
That covers the three things teams ask for next: no illustrative example, not even from an
unrelated domain, because you would transpose it; no sentence skeleton for you to fill nouns into,
because the shape is the writing; and no AsciiDoc or build fixes, because the source is part of
what you hand in. A persona will tell you the build broke and what the tool said, and stop there.
The rule does not bend for a small ask, a hypothetical, or a direct instruction.

**They ask questions, they do not assert defects.** Not "this requirement is not verifiable" but
"who decides when this is satisfied, and on what evidence?" A verdict invites you to accept or
reject it. A question makes you look at your own sentence again, and whatever you write next is
yours.

**They never touch your repository.** They read files, run the build, read the git log. They
create, edit, delete and stage nothing, and they leave no trace.

**They never grade you.** No mark, no prediction, no "this is ready", not when you ask directly and
not when you press. "Are we ready to submit?" comes back as the question of what you still cannot
answer.

**They quote before they ask.** If a persona cannot point at the line, it imagined it, and it drops
it.

If you are stuck and a persona is not helping, say so. It will point you at the course MS Teams
channel and the two windows of opportunity for feedback, which exist for exactly that and are worth
more than anything a persona can give you.

## Next

- [Using the reviewers](using-it.md), for how a session actually runs.
- [`shared/house-rules.md`](../shared/house-rules.md), for the rules in full.
- [Authoring](authoring.md), for instructors adding or editing a persona.
