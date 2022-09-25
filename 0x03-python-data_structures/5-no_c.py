#!/usr/bin/python3

def no_c(my_string):
    """
    removes all characters c and C from a string.
    """
    new_string = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            new_string += x
    return (new_string)
