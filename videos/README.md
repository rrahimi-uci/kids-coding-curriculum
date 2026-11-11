# Teaching videos (Levels 1–3)

This folder holds 36 short, animated teaching videos, one for each week of all three levels, and the pipeline that keeps them in line with the lessons. The videos are for children in Grades 4–5 (ages 9–11). No episode may be longer than five minutes. Each video launches the week's hands-on activity; it never replaces it.

## What is tracked

For each level N (1, 2, 3):

- `video-plan-levelN.md`: the readable production plan, with objectives, timing, storyboards and full narration scripts. It is generated from the spec; do not edit it by hand.
- `specs/levelN.json`: the source of truth for the scripts.
- `manifest-levelN.json`: SHA-256 fingerprints of every curriculum file each week's video is based on (one hash per file, so a change names the file).

The animations themselves live in `pipeline/animated/episodes/` (one file per episode); see "Fully animated episodes" below.
- `pipeline/`: source discovery, the OpenAI Agents SDK workflow, validation, picture and voice providers, captions and FFmpeg composition.

Rendered MP4s, captions, scene pictures and the paid-API cache (`videos/output/`, `videos/.cache/`) are ignored, so reviews stay small and generated files never hide script changes.

## Quick start

```bash
python3 -m venv .venv-videos
source .venv-videos/bin/activate
python -m pip install -r videos/requirements.txt
python -m videos.pipeline.cli check
```

`check` needs no API key and no extra packages. It validates every script (timing per scene, readable on-screen text, evidence paths, the practice activity), checks that the plan matches the spec, and compares the curriculum with the manifest. `make test` runs the same checks.

## When a lesson changes

`check` fails and names each changed file per week. A teacher then reads the change and picks one of two paths:

```bash
# The script still matches the lesson (a typo fix, a new hint): record that. No paid calls.
python -m videos.pipeline.cli accept --week 7

# The script is now wrong: rewrite that week with the agents (paid; needs OPENAI_API_KEY).
python -m videos.pipeline.cli generate --week 7
```

Every command takes `--level N` (`check` and `plan` default to all levels). `generate` with no `--week` rewrites every stale week. It updates the spec, the plan and the fingerprints of the weeks it rewrote; other stale weeks stay visible. If a week fails, the weeks that succeeded are kept in `specs/levelN.candidate.json` for review.

After a hand edit to `specs/levelN.json`, run `python -m videos.pipeline.cli plan --level N` to rewrite the readable plan. If the narration of an animated week changed, its episode file must say the same words; `make test` checks this.

### How generation works

The OpenAI Agents SDK runs three typed roles: a curriculum analyst, a scriptwriter and a teacher reviewer. The analyst reads only the week's public material: lessons, workbook, homework, exercise READMEs, starters and hints, plus the syllabus, teacher guide and project files. **Answer files, tests and self-check scripts are never sent and never fingerprinted.** That way a script cannot show a child the fix they are meant to find. All three roles follow the same course rules: Grade 4–5 reading level, the lesson's own words, code exactly like the course starters, the four detective steps, no spoilers, and Nova and Pixel in fixed roles.

Each draft goes through the same deterministic checks as `check` *before* the reviewer sees it. Failures go back to the writer, with at most two revisions. The week number and slug are kept stable, so file names and links do not move. Traces carry the level, week and source digest.

The default agent model is `gpt-6-astra`. You can override it without changing code with `VIDEO_AGENT_MODEL`. See the official [Agents SDK guide](https://developers.openai.com/api/docs/guides/agents/sdk), [quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart) and [agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents).

## Fully animated episodes (free, local)

`animate` makes a finished, child-ready episode: animated characters and examples, natural neural voices, music, sound effects and captions. It makes no paid calls and needs no API key. All 36 weeks are animated.

```bash
python -m pip install -r videos/requirements-animate.txt   # once (needs the cairo library: brew install cairo)
python -m videos.pipeline.cli fetch-voice                  # once: downloads the voice model (about 350 MB) and checks its SHA-256
python -m videos.pipeline.cli animate --level 1 --week 1   # one episode: about 25 seconds on a recent Mac
python -m videos.pipeline.cli animate --level 2             # every episode of a level
python -m videos.pipeline.cli animate                       # all 36 episodes
python -m videos.pipeline.cli animate --level 1 --week 1 --preview 30   # just the first 30 seconds
```

What goes into an episode:

- **Voices:** [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) (Apache-2.0), an open neural voice that runs on your Mac. A warm narrator (`af_heart`), Nova (`af_bella`) and Pixel (`am_puck`, with a light robot effect) each have their own voice. Each line is generated separately, so the animation is timed to the actual words. Spelling fixes for tricky words live in `LEXICON` in `animated/audio.py`.
- **Animation:** Nova and Pixel blink, change expression, wave and point. Nova's mouth follows the voice. Every idea is shown as it is said: the floor-grid algorithm, step cards, snap-together blocks, the bug hunt, and a recap. Scenes change with a circular wipe.
- **Sound:** gentle music and soft sound effects are synthesized in code, so there is nothing to license. The music ducks about 18 dB under speech. The final mix is normalized to -16 LUFS with peaks at or below -1.5 dBTP.
- **Text:** the course font, large and short, timed to the narration. Captions are a selectable track plus `.srt` and `.vtt` files.

How it is organized (`videos/pipeline/animated/`):

| File | What it holds |
|---|---|
| `timeline.py` | Beats (line, speaker, pause, cue) and the audio-driven clock. |
| `episodes/weekNN_script.py` | Who says each line. **Its text must equal the spec narration**; `make test` checks this. |
| `episodes/weekNN.py` | The scene drawings, timed by cue names, plus the sound-effect cues. |
| `engine.py`, `characters.py`, `props.py` | Drawing helpers, Nova, Pixel and the cat, and reusable props (cards, blocks, bubbles, doors, the logo). |
| `audio.py`, `render.py` | Voices, music, effects and mix; parallel frame rendering and the final MP4. |

Level 1 Week 1 is hand-made (`episodes/week01_script.py` + `week01.py`). Every other episode is a data file, `episodes/l{N}w{WW}.py`, drawn by the **animation kit** (`kit.py`). It contains:

- characters and props;
- Scratch blocks and a stage;
- a Thonny-style code editor that **runs the code shown** and displays its true output;
- a turtle window that draws what the code really draws;
- a Terminal;
- pytest results;
- diagrams (variable boxes, lists, dictionaries, flowcharts, function machines, git timelines, sorting bars, grids, feature charts, tables, class trees, stacks, queues, milestone road maps).

How to write or change an episode is in [`pipeline/animated/KIT.md`](pipeline/animated/KIT.md). Three commands help:

```bash
python -m videos.pipeline.cli episode-check --level 2 --week 3   # script = spec, cues exist, code output is real, every action draws
python -m videos.pipeline.cli contact-sheet --level 2 --week 3   # a grid of stills to look at (videos/output/sheets/)
python -m videos.pipeline.cli apply-narration edits.json --level 2   # change narration safely (locked, validated, plan rewritten)
```

Code shown in a video runs on the course's Python 3.10 (the repository's `.venv`, or `VIDEO_PYTHON`) with the course's headless turtle. Error messages come from Python's own error printer, including hints such as "Did you mean: 'print'?" that Thonny shows. Their wording matches Thonny's bundled Python for every error the videos use.

