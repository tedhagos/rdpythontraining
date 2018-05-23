

try:
    with open('t.txt', 'r') as story:
        for line in story:            # becomes as string
            linedec = line.split()    # linedec is a list
            for word in linedec:      # word is a string
                print(word)

except FileNotFoundError as fe:
    print(fe)
