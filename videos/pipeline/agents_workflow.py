"""OpenAI Agents SDK workflow for evidence-grounded script regeneration."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

from .models import Video, validate_video
from .sources import digest_files, source_bundle, week_sources


class LessonBrief(BaseModel):
    week: int
    source_summary: str
    objectives: list[str] = Field(min_length=2, max_length=4)
    vocabulary: list[str] = Field(min_length=2, max_length=8)
    accurate_examples: list[str] = Field(min_length=1)
    likely_misconception: str
    debugging_focus: str
    safety_and_citizenship: str
    lesson_handoff: str
    practice_activity: str
    evidence_files: list[str] = Field(min_length=1)


class SceneDraft(BaseModel):
    scene_id: str
    duration_seconds: int = Field(ge=10, le=90)
    purpose: str
    narration: str
    visual: str
    on_screen_text: list[str] = Field(min_length=1, max_length=4)  # each item at most 44 characters
    production_notes: str


class VideoDraft(BaseModel):
    week: int
    slug: str
    title: str
    lesson_question: str
    objectives: list[str] = Field(min_length=2, max_length=4)
    vocabulary: list[str] = Field(min_length=2, max_length=8)
    misconception: str
    safety_and_citizenship: str
    lesson_handoff: str
    practice_activity: str
    source_files: list[str] = Field(min_length=1)
    scenes: list[SceneDraft] = Field(min_length=4, max_length=7)


class ReviewResult(BaseModel):
    decision: Literal["approve", "revise"]
    curriculum_alignment: int = Field(ge=1, le=5)
    age_fit: int = Field(ge=1, le=5)
    clarity: int = Field(ge=1, le=5)
    accessibility_and_safety: int = Field(ge=1, le=5)
    timing: int = Field(ge=1, le=5)
    required_changes: list[str]
    evidence_notes: list[str]


AUDIENCE = "children in Grades 4-5 (ages 9-11) who are complete beginners"
COURSE_RULES = """
Course rules that every script must follow:
- Write at a Grade 4-5 reading level in US English: short sentences, every new word explained.
  Use only Grade 4-5 math (whole numbers, simple division such as 360 / sides, degrees).
- Use the lesson's own words for blocks, menus and code. Python code must match the course
  starters exactly (import turtle, t = turtle.Turtle(), t.forward(100), turtle.done()).
- Debugging uses the course's four detective steps: 1. What did I expect? 2. What happened?
  3. Read the blocks (or lines) one at a time with your finger. 4. Change one thing, then test again.
- The digital-citizenship point is the one the syllabus and lesson give for this week, in their words.
- NEVER reveal an answer the learner must find: no exercise, homework, relay, exit-ticket,
  card-sort or project-reference fix. Teach the idea with a nearby, different example instead.
- Rose (a ten-year-old coder) writes the code; Pixi (a literal helper robot) runs it exactly.
  Do not give either character a gendered pronoun.
- Only nicknames and invented data on screen; never ask for real personal information.
""".strip()

ANALYST_INSTRUCTIONS = f"""
You are the curriculum analyst for a beginner coding course for {AUDIENCE}.
Extract only claims supported by the supplied repository files. Preserve the lesson's
actual vocabulary, worked example, bug hunt, digital-citizenship point, and handoff to
practice. Do not invent APIs, Scratch behavior, Python syntax, or activities. List which
examples are answers the learner must find (so the script can avoid them). Set
practice_activity to the repository path of the exercise folder (or project brief) the
video should hand off to, and list the exact repository paths that support the brief.

{COURSE_RULES}
""".strip()

SCRIPTWRITER_INSTRUCTIONS = f"""
You write one friendly, accurate teaching-video script for {AUDIENCE}. Use the recurring
Kids Coding characters Rose and Pixi without making the tone babyish. The complete episode
must be 180-300 seconds; each scene's narration must fit its own duration at 145 spoken words
per minute, leaving room for pauses. Use 4-7 scenes in the series rhythm: mission hook, one
plain-language idea, a worked example, a friendly bug hunt, and a recap with the safety point
and a direct hands-on handoff. Scene ids are w<week, two digits>-s<number>, e.g. w07-s03.
Give each scene narration, concrete visuals, at most four short on-screen text items (44
characters each at most) and production notes. Never put code or UI text inside generated
artwork: specify it as an overlay. Keep every technical claim grounded in the lesson brief.

{COURSE_RULES}
""".strip()

REVIEWER_INSTRUCTIONS = f"""
You are a strict teacher-editor reviewing a short coding video for {AUDIENCE}. Compare the
draft against the evidence brief. Require technical accuracy, a total runtime no longer than
five minutes, age-appropriate language, readable and non-color-only visuals, safe data
practices, an explicit debugging moment, no spoilers, and a useful lesson handoff. Approve
only when every score is at least 4 and there are no required changes. Give concrete,
bounded revision instructions rather than rewriting the script yourself.

