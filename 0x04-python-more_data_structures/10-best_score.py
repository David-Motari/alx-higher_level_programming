#!/usr/bin/python3


# Function that returns best score or None if dictionary is empty.
def best_score(a_dictionary):
    if (a_dictionary and len(a_dictionary)):
        return max(a_dictionary, key=a_dictionary.get)
    else:
        return None
