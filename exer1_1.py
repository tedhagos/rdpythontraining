#!/usr/bin/python
import sys

# Description of the problem is
# found at http://bit.ly/python-top-exer1
# This is second version of the solution


def sum_to(end):
    total = sum(range(0, end))
    print("Sum of numbers from 1 to {0} is {1}".format(end, total))


def sum_of_even(end):
    total = sum(range(0, end, 2))
    print("Sum of even numbers from 1 to {0} is {1}".format(end, total))


def sum_of_odd(end):
    total = sum(x for x in range(0, end) if x % 2 != 0)
    print("Sum of odd numbers from 1 to {0} is {1}".format(end, total))


def sum_of_odd_filter(end):
    numlist = range(1, end)
    total = sum(filter(lambda x: x % 2 != 0, numlist))
    print("filter -> sum of odd numbers is {}".format(total))


def sum_to_map(end):
    numlist = range(1, end)
    total = sum(map(lambda x: x, numlist))
    print("Sum of numbers from 1 to {0} is {1} [map]".format(end, total))


if __name__ == "__main__":
    try:
        sum_to(int(sys.argv[1]))
    except IndexError:
        print("int positional arg is expected")


