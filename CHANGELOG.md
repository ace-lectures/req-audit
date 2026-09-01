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
- Two persona slots, **bertrand** and **peggy**, with a shared body skeleton and criteria
  scaffolded per section (26 sections × 2 personas, all `_TODO_`).
- The section inventory and milestone split of the upstream template, transcribed and checkable
  against it with `make check-template`.
- Installation on Claude Code, Codex, Cursor, Gemini CLI and GitHub Copilot — via `gh skill
  install`, via the Claude Code plugin marketplace (`/plugin marketplace add
  ace-lectures/req-audit`), or by symlink — with per-agent instructions. One skill folder works
  everywhere without modification.
- `make check` (in CI): validates skill frontmatter, per-section criteria coverage, freshness of
  the synced copies, the section inventory, the plugin manifests, and that no agent product name
  appears inside a skill body.

[Unreleased]: https://github.com/ace-lectures/req-audit/compare/main...HEAD
