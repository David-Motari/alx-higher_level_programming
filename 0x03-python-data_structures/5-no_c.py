#!/usr/bin/python3


def no_c(my_string):
    another_string = my_string.translate({ord('C'):None})
    another_string = my_string.translate({ord('c'):None})
    return another_string
