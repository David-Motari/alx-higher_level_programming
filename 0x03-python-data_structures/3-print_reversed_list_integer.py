#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    new_list = [ele for ele in reversed(my_list)]
    for i in range(len(new_list)):
        print("{:d}".format(new_list[i]))
