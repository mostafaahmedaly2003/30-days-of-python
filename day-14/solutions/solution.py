# Day 14 - Scope & Closures | SOLUTION
# Try to solve exercises.py yourself before looking here!

x = 'global'
def outer():
    x = 'outer'
    def inner():
        x = 'inner'
        print(x)
    inner()
    print(x)
outer()
print(x)

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
c = make_counter()
print(c(), c(), c())
