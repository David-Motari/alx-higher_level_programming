#!/usr/bin/python3
"""
validator and implementation error
"""


class BaseGeometry():
    """
    goemetric class
    """

    def area(self):
        """
        implementation exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate if value is a integer.
        Args:
          - name: string
          - value: integer
        """
        if not isinstance(value, int):
            raise TypeError('{:s} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
