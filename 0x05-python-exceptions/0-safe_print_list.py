#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints x number of elements in a list
    my_list: list
    x: number of elemnts in list
    return: number of elements printed.
    """
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
        except IndexError:
            break
        else:
            i += 1
    print()
    return i
