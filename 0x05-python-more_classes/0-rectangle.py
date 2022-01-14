#!/usr/bin/python3
"""Creating a class rectangle"""


class Rectangle:
    """Derives a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize attributes
        Args:
            width (int): width of the rectangle
            heigth (int): height of the rectangle
        Note:
            ''Args'' section doesn't include 'self' parameter
        Raises:
            TypeError: if 'width' or 'height' isn't an integer
            ValueError: if 'width' or 'height' is less than 0
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be an integer')
        self.__width = width
        self.__height = height
