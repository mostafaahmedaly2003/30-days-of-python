# Day 15 - List & Dict Comprehensions | SOLUTION
# Try to solve exercises.py yourself before looking here!

evens_sq = [x**2 for x in range(1,21) if x%2==0]
print(evens_sq)
words = ['hello','hi','python','code','AI']
long_words = [w for w in words if len(w) > 3]
print(long_words)
lengths = {w: len(w) for w in words}
print(lengths)
