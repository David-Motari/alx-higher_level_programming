#!/usr/bin/python3
"""Noma"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle based on basegeometry
    """
    def __init__(self, width, height):
        """
        args: width -  rectangle width
        height: rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
