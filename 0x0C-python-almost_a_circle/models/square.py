#!/usr/bin/python3
"""
square.py
inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    docstring
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        args: size - size of side,
        x -  x-axis position
        y - y-axis position
        id - new square id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        args: *args - array of arguments that reps new attribute values
        - 1st argument represents id attribute
        - 2nd argument represents sizeattribute
        - 3rd argument represent x attribute
        - 4th argument represents y attribute
         **kwargs - 1st arg is id attribute 2nd arg can be\
(size/x/y) attribute
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def __str__(self):
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}"
