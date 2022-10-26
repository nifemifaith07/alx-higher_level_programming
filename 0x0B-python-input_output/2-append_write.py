#!/usr/bin/python3
"""Module for 2. Append to a File"""


def append_write(filename="", text=""):
    """Appends a string to a text file
    Args:
        filename (str): filename to append to
        text (str): text to append
    Returns:
        number of characters written:
    """
    with open(filename, "a", encoding="UTF-8") as file:
        return (file.write(text))
