#!/usr/bin/python3
"""Create class Rectangle"""

from models.base import Base

"""Defines class rectangle that inherite from Base"""


class Rectangle(Base):
    """defines rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize attributes of rectangle class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
