#!/usr/bin/pythom3
"""
append_after
Defines a text file insertion function.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as myFile:
        for line in myFile:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as my_File:
        my_File.write(text)
