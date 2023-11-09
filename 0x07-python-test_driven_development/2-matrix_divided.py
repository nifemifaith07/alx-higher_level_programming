#!/usr/bin/python3
"""
This module divides all elements of a matrix 
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

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError('division by zero')
    if len(matrix) = 0:
        return []
    for l in matrix:
        
