#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    replaces an element in a list at a specific position
    without modifying the original list (like in C).
    """
    new_list = my_list[:]
    if 0 <= idx < len(my_list):
        new_list[idx] = element
        return (new_list)
    return (my_list)
