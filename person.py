import json

try:
    with open('person.son', 'r') as input:
        obj = json.load(input)
        print("Hello %s" % obj['name'])
        hobbies = obj['hobbies']
        for h in hobbies:
            print("\t %s" % h)
except Exception as ffe:
    print("something went wrong")


