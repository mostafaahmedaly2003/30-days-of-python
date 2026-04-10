# Day 13 - Functions Advanced - args kwargs lambda | SOLUTION
# Try to solve exercises.py yourself before looking here!

def total(*args):
    return sum(args)
print(total(1,2,3,4,5))

double = lambda x: x * 2
numbers = [1,2,3,4,5]
print(list(map(double, numbers)))
print(list(filter(lambda x: x%2==0, numbers)))
