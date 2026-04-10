# Day 12 - Functions Basics | SOLUTION
# Try to solve exercises.py yourself before looking here!

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print([x for x in range(2,20) if is_prime(x)])
