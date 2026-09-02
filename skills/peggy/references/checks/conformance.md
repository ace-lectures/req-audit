# Conformance: peggy

**What I compare.** The document against the template's own mechanics. This is housekeeping rather
than requirements review, and I keep it short because none of it is interesting when it is right.

Notation, which is a much larger body of rules, is in `notation.md`.

## Mechanics

- **Anchors.** Every section file opens with its anchor and reftext, as `[#g3,reftext=G.3]`. A
  renamed or missing anchor breaks every cross-reference pointing at it.
- **Cross-references.** Every `<<x>>` resolves to an anchor that exists.
- **`{emptysec}`.** Present means unwritten. A section with content that still carries the marker,
  or an empty section that has lost it, misleads every reader including me.
- **`metadata.adoc`.** Authors, project title, course number, term, revision, milestone. The
  milestone attribute goes stale, which is why I confirm it rather than trust it.
- **Draft mode.** `:env-draft:` shows the template's guidance in the built document. The README
  says to comment it out for the final delivery, so it is worth a question at milestone 3. It only
  affects the built PDF: the `ifdef::env-draft[]` blocks stay in the source either way, so their
  presence in a file says nothing about whether the team did this.
- **Control tables.** The per-section grid in each book's `control.adoc`, and the per-delivery grid
  in `parts/control.adoc`. These are the team's own record of who wrote and who reviewed each
  section.
- **`integrity.adoc` and author blocks.** One per author, matching the authors in `metadata.adoc`.
- **The build.** I may run it. A document that does not compile is worth knowing about, and I can
  say what the tool said without saying how to fix it.

## Questions

- This cross-reference points at an anchor I cannot find. Which section did you mean?
- This section has content and still carries `{emptysec}`. Which is true?
- Who is recorded as reviewer against the sections in the Goals book control table? Is that table
  how you have been working?
- You are at milestone 3 and draft mode is still on in `metadata.adoc`. Deliberate?
- `metadata.adoc` names four authors and `integrity.adoc` has blocks for three. Which is right?
