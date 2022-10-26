#!/usr/bin/python3
"""Module for 5. Save Object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj (str): python object
        filename (str): text file to save JSON representation
    """
    with open(filename, "w" ,) as j_file:
        json.dump(my_obj, j_file)
