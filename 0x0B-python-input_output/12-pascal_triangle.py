#!/usr/bin/python3
"""Module for pascal triangle"""



def pascal_triangle(n):
    """returns list of lists of integers rep Pascal’s triangle of n:""""
    if n <= 0:
        return []
    
    triangle = [[1]]
    while len(triangle) != n:
        prev_list = triangle[-1]
        curr_list = [1]
        for i in range(len(prev_list) - 1):
            curr_list.append(prev_list[i] + prev_list[i + 1])
        curr_list.append(1)
        triangle.append(curr_list)
    return triangle
