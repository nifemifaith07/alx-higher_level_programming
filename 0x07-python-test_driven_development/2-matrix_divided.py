#!/usr/bin/python3
"""
This module divides all elements of a matrix
matrix: list of lists of ints/floats
"""


def matrix_divided(matrix, div):
    """
    This function divides all element of matrix by div
    Returns a new matrix
    matrix: list of lists of ints ot floats
    div: ints or floats
    """
    error_msg = 'matrix must be a matrix (list of lists) of integers/floats'

    if not isinstance(matrix, list):
        raise TypeError(error_msg)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix) == 0:
        return []
    row_len = len(matrix[0])

    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        if row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for elm in row:
            if not isinstance(elm, (int, float)):
                raise TypeError(error_msg)
    return [[round(elm / div, 2) for elm in row] for row in matrix]
