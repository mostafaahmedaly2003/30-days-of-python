# Day 06 - while Loops | SOLUTION
# Try to solve exercises.py yourself before looking here!

import random
secret = random.randint(1, 10)
guess = 0
while guess != secret:
    guess = int(input('Guess (1-10): '))
    if guess < secret:
        print('Too low!')
    elif guess > secret:
        print('Too high!')
print('Correct!')
