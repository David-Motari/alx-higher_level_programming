#!/usr/bin/python3


# print_reversed_list_integer - reverses a list of integers
def print_reversed_list_integer(my_list=[]):
    for x in reversed(my_list):
        print("{:d}".format(x))
