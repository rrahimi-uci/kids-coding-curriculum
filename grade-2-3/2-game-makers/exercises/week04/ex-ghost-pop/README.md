# Exercise 4.2 – Ghost Pop

**Goal:** click the ghost to score. It pops up in surprise places!
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Click **File**, then **New**. Add the **Ghost**. Delete the cat.
2. **Variables** (orange-red): make a variable called `score`.
3. **Events** (yellow): drag in **when green flag clicked**.
4. Variables: snap on **set score to 0**.
5. **Control** (orange): snap on **forever**.
6. Inside the forever: **go to random position** (blue Motion) and **wait 1 seconds** (Control).
7. Events: drag in **when this sprite clicked**.
8. Snap on **change score by 1** (Variables), **start sound Pop** (pink Sound) and **go to random position** (Motion).
9. Click the flag. Catch it!

## The script in words

- when green flag clicked
- set score to 0
- forever
  - go to random position
  - wait 1 seconds

- when this sprite clicked
- change score by 1
- start sound Pop
- go to random position

## Expected behavior

The ghost jumps to a surprise place every second. Each click pops and
adds 1 to the score. The flag puts the score back to 0.

## Checklist

- [ ] The ghost jumps to a surprise place every second.
- [ ] A click adds 1 to the score and pops.
- [ ] The score starts at 0 when I click the flag.
