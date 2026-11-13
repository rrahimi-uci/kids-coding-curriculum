"""Junior Level 1 Week 10: Showcase and Certificate (kit episode, Aiden and Pixi, Grades 2-3).

Follows grade-2-3/1-little-robots/teaching-material/lessons/week10.tex: showcase day, Exercise 10.1 the
last-minute bug check (flag twice, the click or key, the sound) with the most common bug (a sprite that
stays hidden on the second run, fixed with show at the top of a green flag script), the three parts of a
showcase and the chef analogy, the showcase sentence read from the hat block down on Mei's balloon
script, a quiz on the hat block, the gallery walk with sticker feedback, showcase safety (family only,
nicknames), the celebration dance, the Little Robots certificate and the next steps.
"""

from ..kit_dsl import A, NARRATOR, B, Episode, PIXI, Scene

FLAG = ("event", "when {flag} clicked")
CLICKED = ("event", "when this sprite clicked")
POP = ("sound", "play sound [Pop] until done")
SURPRISE = ("looks", "say [Surprise!] for [2] seconds")
BIG = 1.25  # block scale: big enough for young eyes

EPISODE = Episode(level="j1", week=10, scenes=(
    # 1. hook ---------------------------------------------------------------------------------------
    Scene("j1-w10-s01", setting="workshop", lead_in=0.3, beats=(
        B("Welcome back to Kids Coding! Aiden, our eight-year-old scientist and builder, is here with Pixi, his helpful robot friend.", speaker=NARRATOR, cue="hi",
          pause=0.4),
        B("Beep boop! Party time!", speaker=PIXI, cue="party", pause=0.5),
        B("You worked so hard on your greeting cards.", speaker=NARRATOR, cue="hard", pause=0.4),
        B("Today is our showcase. A showcase is a little show where we share what we made.", speaker=NARRATOR,
          cue="showcase", pause=0.5),
        B("You will show your greeting card, say what one script does, and then we celebrate!", speaker=NARRATOR,
          cue="three", pause=0.6),
        B("Are you ready? Let's go!", speaker=NARRATOR, cue="ready", pause=1.0),
    ), actions=(
        A("aiden", x=320, y=960, enter="left", wave=[("hi", "party"), ("ready", "end")],
          moods={"start": "happy", "three": "proud"}),
        A("pixi", x=640, y=760, drop=True, moods={"party": "happy"}),
        A("confetti", at="party", x=1300, y=420),
        A("banner", "MISSION: Show, explain and celebrate", at="showcase"),
        A("cards", items=["Show my card", "Say what one script does", "Celebrate!"], x=1000, y=420, w=680,
          gap=130, reveal=["three@0.1", "three@0.4", "three@0.75"], at="three", color="purple"),
    )),
    # 2. the last-minute bug check -------------------------------------------------------------------
    Scene("j1-w10-s02", setting="workshop", beats=(
        B("Before a show, performers check their props. So we do a last-minute bug check.", speaker=NARRATOR,
          cue="props", pause=0.5),
        B("One: click the green flag. Does the card start?", speaker=NARRATOR, cue="c1", pause=1.0),
        B("Two: click the flag a second time. Does it start the same way?", speaker=NARRATOR, cue="c2", pause=1.0),
        B("Three: click the sprite or press the key. Does the surprise happen?", speaker=NARRATOR, cue="c3",
          pause=1.0),
        B("Four: is the sound on? Can you hear it?", speaker=NARRATOR, cue="c4", pause=1.0),
        B("Check, check, check, check!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=230, y=1000, s=0.75, point=("props", "props$"), moods={"pixi": "proud"}),
        A("pixi", x=440, y=860, s=0.55, ground=1000, beep="pixi"),
        A("banner", "Exercise 10.1: Last-Minute Bug Check", at="props", color="navy"),
        A("cards", items=["Flag: does it start?", "Flag again: same start?", "Click or key: surprise?",
                          "Sound on?"], x=740, y=400, w=820, gap=130, reveal=["c1", "c2", "c3", "c4"],
          done=["pixi@0.1", "pixi@0.3", "pixi@0.5", "pixi@0.7"], color="sky"),
    )),
    # 3. bug hunt: the balloon that stays hidden -----------------------------------------------------
    Scene("j1-w10-s03", setting="mint", beats=(
        B("Here is the most common last-minute bug.", speaker=NARRATOR, cue="common", pause=0.4),
        B("Zoe clicks her balloon. Pop! The balloon hides. That is her surprise.", speaker=NARRATOR, cue="zoe",
          pause=1.0),
        B("Now she clicks the green flag a second time. Watch the balloon.", speaker=NARRATOR, cue="again",
          pause=2.6),
        B("Where is the balloon? Why did it not come back?", speaker=NARRATOR, cue="where", pause=3.2),
        B("It stayed hidden! Nothing tells it to show again.", speaker=NARRATOR, cue="hidden", pause=0.5),
        B("The fix: put show, from purple Looks, at the top of a green flag script.", speaker=NARRATOR, cue="fix",
          pause=0.8),
        B("Click the flag again.", speaker=NARRATOR, cue="test", pause=2.2),
        B("The balloon is back! Every show starts fresh.", speaker=NARRATOR, cue="back", pause=0.5),
        B("Fix one thing, then stop building, and save.", speaker=NARRATOR, cue="save", pause=0.5),
        B("Now Zoe's card is ready for the show!", speaker=NARRATOR, cue="ready", pause=0.8),
    ), actions=(
        A("banner", "BUG HUNT! The Hidden Balloon", at="common", color="navy"),
        A("scratch", "Zoe's balloon", blocks=[CLICKED, POP, ("looks", "hide")], x=150, y=250, w=880, h=380,
          scale=BIG, at="zoe", highlight=[(2, "zoe@0.6", "zoe$+0.6")]),
        A("scratch", "New script", blocks=[FLAG, ("looks", "show")], x=150, y=720, w=880, h=260, scale=BIG,
          at="fix", reveal=["fix@0.3", "fix@0.6"], highlight=[(1, "fix@0.6", "back$")]),
        A("stage", x=1120, y=250, w=700, h=480, at="zoe", sprite="balloon", sprite_scale=1.2, sprite_x=60,
          extra=[("cat", -120, -20)], flag_at="again@0.4",
          actions=[("zoe@0.6", "hide"), ("test@0.4", "show")]),
        A("pointer", x=1680, y=700, at="zoe", until="zoe@0.65", path=[("zoe", 1680, 700), ("zoe@0.5", 1560, 470)]),
        A("sfx", "pop", at="zoe@0.6"),
        A("badge", ok=False, at="where", until="test", x=1470, y=830),
        A("thought", "Where did it go?", at="where$+0.2", until="hidden", x=1470, y=920),
        A("chip", "show at the top: fresh start", at="fix", until="save", x=1470, y=920, color="purple", size=38),
        A("badge", ok=True, at="back", x=1470, y=830),
        A("chip", "Fix one thing. Save.", at="save", x=1470, y=920, color="green", size=44),
    )),
    # 4. a chef explains a recipe --------------------------------------------------------------------
    Scene("j1-w10-s04", setting="peach", beats=(
        B("At a showcase, you are like a chef on TV.", speaker=NARRATOR, cue="chef", pause=0.4),
        B("A chef shows the cake, and tells us one step of the recipe.", speaker=NARRATOR, cue="cake", pause=0.6),
        B("You are the chef. Your card is the cake. Your script is the recipe.", speaker=NARRATOR, cue="you",
          pause=0.6),
        B("So first you show your card. Then you point at one script and tell us what it does.",
          speaker=NARRATOR, cue="point", pause=0.8),
        B("Yum! Code cake!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "happy", "you": "proud"}, point=("point", "point$")),
        A("pixi", x=600, y=780, s=0.75, ground=960, beep="pixi"),
        A("icons", at="cake", until="end", x=1300, y=400, gap=300,
          items=[("person", "You = the chef", "you"), ("heart", "Card = the cake", "you@0.4"),
                 ("book", "Script = the recipe", "you@0.75")]),
        A("chip", "show it, then explain it", at="point", x=1300, y=760, color="orange", size=46),
    )),
    # 5. the showcase sentence -----------------------------------------------------------------------
    Scene("j1-w10-s05", setting="mint", beats=(
        B("Watch me do it with Mei's card for Grandpa.", speaker=NARRATOR, cue="watch", pause=0.4),
        B("First, I show it. I click the balloon.", speaker=NARRATOR, cue="show", pause=2.8),
        B("Now I point at the balloon's script, and read it from the top, one block at a time.", speaker=NARRATOR,
          cue="read", pause=0.5),
        B("When this sprite clicked. Play sound Pop. Say Surprise!", speaker=NARRATOR, cue="blocks", pause=0.6),
        B("So here is my showcase sentence: My card is for Grandpa. When you click the balloon, it pops and "
          "says Surprise!", speaker=NARRATOR, cue="sentence", pause=0.6),
        B("Did you see? First I showed it. Then I explained it.", speaker=NARRATOR, cue="see", pause=0.8),
    ), actions=(
        A("banner", "The showcase sentence", at="watch", color="green"),
        A("scratch", "Balloon's code", blocks=[CLICKED, POP, SURPRISE], x=150, y=280, w=900, h=440, scale=BIG,
          at="read", highlight=[(0, "blocks", "blocks@0.33"), (1, "blocks@0.33", "blocks@0.6"),
                                (2, "blocks@0.6", "blocks$")]),
        A("stage", x=1120, y=250, w=700, h=480, at="watch", flag=False, sprite="balloon", sprite_scale=1.2,
          sprite_x=90, sprite_y=10, extra=[("cat", -110, -20)], actions=[("show+1.0", "say", "Surprise!", 2.4)]),
        A("pointer", x=1700, y=700, at="show", until="read", path=[("show", 1700, 700), ("show+0.8", 1590, 470)]),
        A("sfx", "pop", at="show+0.8"),
        A("chip", "My card is for Grandpa.", at="sentence", x=600, y=830, color="yellow", size=42),
        A("chip", "When you click the balloon, it pops!", at="sentence@0.4", x=600, y=950, color="orange",
          size=40),
    )),
    # 6. your sentence, and a quiz -------------------------------------------------------------------
    Scene("j1-w10-s06", setting="peach", beats=(
        B("Now you! Say your sentence to the person next to you.", speaker=NARRATOR, cue="now", pause=0.4),
        B("My card is for... When you..., it...", speaker=NARRATOR, cue="frame", pause=4.0),
        B("If you get stuck, look at the hat block on top. Quick quiz!", speaker=NARRATOR, cue="stuck", pause=0.4),
        B("Look at this hat block. What do you do to start this script?", speaker=NARRATOR, cue="quiz", pause=3.2),
        B("You press the space key! The hat block tells you what starts the script.", speaker=NARRATOR,
          cue="space", pause=0.8),
    ), actions=(
        A("chip", "My card is for ...", at="frame", until="stuck", x=960, y=380, color="yellow", size=48),
        A("chip", "When you ..., it ...", at="frame@0.4", until="stuck", x=960, y=520, color="orange", size=48),
        A("aiden", x=300, y=1000, s=0.75, at="now", until="stuck", moods={"frame": "thinking"}),
        A("banner", "QUICK QUIZ", at="stuck@0.6", color="purple"),
        A("scratch", "Kai's script", blocks=[("event", "when [space] key pressed"), ("sound", "play sound [Meow] until done")],
          x=180, y=320, w=880, h=320, scale=BIG, at="quiz", highlight=[(0, "quiz", "end")]),
        A("thought", "How does it start?", at="quiz$+0.2", until="space", x=1400, y=460),
        A("chip", "press the space key!", at="space", x=1440, y=460, color="green", size=46),
        A("chip", "hat block = what starts it", at="space@0.5", x=1440, y=580, color="yellow", size=42),
    )),
    # 7. the gallery walk ----------------------------------------------------------------------------
    Scene("j1-w10-s07", setting="lavender", beats=(
        B("Next comes the gallery walk, like visitors in a museum.", speaker=NARRATOR, cue="museum", pause=0.4),
        B("Put your hands behind your back. Ask before you click someone's card.", speaker=NARRATOR, cue="hands",
          pause=0.6),
        B("Watch the card, then put a sticker on the part you liked best: the dance, the sound or the surprise.",
          speaker=NARRATOR, cue="sticker", pause=0.6),
        B("Say it out loud: I liked the surprise!", speaker=NARRATOR, cue="loud", pause=0.6),
        B("Walk slowly from card to card. Look with your eyes, and wait until the owner says yes.", speaker=NARRATOR,
          cue="slowly", pause=0.6),
        B("Only kind words at a showcase. And we never change someone else's card.", speaker=NARRATOR, cue="kind",
          pause=0.6),
        B("I liked the dance! Beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("banner", "Exercise 10.3: Sticker Feedback", at="museum", color="purple"),
        A("cards", items=["Hands behind your back", "Ask before you click"], x=220, y=300, w=700, gap=130,
          reveal=["hands", "hands@0.6"], at="hands", until="sticker"),
        A("icons", at="sticker", until="end", x=960, y=450, gap=320,
          items=[("person", "I liked the dance", "sticker@0.55"), ("music", "I liked the sound", "sticker@0.7"),
                 ("star", "I liked the surprise", "sticker@0.85")]),
        A("bubble", "I liked the surprise!", x=1280, y=380, at="loud", until="slowly", size=38),
        A("chip", "Only kind words", at="kind", x=700, y=820, color="green", size=46),
        A("chip", "Never change someone's card", at="kind@0.5", x=1280, y=820, color="red", size=40),
        A("pixi", x=1700, y=860, s=0.5, at="pixi", ground=960),
    )),
    # 8. showcase safety -----------------------------------------------------------------------------
    Scene("j1-w10-s08", setting="workshop", beats=(
        B("Now, showcase safety.", speaker=NARRATOR, cue="safety", pause=0.4),
        B("Our showcase is for our family, here at home.", speaker=NARRATOR, cue="family", pause=0.5),
        B("On the screen, we use nicknames. Never our full names, our school or our address.", speaker=NARRATOR,
          cue="nick", pause=0.6),
        B("Should we put our card on the internet, for people we do not know?", speaker=NARRATOR, cue="net",
          pause=3.0),
        B("No! If you want to show your card to someone else, ask a grown-up first.", speaker=NARRATOR, cue="no",
          pause=0.6),
        B("And if a grown-up takes a photo of the showcase for the family album, it stays in the family, and "
          "they ask you first.", speaker=NARRATOR, cue="photo", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"net": "thinking", "no": "proud"}, chin=("net", "no")),
        A("pixi", x=600, y=760, moods={"no": "happy"}),
        A("banner", "Showcase safety: family only", at="safety", color="green"),
        A("icons", at="family", until="end", x=1280, y=560, gap=290,
          items=[("house", "Family at home", "family"), ("person", "Nicknames only", "nick"),
                 ("wifi_off", "Not on the internet", "net@0.4")]),
        A("thought", "Internet for everyone?", at="net$+0.2", until="no", x=1280, y=860),
        A("chip", "Ask a grown-up first", at="no", until="photo", x=1280, y=860, color="green", size=46),
        A("chip", "Photos stay in the family", at="photo", x=1280, y=860, color="yellow", size=44),
    )),
    # 9. celebration dance ---------------------------------------------------------------------------
    Scene("j1-w10-s09", setting="workshop", beats=(
        B("Time to celebrate! Stand up and do the dance from your card.", speaker=NARRATOR, cue="stand", pause=0.5),
        B("Do it four times, like a repeat. One, two, three, four!", speaker=NARRATOR, cue="dance", pause=1.0),
        B("Again! One, two, three, four!", speaker=NARRATOR, cue="again", pause=1.4),
        B("And now, one big clap together!", speaker=NARRATOR, cue="clap", pause=1.6),
        B("Clap, clap, beep!", speaker=PIXI, cue="pixi", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, wave=[("stand", "end")], moods={"start": "happy", "clap": "proud"},
          path=[("dance", 300, 960), ("dance@0.4", 340, 960), ("dance@0.6", 260, 960), ("dance@0.8", 340, 960),
                ("dance$", 300, 960)]),
        A("pixi", x=600, y=760, beep=[("dance", "dance$"), ("pixi", "end")], moods={"clap": "happy"}),
        A("bigtext", "Dance x 4!", at="dance", until="clap", x=1300, y=520, size=100, color="orange"),
        A("bigtext", "CLAP!", at="clap@0.5", x=1300, y=520, size=120, color="purple"),
        A("sfx", "sparkle", at="clap@0.6"),
        A("confetti", at="clap@0.6", x=1300, y=420),
    )),
    # 10. the certificate ----------------------------------------------------------------------------
    Scene("j1-w10-s10", setting="workshop", beats=(
        B("And now, the certificates!", speaker=NARRATOR, cue="cert", pause=0.5),
        B("You are now a Little Robots coder!", speaker=NARRATOR, cue="coder", pause=0.6),
        B("You planned a card, built it box by box, and explained your code.", speaker=NARRATOR, cue="did",
          pause=0.6),
        B("Hold your certificate up high! Everyone claps for you!", speaker=NARRATOR, cue="high", pause=1.4),
        B("What are you proudest of in your card?", speaker=NARRATOR, cue="proud", pause=3.0),
        B("And what would you like to make next?", speaker=NARRATOR, cue="nextq", pause=3.0),
        B("Hooray for you!", speaker=PIXI, cue="hooray", pause=0.8),
    ), actions=(
        A("aiden", x=300, y=960, moods={"start": "proud", "proud": "thinking", "hooray": "happy"},
          wave=[("high", "high$"), ("hooray", "end")]),
        A("pixi", x=600, y=760, beep="hooray"),
        A("icons", at="cert", until="proud", x=1300, y=480, gap=280,
          items=[("trophy", "Certificate", "cert@0.3")]),
        A("bigtext", "Little Robots coder!", at="coder", until="proud", x=1300, y=700, size=72, color="orange"),
        A("sfx", "chime", at="coder"),
        A("confetti", at="coder", x=1300, y=420),
        A("chip", "planned • built • explained", at="did", until="proud", x=1300, y=840, color="green", size=44),
        A("thought", "Proudest part?", at="proud$+0.2", until="nextq", x=1300, y=480),
        A("thought", "What next?", at="nextq$+0.2", until="hooray", x=1300, y=480),
        A("confetti", at="hooray", x=1300, y=420),
        A("confetti", at="high", x=1300, y=420),
        A("sfx", "sparkle", at="high@0.6"),
    )),
    # 11. recap and next -------------------------------------------------------------------------------
    Scene("j1-w10-s11", setting="workshop", tail=0.8, beats=(
        B("Say it with me!", speaker=NARRATOR, cue="sayit", pause=0.4),
        B("Show!", speaker=NARRATOR, cue="w1", pause=1.2),
        B("Explain!", speaker=NARRATOR, cue="w2", pause=1.2),
        B("Celebrate!", speaker=NARRATOR, cue="w3", pause=1.2),
        B("Now it's your turn, with your family.", speaker=NARRATOR, cue="turn", pause=0.4),
        B("Do the bug check. Show your card and say what one script does. Then give kind sticker feedback.",
          speaker=NARRATOR, cue="next", pause=0.6),
        B("Put your certificate where you can see it. You did it! Happy coding!", speaker=NARRATOR, cue="bye",
          pause=0.4),
        B("Beep boop, bye, coders!", speaker=PIXI, cue="bye2", pause=0.4),
    ), actions=(
        A("aiden", x=260, y=1000, s=0.75, wave=[("bye", "end")], moods={"start": "proud"}),
        A("pixi", x=480, y=860, s=0.62, ground=1000, moods={"start": "proud"}, beep="bye2"),
        A("bigtext", "Show!", at="w1", until="w1>", y=560, size=90, color="orange"),
        A("bigtext", "Explain!", at="w2", until="w2>", y=560, size=90, color="green"),
        A("bigtext", "Celebrate!", at="w3", until="w3>", y=560, size=90, color="purple"),
        A("banner", "NEXT: Showcase at home", at="turn", color="green"),
        A("cards", items=["Last-minute bug check", "Show and explain my card", "Kind sticker feedback"], x=1000,
          y=300, w=680, gap=120, reveal=["next@0.1", "next@0.4", "next@0.75"], at="next"),
        A("confetti", at="bye", x=1200, y=420),
    )),
))
