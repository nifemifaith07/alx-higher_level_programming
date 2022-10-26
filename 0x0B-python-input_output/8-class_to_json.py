#!/usr/bin/python3
"""returns the dictionary description with simple data
structure for JSON serialization of an object:
"""


def class_to_json(obj):
    """function that returns dictionary description of an object"""
    dict = {}
    if hasattr(obj, "__dict__"):
        dict = obj.__dict__.copy()
    return dict
