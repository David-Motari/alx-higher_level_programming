#!/usr/bin/python3


# Function that deletes key from dictionary.
def simple_delete(a_dictionary, key=""):
    if key in dictionary:
        del a_dictionary[key]
    return a_dictionary
