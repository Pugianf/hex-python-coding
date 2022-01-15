#!/usr/bin/python3
"""function that returns if is instance"""


def is_same_class(obj, a_class):
    """Returns: True if instance, False otherwise"""
    if type(obj) is a_class:
        return True
    return False
