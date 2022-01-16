#!/usr/bin/python3
"""defines to_json_string function"""


import json

def to_json_string(my_obj):
    """function that returns JSON repr"""
    return json.dumps(my_obj)
