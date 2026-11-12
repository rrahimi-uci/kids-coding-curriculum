# Exercise 6.1 – Start Button

**Goal:** click the Star to start the game.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Add the **Star**. Drag it to the middle.
2. Star: **when this sprite clicked** (yellow Events), then **start sound Pop** (pink Sound).
3. Snap on **broadcast message1**. Pick **New message**. Type `start`.
4. **Looks** (purple): snap on **hide**.
5. Star: add **when green flag clicked** and **show**.
6. Click the cat. Events: drag in **when I receive**. Pick **start**.
7. Build the rest of the cat's script.
8. Add the Ballerina. Give her **when I receive start** and a dance.
9. Click the flag, then the Star!

## The script in words

Star:

- when this sprite clicked
- start sound Pop
- broadcast start
- hide

- when green flag clicked
- show

Cat:

- when I receive start
- set rotation style left-right
- say Let's play! for 2 seconds
- forever
  - move 10 steps
  - if on edge, bounce

Ballerina:

- when I receive start
- forever
  - next costume
  - wait 1 seconds

## Expected behavior

Click the Star: pop, it hides, and the cat and the Ballerina start
together.

## Checklist

- [ ] Nothing moves until I click the Star.
- [ ] The cat and the Ballerina both start.
- [ ] The message is called start in every block.
