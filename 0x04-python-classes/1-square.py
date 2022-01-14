#!/usr/bin/python3
"""Creating a class Square"""


class Square:
    """Derives a square"""
    def __init__(self, size=0):
        """initializes attributes
        Args:
            size (int): value to initialize `size`
        Note:
            ``Args`` section don't include `self` parameter.
        Raises:
            TypeError: if `size` isn't an integer
            ValueError: if `size` is less than 0
        """
        
        try:
            if isinstance(size, int) == True:
                if size < 0:
                    raise ValueError
            else:
                raise TypeError
        except ValueError:
            print('size must be >= 0')

        except TypeError:
            print('size must be an integer')

        else:
        self.__size = size
