# Using the reviewers

> **Scaffolding.** Structure only; the guidance below is the instructor's to write.

## Before you start

Open your **document repository** — the one with `index.adoc`, `metadata.adoc` and `parts/` in it
— in your agent. The personas read the AsciiDoc sources directly; there is nothing to upload,
paste, or build first.

## Picking a persona

| Persona | Ask when you want | Works on |
|---|---|---|
| **bertrand** | _TODO_ | One section, plus the sections it depends on |
| **frida** | _TODO_ | One section, plus the sections it depends on |
| **peggy** | _TODO_ | The complete document |

_TODO: when to reach for which, whether they are complementary or sequential, and what to do when
two of them disagree._

## Section-scoped: bertrand and frida

Both work on **one section at a time, plus the sections that section depends on**. They will not
wander into the rest of the document — that is peggy's job.

Name the section when you invoke them:

```
/bertrand S.4
/frida G.3
```

Some agents pass that argument straight through to the skill; others do not. Either way works — if
the persona did not receive a section id, it asks for one. You can equally just say "frida, take
G.3".

_TODO: what a section session looks like, once the persona instructions are written._

## Document-scoped: peggy

Peggy takes no section. She reads the whole document, because what she looks for — consistency,
and conformance to the template's rules — only shows up between sections. Invoke her plainly:

```
/peggy
```

_TODO: what a whole-document pass looks like, and how often it is worth running one._

## What none of them will do

**They do not write your document.**

_TODO: the rationale to give students — see `shared/house-rules.md`, which is also a stub._

## Getting more out of it

_TODO: how to prepare for a session and how to use it well._
