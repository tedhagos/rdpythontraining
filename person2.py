import json
with open('person.json', 'r') as input:
    obj = json.load(input)
    print("Hello %s", obj['name'])

    with open('output.txt', 'w') as output:
        for hobby in obj['hobbies']:
            output.write(hobby + "\n")