

with open('t.txt', 'r') as story:
    for line in story:
        linedec = line.split()
        for word in linedec:
            print(word)