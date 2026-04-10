# Day 24 - JSON & CSV | SOLUTION
# Try to solve exercises.py yourself before looking here!

import json, csv
data = [{'name':'Alice','score':95},{'name':'Bob','score':87}]
with open('data.json','w') as f:
    json.dump(data, f, indent=2)
with open('data.json','r') as f:
    loaded = json.load(f)
print(loaded)
with open('data.csv','w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name','score'])
    writer.writeheader()
    writer.writerows(data)
