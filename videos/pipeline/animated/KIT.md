# Writing an animated episode with the kit

An episode is one data file, `videos/pipeline/animated/episodes/l{LEVEL}w{WEEK:02d}.py`, that defines
`EPISODE`. The kit draws it with the same characters, palette, fonts, music and sound as the hand-made
Level 1 Week 1. **Worked example: `episodes/l1w02.py`** (read it first). Style reference:
`episodes/week01.py` + `week01_script.py`.

```python
from ..kit_dsl import A, B, Episode, NOVA, PIXEL, Scene

EPISODE = Episode(level=2, week=3, scenes=(
    Scene("l2-w03-s01", setting="workshop", lead_in=0.2, beats=(
        B("Welcome back to Code Quest!", cue="welcome", pause=0.3),
        B("‘Can we keep all my stickers in one place?’", speaker=NOVA, cue="ask", pause=0.1),
        B("asks Nova.", cue="asks"),
    ), actions=(
        A("nova", x=320, y=960, enter="left", wave="welcome"),
        A("banner", "MISSION: One box for many things", at="ask"),
    )),
    ...
))
```

## The non-negotiable rules

1. **The beats say exactly the spec narration.** Joined with spaces, a scene's beat texts must equal
   that scene's `narration` in `videos/specs/level{L}.json` (only whitespace and curly vs straight
   quotes are ignored). Split narration into beats at sentences or natural phrases. Keep the quote
   marks inside the beat text.
2. **Speakers:** text inside ‘…’ that a character says is its own beat with `speaker=NOVA` or
   `speaker=PIXEL`. "says Nova" stays a narrator beat. Nova's mouth moves and Pixel's lights flash
   automatically while they speak.
3. **Every important idea is shown while it is said.** Use the cue of the beat that says it.
   Every item of the spec scene's `on_screen_text` must appear on screen at the right moment, spelled
   exactly as in the spec.
4. **Code must be real and correct.** Code panels and turtle canvases run the code. A code panel that
   is run must list `expect=[...]`, the exact Shell lines. `episode-check` runs the code and fails if
   the real output differs. Use the course's code style (`import turtle`, `t = turtle.Turtle()`,
   `turtle.done()`). Keep code short: 12 lines at most, about 46 characters per line at the default size.
   Every line must fit its panel: lines ≤ (h − shell_h − 100) ÷ (size × 1.45), where shell_h counts only when
   the Shell shows. `episode-check` reports a panel that would hide a line.
5. **No spoilers.** Show only the examples the spec narration uses, never an exercise or homework answer.
6. **Clean frames.** Nothing overlaps, nothing runs off screen (canvas 1920×1080; keep 60 px margins),
   and at most about 3 text elements are on screen at once. Remove things with `until=` when they are
   no longer needed. Check every scene in the contact sheet.

## Beats and timing

`B(text, speaker=NARRATOR, pause=0.25, cue="name")`. Each cue must be unique within its scene. `start` and `end` are reserved time words, so never use them as cue names.
Use these pause lengths:

- 0.25–0.5 s after an ordinary sentence;
- 1.5–2.0 s after a quick question;
- 2.4–3.2 s after a "Pause and point" or prediction question (a soft clock ticks during long pauses);
- about 0.6 s at the end of the scene.

`Scene(scene_id, beats, actions, setting="sky", lead_in=0.6, tail=1.2)`. Settings: `workshop` (the
room with the floor; use it for hooks and recaps), `sky`, `lavender`, `mint`, `peach`, `night`, `stage`.

**Time specs** go in `at=`, `until=` and inside options:

| Spec | Meaning |
|---|---|
| `"cue"` | the beat starts speaking |
| `"cue$"` | the beat stops speaking |
| `"cue>"` | the next beat starts |
| `"cue@0.5"` | halfway through the beat |
| `"cue+1.2"`, `"cue$-0.3"`, `"end-2"` | offsets from any of the above |
| `"start"` / `"end"` | the scene's first and last moments |
| a number | seconds from the scene start |

A "window" option (`wave`, `point`, `chin`, `active`, `talk`, `carrying`, `beep`) takes a cue (from
that beat until the next one), a `(from, to)` pair, or a list of them.

## Actions

`A(kind, text="", at="start", until="end", **options)`. Every action pops in at `at` and fades out
after `until`. Actions are drawn in list order, so later ones sit on top. Positions are in pixels.

**Characters and props**

