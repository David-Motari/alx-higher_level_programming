#!/usr/bin/python3


# Multiply values of dictionary by 2.
def multiply_by_2(a_dictionary):
    n_dictionary = {}
    for key in a_dictionary:
        n_dictionary.__setitem__(key, (a_dictionary[key] * 2))
    return n_dictionary
