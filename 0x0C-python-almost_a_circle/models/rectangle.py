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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """defines height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """defines x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """defines y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculates area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        display hash rectangle
        """
        if self.__height == 0 or self.__width == 0:
            print("")
            return
        for y in range(self.y):
            print("")
        for i in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width, end="")
            print("")

    def __str__(self):
        return f"[Rectangle] ({self.id}) \
{self.x}/{self.y} - {self.width}/{self.height}"
