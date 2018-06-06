from datetime import datetime as d

birthYear = int(input("When year of birth "))

# if 1946 <= birthYear <= 2012:
#     print(d.now().year - birthYear)
# else:
#     print("no logic for that")
#
# if birthYear in range(1946, 1965):
#     print("Baby boomer")
# elif birthYear in range(1965, 1980):
#     print("Gen X")
# elif birthYear in range(1980, 1995):
#     print("Millenials")
# elif birthYear in range(1995, 2013):
#     print("Gen Z")
# else:
#     print("Can't handle")

gens = [
    (range(1946, 1965), "Baby Boomer"),
    (range(1965, 1980), "GenX"),
    (range(1979, 1995), "Millenials"),
    (range(1995, 2012), "Gen Z")
]


def getGeneration(byear):
    for i in gens:
        if birthYear in i[0]:
            return i[1]


if 1946 <= birthYear <= 2012:
    age = d.now().year - birthYear
    print("You are {0} years old | {1}".format(age, getGeneration(birthYear)))



