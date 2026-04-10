# Day 22 - Regular Expressions | SOLUTION
# Try to solve exercises.py yourself before looking here!

import re
def is_valid_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w{2,}$'
    return bool(re.match(pattern, email))
print(is_valid_email('test@example.com'))
print(is_valid_email('not-an-email'))
text = 'Call 012-345-6789 or 098-765-4321'
numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(numbers)
