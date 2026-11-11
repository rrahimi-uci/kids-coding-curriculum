# Changelog

All notable changes to the Kids Coding website and course materials. The website version is in `VERSION`.
Dates are in ISO format.

## 1.10.1 - 2026-11-11

More natural video narration.

- The narration sounds like a teacher, not like code being spelled out: "the planet at index 0" instead of "planets of 0", "call stickers with 2 sheets and 3 loose stickers" instead of "stickers of 2 and 3". Captions and transcripts show code names as they are written (`self.height`, `stickers.txt`, `__init__`), while the voice reads them aloud ("self dot height", "stickers dot T X T", "dunder init"). A test stops narration that would make the voice read raw code symbols.
- Fixed a rare frame crash in the video renderer when something on screen grows from nothing.

## 1.10.0 - 2026-11-11

The teaching videos are on the website.

- Every week page of Levels 1, 2 and 3 shows its video in the same place: right below the page header, as the first part of the lesson, with a "Watch the video" link at the top of "On this page". The player has captions on by default, a poster picture, and a "Read the script" transcript; a note says the voices are computer-generated. The video is left out of printouts.
- The videos are not stored in git. Web copies (720p, about 5 MB each) live on the repository's `videos` release, and the website copies them in when it is built, checking each file. If the release cannot be reached, the pages are built without the player.
- New `publish-videos` command: makes the web copies and, with `--upload`, replaces them on the release; `--rebuild-site` then republishes the website. Changing a lesson's video no longer needs a code change.

## 1.9.0 - 2026-11-11

Animated teaching videos for every week of all three levels.

- 36 animated videos, one for each week of Levels 1, 2 and 3, all in the style of the Week 1 video: natural voices for the narrator, Nova and Pixel; animated characters; every idea shown on screen; music, sound effects and captions. They are made on your own computer for free with `animate`.
- New video scripts for Levels 2 and 3, written from the lessons, workbooks, homework, exercises and project briefs. Each was then checked line by line by a separate reviewer, and the review replaced examples that were too close to quiz, checkpoint or exercise answers.
- Level 1 Weeks 2–12 narration was rewritten to sound natural when spoken. The facts checked in 1.7.0 are unchanged.
- Code shown in a video runs for real on the course's Python 3.10, with the course's turtle. The Shell shows the program's true output, errors appear exactly as Thonny shows them (including "Did you mean …?" hints and full tracebacks when a lesson reads them), and turtle windows draw exactly what the code draws. Tests fail if a video's code output changes.
- A reusable animation kit with Scratch blocks and stage, Thonny editor, turtle window, Terminal, pytest results and diagrams (variables, lists, dictionaries, flowcharts, function machines, git timelines, sorting bars, grids, feature charts, tables, class trees, stacks, queues, milestone road maps). There is a guide for writing new episodes (`videos/pipeline/animated/KIT.md`) and checks that catch a script that does not match the spec, a missing cue, code that does not fit its panel or prints something else.
- Every video command now works per level (`--level`). New commands: `episode-check`, `contact-sheet` and `apply-narration`.
- The series is called **Kids Coding with Nova and Pixel**. It uses the website's logo, and the website address appears in a small band at the bottom of every video that never covers the lesson.

## 1.8.0 - 2026-11-10

A fully animated, child-ready Week 1 video.

- New `animate` command: makes finished animated episodes on your own computer, free, with no API key. Week 1, "Robots Need Exact Instructions", is the first (3:26).
- Natural neural voices (Kokoro, open source) replace the robotic draft voice: a warm narrator, plus separate voices for Nova and Pixel. Each line is timed so the picture changes exactly when the words do.
- Animated characters blink, change expression, wave, point and talk. Every idea is shown on screen: Pixel following an algorithm on a floor grid, step cards reordering, blocks snapping together, a stage-show bug hunt with the four detective steps, and a recap.
- Gentle background music and soft sound effects, made in code. The music dips under speech, and the loudness is normalized for online video.
- The Week 1 narration was rewritten to sound natural when spoken, with a friendly opening, short sentences and a recap. Every fact checked in 1.7.0 is kept.
- Captions come as a track in the video plus `.srt` and `.vtt` files.

## 1.7.0 - 2026-11-10

Level 1 teaching videos: checked against the lessons, and ready to render.

