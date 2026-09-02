# Devil's Advocates

Three reviewer personas that help a student team interrogate their own requirements document.
*They ask. You write.*

By [Sébastien Mosser](https://github.com/ace-lectures), Department of Computing and Software,
McMaster University, for **CS/SE 3RA3**. The document under
review is written with
[`cas-handbook-req-template`](https://github.com/ace-lectures/cas-handbook-req-template), the
AsciiDoc implementation of the four books from Bertrand Meyer's *Handbook of Requirements and
Business Analysis*.

Each persona is an [Agent Skill](https://agentskills.io), so the same folder works on every major
coding agent without modification. Everything you install and type is named `req-audit`,
for requirements audit; Devil's Advocates is what the three of them are: auditors.

## They review. They do not write.

The course outline forbids using generative AI to write any part of the project, and treats doing
so as contract cheating. These personas are built so that using them cannot break that rule.

A persona reads your `.adoc` sources and asks you questions about them. It never writes a
requirement, a bullet, a title or a sentence; it gives no illustrative examples to transpose and no
sentence skeletons to fill in; it does not fix your AsciiDoc; it never edits anything in your
repository; and it never tells you whether you are ready to submit. It does not even assert that
something is wrong: it asks the question whose answer would show you. What comes out of a session
is conversation, and whatever you write afterwards is yours.

The rules in full are in [`shared/house-rules.md`](shared/house-rules.md).

## A warning about the thing doing the reviewing

**A generative model does not understand your document.** It is not reading your requirements the
way a person does and then reasoning about them. It is producing the most plausible next thing,
given its training and a pile of constraints that neither you nor I control or can fully inspect. A
persona can therefore ask a piercing question about a sentence that was perfectly fine, walk past
the one that is actually broken, and sound equally certain both times. Plausible is not the same as
correct, and confident is not the same as right.

That is exactly why this is a tool and not an oracle. Everything the course teaches you, what makes
a requirement verifiable, what a domain model is for, what belongs in Goals rather than in System,
is what lets you tell a question worth acting on from one that is noise. Those skills are the
prerequisite for using an agent well, not something an agent saves you from needing. Use the AI;
do not let it do your job.

**You are responsible for every word you hand in.** A question a persona asked you is not a
justification for anything: what goes in the document is your decision, made with your reasoning,
and it is what you are graded on. "The AI told me to write this" is not a conversation we will have
about your grade.

## The three reviewers

| | Persona | What they ask | Why they exist | Subject |
|---|---|---|---|---|
| <img src="avatars/bertrand.jpeg" alt="" width="80"> | **bertrand** | Is this right? | Named for the textbook's author, and holds a section to the Handbook's quality properties: verifiable, unambiguous, justified, abstract. Blunt, hard on the text and never on the author. | One section, plus what it depends on |
| <img src="avatars/frida.jpeg" alt="" width="80"> | **frida** | Is this the only thing you could have written? | Named for Frida Kahlo, and she is the creative facet. Documents fail by closing early more often than by being sloppy, so she finds the decisions written as facts, and names the axis without ever naming the alternative. | One section, plus what it depends on |
| <img src="avatars/peggy.jpeg" alt="" width="80"> | **peggy** | Is this one document? | Named for the four books, Project, Environment, Goals, System. Contradictions, vocabulary drift and both sides of a boundary are invisible from inside one section, so someone has to read all twenty-six. | The complete document |

Two section reviewers who disagree with each other about what a section is, and one who reads
across the whole. [Who they are, in full](docs/personas.md).

**They are clichés, and that is deliberate.** The withering old professor, the exuberant artist,
the archivist who has read every file and remembers all of them: each one is drawn broadly, with
its tics turned up, and none of them is a portrait of a real colleague. The joke is doing work. A
character whose temperament you can predict is easier to argue with than a rubric and easier to
remember than a checklist, and being teased by a caricature is easier to take than being marked
down by a form. The humour is light and the questions underneath it are not.

## Install

Pick one of the two routes. Both install all three personas.

### GitHub CLI, any agent

Requires `gh` v2.90.0 or later. Replace `<your-agent>` with `claude-code`, `codex`, `cursor`,
`gemini-cli` or `github-copilot`:

```
gh skill install ace-lectures/req-audit bertrand --agent <your-agent> --scope user
gh skill install ace-lectures/req-audit frida    --agent <your-agent> --scope user
gh skill install ace-lectures/req-audit peggy    --agent <your-agent> --scope user
```

`--scope user` makes the personas available in every project. Use `--scope project` from inside
your document repository instead, and your teammates get them by cloning.

### Claude Code plugin marketplace

From any directory:

```
/plugin marketplace add ace-lectures/req-audit
/plugin install req-audit@ace-lectures
```

The personas are then `/req-audit:bertrand`, `/req-audit:frida` and `/req-audit:peggy`. Update
later with `/plugin marketplace update ace-lectures`.

### Check it worked

List your agent's skills. All three should appear, and none of them activates on its own: you
always choose the persona.

## Use them

Open your **document repository**, the one holding `index.adoc`, `metadata.adoc` and `parts/`.
There is nothing to upload, paste or build first.

```
/bertrand S.4      one section, torn into
/frida G.3         one section, opened up
/peggy             the whole document, one dimension at a time
```

Section id for the section-scoped two; if your agent does not pass the argument through, they ask
for one. Then answer their questions in your own words, in your own document.

[Using the reviewers](docs/using-it.md) covers what a session looks like, when to reach for which
persona, and how to get more out of it.

## Repository layout

| Path | What it is |
|---|---|
| `skills/<persona>/` | One Agent Skill per persona. Self-contained and individually installable. |
| `shared/` | Single source of truth for material every persona must agree on: the house rules, the section inventory and dependencies, the milestone split. |
| `scripts/` | `sync.py` materialises `shared/` into each skill; `validate.py` backs `make check`. |
| `docs/` | Persona descriptions, student usage notes, authoring notes. |
| `avatars/` | Persona portraits, used in the documentation only. |
| `.claude-plugin/` | Marketplace and plugin manifests, so the repository installs as one plugin. |

Instructors adding a persona or editing the criteria: see [docs/authoring.md](docs/authoring.md).

```
make sync    # regenerate the shared material inside each skill
make check   # validate the catalogue
```

## License

MIT. See [LICENSE](LICENSE).
