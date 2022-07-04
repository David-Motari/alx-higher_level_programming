#!/usr/bin/python3
"""square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a geometric shape Square """

    def __init__(self, size):
        """Instantiates width and height attributes of Square object"""

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def __str__(self):
        return "[square] {}/{}".format(self.__size, self.__size)
