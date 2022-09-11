#!/usr/bin/python3


# function thap sums unique items in a lsit
def uniq_add(my_list=[]):
    uniq_list = []
    uniq_nums = set(my_list)
    # make list of unique items
    for n in uniq_nums:
        uniq_list.append(n)
    result = 0
    # sum unique list
    for i in range(len(uniq_list)):
        result += uniq_list[i]
    return result
