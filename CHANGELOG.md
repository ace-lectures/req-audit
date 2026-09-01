# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Two reviewer personas for a requirements document written with `cas-handbook-req-template`:
  **bertrand**, who challenges precision, justification and section boundaries, and **peggy**, who
  challenges the framing and surfaces the alternatives a team closed on too early. Both work
  through the AsciiDoc sources one section at a time, in conversation, and produce no report.
- A binding rule, shared by every persona, that they never write, draft or reword any part of the
  student's document — only ask questions and criticise. Asked directly, they refuse and return a
  question.
- Installation on Claude Code, Codex, Cursor, Gemini CLI and GitHub Copilot, via `gh skill
  install`, via the Claude Code plugin marketplace (`/plugin marketplace add
  ace-lectures/req-audit`), or by symlink. The personas are Agent Skills; the same folder works
  everywhere without modification.
- Per-agent installation instructions, student usage notes, and instructor notes on adding a
  persona or updating for a new term.

Review criteria are scaffolded per section and per persona but not yet written; the personas will
get sharper as those are filled in.

[Unreleased]: https://github.com/ace-lectures/req-audit/compare/main...HEAD
