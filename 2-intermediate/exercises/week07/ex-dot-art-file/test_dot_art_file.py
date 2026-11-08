"""Checks for Exercise 7.3 - Dot Art from a File."""


def test_parse_line_makes_numbers_and_a_color(load_target):
    art = load_target()
    dot = art.parse_line("-150,-60,40,#009E73\n")
    assert dot == [-150, -60, 40, "#009E73"], (
        f"parse_line('-150,-60,40,#009E73') should give [-150, -60, 40, '#009E73'], not {dot}. "
        "x, y and size must be int numbers."
    )


def test_load_dots_reads_every_line_and_skips_empty_ones(load_target, tmp_path):
    art = load_target()
    art_file = tmp_path / "test_art.txt"
    art_file.write_text("0,0,50,#E69F00\n\n10,20,30,#0072B2\n")
    dots = art.load_dots(str(art_file))
    assert dots == [[0, 0, 50, "#E69F00"], [10, 20, 30, "#0072B2"]], (
        f"The file has 2 dots and an empty line, but load_dots() gave {dots}."
    )


def test_save_then_load_gives_the_same_picture(load_target, tmp_path):
    art = load_target()
    design = [[-100, 40, 25, "#CC79A7"], [60, -30, 70, "#56B4E9"]]
    filename = str(tmp_path / "saved_art.txt")
    art.save_dots(filename, design)
    art.save_dots(filename, design)  # saving twice must not double the dots
    loaded = art.load_dots(filename)
    assert loaded == design, (
        f"I saved 2 dots (twice) and loaded {loaded}. Saving should replace the file, "
        "so use \"w\" in save_dots()."
    )


def test_the_program_draws_every_dot_in_my_art(run_target, target_path):
    lines = [ln for ln in (target_path.parent / "my_art.txt").read_text().splitlines() if ln.strip()]
    result = run_target()
    dots = [d for t in result.turtles for d in t.dots]
    assert len(dots) == len(lines), f"my_art.txt has {len(lines)} dots, but the program drew {len(dots)}."
    assert len({d.color for d in dots}) >= 3, "The picture should use at least 3 colors from the file."
