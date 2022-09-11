#!/usr/bin/python3
"""
save_to_json_file
function that writes an Object to a text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    args: my_obj - python object to write into json file
    filename - json file to write into.
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
