#!/usr/bin/python3
"""model that creates the 'base' class"""


class Base():
    """beginning of the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the instances in this class"""
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            id = __nb_objects += 1
