#!/usr/bin/python3


# function the multiplies a number to items of a list.
def multiply_list_map(my_list=[], number=0):
    return(list(map(lambda a: a * number, my_list)))
