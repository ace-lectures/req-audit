# Authoring, for instructors

## How the repository fits together

```
shared/            single source of truth for anything every persona must agree on
skills/<persona>/  one Agent Skill per persona, self-contained and installable on its own
scripts/           sync.py (shared/ -> skills), validate.py (make check)
docs/              persona descriptions, student-facing usage notes, these notes
.claude-plugin/    marketplace + plugin manifests, so the repo installs as one plugin
```

## Scopes

Every persona declares a scope in its `SKILL.md` frontmatter, and the scope decides how its
reference material is filed:

| Scope | Personas | Subject | Reference material |
|---|---|---|---|
| `section` | bertrand, frida | One section, plus the sections it depends on | `references/criteria/`: `cross-cutting.md` plus one file per book, with an entry for each of the 26 sections |
| `document` | peggy | The complete document | `references/checks/`: one file per check dimension, listed in `_index.md` |

```yaml
metadata:
  req-audit-scope: section    # or: document
```

`metadata` is a standard Agent Skills frontmatter field (an arbitrary string-to-string map), so
declaring the scope there is portable; agents ignore keys they do not know. `make check` reads it
and enforces the matching layout. A section-scoped persona with a `checks/` directory fails, and
so does a document-scoped one with a `criteria/` directory.

### Passing a section to a section-scoped persona

The Agent Skills specification defines **no argument mechanism**; `$1` and `$ARGUMENTS` are
agent-specific extensions. So a section-scoped persona is written to take the section id if the
agent happened to pass one through, and to *ask* otherwise. Never write agent-specific argument
placeholders into a skill body. They would work on one agent and silently do nothing on the rest.

`skills/<persona>/references/{house-rules,document-map,milestones}.md` are **generated copies** of
`shared/`. They carry a `<!-- GENERATED ... -->` banner. Never edit them: edit `shared/`, run
`make sync`, and commit both.

They are copies rather than references because `gh skill install <repo> <persona>` copies only
that one skill folder. A `../../shared/` path would break the moment a student installs a single
persona.

## Editing criteria (section-scoped personas)

Criteria live in `skills/<persona>/references/criteria/`:

- `cross-cutting.md`: properties that apply to any section.
- `goals.md`, `environment.md`, `system.md`, `project.md`: one `##` entry per section, in
  document order, each carrying its file path and milestone.

These are **per-persona and hand-written**: each persona looks at the same section for different
things, so they do not share criteria. `make check` verifies that every section-scoped persona has
an entry for all 26 sections; it does not check that the entries say anything, so `_TODO_` passes.

## Editing checks (document-scoped personas)

Checks live in `skills/<persona>/references/checks/`, one file per dimension, with `_index.md`
saying what each covers. `make check` requires the index to exist and nothing more. The
dimensions are yours to name.

## Adding a persona

1. Decide the scope. Copy the persona that already has it: `cp -r skills/bertrand skills/<name>`
   for a section-scoped one, `cp -r skills/peggy skills/<name>` for a document-scoped one. Clear
   out the reference material you are not keeping.
2. Edit `SKILL.md`. The `name` **must** equal the directory name and be lowercase alphanumerics
   with single hyphens (spec rule, enforced). Set `metadata.req-audit-scope`. Write a
   `description`, at most 1024 characters, that says what this persona looks for and when a team
   should reach for it; it is what the agent matches against, and what students see in a list.
3. Keep the heading skeleton for the scope (`Who I am` / `What I will not do` / `What I work on` /
   `How I start` / `How I work through …` / `Where my criteria|checks live`). It is what keeps the
   personas recognisably one family.
4. Restate the house rules inline in `What I will not do`. They must hold even if `references/`
   is never loaded.
5. `make sync && make check`.
6. Add a row to the persona tables in `README.md`, `docs/personas.md` and `docs/using-it.md`,
   and add the persona to the `gh skill install` block in `README.md`.

Nothing else needs touching. The plugin manifest points at the repo root, so a new folder under
`skills/` is picked up automatically.

## The rules that are not per-persona

`shared/house-rules.md` binds every persona and is synced into all of them. It is written, apart
from rule 10, which is an open slot for rules you add later.

Two of its rules are load-bearing and should not be edited casually. Rule 1, the personas never
write the document, is what makes the tool usable in a course whose outline bans generative AI for
writing the project; rule 0 quotes that outline and says so. Rule 2, questions only, is the same
prohibition read strictly: a persona never asserts that something is missing or wrong, it asks the
question whose answer exposes it. Loosening either changes what the tool is.

Nothing in the house rules is about tone. That is per persona, and belongs in each `SKILL.md`.

Each persona also restates the non-negotiables inline in its `SKILL.md`, deliberately, so they
hold even if `references/` is never loaded. Keep the two in step when you edit either.

## Validation

```
make check                                        # everything CI checks
make check-template TEMPLATE=../cas-handbook-req-template   # also cross-check the inventory
```

`make check` fails on: frontmatter that is missing, mismatched, or breaks the spec's `name` and
`description` constraints; a missing or unknown `req-audit-scope`; reference material filed under
the wrong directory for the scope; a section-scoped persona missing a criteria entry for any
section; a document-scoped persona with no `checks/_index.md`; generated copies out of date; an
inventory that has drifted from the `parts/<book>/<ID>.adoc` convention; a broken plugin manifest;
and **any agent product name appearing inside `skills/` or `shared/`**.

The upstream [`skills-ref`](https://github.com/agentskills/agentskills/tree/main/skills-ref)
library validates a `SKILL.md` against the spec directly, if you want a second opinion:
`skills-ref validate ./skills/bertrand`. It is not wired in, so that nothing here needs installing.

That last check is what keeps the personas portable. Agent-specific instructions belong in the
install section of `README.md`, never in a skill body. The one deliberate exception is the
`disable-model-invocation: true` frontmatter key, which one agent honours and the others ignore.
it makes students choose a persona explicitly rather than having one activate on its own.

## Updating for a new term

The section inventory and milestone split in `shared/` mirror
[`cas-handbook-req-template`](https://github.com/ace-lectures/cas-handbook-req-template). When
that template changes, update `shared/document-map.md` and `shared/milestones.md`, then run
`make check-template` against a local checkout to confirm they agree.

Tag a release per term so students can pin one:
`gh skill install ace-lectures/req-audit bertrand@v1.0.0 --agent codex`.
