# Day 25 - HTTP Requests & REST APIs | SOLUTION
# Try to solve exercises.py yourself before looking here!

import requests
response = requests.get('https://official-joke-api.appspot.com/random_joke')
if response.status_code == 200:
    joke = response.json()
    print(joke['setup'])
    print(f"=> {joke['punchline']}")
else:
    print(f'Error: {response.status_code}')
