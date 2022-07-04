#!/usr/bin/python3
"""
2-is_same_class
function that returns True if the object is exactly an instance of the
specified class otherwise False.
"""


def is_same_class(obj, a_class):
    """
    args: obj object to be compared with,
    a_class is object to be compared.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
