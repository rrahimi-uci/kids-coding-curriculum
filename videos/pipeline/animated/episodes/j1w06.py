"""Junior Level 1 Week 6: When I Click... (kit episode, Aiden and Pixi, Grades 2-3).

Follows junior/1-little-robots/teaching-material/lessons/week06.tex: the "when I clap, you jump" warm-up
(event cards, each robot listens for its own card, nobody listens for banana), events start scripts
(the green flag, a click on a sprite, a key) with hat-shaped blocks in yellow Events, the doorbell
analogy, the worked example Exercise 6.1 Click the Cat ("That tickles!") and the space-key script
with next costume, a quick quiz (does the green flag start a click script?), Exercise 6.3 The Mixed-Up
Ballerina (bug hunt: the script under the wrong sprite, and the wrong key), nicknames and never real
names or photos, and the recap.
Kit notes: the stage has one sprite and no costumes, so the bug hunt shows the cat and Pixi (as the
Ballerina, like week 4) on the floor with the selected sprite named under the code, and the space-key
costume change is shown as a little step with a "next costume" chip.
"""

from ..kit_dsl import A, AIDEN, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
CLICKED = ("event", "when this sprite clicked")
SPACE = ("event", "when [space] key pressed")
KEY_A = ("event", "when [a] key pressed")
MEOW = ("sound", "play sound [Meow] until done")
TICKLE = ("looks", "say [That tickles!] for [2] seconds")
NEXT = ("looks", "next costume")
WAIT = ("control", "wait [1] seconds")
SAYHI = ("looks", "say [Hi!] for [2] seconds")
DANCE = ("control", "repeat [4]", [NEXT, WAIT])
BIG = 1.25  # block scale: big enough for young eyes
CAT = 1.0  # cat size on the stage

# bug hunt floor: the cat and Pixi playing the Ballerina
CX, CY = 1330, 920
PX, PY = 1640, 760
POSES = ["surprised", "proud", "happy", "thinking"]


def hop(base: str, x: float, y: float, times: int, every: float, first: float = 0.3, moods: bool = False):
    """Little hops (dance moves or steps) keyed on `base`: (path, moods)."""
    path, mood = [(base, x, y)], {}
    for i in range(times):
        t = first + i * every
        dx = 40 if i % 2 == 0 else -40
        path += [(f"{base}+{t:.2f}", x + dx, y - 40), (f"{base}+{t + 0.45:.2f}", x, y)]
        if moods:
            mood[f"{base}+{t:.2f}"] = POSES[i % 4]
    return path, mood


S10_PATH, S10_MOODS = hop("space2", PX, PY, 4, 1.0, first=0.6, moods=True)

