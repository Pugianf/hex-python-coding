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
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """Property to retrieve the value of 'width'"""
            return self.__weight

        @property
        def height(self):
            """Property to retrieve the value of 'height'"""
            return self.__height

        @width.setter(self, width):
            """Setter to input new width value
            Args:
                width (int): value to be set
            Raises:
                TypeError: if 'width' isn't an integer
                ValueError: if 'width' is less than 0
            """
            if not isinstance(width, int):
                raise TypeError('width must be an integer')
            if (width < 0):
                raise ValueError('width must be >= 0')
            self.__width = width

        @height.setter(self, height):
            """Setter to input new height value
            Args:
                height (int): value to be set
            Raises:
                TypeError: if 'height' isn't an integer
                ValueError: if 'height' is less than 0
            """
            if not instance (height, int):
                raise TypeError('height must be an integer')
            if (height < 0):
                raise ValueError('height must be >= 0')
            self.__height = height
