#!/usr/bin/python3


# function that searches and replaces item in list and returns a new list.
def search_replace(my_list, search, replace):
    n_list = my_list[:]
    for i in range(len(n_list)):
        if n_list[i] == search:
            n_list[i] == replace
    return n_list
