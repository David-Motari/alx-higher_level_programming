#!/usr/bin/python3


# function that searches and replaces item in list and returns a new list.
def search_replace(my_list, search, replace):
    n_list = []
    for i in my_list:
        if i != search:
            n_list.append(i)
        else:
            n_list.append(replace)
    return n_list
