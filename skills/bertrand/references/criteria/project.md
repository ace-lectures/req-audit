# (P) Project: bertrand criteria

One entry per section: what it owes, where it goes wrong, and what I ask. These sharpen the
cross-cutting properties in `cross-cutting.md`; they do not replace them. "Where it goes wrong" is
my note to myself, not a line I deliver: I ask, I do not pronounce.

Boundaries with other sections are in `document-map.md`. I name the risk here and ask the question;
I do not recite the table.

## (P.1) Roles and personnel

`parts/project/P1.adoc` · milestone 3

**Owes.** The human responsibilities in the project, the staff needed, and the qualifications those roles require.

**Where it goes wrong.** Team members get listed by name with a title attached, which is a roster rather than a set of roles. Or stakeholders from G.7 wander in.

- Are these roles, or your names with titles attached?
- Who is accountable when a deliverable in P.4 is late?
- Which of these roles does nobody on the team currently have the skills for, and what is the plan?

## (P.2) Imposed technical choices

`parts/project/P2.adoc` · milestone 3

**Owes.** Choices binding the project a priori to particular tools, languages or platforms, and the reasons they bind. The template ties this directly to requirements being justified.

**Where it goes wrong.** Preferences get presented as impositions. Or the choices are listed with no source, which leaves nobody able to renegotiate them later.

- Who imposed this, and can you point at them?
- Would you have chosen it anyway if nobody had imposed it? If yes, is it really imposed?
- Is this binding on how you build, or just something you need in order to build? The second belongs elsewhere.

## (P.3) Schedule and milestones

`parts/project/P3.adoc` · milestone 3

**Owes.** The project's key dates and the scheduling of the tasks that P.4 details.

**Where it goes wrong.** Dates appear with no tasks between them. Or the timeline assumes nothing goes wrong, which is the one thing you can rule out.

- What in P.4 happens between these two dates?
- Which of these dates did you choose, and which were handed to you?
- Which date will you miss first, and how would you know early enough to react?

## (P.4) Tasks and deliverables

`parts/project/P4.adoc` · milestone 3

**Owes.** The individual tasks and what each produces, tied to the milestone dates in P.3. The template calls this the core of the Project book.

**Where it goes wrong.** Tasks have no deliverable, or the deliverable is an activity rather than an artefact. Then nobody can tell when anything is finished.

- For each task: what artefact exists at the end that did not exist at the start?
- Which task produces the thing S.5 ranked most critical?
- How would somebody outside the team tell that this task was done?

## (P.5) Required technology elements

`parts/project/P5.adoc` · milestone 3

**Owes.** External systems, hardware and software the project needs in order to build the system. Identifying them is a requirements task because their availability is a risk.

**Where it goes wrong.** Things the running system talks to get listed here instead of E.2. Or policy mandates that belong in P.2 appear. Or nothing here is reflected in P.6.

- Do you need this to build the system, or does the running system talk to it?
- What happens to your schedule if it is unavailable, or its licence changes?
- Which of these appear in P.6, and which do not?

## (P.6) Risk and mitigation analysis

`parts/project/P6.adoc` · milestone 1

**Owes.** Obstacles to meeting the schedule in P.4, with mitigations. Revised at milestone 3 with security threats.

**Where it goes wrong.** Risks arrive without mitigations, or with mitigations that amount to working harder. Or the risks are generic to any student project. Or scope exclusions belonging in G.6 turn up here.

- For each risk: what is the trigger you would actually notice, and what do you do on the day you notice it?
- Which of these risks is specific to your project rather than true of every project in the course?
- Is this a risk to the project, or a limit on what the system will do?
- From milestone 3: the revision asks for security threats. Who is the attacker, what do they want, and what do they gain if they get it?

## (P.7) Requirements process and report

`parts/project/P7.adoc` · milestone 1

**Owes.** The plan for eliciting requirements, which becomes a report of what was actually done and what was learned.

**Where it goes wrong.** It stays the plan written in week two and is never updated, so it reports nothing. Or it describes how the software will be built rather than how the requirements were gathered.

- Who did you actually talk to, and when?
- What did you believe at the start that turned out to be wrong?
- Is this describing how you gathered requirements, or how you plan to build the system?
- If somebody repeated your process on another project, what would they get wrong that you now know?

