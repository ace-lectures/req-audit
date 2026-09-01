# (S) System: bertrand criteria

One entry per section: what it owes, where it goes wrong, and what I ask. These sharpen the
cross-cutting properties in `cross-cutting.md`; they do not replace them. "Where it goes wrong" is
my note to myself, not a line I deliver: I ask, I do not pronounce.

Boundaries with other sections are in `document-map.md`. I name the risk here and ask the question;
I do not recite the table.

## (S.1) Components

`parts/system/S1.adoc` · milestone 2

**Owes.** The major parts of the system itself, software and where relevant hardware. The structure the rest of the System book is organised around.

**Where it goes wrong.** External systems get listed as though the team were building them. Or the decomposition is one the team never justified, and S.2 then has nowhere sensible to hang behaviour.

- Is each of these part of what you are building, or part of the world you are building into?
- Why this decomposition and not another? What would a different split have cost you?
- Does every component here get behaviour in S.2? Which ones do not?

## (S.2) Functionality

`parts/system/S2.adoc` · milestone 2

**Owes.** What the system does. The bulk of the System book, organised one subsection per component from S.1, covering functional and non-functional properties.

**Where it goes wrong.** It is not organised around S.1 at all. Non-functional properties are absent or unquantified. Or it reads as business narrative rather than behaviour anyone could build from.

- Which S.1 component does this behaviour belong to? If none, where did that component go?
- Where are the non-functional properties, and with what numbers attached?
- For any behaviour here: what goes in, what comes out, and who could check it?
- Could a developer build this without asking you a single question? Which sentence would they ask about first?

## (S.3) Interfaces

`parts/system/S3.adoc` · milestone 2

**Owes.** How the functionality in S.2 is made available outward, to people and to other systems.

**Where it goes wrong.** Interfaces the system consumes get described here rather than in E.2. Or interfaces appear that expose nothing specified in S.2, or S.2 behaviours have no way to be reached at all.

- Does this interface expose something specified in S.2, or something you have not written down yet?
- Is this an interface you provide, or one you consume?
- Which behaviours in S.2 have no way of being triggered from outside?

## (S.4) Detailed usage scenarios

`parts/system/S4.adoc` · milestone 2

**Owes.** Concrete interactions that may name components and functionality, covering special and erroneous cases. The basis for test cases.

**Where it goes wrong.** It is G.5 again with longer sentences. Or every scenario is a happy path, which is the half that never causes trouble.

- Which of these is not already in G.5? If they all are, what has this section added?
- Where are the failures: the abandoned interaction, the wrong input, the component that is down?
- Could somebody write a test from this without asking you what you meant?

## (S.5) Prioritization

`parts/system/S5.adoc` · milestone 3

**Owes.** The behaviours, interfaces and scenarios of S.2, S.3 and S.4 classified by criticality, so something can be dropped when the project runs short.

**Where it goes wrong.** Everything is high priority. Or criticality gets confused with the order the work will be done in, which is P.3 and P.4.

- What fraction of these are top priority? If it is most of them, what has the ranking decided?
- The term runs short. Which one goes first, and which goes next?
- Is this ranking criticality, or the order you plan to build things in?
- Which items in S.2, S.3 and S.4 have no priority here at all?

## (S.6) Verification and acceptance criteria

`parts/system/S6.adoc` · milestone 2

**Owes.** The conditions under which an implementation is deemed satisfactory, and the verification strategy that gets you there. Revised at milestone 3 with tests and a traceability matrix.

**Where it goes wrong.** Generic testing vocabulary with nothing project-specific in it. Or criteria nobody could measure, which puts the whole document's verifiability in question.

- Who signs this off, and on what evidence?
- Take the most important behaviour in S.2. Which criterion here would catch it being wrong?
- Is there a criterion here that two people could read and disagree about? What would settle it?
- From milestone 3: the revision asks for five tests on one S.4 scenario plus a traceability matrix. Does each test trace to something actually written, or was the matrix filled in afterwards?

