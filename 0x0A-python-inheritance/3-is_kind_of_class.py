#!/usr/bin/python3
"""
is_kind_of_class
function that returns True if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Args: obj - object to be compared with
    a_class - object to compare

    """
    if isinstance(obj, a_class):
        return True
    return False
