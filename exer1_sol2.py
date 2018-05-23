#!/usr/bin/python
import sys


def sum_to(end):
    numlist = range(1, end + 1)
    print("sum of nos 1 to {0} is = {1}".format(end, sum(numlist)))


def sum_of_even(end):
    numlist = range(0, end + 1, 2)
    print("sum of even nos 1 to {0} is = {1}".format(end, sum(numlist)))


def sum_of_odd(end):
    total = sum(x for x in range(0, end + 1) if x % 2 != 0)
    print("Sum of odd numbers from 1 to {0} is {1}".format(end, total))


def foo(arg):
    return 100


if __name__ == "__main__":
    try:
        sum_to(int(sys.argv[1]))
        sum_to(foo)
    except IndexError:
        print("int positional arg is expected")
