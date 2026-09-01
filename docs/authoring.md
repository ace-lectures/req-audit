# Authoring — for instructors

## How the repository fits together

```
shared/            single source of truth for anything every persona must agree on
skills/<persona>/  one Agent Skill per persona — self-contained and individually installable
scripts/           sync.py (shared/ -> skills), validate.py (make check)
docs/              per-agent install instructions, student-facing usage notes
.claude-plugin/    marketplace + plugin manifests, so the repo installs as one plugin
```

`skills/<persona>/references/{house-rules,document-map,milestones}.md` are **generated copies** of
`shared/`. They carry a `<!-- GENERATED ... -->` banner. Never edit them: edit `shared/`, run
`make sync`, and commit both.

They are copies rather than references because `gh skill install <repo> <persona>` copies only
that one skill folder. A `../../shared/` path would break the moment a student installs a single
persona.

## Editing criteria

Criteria live in `skills/<persona>/references/criteria/`:

- `cross-cutting.md` — properties that apply to any section.
- `goals.md`, `environment.md`, `system.md`, `project.md` — one `##` entry per section, in
  document order, each carrying its file path and milestone.

These are **per-persona and hand-written**: each persona looks at the same section for different
things, so they do not share criteria. `make check` verifies that every persona has an entry for
all 26 sections; it does not check that the entries say anything, so `_TODO_` passes.

## Adding a persona

1. `cp -r skills/bertrand skills/<name>` and delete `references/criteria/*` content you are not
   keeping.
2. Edit `SKILL.md`: the `name` in frontmatter **must** equal the directory name. Write a
   `description` that says what this persona looks for and when a team should reach for it — it is
   what the agent matches against, and it is what students see in a list.
3. Keep the section skeleton (`Who I am` / `What I will not do` / `How I start` / `How I work
   through a section` / `Where my criteria live`). It is what keeps the personas recognisably one
   family.
4. Restate the house rules inline in `What I will not do`. They must hold even if `references/`
   is never loaded.
5. `make sync && make check`.
6. Add a row to the persona table in `README.md` and `docs/using-it.md`.

Nothing else needs touching — the plugin manifest points at the repo root, so a new folder under
`skills/` is picked up automatically.

## The rules that are not per-persona

`shared/house-rules.md` binds every persona and is synced into all of them. Two of its rules are
fixed by design — the personas never write the document, and their output is questions and
critique only. The rest of the file is a set of stubs to fill in.

Each persona also restates the non-negotiables inline in its `SKILL.md`, deliberately, so they
hold even if `references/` is never loaded. Keep the two in step when you edit either.

## Validation

```
make check                                        # everything CI checks
make check-template TEMPLATE=../cas-handbook-req-template   # also cross-check the inventory
```

`make check` fails on: missing or mismatched frontmatter; a persona missing a criteria entry for
any section; generated copies out of date; an inventory that has drifted from the
`parts/<book>/<ID>.adoc` convention; a broken plugin manifest; and **any agent product name
appearing inside `skills/` or `shared/`**.

That last check is what keeps the personas portable. Agent-specific instructions belong in
`docs/install/`, never in a skill body. The one deliberate exception is the
`disable-model-invocation: true` frontmatter key, which one agent honours and the others ignore —
it makes students choose a persona explicitly rather than having one activate on its own.

## Updating for a new term

The section inventory and milestone split in `shared/` mirror
[`cas-handbook-req-template`](https://github.com/ace-lectures/cas-handbook-req-template). When
that template changes, update `shared/document-map.md` and `shared/milestones.md`, then run
`make check-template` against a local checkout to confirm they agree.

Tag a release per term so students can pin one:
`gh skill install ace-lectures/req-audit bertrand@v1.0.0 --agent codex`.
