#!/usr/bin/python3
"""Module for 1. Write to a File"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Args:
        filename (str): Text file to overwrite
        text (str): text to write
    Returns:
        number of characters written:
    """
    with open(filename, "w", encoding="UTF-8") as file:
        return (file.write(text))
