#!/usr/bin/python3
"""defines a function"""


import json


def from_json_string(my_str):
    """function that returns a python object"""
    return json.loads(my_str)
