#!/usr/bin/python3
"""
append_file
appends text to a file.
"""


def append_write(filename="", text=""):
    """
    args: filename - file where text will be appended
    text - text to be appended

    Returns: new string with appended text.
    """
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
