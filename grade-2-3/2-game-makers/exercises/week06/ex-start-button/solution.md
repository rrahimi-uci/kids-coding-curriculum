# Teacher reference: Exercise 6.1 - Start Button
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 6 (Messages)  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** One sprite can tell the others when to start. broadcast sends a message to every sprite; when I receive listens for it.

## The finished project
Setup: File > New. Keep the cat and drag it to one side. Add the Star (drag it to the middle) and the Ballerina.

Sprite: Star, script 1
- when this sprite clicked
- start sound Pop
- broadcast start (made with New message)
- hide

Sprite: Star, script 2
- when green flag clicked
- show

Sprite: Sprite1 (the cat)
- when I receive start
- set rotation style left-right
- say Let's play! for 2 seconds
- forever
  - move 10 steps
  - if on edge, bounce

Sprite: Ballerina
- when I receive start
- forever
  - next costume
  - wait 1 seconds

## What you should see
- Green flag: the Star appears; the cat and the Ballerina stay still.
- Click the Star: a pop, the Star disappears, the cat says "Let's play!" for 2 seconds and then walks back and forth forever; the Ballerina changes pose every second from the same moment.
- Stop and flag again: the Star is back, waiting.

## Talking points
- One message, two listeners: the Star does not tell each sprite one by one; it broadcasts once.
- The flag starts the Star's show script, but only the message starts the game. That is how real games have a start screen (more in week 8).
- Message names are like the words on the notes in the warm-up: they must match.

## Common mistakes and quick fixes
- The cat's hat block says message1: pick start in the dropdown.
- Two messages, "start" and "Start game": use one name everywhere.
- The Star never comes back: the green flag show script is missing.
- The cat walks upside down after a bounce: "set rotation style left-right" is missing. Add it under the hat block and click "point in direction 90" once.
- The when I receive script was built in the Star: drag it onto the cat in the sprite list, then delete it from the Star.

## Check-off list
- [ ] The Star broadcasts start, then hides.
- [ ] The cat and the Ballerina each have a when I receive start script.
- [ ] Nothing moves until the Star is clicked.
- [ ] The flag brings the Star back.
