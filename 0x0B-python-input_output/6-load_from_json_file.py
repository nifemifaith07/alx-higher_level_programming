#!/usr/bin/python3
"""Module for 6. Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """creates an Object from a JSON file
    Args:
        filename (str): name of file
    """
    with open(filename, "r",) as j_file:
        obj = json.load(j_file)
        return obj
