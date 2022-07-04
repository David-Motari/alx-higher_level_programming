#!/usr/bin/python3
"""base_geometry"""


class BaseGeometry:
    """represents geometric shape"""

    def area(self):
        """Getter"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        args: name - variable
        value - integer assigned to name
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
