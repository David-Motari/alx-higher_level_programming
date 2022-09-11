#!/usr/bin/python3
"""
    2-square.py
"""


class Square:
    """
        defines a square
    """
    def __init__(self, size=0):
        """
            creates instance of square
            args: size - size of a square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
