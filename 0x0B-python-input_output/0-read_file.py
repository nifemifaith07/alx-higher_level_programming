#!/usr/bin/python3
"""Module for 0. Read File """


def read_file(filename=""):
    """Reads a file and prints it to STDOUT"""

    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            print(line, end="")
