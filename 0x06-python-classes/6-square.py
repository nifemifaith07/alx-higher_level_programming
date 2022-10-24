#!/usr/bin/python3
"""defines a square"""


class Square:
    """Represents a square
    Attributes:
    __size (int): size of a side of the square
    __positiin (tuple): ppsition of square in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
            size (int): size of a side of the square
            position (tuple): position of a square in 2D space
        Returns:
            None
         """
        self.__size = size
        self.__position = position

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
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("".join([" " for j in range(self.__position[0])]), end="")
            print("".join(["#" for a in range(self.__size)]))

    @property
    def position(self):
        """getter of __position
        Returns:
            position of square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or if len(value) != 2 or \
        if type(value[0]) is not int or value[0] is < 0 or \
        if type(value[1]) is not int of value[1] is < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value    
