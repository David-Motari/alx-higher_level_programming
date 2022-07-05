#!/usr/bin/python3
"""
write_file
writes a string to a text file (UTF8) and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    args: filename - file to write to,
    text -  strings to write to file
    returns: number of charactes written
    """
    with open(filename, mode="w+", encoding="utf-8") as myFile:
        return myFile.write(text)
