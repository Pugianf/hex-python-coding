#!/usr/bin/python3
"""model that creates the 'base' class"""

import os.path


class Base:
    """beginning of the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the instances in this class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects += 1
