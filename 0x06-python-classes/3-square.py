#!/usr/bin/python3
"""defines a square"""


class Square:
    """Represents a square
    Attributes:
    __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
         """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates square's area
        Returns:
            Current square's area
         """
        return (self.__size) ** 2
