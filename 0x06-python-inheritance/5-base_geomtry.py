#!/usr/bin/python3
"""Creates a class base_geometry"""


class BaseGeometry():
    """Start of new class"""
    def area(self):
        """raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if value is not int:
            raise TypeError(f'{name} must be an integer')
        if value < 0:
            raise ValueError(f'{name} must be greater than 0')
