#!/usr/bin/python3


def no_c(my_string):
    for x in "C":
        my_string = my_string.replace(x, "")
    for x in "c":
        my_string = my_string.replace(x, "")
    return my_string
