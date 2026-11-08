"""Checks for Exercise 9.2 - Dodge the Meteors.

The LOGIC functions are tested on their own. The game itself is tested by
pressing keys (screen.press) and running frames of the game loop
(screen.run_timers), with no real window.
"""


def test_move_player_steps_and_stops_at_the_wall(load_target):
    game = load_target()
    assert game.move_player(0, 1, 20, 270) == 20, "From x=0, one step right (20) should give 20."
    assert game.move_player(0, -1, 20, 270) == -20, "From x=0, one step left (20) should give -20."
    x = game.move_player(265, 1, 20, 270)
    assert x == 270, f"From x=265, a step right would pass the wall at 270, so x should stop at 270, not {x}."


def test_is_touching_only_when_close(load_target):
    game = load_target()
    assert game.is_touching(0, 0, 10, 10, 30), "(0, 0) and (10, 10) are about 14 apart: that is touching."
    assert not game.is_touching(0, 0, 100, 0, 30), "(0, 0) and (100, 0) are 100 apart: NOT touching."


def test_arrow_keys_move_the_player_but_not_off_screen(run_target):
    result = run_target(seed=1)
    player = result.namespace["player"]
    assert result.screen.listening, "The window is not listening for keys. Add screen.listen()."
    result.screen.press("Right")
    assert player.xcor() > 0, "Pressing Right should move the player to the right."
    for _ in range(50):
        result.screen.press("Left")
    assert -300 < player.xcor() < 0, f"After 50 Left presses the player should stop at the wall, but x is {player.xcor()}."


def test_the_game_loop_keeps_the_meteors_falling(run_target):
    result = run_target(seed=2)
    meteors = result.namespace["meteors"]
    assert len(meteors) >= 2, "There should be a list of at least 2 meteors."
    start = [m.ycor() for m in meteors]
    frames = result.screen.run_timers(5)
    assert frames == 5, (
        f"The game loop ran {frames} time(s) instead of 5. At the end of game_loop(), "
        "plan the next frame with screen.ontimer(game_loop, FRAME_MS)."
    )
    assert all(m.ycor() < y for m, y in zip(meteors, start)), "Every meteor should fall a little each frame."


def test_a_hit_ends_the_game(run_target):
    result = run_target(seed=3)
    ns = result.namespace
    player, meteor = ns["player"], ns["meteors"][0]
    meteor.goto(player.xcor(), player.ycor() + 5)  # drop a meteor right on the player
    result.screen.run_timers(5)
    assert ns["state"]["running"] is False, "A meteor touching the player should end the game (is_touching)."
    texts = " ".join(t.text for tt in result.turtles for t in tt.texts)
    assert "GAME OVER" in texts, "When the game ends, write GAME OVER on the screen."
    assert not result.screen.timers, "After GAME OVER the game loop should stop (no more ontimer)."
