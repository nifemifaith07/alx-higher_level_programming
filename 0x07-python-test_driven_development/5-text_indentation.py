#!/usr/bin/python3
"""
This is the "5-test_indentation" module
This module has one function, text_indentation(text)
"""


def text_indentation(text):
    """
    splits a text into lines along "?", ":", "."
    followed by 2 new lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for elm in text:
        if flag == 0:
            if elm == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
        if elm == '?' or elm == '.' or elm == ':':
            print(elm)
            print()
            flag = 0
        else:
            print(elm, end="")
