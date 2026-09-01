# req-audit

Reviewer personas that help a student team interrogate their own requirements document.

The document is written with
[`cas-handbook-req-template`](https://github.com/ace-lectures/cas-handbook-req-template), the
AsciiDoc implementation of the four books from Bertrand Meyer's *Handbook of Requirements and
Business Analysis* used in **CS/SE 3RA3** at McMaster University.

Each persona is an [Agent Skill](https://agentskills.io), so the same folder works on Claude Code,
Codex, Cursor, Gemini CLI and GitHub Copilot without modification.

> **Scaffolding.** The repository structure, tooling and install routes are in place and verified.
> The personas' instructions and their review criteria are stubs. See the `_TODO_` markers in
> `shared/` and `skills/*/references/criteria/`.

## The personas

| Persona | Role | Works on |
|---|---|---|
| **bertrand** | The critic. _TODO_ | One section, plus the sections it depends on |
| **frida** | The creative one. _TODO_ | One section, plus the sections it depends on |
| **peggy** | Rules and order. _TODO_ | The complete document: consistency across sections |

**Bertrand** and **frida** take a section as their subject: give them a section id (`S.4`, `G.3`)
when you invoke them, or they will ask for one. **Peggy** takes no section. She reads the whole
document, because the things she looks for only show up between sections.

All three read the `.adoc` sources in your repository. None of them writes any part of the
document, and none produces a report or a score: the output of a session is conversation.

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
gh skill install ace-lectures/req-audit frida    --agent <your-agent> --scope user
gh skill install ace-lectures/req-audit peggy    --agent <your-agent> --scope user
```

On Claude Code you can instead install all three at once as a plugin:

```
/plugin marketplace add ace-lectures/req-audit
/plugin install req-audit@ace-lectures
```

## Use

Open your **document repository**, the one containing `index.adoc`, `metadata.adoc` and
`parts/`, and ask for a persona by name, with a section id for the section-scoped ones. See
[docs/using-it.md](docs/using-it.md).

## Repository layout

| Path | What it is |
|---|---|
| `skills/<persona>/` | One Agent Skill per persona. Self-contained and individually installable. |
| `shared/` | Single source of truth for material every persona must agree on: the house rules, the section inventory and dependencies, the milestone split. |
| `scripts/` | `sync.py` materialises `shared/` into each skill; `validate.py` backs `make check`. |
| `docs/` | Per-agent install instructions, student usage notes, and authoring notes. |
| `.claude-plugin/` | Marketplace and plugin manifests, so the repository installs as one plugin. |

Instructors adding a persona or filling in the stubs: see [docs/authoring.md](docs/authoring.md).

```
make sync    # regenerate the shared material inside each skill
make check   # validate the catalogue
```

## License

MIT. See [LICENSE](LICENSE).
