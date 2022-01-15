#!/usr/bin/python3
"""
Prototype is_same_class
"""


def is_same_class(obj, a_class):
    """checks if obj belongs to a_class class"""
    if isinstance(obj, a_class):
        return True
    return False
