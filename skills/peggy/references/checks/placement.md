# Placement: peggy

**What I compare.** Both sides of a boundary the template draws. This is the check the other two
personas cannot run: someone working inside one section sees one side of a line and has to guess
at the other. I read both files.

**How the mismatch shows.** Material sitting on the wrong side, or the same material sitting on
both.

## The boundaries

The pairs and the line between them are in `document-map.md`, under "Section boundaries". I do not
restate them here. The ones that go wrong most often are the three about direction, E.2 against
S.3, E.3 and E.4 against E.5, and E.5 against E.6, because direction is invisible from inside
either section.

## What I look for that a section-scoped reader cannot

- **The same content in both.** A constraint written in E.3 and again in P.2, worded differently.
  Neither section looks wrong on its own.
- **The gap between them.** Material that belongs to one side of a pair, sitting in neither.
- **A reference pointing the wrong way up the books.** The dependency order runs Environment,
  Goals, System, Project. A section reaching upward, from Project into System or from System into
  Goals, is usually holding something that belongs elsewhere.

## Questions

- This is in E.3 and something very like it is in P.2. Same restriction, or two?
- The template puts interfaces the system offers in S.3 and interfaces offered to it in E.2. This
  one is in E.2. Which direction does it run?
- G.6 and P.6 both mention this. Is it a limit on the system or a risk to the project?
- Neither S.3 nor E.2 mentions this and both could have. Where did you decide it goes?
