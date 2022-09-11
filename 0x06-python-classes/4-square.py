#!/usr/bin/python3
"""
    square
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
        self.size = size

    @property
    def size(self):
        """
            availing the private attribute size for access
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            calculate the area of square
        """
        return self.__size ** 2
