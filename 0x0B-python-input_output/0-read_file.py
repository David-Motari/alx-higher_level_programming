#!/usr/bin/python3
"""
read_file.py
reads a text file and prints to stdout.
"""


def read_file(filename=""):
    """
    args: filename - name of file to be read and printed to stdout.
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        for line in myFile:
            print("{}".format(line), end="")
