# Exercise 5.2 – Bug-Hunt Relay (bug hunt)

**Goal:** fix three broken games.
**Tool:** Scratch app. **Work with a partner:** swap Driver each leg.

## Build steps

1. Click **File**, then **New**. Build the leg with the bug.
2. **Test** it. **Look:** what is wrong?
3. **Change one thing.** Test again. Swap Driver!

## The script in words (with the bugs)

**Leg 1: Stuck at the Edge.** The cat should walk back and forth.

- when green flag clicked (yellow Events)
- set rotation style left-right (blue Motion)
- if on edge, bounce
- forever (orange Control)
  - move 10 steps

**Leg 2: The Stuck Score.** Each click on the Ghost should add 1.
Make a `score` variable (orange-red Variables).

- when green flag clicked
- set score to 0

- when this sprite clicked
- set score to 1
- start sound Pop (pink Sound)

**Leg 3: The Apple That Won't Pop.** The Apple should pop when the cat touches it.

Cat:

- when green flag clicked
- forever
  - go to mouse-pointer

Apple:

- when green flag clicked
- forever
  - if touching edge? then (light blue Sensing)
    - start sound Pop
    - go to random position

## Expected behavior

Each fixed game does what its leg says. Keep leg 3 open for 5.3.

## Checklist

- [ ] Leg 1: the cat bounces.
- [ ] Leg 2: each click adds 1.
- [ ] Leg 3: the Apple pops.
