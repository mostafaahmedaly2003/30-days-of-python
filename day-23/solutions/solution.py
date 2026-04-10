# Day 23 - Standard Library - datetime os sys | SOLUTION
# Try to solve exercises.py yourself before looking here!

from datetime import datetime
import os, sys
now = datetime.now()
print(f'Today: {now.strftime("%Y-%m-%d %H:%M")}')
target = datetime(now.year+1, 1, 1)
days = (target - now).days
print(f'Days until {now.year+1}: {days}')
py_files = [f for f in os.listdir('.') if f.endswith('.py')]
print('Python files:', py_files)
