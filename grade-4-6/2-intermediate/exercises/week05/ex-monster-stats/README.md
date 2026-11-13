# Exercise 5.1 - Monster Stats

**Goal:** store a game monster in a **dictionary** and look things up by name.

```
{"name": "Blobby", "level": 1, "health": 30, "attack": 4, "speed": 2}
   key      value
```

1. Open `starter.py` and press **Run**.
2. **TODO 1:** loop with `for key, value in monster.items():` and build lines
   like `health: 30`.
3. **TODO 2:** finish `level_up()`.
4. Run it and type `magic` when it asks for a stat. **KeyError!** That is
   this week's bug hunt. **TODO 3:** check `if stat in monster:` first.

**Done looks like:**

```
name: Blobby
level: 1
health: 30
attack: 4
speed: 2
color: bluish green
Blobby eats a glowing mushroom... LEVEL UP!
name: Blobby
level: 2
health: 40
attack: 6
...
Which stat do you want to look up? magic
magic: 0
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** make a second monster and write `battle(a, b)` that returns the
name of the one with the higher attack.