EPISODE = Episode(level="j1", week=6, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j1-w06-s01", setting="workshop", lead_in=0.3, beats=(
        B("Hi, coders! It's Aiden and Pixi!", speaker=AIDEN, cue="hi", pause=0.3),
        B("Beep boop! Hello!", speaker=PIXI, cue="hello", pause=0.5),
        B("So far, every script we made starts with the green flag.", speaker=AIDEN, cue="sofar", pause=0.5),
        B("Today, we learn two new ways to start a script: a click on a sprite, and a key on the keyboard!",
          speaker=AIDEN, cue="today", pause=0.5),
        B("Click the cat, and it talks. Press a key, and it moves. Let's go!", speaker=AIDEN, cue="go", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "hello"), ("go", "end")],
          moods={"start": "happy", "today": "proud"}),
        A("pixi", x=640, y=760, drop=True),
        A("scratch", blocks=[FLAG], x=1080, y=300, w=600, h=150, panel=False, scale=BIG, at="sofar",
          until="today"),
        A("icons", at="today", x=1320, y=430, gap=320,
          items=[("person", "A click", "today@0.5"), ("key", "A key", "today@0.8")]),
        A("banner", "MISSION: Make the cat listen", at="go"),
        A("cat", x=1500, y=960, s=0.8, at="go", talk=("go@0.2", "go@0.5")),
    )),
    # 2. warm-up: when I clap, you jump (movement) ---------------------------------------------------
    Scene("j1-w06-s02", setting="workshop", beats=(
        B("Let's warm up with a game. Stand up!", speaker=AIDEN, cue="up", pause=0.4),
        B("This card is a little script. The top part says WHEN. The robot waits until that thing happens.",
          speaker=AIDEN, cue="card", pause=0.6),
        B("When I clap, you jump. When I stomp, you spin. Ready?", speaker=AIDEN, cue="rules", pause=0.8),
        B("Clap!", speaker=AIDEN, cue="clap1", pause=1.4),
        B("Stomp!", speaker=AIDEN, cue="stomp1", pause=1.6),
        B("Clap!", speaker=AIDEN, cue="clap2", pause=1.4),
        B("You listened, and did the right action. Great robots!", speaker=AIDEN, cue="great", pause=0.8),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("clap1", "clap1>"), ("stomp1", "stomp1>"), ("clap2", "clap2>")],
          moods={"start": "happy", "great": "proud"}),
        A("pixi", x=520, y=860, s=0.62, ground=1000, moods={"clap1": "surprised", "stomp1": "happy",
                                                             "clap2": "surprised", "great": "proud"},
          path=[("clap1", 520, 860), ("clap1+0.4", 520, 780), ("clap1+0.9", 520, 860),
                ("stomp1", 520, 860), ("stomp1+0.4", 580, 860), ("stomp1+0.8", 460, 860), ("stomp1+1.2", 520, 860),
                ("clap2", 520, 860), ("clap2+0.4", 520, 780), ("clap2+0.9", 520, 860)]),
        A("cards", items=["When I CLAP: jump", "When I STOMP: spin"], x=820, y=300, w=640, gap=140, size=44,
          at="card", reveal=["card@0.2", "rules@0.4"],
          active=[[("clap1", "clap1>"), ("clap2", "clap2>")], ("stomp1", "stomp1>"), ]),
        A("bigtext", "CLAP!", at="clap1", until="clap1>", x=1140, y=720, size=90, color="orange"),
        A("bigtext", "STOMP!", at="stomp1", until="stomp1>", x=1140, y=720, size=90, color="purple"),
        A("bigtext", "CLAP!", at="clap2", until="clap2>", x=1140, y=720, size=90, color="orange"),
    )),
    # 3. each robot has its own cards; banana -------------------------------------------------------
    Scene("j1-w06-s03", setting="workshop", beats=(
        B("Now each robot gets its own card. Ada only listens for the clap. Sam only listens for the stomp.",
          speaker=AIDEN, cue="own", pause=0.6),
        B("Clap! Only Ada jumps. Each robot has its own scripts.", speaker=AIDEN, cue="clap", pause=0.6),
        B("Last one. Banana!", speaker=AIDEN, cue="banana", pause=1.0),
        B("What happens?", speaker=AIDEN, cue="what", pause=3.0),
        B("Nothing! No card listens for banana, so nothing happens. Remember that!", speaker=AIDEN,
          cue="nothing", pause=0.8),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, moods={"start": "happy", "what": "thinking", "nothing": "happy"},
          chin=("what", "nothing")),
        A("pixi", x=520, y=860, s=0.62, ground=1000, moods={"banana": "confused", "nothing": "happy"}),
        A("icons", x=1220, y=420, gap=420,
          items=[("person", "Ada: CLAP → jump", "own@0.3"), ("person", "Sam: STOMP → spin", "own@0.6")]),
        A("chip", "Ada jumps!", at="clap@0.3", until="banana", x=1010, y=720, color="green", size=46),
        A("chip", "Sam waits", at="clap@0.5", until="banana", x=1430, y=720, color="white", size=46),
        A("bigtext", "BANANA!", at="banana", until="what", x=1220, y=760, size=84, color="orange"),
        A("thought", "Who moves?", at="what$+0.2", until="nothing", x=1220, y=760),
        A("chip", "No card for banana: nothing happens", at="nothing", x=1220, y=760, color="yellow", size=40),
    )),
    # 4. events start scripts ----------------------------------------------------------------------------
    Scene("j1-w06-s04", setting="lavender", beats=(
        B("In our game, the clap was an event. An event is something that happens.", speaker=AIDEN, cue="event",
          pause=0.5),
        B("In Scratch, events start scripts. We already know one: the green flag.", speaker=AIDEN, cue="flag",
          pause=0.5),
        B("Today, we learn two more: when this sprite clicked, and when space key pressed.", speaker=AIDEN,
          cue="two", pause=0.6),
        B("They are all in the yellow Events circle, and they all have a round top, like a hat.", speaker=AIDEN,
          cue="hat", pause=0.6),
        B("It's like a doorbell. When the doorbell rings, someone goes to the door. Nobody goes when the "
          "phone rings.", speaker=AIDEN, cue="door", pause=0.5),
        B("An event block waits, and runs only when its own event happens.", speaker=AIDEN, cue="waits",
          pause=0.8),
    ), actions=(
        A("chip", "event = something that happens", at="event@0.5", until="door", x=1400, y=300, color="yellow",
          size=42),
        A("scratch", blocks=[FLAG], x=200, y=290, w=700, h=150, panel=False, scale=BIG, at="flag@0.5"),
        A("scratch", blocks=[CLICKED], x=200, y=500, w=700, h=150, panel=False, scale=BIG, at="two@0.4"),
        A("scratch", blocks=[SPACE], x=200, y=710, w=700, h=150, panel=False, scale=BIG, at="two@0.75"),
        A("chip", "Events: yellow, round top like a hat", at="hat", until="door", x=1400, y=460,
          color="yellow", size=38),
        A("door", "Ding dong!", x=1400, y=900, s=0.9, at="door", open="door@0.5"),
        A("chip", "It waits for its own event", at="waits", x=1400, y=300, color="orange", size=44),
    )),
    # 5. build Click the Cat ---------------------------------------------------------------------------
    Scene("j1-w06-s05", setting="mint", beats=(
        B("Let's build Click the Cat.", speaker=AIDEN, cue="build", pause=0.4),
        B("Click the yellow Events circle. Drag in: when this sprite clicked.", speaker=AIDEN, cue="events",
          pause=0.8),
        B("Then the pink Sound circle. Snap on: play sound Meow until done.", speaker=AIDEN, cue="sound",
          pause=0.8),
        B("Then the purple Looks circle. Snap on: say Hello for two seconds, and type: That tickles!",
          speaker=AIDEN, cue="looks", pause=0.8),
        B("Look: no green flag block this time!", speaker=AIDEN, cue="noflag", pause=0.8),
    ), actions=(
        A("banner", "Exercise 6.1: Click the Cat", at="build", color="green"),
        A("scratch", "Click the Cat", blocks=[CLICKED, MEOW, ("looks", "say [Hello!] for [2] seconds")], x=110,
          y=280, w=960, h=480, scale=BIG, reveal=["events", "sound", "looks"],
          edits=[("looks@0.85", 2, "say [That tickles!] for [2] seconds")], highlight=[(0, "noflag", "end")]),
        A("chip", "Events: yellow", at="events", until="events>", x=1460, y=560, color="yellow", size=46),
        A("chip", "Sound: pink", at="sound", until="sound>", x=1460, y=560, color="pink", size=46),
        A("chip", "Looks: purple", at="looks", until="looks>", x=1460, y=560, color="purple", size=46),
        A("chip", "No green flag!", at="noflag", x=1460, y=560, color="orange", size=50),
    )),
    # 6. test it: click the cat -----------------------------------------------------------------------
    Scene("j1-w06-s06", setting="mint", beats=(
        B("Now, do not click the green flag. Click the cat on the stage!", speaker=AIDEN, cue="click", pause=3.4),
        B("Meow! That tickles!", speaker=AIDEN, cue="tickles", pause=0.5),
        B("The script waited for its event: a click on the cat.", speaker=AIDEN, cue="waited", pause=0.6),
        B("Click quickly. If you hold the mouse down and move, you drag the cat instead.", speaker=AIDEN,
          cue="quick", pause=0.8),
        B("Hee hee! Beep!", speaker=PIXI, cue="hee", pause=0.8),
    ), actions=(
        A("scratch", "Click the Cat", blocks=[CLICKED, MEOW, TICKLE], x=110, y=280, w=960, h=480, scale=BIG,
          highlight=[(0, "click+1.6", "click+1.9"), (1, "click+1.8", "click+2.8"), (2, "click+2.8", "click+4.6")]),
        A("stage", x=1100, y=230, w=700, h=480, sprite_scale=CAT,
          actions=[("click+1.8", "say", "Meow!", 1.0), ("click+2.8", "say", "That tickles!", 2.0)]),
        A("pointer", x=1650, y=650, at="click@0.4",
          path=[("click@0.4", 1650, 650), ("click+1.5", 1470, 480), ("click+1.8", 1470, 490),
                ("click+2.1", 1470, 480), ("quick", 1470, 480), ("quick+0.8", 1600, 560)]),
        A("sfx", "pop", at="click+1.6"),
        A("chip", "Click the cat!", at="click@0.5", until="tickles", x=1450, y=860, color="orange", size=48),
        A("chip", "It waited for a click", at="waited", until="quick", x=1450, y=860, color="green", size=46),
        A("chip", "Click quickly, don't drag", at="quick", x=1450, y=860, color="sky", size=44),
        A("pixi", x=1810, y=880, s=0.45, at="hee", ground=960),
    )),
    # 7. quick quiz: will the green flag start it? --------------------------------------------------
    Scene("j1-w06-s07", setting="peach", beats=(
        B("Quick quiz!", speaker=AIDEN, cue="quiz", pause=0.4),
        B("If we click the green flag, will the cat say: That tickles?", speaker=AIDEN, cue="flag", pause=3.2),
        B("Let's test it.", speaker=AIDEN, cue="test", pause=2.0),
        B("No! This script does not wait for the flag. It waits for a click on the cat.", speaker=AIDEN, cue="no",
          pause=0.5),
        B("Every hat block waits for its own event.", speaker=AIDEN, cue="own", pause=0.8),
    ), actions=(
        A("banner", "QUICK QUIZ", at="quiz", color="purple"),
        A("scratch", "Click the Cat", blocks=[CLICKED, MEOW, TICKLE], x=110, y=280, w=960, h=480, scale=BIG,
          highlight=[(0, "no", "own$")]),
        A("stage", x=1100, y=230, w=700, h=480, flag_at="test+0.4", sprite_scale=CAT),
        A("thought", "Flag: yes or no?", at="flag$+0.2", until="test", x=1450, y=870),
        A("chip", "Nothing happens!", at="test+1.0", until="own", x=1450, y=860, color="red", size=48),
        A("chip", "Each hat waits for its own event", at="own", x=1450, y=860, color="yellow", size=40),
    )),
    # 8. a key script --------------------------------------------------------------------------------
    Scene("j1-w06-s08", setting="sky", beats=(
        B("Now a key! From yellow Events, drag in: when space key pressed.", speaker=AIDEN, cue="key", pause=0.6),
        B("From purple Looks, snap on: next costume.", speaker=AIDEN, cue="next", pause=0.6),
        B("Click the stage once, then press the space bar, a few times.", speaker=AIDEN, cue="press", pause=4.4),
        B("Every press, the cat changes its costume, like a new pose!", speaker=AIDEN, cue="pose", pause=0.6),
        B("If a key does nothing, click once on the stage and try again.", speaker=AIDEN, cue="tip", pause=0.8),
    ), actions=(
        A("scratch", "Space key", blocks=[SPACE, NEXT], x=110, y=280, w=960, h=360, scale=BIG,
          reveal=["key@0.4", "next@0.5"],
          highlight=[(0, "press+1.4", "press+1.7"), (0, "press+2.4", "press+2.7"), (0, "press+3.4", "press+3.7")]),
        A("stage", x=1100, y=230, w=700, h=480, flag=True, sprite_scale=CAT,
          actions=[("press+1.4", "goto", 12, 8, 0.2), ("press+1.7", "goto", 12, 0, 0.2),
                   ("press+2.4", "goto", 24, 8, 0.2), ("press+2.7", "goto", 24, 0, 0.2),
                   ("press+3.4", "goto", 36, 8, 0.2), ("press+3.7", "goto", 36, 0, 0.2)]),
        *[A("chip", "space", at=f"press+{t:.1f}", until=f"press+{t + 0.6:.1f}", x=1450, y=860, color="white",
            size=52) for t in (1.4, 2.4, 3.4)],
        *[A("sfx", "tick", at=f"press+{t:.1f}") for t in (1.4, 2.4, 3.4)],
        A("chip", "next costume = a new pose", at="pose", until="tip", x=1450, y=860, color="purple", size=44),
        A("chip", "Click the stage, then press", at="tip", x=1450, y=860, color="sky", size=44),
        A("aiden", x=200, y=1080, s=0.5, moods={"start": "happy", "pose": "proud"}),
    )),
    # 9. bug hunt: The Mixed-Up Ballerina (part 1: wrong sprite) --------------------------------------
    Scene("j1-w06-s09", setting="mint", beats=(
        B("Bug hunt! Kai's plan: click the Ballerina, and she says Hi. Press space, and she dances.",
          speaker=AIDEN, cue="bug", pause=0.5),
        B("Pixi is our Ballerina again. Test! Click the Ballerina.", speaker=AIDEN, cue="test", pause=2.2),
        B("Nothing. Press space.", speaker=AIDEN, cue="space", pause=2.0),
        B("Nothing again! Two clues. Let's be detectives.", speaker=AIDEN, cue="nothing", pause=0.5),
        B("When we click a sprite in the sprite list, we see only that sprite's scripts. Let's click the cat.",
          speaker=AIDEN, cue="list", pause=0.6),
        B("Look! The click script is in the cat's code. So which sprite talks when we click it?", speaker=AIDEN,
          cue="which", pause=3.0),
        B("The cat! The script is under the wrong sprite.", speaker=AIDEN, cue="cat", pause=0.6),
        B("Fix: drag the script onto the Ballerina in the sprite list, so it copies. Then drag the cat's copy "
          "back to the blocks, to delete it.", speaker=AIDEN, cue="fix", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The Mixed-Up Ballerina", at="bug", color="navy"),
        A("scratch", "Ballerina's code", blocks=[KEY_A, DANCE], x=110, y=260, w=960, h=560, scale=BIG,
          at="test", until="list@0.6"),
        A("scratch", "Cat's code", blocks=[CLICKED, SAYHI], x=110, y=260, w=960, h=360, scale=BIG,
          at="list@0.6", until="fix@0.8", highlight=[(0, "which", "fix@0.8")]),
        A("scratch", "Ballerina's code", blocks=[CLICKED, SAYHI], x=110, y=260, w=960, h=360, scale=BIG,
          at="fix@0.8", highlight=[(0, "fix@0.8", "end")]),
        A("chip", "Selected: Ballerina", at="test", until="list@0.6", x=520, y=920, color="white", size=42),
        A("chip", "Selected: Cat", at="list@0.6", until="fix@0.8", x=520, y=920, color="white", size=42),
        A("chip", "Selected: Ballerina", at="fix@0.8", x=520, y=920, color="white", size=42),
        A("cat", x=CX, y=CY, s=0.8, talk=("cat+0.6", "cat+1.6")),
        A("pixi", x=PX, y=PY, s=0.8, label="Ballerina", moods={"nothing": "confused", "fix": "happy"}),
        A("pointer", x=1800, y=560, at="test",
          path=[("test", 1800, 560), ("test+1.4", PX, 690), ("which$", PX, 690), ("cat", CX + 20, 760)]),
        A("sfx", "pop", at="test+1.5"),
        A("chip", "space", at="space+0.4", until="space+1.2", x=1480, y=330, color="white", size=52),
        A("sfx", "tick", at="space+0.4"),
        A("badge", ok=False, at="nothing", until="cat", x=1780, y=260),
        A("thought", "Who talks?", at="which$+0.2", until="cat", x=1480, y=380),
        A("bubble", "Hi!", who="cat", x=CX, y=CY, at="cat+0.6", until="fix"),
        A("chip", "Wrong sprite!", at="cat@0.5", until="fix@0.8", x=1480, y=330, color="red", size=46),
        A("chip", "Bug 1 fixed", at="fix@0.9", x=1480, y=330, color="green", size=46),
    )),
    # 10. bug hunt part 2: the wrong key ---------------------------------------------------------------
    Scene("j1-w06-s10", setting="mint", beats=(
        B("Now the Ballerina's dance. It says: when a key pressed.", speaker=AIDEN, cue="dance", pause=0.5),
        B("We pressed space. Does any script listen for space?", speaker=AIDEN, cue="listen", pause=3.0),
        B("No! It is like banana in our game. Nobody listens for it.", speaker=AIDEN, cue="banana", pause=0.5),
        B("Fix: click the little arrow, and pick space.", speaker=AIDEN, cue="fix", pause=0.8),
        B("Test again! Click the Ballerina.", speaker=AIDEN, cue="again", pause=2.4),
        B("Press space!", speaker=AIDEN, cue="space2", pause=4.6),
        B("She says Hi, and she dances! Two bugs fixed.", speaker=AIDEN, cue="fixed", pause=0.4),
        B("I'm a dancing detective! Beep!", speaker=PIXI, cue="detective", pause=0.8),
    ), actions=(
        A("scratch", "Ballerina's code", blocks=[KEY_A, DANCE], x=110, y=260, w=960, h=560, scale=BIG,
          edits=[("fix@0.8", 0, "when [space] key pressed")],
          highlight=[(0, "dance@0.5", "fix$+0.4"), (2, "space2+0.6", "space2+1.0"), (2, "space2+1.6", "space2+2.0"),
                     (2, "space2+2.6", "space2+3.0"), (2, "space2+3.6", "space2+4.0")]),
        A("chip", "Selected: Ballerina", x=520, y=920, color="white", size=42),
        A("cat", x=CX, y=CY, s=0.8),
        A("pixi", x=PX, y=PY, s=0.8, label="Ballerina", moods={"start": "happy", **S10_MOODS, "fixed": "proud"},
          path=S10_PATH),
        A("thought", "Listening for space?", at="listen$+0.2", until="banana", x=1480, y=380),
        A("chip", "a is not space!", at="banana", until="fix@0.8", x=1480, y=330, color="red", size=46),
        A("pointer", x=1800, y=560, at="again",
          path=[("again", 1800, 560), ("again+1.0", PX, 690), ("space2", PX, 690), ("space2+0.5", 1800, 560)]),
        A("sfx", "pop", at="again+1.1"),
        A("bubble", "Hi!", who="pixi", x=PX, y=PY, at="again+1.2", until="space2"),
        A("chip", "space", at="space2+0.4", until="space2+1.2", x=1480, y=330, color="white", size=52),
        A("sfx", "tick", at="space2+0.4"),
        A("badge", ok=True, at="fixed", x=1780, y=260),
        A("confetti", at="fixed", x=1480, y=480),
        A("chip", "Two bugs fixed!", at="fixed@0.4", x=1480, y=330, color="green", size=46),
    )),
    # 11. nicknames, never real names or photos ----------------------------------------------------------
    Scene("j1-w06-s11", setting="workshop", beats=(
        B("Our sprites say nicknames, like Captain Fluff, or Zoom.", speaker=AIDEN, cue="nick", pause=0.4),
        B("Our projects never show our real names, where we live, or photos of us.", speaker=AIDEN, cue="never",
          pause=0.6),
        B("Scratch can take photos with the camera, and upload pictures. We do not use those buttons.",
          speaker=AIDEN, cue="camera", pause=0.5),
        B("Want a sprite that looks like you? Draw one, or pick one from the library.", speaker=AIDEN,
          cue="draw", pause=0.5),
        B("And if an app asks for your name or a photo, stop and ask a grown-up.", speaker=AIDEN, cue="ask",
          pause=0.6),
        B("What nickname would your sprite like?", speaker=AIDEN, cue="what", pause=3.0),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "never": "proud", "what": "thinking"},
          chin=("what$", "end")),
        A("pixi", x=620, y=760),
        A("chip", "Captain Fluff", at="nick", until="never", x=1300, y=380, color="yellow", size=48),
        A("icons", at="never", until="draw", x=1300, y=440, gap=280, crossed=[0, 1, 2],
          items=[("person", "Real name", "never@0.3"), ("house", "Where I live", "never@0.6"),
                 ("camera", "Photos", "never@0.85")]),
        A("icons", at="draw", until="what", x=1300, y=440, gap=320,
          items=[("star", "Draw a sprite", "draw@0.3"), ("grownup", "Ask a grown-up", "ask")]),
        A("thought", "My sprite's nickname...", at="what$+0.2", x=1300, y=460),
    )),
    # 12. recap and next -------------------------------------------------------------------------------
    Scene("j1-w06-s12", setting="workshop", tail=0.8, beats=(
        B("Three ways to start a script. Say them with me!", speaker=AIDEN, cue="sayit", pause=0.4),
        B("Green flag!", speaker=AIDEN, cue="w1", pause=1.2),
        B("Click!", speaker=AIDEN, cue="w2", pause=1.2),
        B("Key!", speaker=AIDEN, cue="w3", pause=1.2),
        B("Each hat block waits for its own event, on its own sprite.", speaker=AIDEN, cue="recap", pause=0.6),
        B("Now it's your turn, with a grown-up.", speaker=AIDEN, cue="turn", pause=0.4),
        B("Build Click the Cat, then Keyboard Cat, then fix The Mixed-Up Ballerina. Then give your cat a "
          "nickname!", speaker=AIDEN, cue="next", pause=0.6),
        B("See you next week. Happy coding!", speaker=AIDEN, cue="bye", pause=0.4),
        B("Beep boop, bye!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Green flag!", at="w1", until="w1>", y=560, size=90, color="green"),
        A("bigtext", "Click!", at="w2", until="w2>", y=560, size=90, color="orange"),
        A("bigtext", "Key!", at="w3", until="w3>", y=560, size=90, color="blue"),
        A("chip", "Each hat waits for its own event", at="recap", until="turn", x=1200, y=560, color="yellow",
          size=44),
        A("banner", "NEXT: Click the Cat and Keyboard Cat", at="turn", color="green"),
        A("cards", items=["Click the Cat", "Keyboard Cat", "The Mixed-Up Ballerina"], x=1000, y=300, w=640,
          gap=120, reveal=["next@0.1", "next@0.35", "next@0.6"], at="next"),
        A("chip", "Nicknames only", at="next@0.85", x=1320, y=760, color="sky", size=44),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
