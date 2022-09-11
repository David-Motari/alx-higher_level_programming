#!/usr/bin/python3
"""
from_json_string
function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    args: my_str - JSON string to return as object
    """
    return json.loads(my_str)
