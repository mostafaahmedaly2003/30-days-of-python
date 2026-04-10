# Day 21 - Decorators & Generators | SOLUTION
# Try to solve exercises.py yourself before looking here!

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} took {time.time()-start:.4f}s')
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))
slow_sum(1_000_000)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
fib = fibonacci()
print([next(fib) for _ in range(10)])