| Kind | Options |
|---|---|
| `nova` | `x`, `y` (feet; 960 on the workshop floor), `s` (0.5–1.0), `enter="left"/"right"`, `moods={time: mood}`, `wave`, `point`, `chin` (thinking pose), `look` ({time: -1..1}), `path=[(time, x, y)]`, `label` |
| `pixel` | `x`, `y` (body bottom; about 760–860 on the floor), `s` (0.4–1.0), `ground` (shadow y), `drop=True` (falls in), `moods`, `beep`, `carrying`, `path`, `label` |
| `cat`, `grownup` | `x`, `y`, `s`, `path`; cat: `talk` |
| `key`, `door`, `chair`, `laptop`, `pointer`, `magnifier` | `x`, `y`, `s`; key: `glow`; door: text = sign, `open=time`, `locked`; pointer/magnifier: `path` |

Moods are `happy`, `surprised`, `confused`, `thinking`, `worried` and `proud`. Pixel also has its LED
faces. Scenes usually place Nova at x≈260–360 and Pixel at x≈470–700, with props on the right.

**Text and callouts**

| Kind | Options |
|---|---|
| `banner` | text; `color` (`navy`, `green`, `orange`, `blue`, `red`, `purple`); `y` (default 96); use it for MISSION / BUG HUNT! / NEXT: … |
| `chip` | text; `x`, `y`, `color` (`sky`, `orange`, `green`, `yellow`, `pink`, `purple`, `red`, `white`, `navy`), `size` (default 42) |
| `bigtext` | text; `x`, `y` (default 960), `size`, `color`; one big takeaway |
| `bubble` | text; `who="nova"/"pixel"/"cat"` with that character's `x`, `y`, or a plain `x`, `y`; `tail` |
| `thought` | text (empty = three bouncing dots); `x`, `y`; use it during prediction pauses |
| `panel` | title text; `x`, `y`, `w`, `items=[(time, "line"), ...]`, `size` |
| `cards` | numbered steps: `items=[...]`, `x`, `y`, `w`, `gap`, `reveal=[time per item]`, `active=[window per item]`, `done=[time per item]`, `reorder=(time, [new order])`, `color` |
| `icons` | `items=[(icon, label, time), ...]`, `x`, `y`, `gap`, `crossed=[indexes]`. Icons: lock, check, cross, star, heart, person, laptop, wifi_off, file, camera, gear, clock, trophy, magnifier, warning, grownup, house, book, key, game, music |
| `arrow` | `x1`, `y1`, `x2`, `y2`, optional text label, `color` |

**Coding views**

| Kind | Options |
|---|---|
| `code` | A Thonny editor. Options: `code="..."`, `title="main.py"`, `x`, `y`, `w`, `h`, `size`. It types with `type=(from, to)`, or shows line by line with `reveal=[time per line]`, or shows everything at `at`. `highlight=[(line, from, to)]`. `run=time` presses Run and fills the Shell with the **real** output. `inputs=[...]` answers `input()`. `expect=[...]` is required when run. `error_line=N` underlines the line when the run raises; `allow_error=True` is needed if the error is the lesson. `traceback=True` shows the whole traceback (file, line number, source line, error) exactly as Thonny does; use it when the narration reads the line number. `exec="..."` runs fuller code than is shown. `shell=False` hides the Shell. |
| `turtle` | A turtle window that draws what the code really draws: `code="..."` (a whole program), `x`, `y`, `w`, `h`, `run=time` (default `at`), `duration` (seconds of drawing), `world` (zoom; it fits automatically) |
| `scratch` | A block stack: `blocks=[(kind, "text"), ("control", "repeat [4]", [inner...]), ("control", "if <cond> then", [inner], [else inner])]`. Kinds: event, motion, looks, sound, control, sensing, operators, variables, pen, myblocks. `[x]` is an input; `{flag}` is the green flag. Options: `reveal=[time per block]`, `highlight=[(index, from, to)]`, `swap=(time, i, j)`, `edits=[(time, index, "new text")]`, title text, `x`, `y`, `w`, `h`, `scale`, `panel=False` |
| `stage` | A Scratch stage. Options: `x`, `y`, `w`, `h`, `sprite` (cat, pixel, ghost, apple, bowl, star, balloon), `sprite_x`, `sprite_y` (stage coordinates, (0, 0) = middle), `flag_at`, `monitors=[(name, [(time, value)])]`, `extra=[(sprite, x, y)]`. `actions=[(time, "say", text, secs), (time, "move", steps, secs), (time, "turn", deg, secs), (time, "goto", x, y, secs), (time, "draw", sides, length, secs[, turn]), (time, "clear"), (time, "hide"/"show")]` |
| `terminal` | `lines=[(time, "git status", "cmd"), (time, "On branch main", "out"), ...]` (commands are typed with a `$` prompt) |
| `tests` | `items=[(time, "test_name", passed)]`, title text |
| `file` | file name text; `lines=[...]` or `states=[(time, [lines])]` |

