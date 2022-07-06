#!/usr/bin/python3
"""
load_from_json_file
function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    args: filename - json file to creat object from.
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        return myFile.read()
