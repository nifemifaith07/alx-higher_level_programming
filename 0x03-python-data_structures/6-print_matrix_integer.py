#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    prints a matrix of integers.
    """
    print('\n'.join([" ".join(["{:d}".format(item)
                              for item in row]) for row in matrix]))