- Every video script was checked line by line against its week's lesson plan, workbook, homework and exercises. Handoffs now name the right exercise and describe what it actually asks. Weeks 1, 7, 9 and 10 had pointed at the wrong exercise or task.
- Five scenes no longer give away answers children must find themselves: the week 2 pentagon (an exit-ticket answer), the week 6 relay hexagon and card-sort matches, the week 4 Apple Catch bug, and the week 8 homework loop. Each now teaches the same idea with a different example.
- Fixed facts: Python scenes use the course's `t = turtle.Turtle()` pattern; week 7's error message is described correctly; week 10 adds `import random` and `random.choice(PALETTE)`; week 6 lists the real six big ideas, including My Blocks. Week 11 uses the project's real milestones (M1–M4); weeks 10–12 list all six project ingredients and the exit quiz.
- Citizenship points now use each lesson's own wording: "two stars and a wish", credits comments for library art, saving files safely, "three before me", questions a program should not ask, and showcase safety (shown on screen only).
- Scripts use the course's four detective steps and its block names. They are written for Grades 4–5 (ages 9–11), and Nova always writes the code while Pixel runs it.
- Free offline draft videos: `render --voice-provider macos-say` makes a full captioned MP4 with storyboard cards in the course font. No API key is needed.
- Production narration moves to the Realtime API before the Speech API models shut down on January 6, 2027. A read that does not follow the script word for word is rejected.
- Captions are timed to the measured voice, split at sentence boundaries, and also written as `.srt` and `.vtt` files. Symbols the course font lacks (→, ✓) fall back to another font. Paid pictures and narration are cached, so nothing is paid for twice.
- New `accept --week N` records that a script still fits a changed lesson without paid calls. `check` names every changed file. Rendering refuses scripts whose lessons changed. Answer files and tests are no longer sent to the agents or fingerprinted.
- Fixed pipeline bugs: regenerating one week no longer hid other stale weeks; on-screen text beyond the third item was silently dropped; the image request used a parameter that GPT Image models reject.

## 1.6.0 - 2026-11-10

More answers for parents and production-ready Level 1 teaching-video plans.

- The questions and answers page now answers about 80 questions instead of about 30: who the course is for, cost, missed sessions, grades and showcases, why Scratch and then Python, Windows, Chromebooks and iPads, setup help, helping with homework, frustration, screen time and video games, accounts and the Scratch online community, dyslexia, ADHD, color blindness, advanced learners, families who speak another language at home, AI, and what to do after Level 3.
- The four questions on the "Common questions" slide (too young, AI, screen time, "I can't code") now have full answers on the page too.
- The page starts with a list of topics, and topics are ordered from "Before you join" to "After the course".
- The new questions live in `parents/content/faq.tex`, so the slide deck and presenter notes stay the same.

- Twelve age-appropriate, 4:30 video scripts now cover every Level 1 lesson with objectives, narration, scene timing, visual direction, misconceptions, debugging moments, digital citizenship and direct practice handoffs.
- A typed OpenAI Agents SDK workflow grounds revisions in the current curriculum, runs a teacher-review agent, and uses bounded revision loops plus deterministic quality gates.
- Per-week SHA-256 manifests detect curriculum drift and regenerate only affected episodes; the tracked JSON specification reproducibly generates the readable Markdown plan.
- The media pipeline creates accessible 16:9 scene cards or optional text-free illustrations, synthetic narration, short caption cues and FFmpeg-composed MP4 files behind an explicit human-approval gate.
- Image and voice providers are isolated so production can migrate away from retiring Speech API models without changing the curriculum workflow.

## 1.5.1 - 2026-11-10

Correct and executable Mac setup instructions.

- The Mac setup page now matches the current Thonny 5 installers, including macOS and Intel/Apple-silicon requirements.
- The one-command installer description now names all download sources, explains the Command Line Tools rerun, and distinguishes the expected administrator prompt from unexpected permission requests.
- pytest is correctly documented as required for Level 1 week 7 self-checks as well as Level 2 week 8 testing; current Thonny interpreter and system-shell paths are documented.
- Git identity guidance now matches Git's actual behavior, and the troubleshooting link follows the updated pytest section anchor.

## 1.5.0 - 2026-11-09

Written for Grades 4–5 at every level.