The voice is AI-generated. The end card and the file metadata say so, and a published description must say so too.

## Render

Rendering refuses scripts whose lessons have changed since they were checked. Pass `--allow-stale` only for a throwaway draft.

**Free offline draft**, for timing and teacher review. This needs macOS and `ffmpeg`, but no API key and no approval:

```bash
python -m videos.pipeline.cli render --week 7 --voice-provider macos-say
```

It renders storyboard cards in the course font, a draft computer voice, and captions timed to that voice. Use `--voice-provider silent` for cards and captions only.

**Production render**, with paid calls. Review the plan first, then pass `--approved`:

```bash
python -m videos.pipeline.cli render --week 7 --approved                           # cards + AI voice
python -m videos.pipeline.cli render --week 7 --visual-provider openai --approved  # illustrated
```

| Provider | Flag | Paid | Notes |
|---|---|---|---|
| Storyboard cards | `--visual-provider cards` (default) | no | Deterministic, high-contrast animatic frames. |
| OpenAI illustrations | `--visual-provider openai` | yes | Text-free backgrounds; titles and labels are overlaid afterwards. |
| Realtime voice | `--voice-provider openai-realtime` (default) | yes | `gpt-realtime-2.1-mini`. The transcript is compared with the script, and a paraphrased read is rejected. |
| Speech API voice | `--voice-provider openai-speech` | yes | Legacy: these models shut down on **January 6, 2027**. |
| macOS draft voice | `--voice-provider macos-say` | no | For timing reviews only; never publish it. |
| Silent | `--voice-provider silent` | no | Cards and captions, no audio. |

Output goes to `videos/output/`:

- `levelN-weekWW-<slug>.mp4`: 1920×1080, 30 fps, AAC audio, with an English caption track;
- matching `.srt` and `.vtt` caption files, for web players;
- draft renders end in `-draft`.

A scene whose narration runs longer than its time slot stops the render with a clear message. Paid pictures and narration are cached in `videos/.cache/` by their exact inputs, so re-rendering an unchanged scene costs nothing. Scenes that call for Scratch or Thonny must use an authentic, privacy-scrubbed screen capture during editing, never an invented interface.

The voice disclosure is printed on the end card and written into the MP4 metadata. Every published description must also say that the voice is AI-generated. OpenAI's usage policies require this; see the [text-to-speech guide](https://developers.openai.com/api/docs/guides/text-to-speech), the [deprecations page](https://developers.openai.com/api/docs/deprecations) and the [image generation guide](https://developers.openai.com/api/docs/guides/image-generation).

## Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | none | Required for agent, image and OpenAI voice calls. |
| `VIDEO_AGENT_MODEL` | `gpt-6-astra` | Model for the analyst, writer and reviewer agents. |
| `VIDEO_IMAGE_MODEL` | `gpt-image-2.5-flare` | Text-free scene illustrations. |
| `VIDEO_IMAGE_SIZE` | `1536x864` | Illustration size (16:9, both sides divisible by 16). |
| `VIDEO_IMAGE_QUALITY` | `medium` | `low`, `medium`, `high`, `xhigh` or `max`. |
| `VIDEO_REALTIME_MODEL` | `gpt-realtime-2.1-mini` | Realtime narration model. |
| `VIDEO_MIN_TRANSCRIPT_MATCH` | `0.97` | How closely the Realtime voice must follow the script (0–1). |
| `VIDEO_SPEECH_MODEL` | `gpt-4o-mini-tts` | Legacy Speech API model (shuts down 2027-01-06). |
| `VIDEO_VOICE` | `coral` | OpenAI narration voice. |
| `VIDEO_SAY_VOICE` | `Samantha` | macOS draft voice. |

Never commit API keys, generated voice files, or anything about a real child.

## Required human checks

Before publishing a rendered episode, a teacher should confirm:

- the code or Scratch blocks match the current lesson;
- the episode does not show the answer to any exercise, homework, relay, exit ticket or card sort;
- the narration is understandable at normal speed;
- the captions match the voice and stay readable;
- important information is never shown by color alone;
- no screen contains personal or private information;
- the synthetic narration is disclosed;
- the practice handoff points to the correct current activity.
