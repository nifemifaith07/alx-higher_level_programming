#!/usr/bin/python3
"""
This module implements class Square that inherits from class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square implementation"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.size

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = self.height = value
        self.size = value

    def __str__(self):
        """overides the str method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)
