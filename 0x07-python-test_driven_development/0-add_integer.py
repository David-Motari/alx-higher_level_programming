#!/usr/bin/python3
"""
0-add_integer.py-adds two integers
"""


def add_integer(a, b=98):
    """
    adds two integers.

    args: a - first integer(float), b - second integer(float)
    raises: type error if either  a or b is not integer/float
    returns: sum of two integers/float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
