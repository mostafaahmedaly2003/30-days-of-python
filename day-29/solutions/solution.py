# Day 29 - Mini Project - Password Generator | SOLUTION
# Try to solve exercises.py yourself before looking here!

import random, string
def generate_password(length=12, digits=True, symbols=True):
    chars = string.ascii_letters
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
for _ in range(5):
    print(generate_password(16))
