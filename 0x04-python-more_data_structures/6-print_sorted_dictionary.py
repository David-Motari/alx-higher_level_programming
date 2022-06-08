#!/usr/bin/python3


# prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(i, a_dictinary[i])) for i in sorted(a_dictionary)]
