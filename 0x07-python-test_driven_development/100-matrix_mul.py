#!/usr/bin/python3
"""
this is the matrix_mul module
Contains one function "matrix_mul(m_a, m_b)"
"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices(list of lists of integers or floats)"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    len_ma =len(m_a)
    if len_ma == 0:
        raise ValueError(" m_a can't be empty")
    len_la = None
    for i in m_a:
        if type(i) is not lists:
            raise TypeError("m_a must be a list of lists")
        if len_la is None:
            len_la = len(i)
            if len_la == 0:
                raise ValueError("m_a can't be empty")
        if len_la != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for elm in i:
            if type(elm) is not int and type(elm) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    len_mb =len(m_b)
    if len_mb == 0:
        raise ValueError(" m_b can't be empty")
    len_lb = None
    for i in m_b:
        if type(i) is not lists:
            raise TypeError("m_b must be a list of lists")
         if len_lb is None:
            len_lb = len(i)
            if len_lb == 0:
                raise ValueError("m_b can't be empty")
        if len_lb != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for elm in i:
            if type(elm) is not int and type(elm) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len_la != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(len_ma):
        l = []
        for j in range(len_lb):
            n = 0
            for k in range(len_la):
                n += m_a[i][k] * m_b[k][j]
            l.append(n)
        matrix.append(l)
    return matrix
