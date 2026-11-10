# Level 1 teaching videos

This folder holds the plan for twelve short teaching videos, one per Level 1 week, and the pipeline that keeps them in line with the lessons. The videos are for children in Grades 4–5 (ages 9–11) who are complete beginners. No episode may be longer than five minutes. Each video launches the week's hands-on activity; it never replaces it.

## What is tracked

- `video-plan-level1.md`: the readable production plan, with objectives, timing, storyboards and full narration scripts. It is generated from the spec; do not edit it by hand.
- `specs/level1.json`: the source of truth for the scripts.
- `manifest-level1.json`: SHA-256 fingerprints of every curriculum file each week's video is based on (one hash per file, so a change names the file).
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

`generate` with no `--week` rewrites every stale week. It updates the spec, the plan and the fingerprints of the weeks it rewrote; other stale weeks stay visible. If a week fails, the weeks that succeeded are kept in `specs/level1.candidate.json` for review.

After a hand edit to `specs/level1.json`, run `python -m videos.pipeline.cli plan` to rewrite the readable plan.

### How generation works

The OpenAI Agents SDK runs three typed roles: a curriculum analyst, a scriptwriter and a teacher reviewer. The analyst reads only the week's public material: lessons, workbook, homework, exercise READMEs, starters and hints, plus the syllabus, teacher guide and project files. **Answer files, tests and self-check scripts are never sent and never fingerprinted.** That way a script cannot show a child the fix they are meant to find. All three roles follow the same course rules: Grade 4–5 reading level, the lesson's own words, code exactly like the course starters, the four detective steps, no spoilers, and Nova and Pixel in fixed roles.

Each draft goes through the same deterministic checks as `check` *before* the reviewer sees it. Failures go back to the writer, with at most two revisions. The week number and slug are kept stable, so file names and links do not move. Traces carry the level, week and source digest.

The default agent model is `gpt-6-astra`. You can override it without changing code with `VIDEO_AGENT_MODEL`. See the official [Agents SDK guide](https://developers.openai.com/api/docs/guides/agents/sdk), [quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart) and [agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents).

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

- `level1-weekNN-<slug>.mp4`: 1920×1080, 30 fps, AAC audio, with an English caption track;
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
