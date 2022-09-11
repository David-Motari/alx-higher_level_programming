#!/usr/bin/python3
"""my_int"""


class MyInt(int):
    """creates a class that inherits from int"""

    def __eq__(self, other):
        """Defines behavior for '=='"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Defines behavior for '!='"""
        return super().__eq__(other)
