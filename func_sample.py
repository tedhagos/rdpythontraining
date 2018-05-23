#!/usr/bin/python
import sys


def foo(args):
    print("function foo")
    print(sys.argv)

    for i in sys.argv:
        print(i)


if __name__ == "__main__":
    foo(sys.argv)




