# Day 10 - Dictionaries | SOLUTION
# Try to solve exercises.py yourself before looking here!

student = {'name': 'Mostafa', 'age': 22, 'grade': 'A'}
student['university'] = 'MUST'
print(student.get('name'))
for key, value in student.items():
    print(f'{key}: {value}')
