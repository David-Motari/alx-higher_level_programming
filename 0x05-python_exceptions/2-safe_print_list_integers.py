#!/usr/bin/python3

from itertools import count


def safe_print_list_integers(my_list=[], x=0):
    """
        prints the first x elements of a list and only integers.
        my_list: contains any type (integer/string)

    """
    i = 0
    counter = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            counter += 1
        finally:
            i += 1
    print()
    return(counter)
