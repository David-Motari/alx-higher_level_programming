#!/usr/bin/python3
"""
base.py
"""
import json


class Base:
    """
    dostring
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        args: id - integer identity of base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        args: list_dictionaries -  is a list of dictionaries
        returns: the string: "[]" if list_dictionaries is None
        else the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"

        return json.dumps(list_dictionaries)
