#!/usr/bin/python3
"""
add_attribute
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it’s possible
    Args: object - object whose attribute has to be set
    name - attribute name
    value - value given to the attribute
    Returns: None
    """
    # checking for dict () method in obj
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
