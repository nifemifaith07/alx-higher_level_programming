#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The module has one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """Divides all the elements in the matrix by div"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    rowSize = None
    for lt in matrix:
        if type(lt) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if rowSize is None:
            rowSize = len(lt)
        elif rowSize != len(lt):
            raise TypeError("Each row of the matrix must have the same size")
        for i in lt:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in lt] for lt in matrix]
