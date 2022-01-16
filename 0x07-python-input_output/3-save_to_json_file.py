#!/usr/bin/python3
"""module that adds a json loads"""


import json


def save_to_json_file(my_obj, filename):
    """saves json to a file"""
    with open(filename, 'w', encoding='utf-8') as fn:
        x = fn.write(json.dumps(my_obj)
    return x
