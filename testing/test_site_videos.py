"""The week pages get their videos from the `videos` release (tools/site/videos.py, videos/pipeline/publish.py).

Offline tests: a fake release folder stands in for GitHub, so nothing is downloaded or uploaded.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("site_videos", ROOT / "tools" / "site" / "videos.py")
sv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sv)

VTT = """WEBVTT

00:00:04.800 --> 00:00:06.535
Welcome back to <b>Kids Coding</b>!

00:00:06.835 --> 00:00:08.823
Today's door needs a square
of light.

00:00:12.000 --> 00:00:13.500
A loop repeats instructions.
"""


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture
def release(tmp_path, monkeypatch):
    """A folder laid out like the release, with one video for level 1 week 2."""
    folder = tmp_path / "release"
    folder.mkdir()
    (folder / "level1-week02.mp4").write_bytes(b"\x00" * 2_500_000)
    (folder / "level1-week02.jpg").write_bytes(b"jpeg")
    (folder / "level1-week02.vtt").write_text(VTT, encoding="utf-8")
    names = ["level1-week02.mp4", "level1-week02.jpg", "level1-week02.vtt"]
    listing = {"release": "videos", "videos": {"1-2": {
        "video": names[0], "poster": names[1], "captions": names[2], "seconds": 175.8, "bytes": 2_500_000,
        "sha256": {name: _sha(folder / name) for name in names}}}}
    (folder / "videos.json").write_text(json.dumps(listing), encoding="utf-8")
    monkeypatch.setattr(sv, "PUBLIC", tmp_path / "public" / "videos")
    monkeypatch.setattr(sv, "CACHE", tmp_path / "cache")
    monkeypatch.setenv("SITE_VIDEOS", str(folder))
    return folder


def test_transcript_joins_caption_lines_and_starts_paragraphs_at_long_pauses() -> None:
    assert sv.transcript(VTT) == [
        "Welcome back to Kids Coding! Today's door needs a square of light.",
        "A loop repeats instructions.",
    ]


def test_videos_are_copied_into_the_site_with_page_data(release) -> None:
    warnings: list[str] = []
    found = sv.collect(warnings)
    assert warnings == []
    video = found[(1, 2)]
    assert video["src"] == "%BASE%videos/level1-week02.mp4"
    assert video["poster"] == "%BASE%videos/level1-week02.jpg"
    assert video["captions"] == "%BASE%videos/level1-week02.vtt"
    assert (video["minutes"], video["seconds"], video["mb"]) == (3, 176, 2.5)
    assert video["transcript"][0].startswith("Welcome back to Kids Coding!")
    assert sorted(p.name for p in sv.PUBLIC.iterdir()) == ["level1-week02.jpg", "level1-week02.mp4",
                                                           "level1-week02.vtt"]


def test_a_file_that_does_not_match_its_checksum_is_left_out(release) -> None:
    (release / "level1-week02.mp4").write_bytes(b"something else")
    warnings: list[str] = []
    assert sv.collect(warnings) == {}
    assert any("level 1 week 2 left out" in w and "checksum" in w for w in warnings)


def test_the_site_still_builds_when_the_videos_cannot_be_reached(release, monkeypatch) -> None:
    monkeypatch.setenv("SITE_VIDEOS", str(release / "missing"))
    warnings: list[str] = []
    assert sv.collect(warnings) == {}
    assert len(warnings) == 1 and warnings[0].startswith("videos: none on the site")


def test_videos_can_be_switched_off_and_old_copies_are_removed(release, monkeypatch) -> None:
    sv.collect([])
    assert sv.PUBLIC.exists()
    monkeypatch.setenv("SITE_VIDEOS", "off")
    assert sv.collect([]) == {}
    assert not sv.PUBLIC.exists()


def test_publish_finds_only_final_renders(tmp_path, monkeypatch) -> None:
    from videos.pipeline import publish

    for name in ["level1-week02-loop-de-loop.mp4", "level1-week02-loop-de-loop-draft.mp4",
                 "level2-week11-final-preview.mp4", "level3-week12-showcase.mp4", "notes.mp4"]:
        (tmp_path / name).write_bytes(b"")
    monkeypatch.setattr(publish, "OUTPUT", tmp_path)
    assert {key: path.name for key, path in publish.rendered_videos().items()} == {
        (1, 2): "level1-week02-loop-de-loop.mp4", (3, 12): "level3-week12-showcase.mp4"}


def test_publish_videos_needs_a_render_first(tmp_path, monkeypatch, capsys) -> None:
    from videos.pipeline import cli, publish

    monkeypatch.setattr(publish, "OUTPUT", tmp_path)
    assert cli.main(["publish-videos", "--level", "1", "--week", "2"]) == 2
    assert "run `animate` first" in capsys.readouterr().err
