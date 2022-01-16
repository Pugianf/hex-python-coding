#!/usr/bin/python3
"""defines a function that appends a str"""


def append_write(filename='', text=''):
    """function that appends a str"""
    with open(filename, 'a', enconding='utf-8') as a_file:
        a_file.write(text)
