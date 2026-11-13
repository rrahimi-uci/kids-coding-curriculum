"""Junior Level 2 Week 1: Forever and Bounce (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/2-game-makers/teaching-material/lessons/week01.tex: the welcome back to Game Makers, the
forever freeze dance, repeat versus forever (a merry-go-round; the red stop sign is the pause button),
Exercise 1.1 Bounce Cat built step by step (point in direction 90, forever, move 10 steps: stuck at the
edge; if on edge, bounce: upside down; set rotation style left-right: fixed; the stop sign), the exit
quiz (repeat 4 or forever?), the bounce-walk wiggle break, Exercise 1.3 The Missing Hello (blocks under a
forever loop never run), and the stop plan for screen-time balance.
The kit stage does not rotate sprites, so the upside-down cat is a flipped cat drawn over the stage.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
POINT = ("motion", "point in direction [90]")
STYLE = ("motion", "set rotation style [left-right]")
MOVE = ("motion", "move [10] steps")
BOUNCE = ("motion", "if on edge, bounce")
SAY = ("looks", "say [Watch me!] for [2] seconds")
MEOW = ("sound", "start sound [Meow]")
BIG = 1.25  # block scale: big enough for young eyes
CAT = 1.0  # cat size on the stage
EDGE = 190  # how far the cat walks from the middle before it touches an edge (stage steps)

# The build stage: x=1080, y=240, w=760, h=500, so one stage step is 760 / 480 screen pixels.
SX, SY, SW, SH = 1080, 240, 760, 500
_K = SW / 480
FEET = SY + SH / 2 + 50  # where the stage draws the cat's feet
UPSIDE_Y = FEET - 214 * CAT  # a cat flipped upside down hangs from here


def _screen_x(steps):
    return SX + SW / 2 + steps * _K


def bounce_actions(t0, legs, leg=1.6):
    """Stage actions: from the middle, walk to the right edge, then bounce back and forth `legs` times."""
    acts = [(f"{t0}", "move", EDGE, leg / 2)]
    for i in range(legs):
        start = f"{t0}+{leg / 2 + i * leg:.2f}"
        acts.append((start, "turn", 180, 0.05))
        acts.append((start, "move", 2 * EDGE, leg))
    return acts


EPISODE = Episode(level="j2", week=1, scenes=(
    # 1. welcome back to Game Makers ---------------------------------------------------------------
    Scene("j2-w01-s01", setting="workshop", lead_in=0.3, beats=(
        B("Welcome back, coders! It's me, Aiden, and my robot friend, Pixi.", speaker=AIDEN, cue="hi",
          pause=0.3),
        B("Beep boop! We missed you!", speaker=PIXI, cue="missed", pause=0.5),
        B("In Level one, you were Little Robots. You made animations and greeting cards.", speaker=AIDEN,
          cue="level1", pause=0.5),
        B("Now, in Level two, you are Game Makers!", speaker=AIDEN, cue="level2", pause=0.5),
        B("By week ten, you will make your own arcade game and let other people play it.", speaker=AIDEN,
          cue="arcade", pause=0.5),
        B("Today, we make a cat that bounces, and bounces, and bounces. Let's go!", speaker=AIDEN, cue="today",
          pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "missed"), ("today", "end")],
          moods={"start": "happy", "level2": "proud"}),
        A("pixi", x=640, y=760, drop=True),
        A("chip", "Level 1: Little Robots", at="level1", until="level2", x=1300, y=420, color="sky", size=44),
        A("bigtext", "Game Makers!", at="level2", until="today", x=1300, y=480, size=96, color="orange"),
        A("icons", at="arcade", until="today", x=1300, y=680, gap=280,
          items=[("game", "My own arcade game", "arcade@0.3"), ("trophy", "Week 10 showcase", "arcade@0.6")]),
        A("banner", "MISSION: Make the cat bounce forever", at="today"),
        A("stage", x=1000, y=410, w=760, h=460, at="today", flag=False, sprite_scale=CAT,
          actions=bounce_actions("today@0.3", 2, 1.2)),
    )),
    # 2. warm-up: the forever freeze dance ---------------------------------------------------------
    Scene("j2-w01-s02", setting="workshop", beats=(
        B("Let's warm up with a freeze dance. Stand up!", speaker=AIDEN, cue="stand", pause=0.4),
        B("When the music plays, you dance. You keep dancing and dancing, until the music stops.",
          speaker=AIDEN, cue="rule", pause=0.5),
        B("Pixi has the pause button. Music, please!", speaker=AIDEN, cue="music", pause=3.4),
        B("Freeze!", speaker=PIXI, cue="freeze", pause=1.6),
        B("Who decided when we stopped? Us, or Pixi?", speaker=AIDEN, cue="who", pause=2.8),
        B("Pixi did, with the pause button!", speaker=AIDEN, cue="pixi", pause=0.5),
        B("That was a forever dance. It did not stop after four moves, like a repeat four. It kept going until "
          "someone pressed stop.", speaker=AIDEN, cue="forever", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("music@0.4", "freeze")],
          moods={"start": "happy", "freeze": "surprised", "who": "thinking", "pixi": "happy"},
          chin=("who", "pixi"),
          path=[("music@0.4", 300, 960), ("music$+0.4", 350, 960), ("music$+1.2", 260, 960),
                ("music$+2.0", 350, 960), ("freeze", 300, 960)]),
        A("pixi", x=640, y=760, moods={"freeze": "proud"}, beep=("freeze", "freeze$")),
        A("chip", "music on = dance", at="rule", until="freeze", x=1300, y=420, color="green", size=46),
        A("icons", at="music@0.4", until="freeze", x=1300, y=600, items=[("music", "Dance, dance, dance!")]),
        A("sfx", "sparkle", at="music@0.6"),
        A("bigtext", "FREEZE!", at="freeze", until="who", x=1300, y=500, size=110, color="blue"),
        A("thought", "Who stopped us?", at="who$+0.2", until="pixi", x=1300, y=500),
        A("chip", "the pause button stops it", at="pixi", until="forever", x=1300, y=500, color="red", size=44),
        A("chip", "a forever dance", at="forever", x=1300, y=440, color="orange", size=48),
        A("chip", "stops only when someone presses stop", at="forever@0.6", x=1300, y=560, color="sky", size=36),
    )),
    # 3. repeat or forever ---------------------------------------------------------------------------
    Scene("j2-w01-s03", setting="sky", beats=(
        B("Games keep going. The apple keeps falling. The ghost keeps flying.", speaker=AIDEN, cue="games",
          pause=0.5),
        B("In Level one we had repeat. It does the steps a number of times, then it stops.", speaker=AIDEN,
          cue="repeat", pause=0.6),
        B("Today we meet forever. A forever loop does the steps inside it again and again, and never stops by "
          "itself.", speaker=AIDEN, cue="forever", pause=0.6),
        B("It is like a merry-go-round. It does not count the turns. It keeps going until someone presses stop.",
          speaker=AIDEN, cue="merry", pause=0.6),
        B("In Scratch, the red stop sign is our pause button.", speaker=AIDEN, cue="stop", pause=0.4),
        B("Forever is in the orange Control circle, next to repeat.", speaker=AIDEN, cue="orange", pause=0.8),
    ), actions=(
        A("stage", x=580, y=260, w=760, h=500, at="games", until="repeat", flag=False, sprite="apple",
          sprite_scale=1.2, sprite_x=-120, sprite_y=150, extra=[("ghost", 140, 40)],
          actions=[("games+0.3", "goto", -120, -150, 1.2), ("games+1.5", "goto", -120, 150, 0.05),
                   ("games+1.6", "goto", -120, -150, 1.2), ("games+2.8", "goto", -120, 150, 0.05),
                   ("games+2.9", "goto", -120, -150, 1.2), ("games+4.1", "goto", -120, 150, 0.05),
                   ("games+4.2", "goto", -120, -150, 1.2)]),
        A("scratch", "Repeat", blocks=[("control", "repeat [4]", [MOVE])], x=180, y=300, w=760, h=330,
          scale=BIG, at="repeat"),
        A("chip", "4 times, then stop", at="repeat@0.6", x=500, y=740, color="sky", size=44),
        A("scratch", "Forever", blocks=[("control", "forever", [MOVE])], x=1060, y=300, w=760, h=330,
          scale=BIG, at="forever"),
        A("chip", "again and again", at="forever@0.6", x=1400, y=740, color="orange", size=44),
        A("chip", "merry-go-round!", at="merry", until="stop", x=960, y=880, color="purple", size=46),
        A("chip", "red stop sign = pause button", at="stop", until="orange", x=960, y=880, color="red", size=42),
        A("chip", "Control: orange", at="orange", x=960, y=880, color="orange", size=46),
    )),
    # 4. Bounce Cat: forever and move --------------------------------------------------------------
    Scene("j2-w01-s04", setting="mint", beats=(
        B("Let's build Bounce Cat together.", speaker=AIDEN, cue="build", pause=0.4),
        B("Yellow Events: when green flag clicked.", speaker=AIDEN, cue="events", pause=0.5),
        B("Blue Motion: point in direction ninety. Ninety means facing right, like in Level one.", speaker=AIDEN,
          cue="point", pause=0.6),
        B("Orange Control: forever. Look at its flat bottom. No bump! Nothing can go after forever.",
          speaker=AIDEN, cue="forever", pause=0.6),
        B("Blue Motion: put move ten steps inside the forever. Click the flag!", speaker=AIDEN, cue="move",
          pause=2.4),
        B("The cat runs to the edge and gets stuck there, running on the spot.", speaker=AIDEN, cue="stuck",
          pause=0.5),
        B("Click the red stop sign.", speaker=AIDEN, cue="stop", pause=0.8),
    ), actions=(
        A("banner", "Exercise 1.1: Bounce Cat", at="build", color="green"),
        A("scratch", "Bounce Cat", blocks=[FLAG, POINT, ("control", "forever", [MOVE])], x=140, y=260, w=880,
          h=560, scale=BIG, reveal=["events", "point", "forever", "move"],
          highlight=[(2, "forever@0.4", "forever$")]),
        A("chip", "no bump at the bottom", at="forever@0.4", until="move", x=1460, y=860, color="orange", size=42),
        A("chip", "Motion: blue", at="point", until="forever", x=1460, y=860, color="sky", size=44),
        A("stage", x=SX, y=SY, w=SW, h=SH, at="build", flag_at="move$", sprite_scale=CAT,
          actions=[("move$+0.2", "move", EDGE, 1.4), ("stuck", "move", 6, 0.2), ("stuck+0.3", "move", -6, 0.2),
                   ("stuck+0.6", "move", 6, 0.2), ("stuck+0.9", "move", -6, 0.2), ("stuck+1.2", "move", 6, 0.2),
                   ("stuck+1.5", "move", -6, 0.2)]),
        A("chip", "stuck at the edge!", at="stuck", until="stop", x=1460, y=860, color="red", size=44),
        A("chip", "STOP", at="stop", x=1460, y=860, color="red", size=56),
        A("sfx", "pop", at="stop@0.5"),
    )),
    # 5. bounce, and an upside-down cat ------------------------------------------------------------
    Scene("j2-w01-s05", setting="mint", beats=(
        B("Blue Motion again: put if on edge, bounce inside the forever, under the move.", speaker=AIDEN,
          cue="bounce", pause=0.6),
        B("A bounce is like a ball hitting a wall. It turns around and comes back. Click the flag!",
          speaker=AIDEN, cue="ball", pause=0.2),
        B("It bounces from side to side!", speaker=AIDEN, cue="sides", pause=0.6),
        B("But wait. Look at the cat when it walks left.", speaker=AIDEN, cue="left", pause=1.4),
        B("It is upside down!", speaker=AIDEN, cue="upside", pause=1.2),
        B("Ha ha! A topsy-turvy cat!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("scratch", "Bounce Cat", blocks=[FLAG, POINT, ("control", "forever", [MOVE, BOUNCE])], x=140, y=260,
          w=880, h=620, scale=BIG, reveal=["start", "start", "start", "start", "bounce@0.5"],
          highlight=[(4, "bounce@0.5", "ball$")]),
        A("stage", x=SX, y=SY, w=SW, h=SH, at="start", flag_at="ball$-0.4", sprite_scale=CAT, sprite_x=EDGE,
          actions=[("start", "goto", 0, 0, 0.6),
                   ("ball$", "move", EDGE, 1.0), ("ball$+1.0", "hide"),
                   ("ball$+1.0", "goto", -EDGE, 0, 0.05), ("ball$+3.0", "show"),
                   ("ball$+3.0", "move", 2 * EDGE, 2.0), ("ball$+5.0", "hide"),
                   ("ball$+5.0", "goto", -EDGE, 0, 0.05), ("ball$+7.0", "show"),
                   ("ball$+7.0", "move", 2 * EDGE, 2.0), ("ball$+9.0", "hide")]),
        A("cat", x=_screen_x(EDGE), y=UPSIDE_Y, s=-CAT, at="ball$+1.0", until="ball$+2.95",
          path=[("ball$+1.0", _screen_x(EDGE), UPSIDE_Y), ("ball$+3.0", _screen_x(-EDGE), UPSIDE_Y)]),
        A("cat", x=_screen_x(EDGE), y=UPSIDE_Y, s=-CAT, at="ball$+5.0", until="ball$+6.95",
          path=[("ball$+5.0", _screen_x(EDGE), UPSIDE_Y), ("ball$+7.0", _screen_x(-EDGE), UPSIDE_Y)]),
        A("cat", x=_screen_x(EDGE), y=UPSIDE_Y, s=-CAT, at="ball$+9.0", until="end",
          path=[("ball$+9.0", _screen_x(EDGE), UPSIDE_Y), ("ball$+11.0", _screen_x(-EDGE), UPSIDE_Y)]),
        A("chip", "bounce = turn around at the edge", at="ball", until="left", x=1460, y=860, color="sky",
          size=38),
        A("chip", "upside down!", at="upside", x=1460, y=860, color="red", size=48),
    )),
    # 6. rotation style left-right ------------------------------------------------------------------
    Scene("j2-w01-s06", setting="mint", beats=(
        B("Let's fix it. Blue Motion: snap set rotation style left-right above the forever.", speaker=AIDEN,
          cue="style", pause=0.6),
        B("Click point in direction ninety once, to turn the cat the right way up. Then click the flag.",
          speaker=AIDEN, cue="flag", pause=2.6),
        B("Now the cat turns to face the way it walks!", speaker=AIDEN, cue="faces", pause=1.6),
        B("Click the red stop sign. Who stopped the cat?", speaker=AIDEN, cue="stop", pause=2.0),
        B("We did! Forever only stops when we press stop.", speaker=AIDEN, cue="we", pause=0.5),
        B("Bouncy, bouncy, beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("scratch", "Bounce Cat", blocks=[FLAG, POINT, STYLE, ("control", "forever", [MOVE, BOUNCE])], x=140,
          y=240, w=880, h=780, scale=1.1, reveal=["start", "start", "style@0.6", "start", "start", "start"],
          highlight=[(2, "style@0.6", "faces$")]),
        A("stage", x=SX, y=SY, w=SW, h=SH, at="start", flag_at="flag$-0.6", sprite_scale=CAT, sprite_x=-EDGE,
          actions=[("flag@0.3", "goto", 0, 0, 0.8), ("flag$", "move", EDGE, 0.9),
                   ("flag$+0.9", "turn", 180, 0.05), ("flag$+0.9", "move", 2 * EDGE, 1.8),
                   ("flag$+2.7", "turn", 180, 0.05), ("flag$+2.7", "move", 2 * EDGE, 1.8),
                   ("flag$+4.5", "turn", 180, 0.05), ("flag$+4.5", "move", EDGE, 0.9)]),
        A("chip", "rotation style: left-right", at="style@0.6", until="stop", x=1460, y=860, color="sky",
          size=40),
        A("chip", "STOP", at="stop@0.4", until="we", x=1460, y=860, color="red", size=56),
        A("chip", "We are the stop sign!", at="we", x=1460, y=860, color="green", size=44),
        A("badge", ok=True, at="faces", x=1760, y=300),
        A("confetti", at="we", x=1460, y=480),
    )),
    # 7. quick quiz: repeat 4 or forever? -----------------------------------------------------------
    Scene("j2-w01-s07", setting="peach", beats=(
        B("Quick quiz!", speaker=AIDEN, cue="quiz", pause=0.4),
        B("I want the Ballerina to dance until I press stop. Do I use repeat four, or forever?", speaker=AIDEN,
          cue="which", pause=3.2),
        B("Forever! A repeat four stops by itself after four times.", speaker=AIDEN, cue="answer", pause=0.5),
        B("Forever keeps going until someone presses stop.", speaker=AIDEN, cue="keeps", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("scratch", "A", blocks=[("control", "repeat [4]", [("looks", "next costume")])], x=200, y=330, w=720,
          h=330, scale=BIG, at="which@0.4", highlight=[(0, "answer@0.4", "keeps")]),
        A("scratch", "B", blocks=[("control", "forever", [("looks", "next costume")])], x=1080, y=330, w=720,
          h=330, scale=BIG, at="which@0.6", highlight=[(0, "answer", "end")]),
        A("thought", "Repeat or forever?", at="which$+0.2", until="answer", x=960, y=820),
        A("chip", "repeat 4: stops by itself", at="answer@0.4", x=520, y=820, color="sky", size=40),
        A("chip", "forever: until you press stop", at="keeps", x=1400, y=820, color="orange", size=40),
        A("badge", ok=True, at="answer", x=1760, y=300),
    )),
    # 8. wiggle break: the bounce walk --------------------------------------------------------------
    Scene("j2-w01-s08", setting="workshop", beats=(
        B("Wiggle break! Let's do a bounce walk.", speaker=AIDEN, cue="walk", pause=0.4),
        B("Stand at one side of the room. Walk forward slowly. You are moving ten steps, forever.",
          speaker=AIDEN, cue="forward", pause=1.2),
        B("When you touch a wall, bounce! Turn around and walk back.", speaker=AIDEN, cue="wall", pause=3.0),
        B("Stop!", speaker=PIXI, cue="stop", pause=1.0),
        B("Pixi was our stop sign!", speaker=AIDEN, cue="sign", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "stop": "surprised", "sign": "happy"},
          path=[("forward", 300, 960), ("forward$+1.0", 760, 960), ("wall@0.4", 760, 960), ("wall$+2.4", 300, 960)]),
        A("pixi", x=1680, y=760, beep=("stop", "stop$"), moods={"stop": "proud"}),
        A("bigtext", "Bounce walk!", at="walk", until="stop", x=1240, y=440, size=90, color="green"),
        A("chip", "touch a wall: bounce!", at="wall", until="stop", x=1240, y=580, color="sky", size=44),
        A("bigtext", "STOP!", at="stop", x=1240, y=480, size=110, color="red"),
    )),
    # 9. bug hunt: the Missing Hello ----------------------------------------------------------------
    Scene("j2-w01-s09", setting="mint", beats=(
        B("Uh oh. Time for a bug hunt!", speaker=AIDEN, cue="bug", pause=0.5),
        B("Kai wants the cat to say Watch me, meow, and then bounce forever.", speaker=AIDEN, cue="kai",
          pause=0.5),
        B("He clicks the flag. The cat bounces, but it never talks, and it never meows.", speaker=AIDEN,
          cue="never", pause=1.0),
        B("Look at where Kai put the say and sound blocks. Why do they never run?", speaker=AIDEN, cue="why",
          pause=3.2),
        B("They are under the forever loop. Forever has a flat bottom, so they cannot snap on.", speaker=AIDEN,
          cue="under", pause=0.5),
        B("And the loop never ends, so their turn never comes.", speaker=AIDEN, cue="turn", pause=0.5),
        B("It is like: dance until the music stops, and then eat a cookie. But the music never stops. No cookie!",
          speaker=AIDEN, cue="cookie", pause=0.6),
        B("The fix: drag them up, between when green flag clicked and the forever.", speaker=AIDEN, cue="fix",
          pause=0.8),
        B("Test it again.", speaker=AIDEN, cue="test", pause=3.4),
        B("Watch me! Meow! Then it bounces. We fixed the bug!", speaker=AIDEN, cue="fixed", pause=0.4),
        B("Bug squashed!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The Missing Hello", at="bug", color="navy"),
        A("scratch", "Kai's script", blocks=[FLAG, ("control", "forever", [MOVE, BOUNCE])], x=140, y=250, w=880,
          h=460, scale=BIG, at="kai", until="fix+0.4", highlight=[(1, "under", "under@0.6")]),
        A("scratch", blocks=[SAY, MEOW], x=200, y=790, w=700, h=200, panel=False, scale=BIG, at="kai",
          until="fix+0.4", highlight=[(0, "why", "fix"), (1, "why", "fix")]),
        A("scratch", "Kai's script (fixed)", blocks=[FLAG, SAY, MEOW, ("control", "forever", [MOVE, BOUNCE])],
          x=140, y=250, w=880, h=770, scale=1.1, at="fix+0.4", highlight=[(1, "fix+0.4", "fix+1.6"),
                                                                          (2, "fix+0.4", "fix+1.6")]),
        A("sfx", "snap", at="fix+0.4"),
        A("stage", x=SX, y=SY, w=SW, h=SH, at="kai", flag_at="never@0.1", sprite_scale=CAT,
          actions=[("never@0.2", "move", EDGE, 1.0), ("never@0.2+1.0", "turn", 180, 0.05),
                   ("never@0.2+1.0", "move", 2 * EDGE, 2.0), ("never@0.2+3.0", "turn", 180, 0.05),
                   ("never@0.2+3.0", "move", EDGE, 1.0),
                   ("test", "say", "Watch me!", 2.0), ("test+2.2", "move", EDGE, 1.0)]),
        A("sfx", "pop", at="test+2.0"),
        A("badge", ok=False, at="never@0.6", until="test", x=1760, y=310),
        A("thought", "Why never?", at="why$+0.2", until="under", x=1460, y=870),
        A("chip", "under forever = never runs", at="under", until="cookie", x=1460, y=870, color="red", size=40),
        A("chip", "No cookie!", at="cookie@0.7", until="test", x=1460, y=870, color="orange", size=48),
        A("badge", ok=True, at="fixed", x=1760, y=310),
        A("confetti", at="fixed", x=1460, y=480),
    )),
    # 10. the stop plan -------------------------------------------------------------------------------
    Scene("j2-w01-s10", setting="workshop", beats=(
        B("A forever loop never stops by itself.", speaker=AIDEN, cue="loop", pause=0.4),
        B("Lots of games and videos are made like that too. They keep going and going.", speaker=AIDEN,
          cue="games", pause=0.5),
        B("So it is up to us to press stop. You are the stop sign!", speaker=AIDEN, cue="us", pause=0.6),
        B("When the timer rings, we finish our sentence, save, and stand up.", speaker=AIDEN, cue="timer",
          pause=0.6),
        B("What is your stop plan at home? When the timer rings, I will...", speaker=AIDEN, cue="plan",
          pause=3.0),
        B("Press stop, save, and go and play outside. Great plan!", speaker=AIDEN, cue="great", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"plan": "thinking", "great": "proud"}, chin=("plan", "great")),
        A("pixi", x=600, y=760, moods={"great": "happy"}),
        A("banner", "My stop plan", at="loop", color="green"),
        A("icons", at="timer", until="end", x=1280, y=540, gap=270,
          items=[("clock", "Timer rings", "timer"), ("file", "Save", "timer@0.5"), ("person", "Stand up", "timer@0.8")]),
        A("chip", "You are the stop sign!", at="us", until="timer", x=1280, y=540, color="red", size=46),
        A("thought", "My stop plan?", at="plan$+0.2", until="great", x=1280, y=860),
        A("chip", "stop, save, play outside!", at="great", x=1280, y=860, color="green", size=44),
    )),
    # 11. recap and next -------------------------------------------------------------------------------
    Scene("j2-w01-s11", setting="workshop", tail=0.8, beats=(
        B("Say the new words with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Forever!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Bounce!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Stop!", speaker=AIDEN, cue="w3", pause=1.2),
        B("A repeat stops by itself. A forever loop keeps going until you press stop.", speaker=AIDEN,
          cue="recap", pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Build Bounce Cat, then Dance Forever, then fix the Missing Hello.", speaker=AIDEN, cue="next",
          pause=0.6),
        B("Save your game in the Game Makers folder, with your nickname.", speaker=AIDEN, cue="save", pause=0.5),
        B("See you next week, Game Makers. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Forever!", at="w1", until="w1>", y=560, size=90, color="orange"),
        A("bigtext", "Bounce!", at="w2", until="w2>", y=560, size=90, color="blue"),
        A("bigtext", "Stop!", at="w3", until="w3>", y=560, size=90, color="red"),
        A("chip", "repeat stops • forever keeps going", at="recap", until="turn", x=1200, y=560, color="orange",
          size=42),
        A("banner", "NEXT: Forever and Bounce", at="turn", color="green"),
        A("cards", items=["Build Bounce Cat", "Dance Forever", "Fix the Missing Hello"], x=1000, y=300, w=640,
          gap=120, reveal=["next@0.1", "next@0.45", "next@0.8"], at="next"),
        A("chip", "Save: Game Makers folder", at="save", x=1320, y=760, color="sky", size=42),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
