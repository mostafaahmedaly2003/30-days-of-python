# Day 28 - Data Visualization with matplotlib | SOLUTION
# Try to solve exercises.py yourself before looking here!

import matplotlib.pyplot as plt
languages = ['Python','JavaScript','Java','C++','Rust']
popularity = [30, 25, 20, 15, 10]
plt.figure(figsize=(8,5))
plt.bar(languages, popularity, color='steelblue')
plt.title('Programming Language Popularity')
plt.ylabel('Usage %')
plt.tight_layout()
plt.savefig('languages.png')
print('Chart saved!')
