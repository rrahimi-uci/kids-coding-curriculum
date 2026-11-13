# Parent information deck

A 20–30 minute talk for families of Grade 4–6 children deciding whether to
join the Grades 4–6 course (`grade-4-6/`): why coding matters, what the research does and does not
show, how the course works, and how parents can help.

| Output | File (after `make`) |
|---|---|
| Slide deck (27 slides + appendix, 16:9) | `build/parent-deck.pdf` |
| Presenter edition (every slide followed by its speaker notes) | `build/parent-deck-notes.pdf` |
| One-page handout (US Letter) | `build/parent-handout.pdf` |

The sources, the claims that were left out and the assumptions are listed in
[NOTES.md](NOTES.md).

## Before presenting

Edit the three placeholders at the top of [content/shared.tex](content/shared.tex):
`\Presenter`, `\ContactLine` and `\StartDate`. Then run `make`.

## Build

```sh
cd parents
make            # deck + notes + handout (about a minute)
make png        # also render every page to build/png/ for a visual check
make clean
```

Requirements: LuaLaTeX and **biber** (MacTeX includes both; with BasicTeX
add `biber` with `brew install biber`), plus these TeX packages on top of the
curriculum's list in `.github/workflows/ci.yml`: `beamer`, `biblatex`,
`biblatex-apa`, `babel-english`, `logreq`, `translator`.

`latexmk` is not needed: the Makefile runs LuaLaTeX → biber → LuaLaTeX ×2.

## Files

```
main.tex                 the deck (slides + \note speaker notes)
notes.tex                presenter edition: defines \kcwithnotes, inputs main.tex
handout.tex              one-page handout (uses shared/latex/kidscode.cls)
content/shared.tex       text used by both deck and handout: course facts,
                         level summaries, "how to help", safety promises
content/faq.tex          extra questions and answers for the website's FAQ page
                         (not in the deck or handout; see "Website FAQ" below)
references.bib           the one bibliography (APA style via biblatex)
beamerthemekidscode.sty  original Beamer theme (layout, badges, boxes, notes page)
Makefile
```

Colors come from [shared/latex/kidscode-colors.sty](../shared/latex/kidscode-colors.sty),
the same Okabe–Ito palette as every printed document; fonts are the
curriculum's Atkinson Hyperlegible Next and Mono.

## Theme reference

The page is a standard 13.333 × 7.5 in widescreen slide, so point sizes are
literal: body text 20 pt, headings larger; source lines and figure captions
are smaller.

| Macro | Purpose |
|---|---|
| `\kicker{Section}` | small label above the following frame titles |
| `\source{\textcite{key}}` | source line at the bottom-left of a frame |
| `\evStrong` `\evMixed` `\evOpen` | evidence badges: color + icon + word |
| `\begin{keybox}[title]` | one-sentence take-away |
| `\begin{cardbox}[color]{title}` | card; cards on one slide share a height |
| `\kcnotes{say}{plain language}{questions}` | structured speaker notes |
| `\qa{question}{answer}` | a likely question inside `\kcnotes` |
| `\figalt{text}` | visible text description under a figure (in main.tex) |

Rules used when writing slides: one idea per slide, at most six bullets of
about ten words, a `\source` on every slide that states a fact, and a
`\figalt` under every chart or diagram.

## Website FAQ

The website's [questions and answers page](https://rrahimi-uci.github.io/kids-coding-curriculum/parents/faq/)
combines two sources:

1. the `\qa{question}{answer}` entries in the third argument of each `\kcnotes` in
   `main.tex` (questions a presenter may get on the evening), grouped by the slide's kicker;
2. `content/faq.tex`, for questions families ask outside the evening (setup, missed sessions,
   homework help, screen time, privacy, different learners, what comes next). It is never
   typeset; only `tools/site/parents.py` reads it.

In `content/faq.tex`, `\faqtopic{Name}` starts a topic and `\qa{...}{...}` adds an entry.
Macros from `content/shared.tex`, `\textcite`/`\parencite` (linked to the research page) and
`\sitelink{path/}{text}` (a link within the website) work in both. The topic order is set by
`TOPIC_ORDER` in `site/src/pages/parents/faq.astro`. Keep course facts in line with
`grade-4-6/SYLLABUS.md` and `docs/ASSUMPTIONS.md`, and research claims in line with [NOTES.md](NOTES.md).
