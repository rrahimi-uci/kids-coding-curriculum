"""Checks for Exercise 3.1 - Enemy Family."""


def test_children_are_enemies(load_target):
    game = load_target()
    for child in ["Guard", "Zigzagger", "Sprinter"]:
        assert issubclass(getattr(game, child), game.Enemy), f"{child} should be a child class: class {child}(Enemy):"


def test_zigzagger_goes_up_and_down(load_target):
    game = load_target()
    zig = game.Zigzagger("Zig")
    zig.move()
    assert (zig.x, zig.y) == (1, 1), f"After 1 move Zig should be at (1, 1), not ({zig.x}, {zig.y}). Did you call super().move()?"
    zig.move()
    assert (zig.x, zig.y) == (2, 0), f"After 2 moves Zig should be back down at (2, 0), not ({zig.x}, {zig.y})."


def test_sprinter_uses_super_init(load_target):
    game = load_target()
    zoom = game.Sprinter("Zoom", 2, 5, speed=4)
    assert getattr(zoom, "name", None) == "Zoom", "Sprinter has no name. Call super().__init__(name, x, y) in __init__."
    assert (zoom.x, zoom.y, zoom.speed) == (2, 5, 4), "Sprinter('Zoom', 2, 5, speed=4) should start at (2, 5) with speed 4."


def test_sprinter_moves_fast(load_target):
    game = load_target()
    zoom = game.Sprinter("Zoom", speed=4)
    zoom.move()
    zoom.move()
    assert zoom.x == 8, f"With speed 4, two moves should reach x = 8, not {zoom.x}."
    assert zoom.steps == 2, f"Sprinter should count its steps too (expected 2, got {zoom.steps})."


def test_move_all_moves_everyone_their_own_way(load_target):
    game = load_target()
    enemies = [game.Enemy("Blob"), game.Guard("Rocky"), game.Sprinter("Zoom", speed=3)]
    game.move_all(enemies)
    xs = [e.x for e in enemies]
    assert xs == [1, 0, 3], f"After move_all, x should be [1, 0, 3] (Blob, Guard, Sprinter), not {xs}."
