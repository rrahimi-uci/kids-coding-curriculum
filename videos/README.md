# Level 1 teaching videos

This folder contains a production-ready plan for twelve short teaching videos and the pipeline that keeps those videos aligned with the Level 1 curriculum. The intended audience is children ages 10–11. No episode may exceed five minutes.

## What is tracked

- `video-plan-level1.md` — the readable production plan, objectives, timing, storyboards, and complete narration scripts.
- `specs/level1.json` — the canonical machine-readable version of the scripts.
- `manifest-level1.json` — SHA-256 fingerprints of every curriculum file that informed each week.
- `pipeline/` — source discovery, OpenAI Agents SDK workflow, validation, media adapters, captions, and FFmpeg composition.

Rendered MP4s, temporary scene assets, narration files, and paid-API caches are intentionally ignored. This keeps reviews small and prevents generated binaries from hiding script changes.

## Quick start

```bash
python3 -m venv .venv-videos
source .venv-videos/bin/activate
python -m pip install -r videos/requirements.txt
python -m videos.pipeline.cli check
```

The offline `check` command validates all scripts, timings, evidence paths, accessible scene requirements, the generated Markdown plan, and curriculum fingerprints. It does not need an API key.

## Regenerate after a course change

Set an API key, then regenerate only the weeks detected as stale:

```bash
export OPENAI_API_KEY="your-key-in-your-shell-or-secret-manager"
python -m videos.pipeline.cli generate
```

To work on one week deliberately:

```bash
python -m videos.pipeline.cli generate --week 7
```

The OpenAI Agents SDK runs three typed roles: a curriculum analyst, a child-friendly scriptwriter, and a teacher reviewer. The reviewer can request at most two revisions. Deterministic checks run after the agents and before tracked files are replaced. Agent traces include the level, week, and source digest.

The default agent model is `gpt-6-astra`, following the current Agents SDK quickstart. Override it without changing code:

```bash
export VIDEO_AGENT_MODEL="an-approved-model-id"
```

See the official [Agents SDK guide](https://developers.openai.com/api/docs/guides/agents/sdk), [quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart), and [agent definition guide](https://developers.openai.com/api/docs/guides/agents/define-agents).

## Review and render

Generation updates scripts and storyboards only. A teacher must review the diff before media generation. Rendering is blocked unless the operator passes `--approved`:

```bash
python -m videos.pipeline.cli render --week 7 --approved
```

The default visual provider creates deterministic, high-contrast **animatic cards** for timing and review. They are not a substitute for the storyboard's final motion graphics. For production, optional OpenAI illustrations can provide text-free backgrounds; code and UI labels stay deterministic overlays. Scenes that call for Scratch or Thonny must use an authentic, privacy-scrubbed capture during the editing pass rather than an invented interface:

```bash
python -m videos.pipeline.cli render --week 7 --visual-provider openai --approved
```

Rendering needs `ffmpeg` and `ffprobe`. Output appears in `videos/output/` and includes an English caption track. Every published video and description must disclose that its voice is AI-generated.

The optional illustration adapter follows the official [image generation guide](https://developers.openai.com/api/docs/guides/image-generation). The current narration adapter uses the Speech API only as a replaceable bridge. OpenAI documents that its current Speech API models are scheduled to shut down on January 6, 2027 and recommends migrating to Realtime voice. The adapter boundary allows that migration without changing lesson analysis, scripts, tests, or FFmpeg composition. See the [text-to-speech guide](https://developers.openai.com/api/docs/guides/text-to-speech).

## Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | none | Required for agent, image, and OpenAI voice calls. |
| `VIDEO_AGENT_MODEL` | `gpt-6-astra` | Model used by curriculum, writing, and review agents. |
| `VIDEO_IMAGE_MODEL` | `gpt-image-2.5-flare` | Optional text-free scene illustration model. |
| `VIDEO_SPEECH_MODEL` | `gpt-4o-mini-tts` | Temporary Speech API adapter; migrate before retirement. |
| `VIDEO_VOICE` | `coral` | Synthetic narration voice. |

Never commit API keys, generated voice files, or child information.

## Required human checks

Before publishing a rendered episode, a teacher should confirm:

- the code or Scratch blocks match the current lesson;
- the narration is understandable at normal speed;
- captions match the voice and remain readable;
- important information is not communicated by color alone;
- no screen contains personal or private information;
- synthetic narration is disclosed;
- the practice handoff points to the correct current activity.
