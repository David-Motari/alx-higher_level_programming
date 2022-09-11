#!/usr/bin/python3
"""
0-rectangle.py
defines a rectangle
"""


class Rectangle:
    """
    represantation of a rectangle
    args: @width - width of rectangle, @height - heigth of rectangle.
    Raises: width(TypeError and ValueError), height(TypeError and ValueError)

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            availing the private attribute width for access
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            availing the private attribute height for access
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
