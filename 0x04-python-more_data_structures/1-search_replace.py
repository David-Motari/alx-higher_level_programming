#!/usr/bin/python3


# function that searches and replaces item in list and returns a new list.
def search_replace(my_list, search, replace):
    i = my_list.index(search)
    n_list = my_list[:i] + [replace] + [(i + 1):]
    return n_list
