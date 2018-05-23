#!/usr/bin/python
import sys

# Description of the problem is
# found at http://bit.ly/python-top-exer1


def sum_to(end):
    num_list = range(1, int(end))
    sum = 0
    for i in num_list:
        sum = sum + i
    print("Sum of numbers from 1 to {0} is {1}".format(end, sum))


def sum_of_even(end):
    # print("not yet implemented")
    num_list = range(1, end)
    sum = 0
    for i in num_list:
        if i % 2 == 0:
            sum = sum + i
    print("Sum of even numbers from 1 to {0} is {1}".format(end, sum))


def sum_of_odd(end):
    num_list = range(1, end)
    sum = 0
    for i in num_list:
        if i % 2 != 0:
            sum = sum + i
    print("Sum of odd numbers from 1 to {0} is {1}".format(end, sum))


if __name__ == "__main__":
    sum_to(sys.argv[1])


