"""Render the tracked production plan from the machine-readable specification."""

from __future__ import annotations

from pathlib import Path

from .models import Series


def clock(seconds: int) -> str:
    return f"{seconds // 60}:{seconds % 60:02d}"


def render_plan(series: Series) -> str:
    direction = series.creative_direction
    lines = [
        "# Level 1 Teaching Video Production Plan",
        "",
        "> **Status:** Production-ready scripts and an automated regeneration contract for all 12 Level 1 lessons.",
        "> Each video is designed for children ages 10–11 and is shorter than five minutes.",
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
        "### Production rules",
        "",
        "- Keep the final runtime at or below 5:00; the planned episodes are 4:30.",
        "- Record at roughly 140–145 words per minute, with pauses after questions.",
        "- Caption every spoken word. Never use color as the only clue.",
        "- Render code, Scratch blocks, filenames, and UI labels as deterministic overlays—not inside generated artwork.",
        "- Use the Okabe–Ito color palette, high contrast, readable type, gentle motion, and no rapid flashes.",
        "- Show only nicknames and invented data. Never ask a child for a real name, address, school, password, or contact information.",
        "- End with an age-appropriate practice prompt and normalize debugging as part of coding.",
        "- Disclose synthetic narration in the end card and video description.",
        "",
        "## 2. Curriculum audit summary",
        "",
        "The source review covered the Level 1 syllabus, teacher guide, all 12 lesson plans, workbook and homework chapters, every exercise brief and starter, and the final project materials. The sequence moves from Scratch (weeks 1–6) to Python and Thonny (weeks 7–12), while repeatedly connecting algorithms, events, loops, choices, variables, decomposition, testing, and reflection.",
        "",
        "The videos preserve the course's strongest teaching choices: concrete analogies before vocabulary; one-change-at-a-time debugging; Grade 4–5 mathematics; visible, testable outcomes; creativity alongside correctness; safe sharing; and a final interactive art project. Each script below names the misconception it prevents and points learners back to the exact lesson activity.",
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
            "                                                    │",
            "                                                    v",
            "tracked plan/spec <── deterministic gates <── scriptwriter agent",
            "       │                 ^                          │",
            "       │                 └──── reviewer agent ──────┘",
            "       v",
            "scene cards / optional illustrations ──> voice provider ──> FFmpeg + captions",
            "       │",
            "       └──> ignored media output; tracked manifest records curriculum inputs",
            "```",
            "",
            "The Python pipeline uses the OpenAI Agents SDK for a typed, traceable three-agent workflow. A curriculum analyst extracts only source-supported outcomes, vocabulary, examples, and safety points. A scriptwriter turns that brief into the `VideoSpec` contract. A reviewer scores curriculum alignment, age fit, timing, accessibility, and safety; failed reviews return to the scriptwriter for at most two bounded revisions. Deterministic validators remain the final authority.",
            "",
            "### Change and approval flow",
            "",
            "1. `check` hashes the syllabus, teacher guide, weekly lesson, workbook, homework, exercises, and project sources. It reports exactly which weeks changed.",
            "2. `generate` sends only stale weeks through the agent workflow, validates structured output, updates `videos/specs/level1.json`, refreshes this plan, and writes a new manifest.",
            "3. A teacher reviews the script and storyboard in the PR. Paid media generation never begins implicitly.",
            "4. `render --approved` creates deterministic cards or optional generated illustrations, synthetic narration through the configured provider, captions, and an MP4 for each approved week.",
            "5. Generated media and API caches remain ignored. Scripts, evidence paths, configuration, and source hashes remain reviewable in Git.",
            "",
            "### Commands",
            "",
            "```bash",
            "python3 -m venv .venv-videos",
            "source .venv-videos/bin/activate",
            "python -m pip install -r videos/requirements.txt",
            "python -m videos.pipeline.cli check",
            "python -m videos.pipeline.cli generate --week 7",
            "python -m videos.pipeline.cli render --week 7 --approved",
            "```",
            "",
            "`OPENAI_API_KEY` is required for agent, illustration, or OpenAI voice calls. `ffmpeg` and `ffprobe` are required for MP4 rendering. The current OpenAI Speech API adapter is deliberately isolated because its supported models are scheduled to retire on January 6, 2027; replace the adapter with a Realtime voice implementation without changing lesson analysis, scripts, or render contracts.",
            "",
            "### Automated quality gates",
            "",
            "- Exactly one episode for each Level 1 week, in order.",
            "- Runtime from 3:00 through 5:00 and narration within the 145-wpm budget.",
            "- At least two objectives and four fully specified scenes per episode.",
            "- Existing curriculum evidence for every episode; changed evidence makes the manifest stale.",
            "- Narration, visuals, readable on-screen text, and production notes in every scene.",
            "- Human `--approved` gate before media calls; no automatic publication.",
            "- Caption track, AI-voice disclosure, accessible palette, and deterministic code/UI overlays.",
            "",
            "### Maintainability decisions",
            "",
            "- The JSON spec is the machine-readable source; this Markdown file is reproducible from it.",
            "- Agent prompts and typed output contracts live in code, separate from curriculum content.",
            "- Source fingerprints support incremental regeneration and make drift visible in CI.",
            "- Media providers are adapters. Replacing image or voice technology does not change the educational workflow.",
            "- Agent traces carry level, week, and source digest metadata for review and troubleshooting.",
            "- The system proposes updates; deterministic checks and a teacher review decide whether they ship.",
            "",
        ]
    )
    return "\n".join(lines)


def write_plan(series: Series, destination: Path) -> None:
    destination.write_text(render_plan(series), encoding="utf-8")
