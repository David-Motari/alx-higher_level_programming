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

    def __str__(self):
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}"
