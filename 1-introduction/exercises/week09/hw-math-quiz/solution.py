# Mini Math Quiz - reference solution
# A variable called score remembers how many answers were right.

print("Welcome to the Mini Math Quiz!")
score = 0

# Question 1
answer = int(input("What is 7 x 8? "))
if answer == 56:
    print("Correct!")
    score = score + 1
else:
    print("Good try! 7 x 8 = 56")

# Question 2
answer = int(input("What is 9 + 15? "))
if answer == 24:
    print("Correct!")
    score = score + 1
else:
    print("Good try! 9 + 15 = 24")

print("You scored", score, "out of 2")
