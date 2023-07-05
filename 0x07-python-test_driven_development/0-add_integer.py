#!/usr/bin/python3
"""
This is the '0-add_integer.py' module
It has a function 'add_integer' with two parameters 'a and b'
"""


def add_integer(a, b):
    """ this function adds 2 integers."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
