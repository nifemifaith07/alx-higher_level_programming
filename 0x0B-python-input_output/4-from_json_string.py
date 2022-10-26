#!/usr/bin/python3
"""Module for 4. From JSON string to Object"""


def from_json_string(my_str):
    """Returns object represented by JSON string(my_str)"""
    return (json.loads(my_str))
