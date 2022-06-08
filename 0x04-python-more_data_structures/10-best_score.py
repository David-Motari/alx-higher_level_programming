#!/usr/bin/python3


# Function that returns best score or None if dictionary is empty.
def best_score(a_dictionary):
    if (a_dictionary and len(a_dictionary)):
        b_key = max(a_dictionary)
        return b_key
    else:
        return None
