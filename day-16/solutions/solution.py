# Day 16 - File IO | SOLUTION
# Try to solve exercises.py yourself before looking here!

with open('names.txt', 'w') as f:
    f.write('Alice\nBob\nCharlie\n')
with open('names.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
print(f'{len(lines)} names found')
