import random

highest 20
answer = random.randint(1, highest)

print("Please pick a number between 1 and {}: ".format(highest))
guess = 0 # initialize to any number outside the valid range
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer: # guess must be greater than number
        print("please guess lower")
    else:
        print("Not bad, you guessed it")
