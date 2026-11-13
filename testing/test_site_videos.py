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


def _add_video(folder: Path, list_name: str, key: str, stem: str, size: int) -> None:
    (folder / f"{stem}.mp4").write_bytes(b"\x00" * size)
    (folder / f"{stem}.jpg").write_bytes(b"jpeg")
    (folder / f"{stem}.vtt").write_text(VTT, encoding="utf-8")
    names = [f"{stem}.mp4", f"{stem}.jpg", f"{stem}.vtt"]
    path = folder / list_name
    listing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"release": "videos", "videos": {}}
    listing["videos"][key] = {"video": names[0], "poster": names[1], "captions": names[2], "seconds": 175.8,
                              "bytes": size, "sha256": {name: _sha(folder / name) for name in names}}
    path.write_text(json.dumps(listing), encoding="utf-8")


@pytest.fixture
def release(tmp_path, monkeypatch):
    """A folder laid out like the release: Grades 4-6 level 1 week 2 and Grades 2-3 level 1 week 3."""
    folder = tmp_path / "release"
    folder.mkdir()
    _add_video(folder, "videos.json", "1-2", "level1-week02", 2_500_000)
    _add_video(folder, "junior-videos.json", "j1-3", "junior1-week03", 1_000_000)
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
    video = found[("1", 2)]
    assert video["src"] == "%BASE%videos/level1-week02.mp4"
    assert video["poster"] == "%BASE%videos/level1-week02.jpg"
    assert video["captions"] == "%BASE%videos/level1-week02.vtt"
    assert (video["minutes"], video["seconds"], video["mb"]) == (3, 176, 2.5)
    assert video["transcript"][0].startswith("Welcome back to Kids Coding!")
    assert found[("j1", 3)]["src"] == "%BASE%videos/junior1-week03.mp4"
    assert sorted(p.name for p in sv.PUBLIC.iterdir()) == [
        "junior1-week03.jpg", "junior1-week03.mp4", "junior1-week03.vtt",
        "level1-week02.jpg", "level1-week02.mp4", "level1-week02.vtt"]


def test_local_preview_reads_separate_grade_band_web_folders(tmp_path, monkeypatch) -> None:
    output = tmp_path / "output"
    older = output / "grades-4-6" / "web"
    younger = output / "grades-2-3" / "web"
    older.mkdir(parents=True)
    younger.mkdir(parents=True)
    _add_video(older, "videos.json", "1-2", "level1-week02", 2_500_000)
    _add_video(younger, "junior-videos.json", "j1-3", "junior1-week03", 1_000_000)
    monkeypatch.setattr(sv, "PUBLIC", tmp_path / "public" / "videos")
    monkeypatch.setattr(sv, "CACHE", tmp_path / "cache")
    monkeypatch.setenv("SITE_VIDEOS", str(output))

    warnings: list[str] = []
    found = sv.collect(warnings)

    assert warnings == []
    assert set(found) == {("1", 2), ("j1", 3)}


def test_a_missing_grades_2_3_list_keeps_the_grades_4_6_videos(release) -> None:
    (release / "junior-videos.json").unlink()
    warnings: list[str] = []
    found = sv.collect(warnings)
    assert set(found) == {("1", 2)}
    assert len(warnings) == 1 and "junior-videos.json" in warnings[0]


def test_a_file_that_does_not_match_its_checksum_is_left_out(release) -> None:
    (release / "level1-week02.mp4").write_bytes(b"something else")
    warnings: list[str] = []
    assert set(sv.collect(warnings)) == {("j1", 3)}
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
    monkeypatch.setattr(publish, "GRADES_4_6_OUTPUT", tmp_path)
    assert {key: path.name for key, path in publish.rendered_videos().items()} == {
        (1, 2): "level1-week02-loop-de-loop.mp4", (3, 12): "level3-week12-showcase.mp4"}


def test_publish_videos_needs_a_render_first(tmp_path, monkeypatch, capsys) -> None:
    from videos.pipeline import cli, publish

    monkeypatch.setattr(publish, "GRADES_4_6_OUTPUT", tmp_path)
    assert cli.main(["publish-videos", "--level", "1", "--week", "2"]) == 2
    assert "run `animate` first" in capsys.readouterr().err


def test_publish_finds_junior_renders_only_in_grades_2_3(tmp_path, monkeypatch) -> None:
    from videos.pipeline import publish

    younger = tmp_path / "grades-2-3"
    older = tmp_path / "grades-4-6"
    younger.mkdir()
    older.mkdir()
    (younger / "junior1-week01-robots-need-instructions.mp4").write_bytes(b"")
    (older / "junior1-week02-wrong-folder.mp4").write_bytes(b"")
    monkeypatch.setattr(publish, "GRADES_2_3_OUTPUT", younger)

    assert {key: path.name for key, path in publish.junior_rendered_videos().items()} == {
        (1, 1): "junior1-week01-robots-need-instructions.mp4"
    }


def test_web_copy_preserves_the_normalized_master_audio(tmp_path, monkeypatch) -> None:
    from videos.pipeline import publish

    source = tmp_path / "junior1-week01-test.mp4"
    source.write_bytes(b"master")
    source.with_suffix(".vtt").write_text(VTT, encoding="utf-8")
    commands: list[list[str]] = []

    def fake_run(args: list[str]) -> str:
        commands.append(args)
        if args[0] == "ffmpeg":
            Path(args[-1]).write_bytes(b"generated")
        return "123.4" if args[0] == "ffprobe" else ""

    monkeypatch.setattr(publish, "_run", fake_run)
    publish.make_web_copy(1, 1, source, tmp_path / "web", "junior1-week01")

    video_command = commands[0]
    assert video_command[video_command.index("-c:a") + 1] == "copy"
    assert "-b:a" not in video_command, "the web copy must not recompress the narration"
