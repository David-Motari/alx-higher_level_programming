#!/usr/bin/python3


# divisible_by_2 - finds all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    div_abl = []
    for i in range(len(my_list)):
        div_abl.append(True) if my_list[i] % 2 == 0 else div_abl.append(False)
    return div_abl
