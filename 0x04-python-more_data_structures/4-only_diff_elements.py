#!/usr/bin/python3


# Function that returns only elements of both set
# except those appearing in both.
def only_diff_elements(set_1, set_2):
    n_set = set_1 ^ set_2
    return n_set
