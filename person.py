import json
with open('person.json', 'r') as input:
    obj = json.load(input)
    print("Hello %s", obj['name'])
    for hobby in obj['hobbies']:
        print(hobby)