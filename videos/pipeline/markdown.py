"""Render the tracked production plan from the machine-readable specification."""

from __future__ import annotations

from pathlib import Path

from .models import Series


def clock(seconds: int) -> str:
    return f"{seconds // 60}:{seconds % 60:02d}"


def render_plan(series: Series) -> str:
    direction = series.creative_direction
    longest = max(video.duration_seconds for video in series.videos)
    lines = [
        "# Level 1 Teaching Video Production Plan",
        "",
        "> **Status:** Reviewed scripts and an automated regeneration contract for all 12 Level 1 lessons.",
        f"> Audience: {series.audience}. Every episode is at most {clock(longest)} long (the limit is 5:00).",
        "> This file is generated from `videos/specs/level1.json`; edit the JSON, then run `python -m videos.pipeline.cli plan`.",
        "",
        "## 1. Instructional and creative direction",
        "",
        f"- **Series:** {series.series_title}",
        f"- **Audience:** {series.audience}",
        f"- **Frame:** {direction['frame']}",
        f"- **Narration:** {direction['narration']}",
        f"- **Visual language:** {direction['visual_language']}",
        f"- **Accessibility:** {direction['accessibility']}",
        "",
        "### Recurring story world",
        "",
        direction["story_world"],
        "",
        "### Five-part learning rhythm",
        "",
        "Every episode follows the same reassuring rhythm: a surprising mission, one plain-language idea, a worked example, a friendly bug hunt, and a direct handoff to the lesson activity. The video launches hands-on learning; it does not replace it.",
        "",
        "Bug hunts use the course's four detective steps: *What did I expect? What happened? Read one block (or line) at a time with your finger. Change one thing, then test again.*",
        "",
        "### Production rules",
        "",
        "- Keep the final runtime at or below 5:00, and each scene's narration within its own timing budget.",
        "- Record at roughly 140 words per minute, with pauses after questions.",
        "- Never show the answer to an exercise, homework, relay, exit ticket, card sort or the project reference; teach with a nearby example instead.",
        "- Caption every spoken word. Never use color as the only clue.",
        "- Render code, Scratch blocks, filenames, and UI labels as deterministic overlays—not inside generated artwork.",
        "- Use the Okabe–Ito color palette, high contrast, readable type, gentle motion, and no rapid flashes.",
        "- Show only nicknames and invented data. Never ask a child for a real name, address, school, password, or contact information.",
        "- End with an age-appropriate practice prompt and normalize debugging as part of coding.",
        "- Disclose synthetic narration on the end card, in the file metadata and in the video description.",
        "",
        "## 2. Curriculum audit summary",
        "",
        "The source review covered the Level 1 syllabus, teacher guide, all 12 lesson plans, workbook and homework chapters, every exercise brief and starter, and the final project materials. The sequence moves from Scratch (weeks 1–6) to Python and Thonny (weeks 7–12), while repeatedly connecting algorithms, events, loops, choices, variables, decomposition, testing, and reflection.",
        "",
        "The videos preserve the course's strongest teaching choices: concrete analogies before vocabulary; one-change-at-a-time debugging; Grade 4–5 mathematics; visible, testable outcomes; creativity alongside correctness; safe sharing; and a final interactive art project. Each script below names the misconception it prevents and points learners back to the exact lesson activity.",
        "",
        "In November 2026 every script was checked line by line against its week's lesson plan, workbook, homework and exercises. That review fixed handoffs that named the wrong exercise or task, three citizenship points that did not use the lesson's wording, Python code that did not match the course starters, invented project milestones, and five bug hunts or examples that gave away exercise or exit-ticket answers.",
        "",
        "## 3. Episode scripts and storyboards",
        "",
    ]

    for video in series.videos:
        lines.extend(
            [
                f"## Week {video.week}: {video.title}",
                "",
                f"- **Driving question:** {video.lesson_question}",
                f"- **Planned runtime:** {clock(video.duration_seconds)} ({video.duration_seconds} seconds)",
                f"- **Vocabulary:** {', '.join(video.vocabulary)}",
                f"- **Misconception to prevent:** {video.misconception}",
                f"- **Digital citizenship:** {video.safety_and_citizenship}",
                f"- **Practice activity:** `{video.practice_activity}`",
                "",
                "### Instructional objectives",
                "",
                *[f"- {objective}" for objective in video.objectives],
                "",
                "### Scene-by-scene script",
                "",
                "| Time | Purpose | Narration | Visuals and on-screen text | Production notes |",
                "|---|---|---|---|---|",
            ]
        )
        elapsed = 0
        for scene in video.scenes:
            start = elapsed
            elapsed += scene.duration_seconds
            narration = scene.narration.replace("|", "\\|").replace("\n", " ")
            visual = scene.visual.replace("|", "\\|").replace("\n", " ")
            on_screen = "; ".join(scene.on_screen_text).replace("|", "\\|")
            notes = scene.production_notes.replace("|", "\\|").replace("\n", " ")
            lines.append(
                f"| {clock(start)}–{clock(elapsed)} | **{scene.purpose}** | {narration} | {visual} **On screen:** {on_screen} | {notes} |"
            )
        lines.extend(
            [
                "",
                f"**Lesson handoff:** {video.lesson_handoff}",
                "",
                "**Curriculum evidence:**",
                "",
                *[f"- `{source}`" for source in video.source_files],
                "",
            ]
        )

    lines.extend(
        [
            "## 4. Automated, adaptable regeneration pipeline",
            "",
            "### Architecture",
            "",
            "```text",
            "Level 1 sources ──> SHA-256 change detector ──> curriculum analyst agent",
            "(answers and tests excluded)                        │",
            "                                                    v",
            "tracked plan/spec <── deterministic gates <──> scriptwriter agent",
            "       │                 ^                          │",
            "       │                 └──── reviewer agent ──────┘",
            "       v",
            "scene cards / optional illustrations ──> voice provider ──> FFmpeg + captions",
            "       │",
            "       └──> ignored media output and paid-API cache; tracked manifest records curriculum inputs",
            "```",
            "",
            "The Python pipeline uses the OpenAI Agents SDK for a typed, traceable three-agent workflow. A curriculum analyst extracts only source-supported outcomes, vocabulary, examples, and safety points, and notes which examples are answers learners must find. A scriptwriter turns that brief into the video contract. Deterministic checks and a reviewer then score each draft; failures go back to the scriptwriter for at most two bounded revisions. Deterministic validators remain the final authority.",
            "",
            "### Change and approval flow",
            "",
            "1. `check` fingerprints the syllabus, teacher guide, weekly lesson, workbook, homework, public exercise files and project sources (never answers or tests). It names each changed file, per week.",
            "2. A teacher reads the change. If the script still fits, `accept --week N` records the new fingerprints with no paid calls. Otherwise `generate --week N` sends only that week through the agent workflow and refreshes the spec, this plan and that week's fingerprints.",
            "3. A teacher reviews the script and storyboard in the PR. Paid media generation never begins implicitly.",
            "4. `render --voice-provider macos-say` makes a free offline draft (cards, draft voice, captions) for timing review. `render --approved` makes the production version with paid illustrations or narration. Rendering refuses scripts whose lessons have changed.",
            "5. Generated media and API caches remain ignored. Scripts, evidence paths, configuration, and source hashes remain reviewable in Git.",
            "",
            "### Commands",
            "",
            "```bash",
            "python3 -m venv .venv-videos",
            "source .venv-videos/bin/activate",
            "python -m pip install -r videos/requirements.txt",
            "python -m videos.pipeline.cli check",
            "python -m videos.pipeline.cli accept --week 7          # script still matches a changed lesson",
            "python -m videos.pipeline.cli generate --week 7        # paid: rewrite the script with agents",
            "python -m videos.pipeline.cli render --week 7 --voice-provider macos-say   # free draft",
            "python -m videos.pipeline.cli render --week 7 --approved                   # paid production",
            "```",
            "",
            "`OPENAI_API_KEY` is required for agent, illustration, or OpenAI voice calls. `ffmpeg` and `ffprobe` are required for MP4 rendering. Production narration uses the Realtime API (`openai-realtime`), the documented replacement for the Speech API models that shut down on January 6, 2027; its transcript is compared with the script so a paraphrased read is rejected. The legacy `openai-speech` adapter remains available until that date.",
            "",
            "### Automated quality gates",
            "",
            "- Exactly one episode for each Level 1 week, in order, with stable slugs and scene ids.",
            "- Runtime from 3:00 through 5:00, and every scene's narration within its 145-wpm budget.",
            "- At least two objectives and 4–7 fully specified scenes per episode.",
            "- Evidence files and the practice activity must be part of that week's fingerprinted material; answers and tests never are.",
            "- At most four on-screen text items per scene, each short enough to read; US spelling.",
            "- Human `--approved` gate before paid media calls; refusal to render stale scripts; no automatic publication.",
            "- Caption track plus `.srt` and `.vtt` files timed to the measured narration, voice disclosure, accessible palette, and deterministic code/UI overlays.",
            "",
            "### Maintainability decisions",
            "",
            "- The JSON spec is the machine-readable source; this Markdown file is reproducible from it.",
            "- Agent prompts and typed output contracts live in code, separate from curriculum content.",
            "- Per-file fingerprints support incremental regeneration and show exactly what changed.",
            "- Media providers are adapters in one registry. Replacing image or voice technology does not change the educational workflow.",
            "- Paid images and narration are cached by their exact inputs, so re-rendering never pays twice.",
            "- Agent traces carry level, week, and source digest metadata for review and troubleshooting.",
            "- The system proposes updates; deterministic checks and a teacher review decide whether they ship.",
            "",
        ]
    )
    return "\n".join(lines)


def write_plan(series: Series, destination: Path) -> None:
    destination.write_text(render_plan(series), encoding="utf-8")
