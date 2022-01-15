#!/usr/bin/python3
"""Module for the function: inherits from"""


def inherits_from(obj, a_class):
    """Returns True if derives of a class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
