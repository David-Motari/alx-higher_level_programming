#!/usr/bin/python3
"""base_geometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implements a geometric shape Rectangle"""

    def __init__(self, width, height):
        """instantiates width and height attributes of Rectangle object"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """determines the area of a Rectangle object"""
        return self.__width * self.__height

    def __str__(self):
        """str rep of a Rectangle object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
