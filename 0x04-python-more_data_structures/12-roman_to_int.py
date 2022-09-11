#!/usr/bin/python3


# function that converts roman numeral to an integer.
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string = None:
        return 0

    rmn_lttrs = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    num = 0
    last = 0

    for lttr in roman_string:
        for elem in rmn_lttrs:
            if lttr == elem[0]:
                if last == 0 or last >= elem[1]:
                    num += elem[1]
                elif last < elem[1]:
                    num += elem[1] - (last * 2)

                last = elem[1]

    return num