{COURSE_RULES}
""".strip()


def _sdk():
    try:
        from agents import Agent, Runner, trace
    except ImportError as exc:  # pragma: no cover - exercised only without optional SDK
        raise RuntimeError(
            "Video generation needs the optional dependencies in videos/requirements.txt"
        ) from exc
    return Agent, Runner, trace


async def generate_video(
    repo_root: Path,
    week: int,
    current_video: dict[str, object] | None = None,
    max_revisions: int = 2,
    level: int = 1,
) -> dict[str, object]:
    """Generate and review one week using typed Agent SDK outputs."""
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for Agent SDK generation")
    Agent, Runner, trace = _sdk()
    model = os.getenv("VIDEO_AGENT_MODEL", "gpt-6-astra")
    paths = week_sources(repo_root, week, level)
    allowed = "\n".join(f"- {path}" for path in paths)
    source_digest = digest_files(repo_root, paths)
    evidence = source_bundle(repo_root, week, level=level)

    analyst = Agent(
        name=f"Level {level} curriculum analyst",
        model=model,
        instructions=ANALYST_INSTRUCTIONS,
        output_type=LessonBrief,
    )
    writer = Agent(
        name=f"Level {level} child-friendly scriptwriter",
        model=model,
        instructions=SCRIPTWRITER_INSTRUCTIONS,
        output_type=VideoDraft,
    )
    reviewer = Agent(
        name=f"Level {level} teacher reviewer",
        model=model,
        instructions=REVIEWER_INSTRUCTIONS,
        output_type=ReviewResult,
    )

    metadata = {"level": str(level), "week": str(week), "source_digest": source_digest}
    with trace(f"level{level}-video-regeneration", metadata=metadata):
        brief_result = await Runner.run(
            analyst,
            f"Build the evidence brief for Level {level} week {week}. Evidence paths must come from "
            f"this list:\n{allowed}\n\n{evidence}",
            max_turns=4,
        )
        brief: LessonBrief = brief_result.final_output
        writer_input = (
            "Create a complete production draft from this brief.\n\n"
            + brief.model_dump_json(indent=2)
        )
        if current_video:
            writer_input += (
                "\n\nThe tracked version below may be preserved where still accurate:\n"
                + json.dumps(current_video, indent=2)
            )
        draft_result = await Runner.run(writer, writer_input, max_turns=6)
        draft: VideoDraft = _pin_identity(draft_result.final_output, week, current_video)

        for revision in range(max_revisions + 1):
            # Deterministic checks run before the reviewer, so timing, evidence-path and
            # readability problems go back to the writer instead of failing the whole run.
            problems = validate_video(Video.from_dict(draft.model_dump(mode="json")), repo_root, level)
            review_result = await Runner.run(
                reviewer,
                "Review this draft against the evidence brief.\n\nBRIEF:\n"
                + brief.model_dump_json(indent=2)
                + "\n\nDRAFT:\n"
                + draft.model_dump_json(indent=2),
                max_turns=4,
            )
            review: ReviewResult = review_result.final_output
            if problems:
                review.decision = "revise"
                review.required_changes.extend(f"Deterministic check: {problem}" for problem in problems)
            scores = (
                review.curriculum_alignment,
                review.age_fit,
                review.clarity,
                review.accessibility_and_safety,
                review.timing,
            )
            mechanically_approved = (
                review.decision == "approve"
                and min(scores) >= 4
                and not review.required_changes
            )
            if mechanically_approved:
                return draft.model_dump(mode="json")
            if review.decision == "approve":
                review.decision = "revise"
                review.required_changes.append(
                    "Resolve every score below 4 and remove all required changes before approval."
                )
            if revision == max_revisions:
                raise RuntimeError(
                    f"week {week} failed review after {max_revisions} revisions: "
                    + "; ".join(review.required_changes)
                )
            revision_result = await Runner.run(
                writer,
                "Revise the complete draft. Apply every required change while preserving "
                "accurate material. Return the entire VideoDraft.\n\nBRIEF:\n"
                + brief.model_dump_json(indent=2)
                + "\n\nCURRENT DRAFT:\n"
                + draft.model_dump_json(indent=2)
                + "\n\nREVIEW:\n"
                + review.model_dump_json(indent=2),
                max_turns=6,
            )
            draft = _pin_identity(revision_result.final_output, week, current_video)
    raise AssertionError("unreachable")


def _pin_identity(draft: VideoDraft, week: int, current_video: dict[str, object] | None) -> VideoDraft:
    """Keep the week number and slug stable, so output files and links do not move."""
    draft.week = week
    if current_video and current_video.get("slug"):
        draft.slug = str(current_video["slug"])
    return draft
