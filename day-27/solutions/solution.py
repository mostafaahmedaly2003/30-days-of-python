# Day 27 - Data Analysis with pandas | SOLUTION
# Try to solve exercises.py yourself before looking here!

import pandas as pd
data = {'name':['Alice','Bob','Charlie','Diana'],'score':[85,92,78,96],'subject':['Math','Math','Science','Science']}
df = pd.DataFrame(data)
print(df.describe())
print(df[df['score'] > 85])
print(df.groupby('subject')['score'].mean())
