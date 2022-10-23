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
        self.__size = size

    def area(self):
        """calculates square's area
        Returns:
            Current square's area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): new value to set size to
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
