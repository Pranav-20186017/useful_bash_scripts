import json

with open('aws.json') as f:
  data = json.load(f)

print(type(data))
