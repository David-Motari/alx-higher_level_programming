#!/usr/bin/python3

def remove_char_at(str, n):
"""
Removes the character at position n is string
arg
str: string
n: integer
Return:
a copy of a string without chacter n
"""
return str[:] if n < 0 else str[:n] + str[n + 1:]
