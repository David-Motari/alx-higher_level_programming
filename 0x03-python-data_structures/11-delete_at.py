#!/usr/bin/python3


# delete_at - deletes item at specified index.
def delete_at(my_list=[], idx=0):
    if my_list and 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
