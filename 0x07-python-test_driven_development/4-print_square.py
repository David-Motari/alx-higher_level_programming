#!/usr/bin/python3
"""
4-print_square.py
prints a square with the character #.
"""


def print_square(size):
    """
    args: size - size of square.
    Raises:  TypeError for non-integer size \
        and ValueError for size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for j in range(size):
        if size == 0:
            return ()
        for i in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
