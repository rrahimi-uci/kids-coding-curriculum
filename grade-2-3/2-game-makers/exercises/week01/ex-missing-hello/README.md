# Exercise 1.3 – The Missing Hello (bug hunt)

**Goal:** find out why Kai's cat never talks, and fix it.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

Kai's plan: the cat says "Watch me!", meows, then bounces forever.

## Build steps

1. Use the cat. Build Kai's script below.
2. Try to snap the say block under the forever. What happens?
3. Leave the say and sound blocks there, close under the forever.
4. Click the green flag. Does the cat talk?
5. Find the bug. Fix it. Test again.

## The script in words (with the bug)

- when green flag clicked (yellow Events)
- forever (orange Control)
  - move 10 steps (blue Motion)
  - if on edge, bounce (blue Motion)

Under the forever, not snapped on:

- say Watch me! for 2 seconds (purple Looks)
- start sound Meow (pink Sound)

## Expected behavior

With the bug, the cat bounces, but it never talks and never meows.
After the fix, the cat says "Watch me!" and meows. Then it bounces until
you click the red stop sign.

## Checklist

- [ ] I found the blocks that never run.
- [ ] I can say why they never run.
- [ ] The cat talks, meows, then bounces.