- All three levels now speak to children in Grades 4–5 (ages 9–11): shorter sentences, every new word explained, and the same ideas as before.
- "Math helper" boxes explain math that Grade 4–5 children have not met yet, the first time a lesson needs it: numbers below zero and where x and y are, `*` and `/`, remainders and the `%` sign, the average as a fair share, rounding, percent, cutting a number in half again and again, and a "steps distance" (gap + gap) instead of a ruler formula.
- More practice before the big exercises: worked examples, "try it in the Shell" steps, small trace tables and hand-worked sorts, a click-by-click debugger walkthrough, and a "Turtle toolbox" table before the Level 1 project.
- Almost every exercise and homework task now says what "done" looks like, often with the exact output to expect.
- Fixed mistakes: a Level 2 bug hunt whose third bug could not be seen when the program ran, a Level 1 project rubric that did not match, a Scratch claim about hidden sprites and stamping, a "game over" explanation, and a few trace and warm-up questions that needed numbers below zero.
- Level 3 project: a clearly marked Core path for younger builders, next to the unchanged Full path. Level 2 project: step-by-step recipes for the bigger starter steps.
- Git setup: a check that git uses your nickname, because on a Mac it quietly uses the computer owner's real name if none is set.
- The self-check boxes say "check off" instead of "tick".

## 1.4.0 - 2026-11-08

The pages are for reading, not for clicking.

- Self-check lists are ordinary lists (no checkboxes), and the "mark this as done" button, the progress bar and the "Done" badges are gone. Nothing on the lesson pages looks like a form any more.
- Hints are three plain sections in order (a small nudge, a bigger nudge, the most specific), instead of boxes that lock and unlock.
- The only things left that you can press are for reading comfort: the menu, the search box, Dark mode, Easy-read font, and the Copy button on code and commands.
- Nothing about a child's progress is stored in the browser any more.

## 1.3.0 - 2026-11-08

One command to set up a Mac.

- The Set up your Mac guide starts with a copy-and-paste command that installs Scratch 3, Thonny, pytest and git, step by step, asking for the Mac password once. The full script can be read on the page or downloaded, and running it again skips anything already installed.
- Command lines in the guides now have a Copy button and wrap instead of scrolling sideways.

## 1.2.0 - 2026-11-08

Clearer navigation and easier reading.

- The top toolbar is now a menu on the left. It follows the order a family meets the course: Home and the curriculum, then the three levels (each opens to its overview, twelve weeks, final project, cheat sheet and notes for families), then the parent pages, then resources. The current page and the current week are highlighted; exercise pages highlight their week.
- A search box at the top of the menu opens the search page with the results; Dark mode and Easy-read font are switches at the bottom of the menu.
- On phones and tablets the same menu opens as a drawer from a slim top bar (Escape or the close button closes it; without JavaScript it is shown above the page).
- "On this page" moved to the right-hand side on wide screens and folds above the text on smaller ones.
- Easier reading: bold instead of extra-bold headings, calmer heading sizes, sentence-case labels instead of capitals, a little more line spacing and a 70-character line length.
- Smaller, standard icons (Lucide) throughout, including the colored boxes (tip, safety, challenge, bug hunt and so on); smaller week numbers, step numbers and hint markers.
- Search results use the site colors in dark mode.

Teacher answer files (kept in the course folder, never published on this website):

- Every Scratch and Terminal exercise now has a teacher reference answer: the finished script block by block, what you should see, bug-hunt answers, talking points, common mistakes and a check-off list.
- Every Python reference answer was reviewed and rewritten with comments a parent can follow (what it does, why each step, common mistakes, another correct way); new repository tests keep it that way.

## 1.1.0 - 2026-11-08

Levels 2 and 3, projects and resources.

- Level 2 and Level 3: 12 week pages each, 68 more exercise pages with three hints each, descriptions for all 45 remaining diagrams.
- Final project pages for all three levels: brief, plan sheet, rubric and the starter files to download. Teacher-only material and solutions are not published.
- Resources: Mac setup guide (Scratch, Thonny, Python, pytest, git), troubleshooting, cheat sheets and a combined glossary for the three levels, printable progress trackers, and notes for families for each level.
- Quality gates now cover all three levels.
- Every hint was reviewed a second time against its exercise; hints no longer name bug fixes or copy solution lines.
- Fixed overlapping labels in four Level 3 workbook diagrams (bar chart, scatter plot axis, CRC card, feedback cards).
- Exercise pages and starter downloads no longer point to the self-check script, which is not published.

## 1.0.0 - 2026-11-08

First public version of the website, generated from the course sources.

- Home, For parents, Curriculum and Level 1 pages (12 week pages, 38 exercise pages with hints).
- Parent research page, slide gallery and FAQ generated from the parent deck and its bibliography.
- Each level now runs 10 to 12 weeks; the two buffer sessions are optional.
- Student-facing PDFs for download; teacher-only material and solutions are never published.
