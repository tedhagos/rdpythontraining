# ask the user for input
# find the divisors of that number


def imperative_solution(end):
    numrange = range(1, num + 1)
    divisors = []
    for i in numrange:
        if num % i == 0:
            divisors.append(i)
    print("divisors of {0}".format(num))
    print("-----------------")
    print(divisors)


def declarative_solution(end):
    numrange = range(1, num + 1)
    print("divisors of {0}".format(num))
    print("-----------------")
    print(list(filter(lambda x: num % x == 0, numrange)))


num = int(input("enter a number : "))
declarative_solution(num)
# imperative_solution(num)


# if we were to write the lambda in line no 20, this is
# how it will look like
# def fun foo(x):
#   if num % x == 0:
#       True

