#!/usr/bin/python3
"""
This is the '0-add_integer.py' module
it has one funtion and recieves two parameters
"""


def add_integer(a, b=98):
    """
    Function adds two integers together
    Args
    a: int or float
    b: int or float
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
