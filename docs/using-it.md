# Using the reviewers

For student teams. Who the three are and why they differ is in [the personas](personas.md); this
page is about running a session.

## Before you start

Open your **document repository**, the one with `index.adoc`, `metadata.adoc` and `parts/` in it,
in your agent. The personas read the AsciiDoc sources directly: there is nothing to upload, paste,
or build first, and no need to have the PDF working.

Two things are worth doing first, because a persona will ask about both.

- **Know which milestone you are on.** They read `:milestone:` from `metadata.adoc` and then
  confirm it with you, because that attribute goes stale. It decides which empty sections are
  legitimately empty.
- **Have the section written.** A body still holding `{emptysec}` is unwritten, and a persona will
  say so in one line and ask what you intend to put there rather than interrogating a section into
  existence. Write something first, however rough. Rough is exactly what they are for.

## Picking a persona

| Persona | Ask when you want | Subject |
|---|---|---|
| **bertrand** | To know whether a section survives a hostile reading: verifiable, unambiguous, justified, not a design decision in disguise | One section, plus the sections it depends on |
| **frida** | To know how much of a section you chose and how much you inherited, before the framing sets | One section, plus the sections it depends on |
| **peggy** | To know whether twenty-six files written by several people are one document | The complete document |

They are complementary rather than sequential, but there is an order that wastes less of your time.

**Frida before Bertrand, on a section that is new.** She asks whether you are writing the right
thing, he asks whether you are writing it well. Polishing a framing you are about to abandon is
work you did twice.

**Bertrand before a delivery, on a section that is settled.** By then the framing is not moving and
the question is whether the sentences hold.

**Peggy before every delivery, whatever else you did.** Her findings are the ones that no amount of
section-level care prevents, because they only exist between sections. She is also the one whose
answers cost the most when they arrive late: a word that means two things across twenty-six files
is a cheap fix in October and a rewrite in December.

**When two of them push in different directions**, that is not a malfunction. Frida opening up an
option and Bertrand demanding you justify one is the same argument seen from two sides, and the
answer is usually to write down why you chose. None of them is the last word. Your instructor is,
and a persona will tell you so if you press.

## Section-scoped: bertrand and frida

Both take **a single section as their subject, plus the sections it depends on**. They will not
wander into the rest of the document. That is Peggy's job.

Name the section when you invoke them:

```
/bertrand S.4
/frida G.3
```

Some agents pass that argument straight through to the skill; others do not. Either way works: if
the persona did not receive a section id, it asks for one. You can equally just say "frida, take
G.3". Neither of them will pick a section for you.

**What a session looks like.** The persona reads `metadata.adoc`, the section file, and the
sections that section depends on. Those dependencies are context and nothing else: a dependency
that is still empty is never held against you. It ignores the `ifdef::env-draft[]` guidance blocks,
because those are the template's words and not yours. At milestones 2 and 3 it also looks at the
git log for the file, because a section untouched since it was due either was right the first time
or stopped being thought about.

Then it puts the questions that bite on the table, ordered by how much damage the answer would do,
and stops. Not the whole criteria file walked end to end, and not one question at a time. It is
your document, and the next turn is yours.

Every question quotes the line it is about. If a persona cannot point at the text, it does not
raise it.

**The most valuable outcome is the one that feels like a win:** you answer a question well, and the
answer is not in the document. That happens constantly. You know why the scope is drawn there, why
that stakeholder is out, why the benefit is worth having. The document does not say it, and the
next person to read it cannot tell your reasoning from an accident. The persona's next question
will be why.

## Document-scoped: peggy

Peggy takes no section:

```
/peggy
```

She reads the whole document, because what she looks for only shows up between sections. Asked to
look at one section on its own, she will say that is Bertrand's or Frida's work.

**She will ask you what to sweep for**, and you pick one:

| Dimension | What it finds |
|---|---|
| Consistency | Two sections that cannot both be true |
| Terminology | E.1 against the words you actually use |
| Traceability | Chains that should connect: a goal, the behaviour serving it, the check catching it |
| Coverage | What this milestone expects, and what is delimited as out of scope |
| Placement | Material sitting on the wrong side of a boundary the template draws |
| Conformance | The template's own mechanics: anchors, cross-references, control tables, draft mode |
| Notation | EARS, the domain model, UML, user stories, Gherkin, MoSCoW |

One dimension per pass, deliberately. Seven dimensions over twenty-six files at once would be a
report, and nobody acts on a report. If you have no preference she takes consistency.

**How often.** Once before each milestone delivery, at minimum, and worth it again whenever two
people have been editing in parallel for a week. Consistency and terminology are the two to run
first; notation is the one to run once the requirements themselves have stopped moving.

Her method is two quotations and one question: this line from one file, that line from another,
which of them did you mean. The most common answer, and a perfectly respectable one, is that nobody
knew the other section said that.

## What none of them will do

**They do not write your document.** Ask for a well-formed example, a sentence skeleton, a
rewording, or a fix for the AsciiDoc that will not build, and you get one flat sentence of refusal
and a question back. This is not the tool being coy. The course outline forbids using generative AI
to write parts of your project and treats it as contract cheating, and page one of your own
document is the integrity affirmation where you sign that the content is entirely your own. The
personas exist because they cannot put anything in your document: questions are not content, and a
question you answered in your own words is your own work.

They will also not tell you that something is wrong, only ask the question whose answer shows you;
will not edit, create or stage a single file in your repository; will not count anything; and will
not tell you whether you are ready to submit, however you ask.

If the build is broken, a persona will tell you that it broke and what the tool said, and stop
there. The source is part of what you hand in.

## Getting more out of it

**Bring a section you are unsure about, not the one you are proudest of.** The proud one produces a
short session.

**Answer out loud before you edit.** The gap between what you can say about a requirement and what
the document says is the finding. You cannot see that gap by rereading the document, only by trying
to answer a question about it.

**Take the answers back to the document yourself, after the session.** Not during. Writing while
being questioned is how a persona's phrasing ends up in your text, which is exactly what the rules
exist to prevent, and it is also worse writing.

**Push back when you have a reason.** A reason ends the thread: the persona notes that it exists
and moves on. It is not trying to win. If you find yourself unable to state the reason, that is
information too.

**Do not try to finish.** There is no bottom to these questions and no completion state. A useful
session is one where you learned three things your document does not say. Stop there and go write
them down.

**If you are stuck and the persona is not helping, say so.** It will point you at the course MS
Teams channel and the two windows of opportunity for feedback. Those exist for this, and they are
worth more than anything a persona can give you.
