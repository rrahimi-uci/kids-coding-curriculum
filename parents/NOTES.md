# Notes: sources, removed claims and assumptions

Written November 2026 for the parent deck (`main.tex`), the presenter notes
and the handout. Full citations are in [references.bib](references.bib)
and on the deck's References slides.

## How sources were checked

* Every journal or conference DOI in `references.bib` was resolved through
  the Crossref API. The title and year returned matched in all 26 cases.
* Non-DOI sources (WEF, Code.org, Google–Gallup, K12CS, CSTA, eCFR, Okabe &
  Ito) were checked by search and by opening the URL. WEF and CSTA block
  automated requests (HTTP 403) but are the official pages. The FTC's own
  COPPA page returned 404 to automated requests, so the citation points to
  the official eCFR text of 16 CFR Part 312.
* The figures used on slides were taken from abstracts, publisher or
  repository pages. Where only secondary coverage was available, the figure
  was dropped and the point kept qualitatively (see below).

## Sources and what each one supports

| Source | Used for (slide) | Strength label | Notes |
|---|---|---|---|
| World Economic Forum (2025), *Future of Jobs Report 2025* | 3 | survey | Top 3 fastest-growing skills to 2030; analytical thinking named essential by 7 in 10 employers. An employer forecast, not an outcome. |
| Code.org, CSTA & ECEP (2025), *State of AI & CS Education* | 4 | survey | 60% of US public high schools offered foundational CS and 6.1% of students enrolled, 2024–25. The figures come from Education Week's summary of the report. **Check against the report PDF before presenting.** |
| Kazemitabaar et al. (2023), CHI | 5, appx | one controlled study | 69 learners aged 10–17. With AI, more tasks completed and higher scores; editing by hand did not get worse; retention difference not significant. |
| OECD (2026), *Digital Education Outlook 2026* | 5, appx | report | Used only qualitatively: general chatbots can raise performance without lasting learning, while tools designed for learning do better. Specific percentages in press coverage were **not** used. |
| Scherer, Siddiq & Sánchez Viveros (2019), *J. Educ. Psych.* | 6, 7, 11 | meta-analysis | 105 studies, 539 effects. Transfer to creative thinking, math, metacognition, then spatial skills and reasoning; least to literacy and school achievement; larger effects with untreated controls and in published studies. |
| Scherer et al. (2020), *Computers in Human Behavior* | 6, 7 | meta-analysis | Large effect of instruction on programming skill itself. |
| Montuori et al. (2024), *Computers & Education* | 6, 8 | meta-analysis (small) | 19 experiments, 1,523 children, 11 pooled (fixed effect): problem solving 0.89, planning 0.36, working memory 0.20, inhibition 0.17. These are the only numbers charted. |
| Arfé, Vardanega & Ronconi (2020), *Computers & Education* | 9 | cluster-RCT | 179 first graders, 8 h of Code.org over 4 weeks; planning improved more than controls, inhibition less so. |
| Master et al. (2017), *J. Exp. Child Psych.* | 10, 24 | experiment | Programming a robot removed the first-grade gender gap in tech interest and confidence; stereotypes unchanged. |
| Tai et al. (2006), *Science* | 10 | longitudinal, correlational | Eighth-grade career expectations predicted science degrees (about 2–3×). **Old data (1988–2000); association only.** |
| Google & Gallup (2016) | 10, 24 | survey | Girls report less encouragement in CS from parents and teachers. **Ten years old.** |
| Pea & Kurland (1984), *New Ideas in Psychology* | 11 | critique | Cited for the long-standing doubt about automatic transfer. **Flagged as old.** |
| Sala & Gobet (2017), *Current Directions in Psych. Science* | 11 | meta-analyses | Far transfer is rare (chess, music, working memory); effects shrink with better designs. |
| Papert (1980); Resnick et al. (2009); Lee et al. (2011) | 12, 13 | design principles | Projects, low floor / high ceiling / wide walls, Use–Modify–Create. Labeled as principles, not experiments. |
| Umapathy & Ritzhaupt (2017), *ACM TOCE* | 12, 14 | meta-analysis | Pair programming favored in 3 of 4 outcome areas (not attitudes). Mostly university courses. |
| Denner et al. (2014), *JRTE* | 14 | study, 320 middle schoolers | Pairs gained more, especially less-experienced students. |
| Michaeli & Romeike (2019), WiPSCE | 12, 14 | controlled classroom study | Explicitly taught debugging process improved debugging and self-efficacy. Labeled "mixed (few studies)". |
| Wisniewski, Zierer & Hattie (2020), *Frontiers in Psych.* | 14, 24 | meta-analysis | Feedback has a medium effect, more when it gives task and process information. Used instead of the often-quoted 0.79. |
| del Olmo-Muñoz et al. (2020), *Computers & Education* | 15 | quasi-experiment | Unplugged-first helped early primary pupils' CT and motivation. |
| Sentance, Waite & Kallia (2019), *CS Education* | 12, 15 | multi-school study | PRIMM: 493 students aged 11–14 in 13 schools outperformed comparison group. |
| Bruner (1960) | 12, 15 | theory | Spiral curriculum. **Old; cited for the idea.** |
| Weintrop & Wilensky (2017, 2019) | 17 | quasi-experiment | Blocks ahead after 5 weeks; no difference after moving to Java. |
| Xu et al. (2019), *CS Education* | 17 | meta-analysis | 13 studies: g = 0.245, 95% CI −0.078 to 0.567 (not significant). Charted. |
| Wing (2006); K-12 CS Framework (2016) | 6 | definitions | Computational thinking. |
| CSTA (2017); Touretzky et al. (2019, AI4K12) | 19–21 | standards | Level alignment. CSTA published a 2025 draft revision; the 2017 standards are cited. |
| FTC COPPA Rule, 16 CFR 312 (amended 2025) | 25 | law | Verifiable parental consent before collecting personal information from children under 13. |
| AAP (2016), *Pediatrics* | 25 | policy statement | Family media plans and consistent limits for school-age children. |
| Okabe & Ito (2008) | 25, credits | design guide | Color-blind-safe palette. |

