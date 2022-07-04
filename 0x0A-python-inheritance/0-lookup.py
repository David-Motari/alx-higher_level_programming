#!/usr/bin/python3
"""
0-lookup.py
Function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    args: obj - object to extract attributes and methods from
    """
    return dir(obj)
