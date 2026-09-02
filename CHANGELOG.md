# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Nothing released yet. The repository holds Devil's Advocates, a catalogue of three reviewer
personas that question a student team about a requirements document written with
`cas-handbook-req-template`, and never write any part of it. Everything installable stays named
`req-audit`.

### Added

- Repository structure for a catalogue of reviewer-persona [Agent Skills](https://agentskills.io):
  `skills/<persona>/` self-contained and individually installable, `shared/` as the single source
  of truth for material every persona must agree on, and `scripts/sync.py` materialising one into
  the other so a single-persona install stays whole.
- Three personas in two scopes. **bertrand** (the critic) and **frida** (the creative one)
  are *section-scoped*: each works on one section, named when the persona is invoked, plus the
  sections it depends on. **peggy** (rules and order) is *document-scoped*: she sweeps the
  complete document for consistency and takes no section argument. A persona declares its scope in
  `metadata.req-audit-scope`, and the scope decides how its reference material is filed:
  `references/criteria/` with an entry per section, or `references/checks/` with one file per
  dimension.
- The section inventory, milestone split and section dependency map of the upstream template,
  transcribed in `shared/` and checkable against it with `make check-template`. The dependency map
  is what a section-scoped persona reads to know which other sections give a section its context.
- Each persona's voice, boundaries and review material: what it looks at, in what order, and how
  it sounds. Section-scoped criteria for all 26 sections of the template, per persona, and
  whole-document checks in seven dimensions. All of it built on `shared/house-rules.md`, whose
  first rule is that a persona never writes the document, restated inline in every persona so it
  holds even if nothing else loads.
- Installation in two routes, both in `README.md`: `gh skill install` for any of Claude Code,
  Codex, Cursor, Gemini CLI and GitHub Copilot, or the Claude Code plugin marketplace
  (`/plugin marketplace add ace-lectures/req-audit`). One skill folder works everywhere without
  modification.
- Documentation for the two audiences: `docs/personas.md` on who the three reviewers are and why
  there are three, `docs/using-it.md` on running a session, and `docs/authoring.md` for
  instructors adding or editing a persona.
- `make check` (in CI): validates skill frontmatter against the Agent Skills spec's `name` and
  `description` constraints, the declared scope and the reference layout it implies, per-section
  criteria coverage, freshness of the synced copies, the section inventory, the plugin manifests,
  and that no agent product name appears inside a skill body.

[Unreleased]: https://github.com/ace-lectures/req-audit/compare/main...HEAD
