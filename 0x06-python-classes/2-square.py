#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represent a Square
    Attributes:
        __size (int): size of the side of the square
    """
    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the Square
        Returns: None
        """
        if type(size) is not int:
        raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
