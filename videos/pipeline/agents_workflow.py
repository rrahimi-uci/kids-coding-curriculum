"""OpenAI Agents SDK workflow for evidence-grounded script regeneration."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

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
    evidence_files: list[str] = Field(min_length=1)


class SceneDraft(BaseModel):
    scene_id: str
    duration_seconds: int = Field(ge=10, le=90)
    purpose: str
    narration: str
    visual: str
    on_screen_text: list[str] = Field(min_length=1, max_length=4)
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


ANALYST_INSTRUCTIONS = """
You are the curriculum analyst for a beginner coding course for children ages 10-11.
Extract only claims supported by the supplied repository files. Preserve the lesson's
actual vocabulary, worked example, debugging routine, digital-citizenship point, and
handoff to practice. Do not invent APIs, Scratch behavior, Python syntax, or activities.
Keep mathematics within Grades 4-5 and treat bugs as normal evidence for learning.
List the exact repository paths that support the brief.
""".strip()

SCRIPTWRITER_INSTRUCTIONS = """
You write one friendly, accurate teaching-video script for ages 10-11. Use the recurring
Code Quest characters Nova (a curious child coder) and Pixel (a friendly helper robot),
without making the tone babyish. The complete episode must be 180-300 seconds and fit
within 145 spoken words per minute. Use 4-7 scenes with narration, concrete visuals,
short readable on-screen text, and production notes. Include a pause-and-predict moment,
a friendly bug hunt, the lesson's safety point, and a direct hands-on handoff. Never put
code or UI text inside generated artwork: specify it as an overlay. Never request real
personal information. Keep every technical claim grounded in the lesson brief.
""".strip()

REVIEWER_INSTRUCTIONS = """
You are a strict teacher-editor reviewing a short coding video for ages 10-11. Compare
the draft against the evidence brief. Require technical accuracy, a total runtime no
longer than five minutes, age-appropriate language, readable and non-color-only visuals,
safe data practices, an explicit debugging moment, and a useful lesson handoff. Approve
only when every score is at least 4 and there are no required changes. Give concrete,
bounded revision instructions rather than rewriting the script yourself.
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
) -> dict[str, object]:
    """Generate and review one week using typed Agent SDK outputs."""
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for Agent SDK generation")
    Agent, Runner, trace = _sdk()
    model = os.getenv("VIDEO_AGENT_MODEL", "gpt-6-astra")
    paths = week_sources(repo_root, week)
    source_digest = digest_files(repo_root, paths)
    evidence = source_bundle(repo_root, week)

    analyst = Agent(
        name="Level 1 curriculum analyst",
        model=model,
        instructions=ANALYST_INSTRUCTIONS,
        output_type=LessonBrief,
    )
    writer = Agent(
        name="Level 1 child-friendly scriptwriter",
        model=model,
        instructions=SCRIPTWRITER_INSTRUCTIONS,
        output_type=VideoDraft,
    )
    reviewer = Agent(
        name="Level 1 teacher reviewer",
        model=model,
        instructions=REVIEWER_INSTRUCTIONS,
        output_type=ReviewResult,
    )

    metadata = {"level": "1", "week": str(week), "source_digest": source_digest}
    with trace("level1-video-regeneration", metadata=metadata):
        brief_result = await Runner.run(
            analyst,
            f"Build the evidence brief for Level 1 week {week}.\n\n{evidence}",
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
        draft: VideoDraft = draft_result.final_output

        for revision in range(max_revisions + 1):
            review_result = await Runner.run(
                reviewer,
                "Review this draft against the evidence brief.\n\nBRIEF:\n"
                + brief.model_dump_json(indent=2)
                + "\n\nDRAFT:\n"
                + draft.model_dump_json(indent=2),
                max_turns=4,
            )
            review: ReviewResult = review_result.final_output
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
            draft = revision_result.final_output
    raise AssertionError("unreachable")
