# Standards alignment

The level goals are aligned to the **CSTA K-12 Computer Science Standards
(revised 2017)**, published by the Computer Science Teachers Association.
The AI week and the Level 3 AI goal are also aligned to **AI4K12's “Five Big
Ideas in AI”**.

| Level | Students | Main CSTA band | Also uses |
|---|---|---|---|
| 1 Introduction | Grade 5 (age 10–11) | **1B** (grades 3–5) | — |
| 2 Intermediate | Grade 5–6 | **2** (grades 6–8) | 1B (review), 3A-AP-14 |
| 3 Advanced | Grade 6–7 | **2** (grades 6–8) | selected **3A** (grades 9–10), AI4K12 |

Using a few 3A standards in Level 3 is deliberate: object-oriented design,
version control and algorithm comparison are 3A topics, taught here at a
kid-sized depth (see [DESIGN.md](DESIGN.md)).

How the alignment is traced:

1. Each level has 9 goals (L1.G1 … L3.G9) in [SYLLABUS.md](SYLLABUS.md), each
   mapped to CSTA codes.
2. Every lesson objective (“The student can …”) ends with the goal code(s)
   it serves, e.g. `(L2.G4)`.
3. `tools/coverage.py` reads the lesson plans and generates the objective →
   lesson coverage tables included in each Teacher Guide; the Teacher Guide
   also has a hand-written goals × weeks I/R/E (introduce / revisit /
   extend) table. `make test` fails if the generated tables are stale.

## CSTA standards used

### Level 1B (grades 3–5)

| Code | Standard (abridged) | Where |
|---|---|---|
| 1B-CS-03 | Determine potential solutions to simple hardware and software problems using common troubleshooting strategies | L1.G6 |
| 1B-NI-05 | Discuss real-world cybersecurity problems and how personal information can be protected | L1.G8 |
| 1B-AP-08 | Compare and refine multiple algorithms for the same task | L1.G1, L3.G2 |
| 1B-AP-09 | Create programs that use variables to store and modify data | L1.G4 |
| 1B-AP-10 | Create programs that include sequences, events, loops, and conditionals | L1.G1–G3, G9 |
| 1B-AP-11 | Decompose problems into smaller, manageable subproblems | L1.G5 |
| 1B-AP-12 | Modify, remix, or incorporate portions of an existing program | L1.G5, G9 |
| 1B-AP-14 | Observe intellectual property rights and give attribution | L1.G8 |
| 1B-AP-15 | Test and debug a program or algorithm | L1.G6 |
| 1B-AP-16 | Take on varying roles when collaborating with peers | L1.G7 |
| 1B-AP-17 | Describe choices made during program development | L1.G7 |
| 1B-IC-19 | Brainstorm ways to improve the accessibility and usability of technology | L1.G8 |
| 1B-IC-20 | Seek diverse perspectives to improve computational artifacts | L1.G7 |
| 1B-IC-21 | Use public domain or creative commons media; don't copy without permission | L1.G8 |

### Level 2 (grades 6–8)

| Code | Standard (abridged) | Where |
|---|---|---|
| 2-NI-05 | Explain how physical and digital security measures protect electronic information | L2.G9 |
| 2-NI-06 | Apply multiple methods of encryption to model secure transmission | L2.G9 (Caesar cipher) |
| 2-DA-08 | Collect data using computational tools and transform it to be more useful | L2.G5, L3.G6 |
| 2-AP-10 | Use flowcharts and/or pseudocode to address complex problems as algorithms | L2.G8 |
| 2-AP-11 | Create clearly named variables of different data types | L2.G1, G4 |
| 2-AP-12 | Design programs that combine control structures (nested loops, compound conditionals) | L2.G2, G7 |
| 2-AP-13 | Decompose problems and subproblems into parts | L2.G3 |
| 2-AP-14 | Create procedures with parameters | L2.G3 |
| 2-AP-15 | Seek and incorporate feedback from team members and users | L2.G8 |
| 2-AP-16 | Incorporate existing code, media and libraries, and give attribution | L2.G7 |
| 2-AP-17 | Systematically test and refine programs using a range of test cases | L2.G6, L3.G8 |
| 2-AP-18 | Distribute tasks and maintain a project timeline | L2.G8, L3.G5 |
| 2-AP-19 | Document programs to make them easier to follow, test, and debug | L2.G6, L3.G4 |
| 2-IC-21 | Discuss issues of bias and accessibility in the design of technologies | L2.G9 |
| 2-IC-23 | Describe tradeoffs between public and private information | L2.G9 |

### Level 3A (grades 9–10), used selectively in Level 3

| Code | Standard (abridged) | Where |
|---|---|---|
| 3A-DA-10 | Evaluate tradeoffs in how data elements are organized and where data is stored | L3.G3 |
| 3A-DA-11 | Create interactive data visualizations | L3.G6 |
| 3A-DA-12 | Create computational models that represent relationships in data | L3.G6 |
| 3A-AP-14 | Use lists to simplify solutions, generalizing computational problems | L2.G4, L3.G3 |
| 3A-AP-15 | Justify the selection of specific control structures/algorithms (tradeoffs) | L3.G2 |
| 3A-AP-16 | Design and iteratively develop artifacts using events | L3.G5 |
| 3A-AP-17 | Decompose problems using constructs such as procedures, modules, and objects | L3.G1 |
| 3A-AP-18 | Create artifacts using procedures, combinations of data and procedures | L3.G1 |
| 3A-AP-19 | Systematically design programs for broad audiences, incorporating user feedback | L3.G5 |
| 3A-AP-20 | Evaluate licenses that limit or restrict use of computational artifacts | L3.G9 |
| 3A-AP-21 | Evaluate and refine artifacts to make them more usable and accessible | L3.G8 |
| 3A-AP-22 | Design and develop artifacts working in team roles using collaborative tools | L3.G4 |
| 3A-AP-23 | Document design decisions | L3.G5 |
| 3A-IC-24 | Evaluate the ways computing impacts personal, ethical, social, economic, cultural practices | L3.G7, G9 |
| 3A-IC-25 | Test and refine artifacts to reduce bias and equity deficits | L3.G9 |
| 3A-IC-26 | Demonstrate ways a given algorithm applies to problems across disciplines | L3.G2 |
| 3A-IC-29 | Explain privacy concerns related to the collection and generation of data | L3.G9 |

### AI4K12 Five Big Ideas (Level 3, week 9 and final project option c)

1. Perception · 2. Representation & reasoning · 3. Learning ·
4. Natural interaction · 5. Societal impact.

> Standards text above is abridged. Verify wording against the official CSTA
> and AI4K12 publications before using the mapping for any formal purpose
> (see ASSUMPTIONS.md).
