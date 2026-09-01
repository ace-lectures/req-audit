# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Nothing released yet. The repository currently holds the scaffolding for a catalogue of reviewer
personas that question a student team about a requirements document written with
`cas-handbook-req-template`; the personas' instructions and criteria are stubs.

### Added

- Repository structure for a catalogue of reviewer-persona [Agent Skills](https://agentskills.io):
  `skills/<persona>/` self-contained and individually installable, `shared/` as the single source
  of truth for material every persona must agree on, and `scripts/sync.py` materialising one into
  the other so a single-persona install stays whole.
- Three persona slots in two scopes. **bertrand** (the critic) and **frida** (the creative one)
  are *section-scoped*: each works on one section, named when the persona is invoked, plus the
  sections it depends on. **peggy** (rules and order) is *document-scoped*: she sweeps the
  complete document for consistency and takes no section argument. A persona declares its scope in
  `metadata.req-audit-scope`, and the scope decides how its reference material is filed:
  `references/criteria/` with an entry per section, or `references/checks/` with one file per
  dimension.
- The section inventory and milestone split of the upstream template, transcribed and checkable
  against it with `make check-template`, plus a slot for the section dependency map that the
  section-scoped personas work from.
- Installation on Claude Code, Codex, Cursor, Gemini CLI and GitHub Copilot, via `gh skill
  install`, via the Claude Code plugin marketplace (`/plugin marketplace add
  ace-lectures/req-audit`), or by symlink, with per-agent instructions. One skill folder works
  everywhere without modification.
- `make check` (in CI): validates skill frontmatter against the Agent Skills spec's `name` and
  `description` constraints, the declared scope and the reference layout it implies, per-section
  criteria coverage, freshness of the synced copies, the section inventory, the plugin manifests,
  and that no agent product name appears inside a skill body.

[Unreleased]: https://github.com/ace-lectures/req-audit/compare/main...HEAD
