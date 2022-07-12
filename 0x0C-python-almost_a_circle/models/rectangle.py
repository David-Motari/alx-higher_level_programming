#!/usr/bin/python3
"""
rectangle.py
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle object class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        args:
        width - of rectangle
        height - of rectangle
        x - x axis position of new triangle
        y - y axis position of new triangle
        id - identity of triangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """defines width"""
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        @property
        def height(self):
            """defines height"""
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        @property
        def x(self):
            """defines x"""
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        @property
        def y(self):
            """defines y"""
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
