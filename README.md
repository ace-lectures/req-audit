# req-audit

Reviewer personas that help a student team interrogate their own requirements document — and never
write it for them.

The document in question is written with
[`cas-handbook-req-template`](https://github.com/ace-lectures/cas-handbook-req-template), the
AsciiDoc implementation of the four books from Bertrand Meyer's *Handbook of Requirements and
Business Analysis* used in **CS/SE 3RA3** at McMaster University.

Each persona is an [Agent Skill](https://agentskills.io), so the same folder works on Claude Code,
Codex, Cursor, Gemini CLI and GitHub Copilot without modification.

## The personas

| Persona | Reach for it when you want |
|---|---|
| **bertrand** | To be argued with. Is this sentence precise? Could anyone verify it? Why is this here? Does it belong in this section? |
| **peggy** | To be widened. What else could this have been? Who did we not think about? What are we assuming without saying so? |

Both read the `.adoc` sources in your repository, work through one section at a time, and stop to
wait for you. Neither produces a report, a score, or a verdict.

## Neither of them writes your document

Not a section, not a paragraph, not one sentence, not an example, not a fill-in-the-blank
template. Ask directly and you get a one-line refusal and a question back.

Every author signs an academic-integrity affirmation inside the document itself. These reviewers
are built so that using them cannot put you on the wrong side of it. The rules are in
[`shared/house-rules.md`](shared/house-rules.md) and are binding on every persona in this
repository.

## Install

Pick your agent:

- [Claude Code](docs/install/claude-code.md)
- [Codex](docs/install/codex.md)
- [Cursor](docs/install/cursor.md)
- [Gemini CLI](docs/install/gemini-cli.md)
- [GitHub Copilot / VS Code](docs/install/copilot.md)

The short version, for any of them, with `gh` v2.90.0 or later:

```
gh skill install ace-lectures/req-audit bertrand --agent <your-agent> --scope user
gh skill install ace-lectures/req-audit peggy    --agent <your-agent> --scope user
```

On Claude Code you can instead install both at once as a plugin:

```
/plugin marketplace add ace-lectures/req-audit
/plugin install req-audit@ace-lectures
```

## Use

Open your **document repository** — the one containing `index.adoc`, `metadata.adoc` and `parts/`
— and ask for a persona by name. See [docs/using-it.md](docs/using-it.md) for what a session looks
like and how to get value out of one.

## Repository layout

| Path | What it is |
|---|---|
| `skills/<persona>/` | One Agent Skill per persona. Self-contained and individually installable. |
| `shared/` | Single source of truth for material every persona must agree on: the house rules, the section inventory, the milestone split. |
| `scripts/` | `sync.py` materialises `shared/` into each skill; `validate.py` backs `make check`. |
| `docs/` | Per-agent install instructions, student usage notes, and authoring notes. |
| `.claude-plugin/` | Marketplace and plugin manifests, so the repository installs as one plugin. |

Instructors adding a persona or updating for a new term: see
[docs/authoring.md](docs/authoring.md).

```
make sync    # regenerate the shared material inside each skill
make check   # validate the catalogue
```

## License

MIT — see [LICENSE](LICENSE).