## Claims considered and removed

* **Jobs, salary and college admissions.** Left out on purpose. The deck says
  so explicitly (slides 3 and 11).
* **"Coding improves math/reading grades."** Not supported. Shown as mixed
  or little effect.
* **Growth mindset benefits.** The evidence is weak and mixed, so this was not
  used as a selling point.
* **Hattie & Timperley's feedback effect of 0.79.** Replaced by the larger
  2020 re-analysis (about 0.48), which is mentioned in the notes and appendix.
* **OECD 2026 percentages** (for example "17% worse without AI" and "48%
  higher short-term scores"). These were seen only in secondary coverage, so
  only the qualitative finding was kept.
* **Exact Google–Gallup ratios** (for example "1.5× more encouragement").
  The ratios were reported inconsistently across secondary sources. The
  qualitative finding was kept.
* **Pair programming improving enjoyment or attitudes.** The meta-analysis
  found no benefit for affective outcomes.
* **Specific screen-time hour limits.** The AAP guidance for school-age
  children asks for a family plan, not a fixed number.
* **An elementary-school CS access figure.** It is measured differently in the
  Code.org report, so no figure is quoted.

## Assumptions

1. **Course length.** The brief said "about 10 months each". The repository
   (docs/SYLLABUS.md, docs/DESIGN.md) defines 12 sessions plus 2 spare
   sessions per level, about 4 months each and about a year for all three.
   The deck follows the repository. The months on the roadmap are the sample
   calendar from the Teacher Guides (Level 1 starts January 2027).
2. **Who runs it.** A small home course, led by a parent or volunteer
   (`\Presenter` placeholder), for up to 4 children. This follows
   docs/ASSUMPTIONS.md.
3. **US setting.** US Letter handout, US law (COPPA), US data (Code.org),
   CSTA standards, as in the rest of the repository.
4. **Font size.** "Minimum 20 pt body" is applied literally on a
   13.333 × 7.5 in slide. Source lines, figure descriptions, diagram
   labels, badge labels and the appendix tables are smaller by design.
5. **Alt text.** Every chart and diagram has a visible one-line text
   description under it (`\figalt`). The speaker notes describe each figure
   in words. The PDF is not tagged: LuaLaTeX tagging does not yet support
   Beamer.
6. **Handout edition.** Only the standard edition is built. The handout uses
   `kidscode.cls`, so a dyslexia-friendly build could be added later.

## Double-check before presenting

* The three placeholders in `content/shared.tex`.
* The Code.org 60% / 6.1% figures, against the current report.
* Whether a newer WEF Future of Jobs report (expected 2027) has been
  published.
