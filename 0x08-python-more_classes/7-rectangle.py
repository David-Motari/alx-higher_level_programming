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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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

    def area(self):
        """
        returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        return rectangle using hash(#)
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        hash_rect = []
        for i in range(self.__height):
            [hash_rect.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i != self.__height - 1:
                hash_rect.append("\n")
        return ("".join(hash_rect))

    def __repr__(self):
        """
        Return the string representation of the Rectangle.
        """

        new_rect = f"Rectangle({str(self.__width)}"
        new_rect += f", {str(self.__height)})"
        return (new_rect)

    def __del__(self):
        """
        prints message when an instance of Rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