**Diagrams**

| Kind | Options |
|---|---|
| `box` | Variable name text; `values=[(time, value)]`, `x`, `y`, `color` |
| `listrow` | Name text; `items=[...]` or `states=[(time, [...])]`, `highlight=[(from, to, index)]`, `cell`, `indexes=False` |
| `dict` | Name text; `rows=[(key, value)]` or `states`, `highlight=[(from, to, key)]`, `x`, `y`, `w` |
| `flow` | `items=["size > 100?", ...]`, `outcomes=[... one more for else]`, `token=[(time, "label", outcome_index)]` |
| `machine` | Function name text; `items=[(time, input, output)]` |
| `timeline` | `commits=[(time, "message")]`, `head` |
| `bars` | `states=[(time, [values])]` or `values`, `labels`, `highlight=[(from, to, [indexes])]`, `x`, `y`, `w`, `h` |
| `grid` | `rows=["#..#", ...]` or `states`, `cell`, `marks=[(time, row, col, "label")]`, `walker=[(time, col, row)]`. Characters: `#` wall, `.` floor, `S` start, `G` goal, `R`/`B`/`O`/`P`/`F`/`W`/`X` colors, digits as labels |
| `scatter` | `points=[(fx, fy, "label", "color")]`, `axes=("x name", "y name")`, `span=10`, `query=(time, fx, fy)`, `nearest=(time, index)` (draws the steps path) |
| `table` | `header=[...]`, `rows=[[...]]`, `highlight=[(from, to, row)]`, `reveal=[time per row]`, `col_w` |
| `tree` | `nodes=[(name, parent_or_None, ["line", ...], time)]`, `gap`, `level_gap`, `w` |
| `stack` / `queue` | Title text; `states=[(time, [items])]` (stack: bottom→top; queue: front→back) |
| `roadmap` | `items=["M1 Plan", ...]`, `checks=[(time, index)]`, `current=[(time, index)]` |

**Feedback and sound**

`badge` (`ok=True/False`, `x`, `y`; plays a chime or a gentle "oops"), `confetti` (`x`, `y`) and
`sfx` (text = pop, snap, whoosh, chime, sparkle, beep_boop, boing, oops, tick, door or zoom).

Most kinds already play a soft pop when they appear; cards, blocks, tests and commits play their own
sounds. Add `sfx` only for story moments.

## A good scene (what reviewers check)

- **Hook (workshop):** Nova and Pixel, the mission banner, a story problem acted out, and a question
  with a thinking pause.
- **Idea:** one concept at a time, with a diagram that changes as the words change, and the spec's
  on-screen text as chips.
- **Worked example:** code typed in step with the narration and run at the moment the narration says
  so, with a turtle drawing or diagram showing the result.
- **Bug hunt:** a `BUG HUNT!` banner, the buggy code or blocks, the symptom, the course's debugging
  steps as chips or cards, a pause, the one-change fix, a rerun, and a badge.
- **Recap (workshop):** recap chips, the citizenship point with icons, a `NEXT: …` banner with the
  hands-on steps as cards, a cheer and "Happy coding!" if the script has it.

## Workflow

```bash
python -m videos.pipeline.cli episode-check --level 2 --week 3      # script, cues, real code output, every component draws
python -m videos.pipeline.cli contact-sheet --level 2 --week 3      # writes videos/output/sheets/l2w03-sheet.png; open it and look
python -m videos.pipeline.cli contact-sheet --level 2 --week 3 --per-scene 8   # closer look
```

Fix everything the contact sheet shows (overlaps, text off screen, empty stretches, wrong timing),
then run both commands again. The first contact sheet generates the voices, so it takes about a
minute; after that it is fast.

**Narration edits (only when asked).** Put `{scene_id: "new narration"}` in a JSON file and run
`python -m videos.pipeline.cli apply-narration FILE --level L`. It locks the spec, validates the
change and regenerates the plan. Keep every fact, the word budget and the on-screen text.
