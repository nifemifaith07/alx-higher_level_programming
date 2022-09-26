#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds two tuple
    Returns a tuple with 2 integers:
    The first element should be the addition of the first element of each argument
    The second element should be the addition of the second element of each argument
    """
    a, b = len(tuple_a), len(tuple_b)
    tuple_n = ((tuple_a[0] if a >= 1 else 0) + (tuple_b[0] if a >= 1 else 0),
               (tuple_a[1] if a >= 2 else 0) + (tuple_b[1] if a >= 2 else 0))
    return (tuple_n)
