#!/usr/bin/python3
"""module that writes and save a json to file"""


import json


def save_to_json_file(my_obj, filename):
    """writes and saves a json dumps to a new file"""
    with open(filename, 'w', encoding='utf-8') as fn:
        x = fn.write(json.dumps(my_obj)
    return x
