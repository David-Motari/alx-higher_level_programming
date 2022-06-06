#!/usr/bin/python3


# print_reversed_list_integer - reverses a list of integers
def print_reversed_list_integer(my_list=[]):
    new_list = [x for x in reversed(my_list)]
    for i in range(len(new_list)):
        print("{:d}".format(new_list[i]))
