

# It even prevents printing of duplicate
# numbers

for i in range(1, 101):
    printednums = []
    if i % 10 == 0:   # I already know this is even
        print("{0} | FizzBuzz".format(i))
        printednums.append(i)
    if i % 2 == 0:
        if i not in printednums:
            print("{0} | Buzz".format(i))
    else:
        print("{0} | Fizz".format(i))



