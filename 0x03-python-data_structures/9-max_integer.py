#!/usr/bin/python3


# max_integer - finds the biggest integer of a list
def max_integer(my_list=[]):
    highest_val = 0
    if len(my_list) != 0:
        for i in my_list:
            if (highest_val is None or i > highest_val):
                highest_val = i
        return highest_val
    else:
        return None
