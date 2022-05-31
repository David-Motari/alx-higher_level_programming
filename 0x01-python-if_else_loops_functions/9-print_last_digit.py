#!/usr/bin/python3

def print_last_digit(number):
    lst_dgt = (-number % 10) if number < 0 else number % 10
    print("{:d}".format(lst_dgt), end="")
    return lst_dgt
