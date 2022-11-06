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

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = self.height = value

    def __str__(self):
        """overides the str method"""
        return "[Square] ({}) {}/{} - {}" /
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update class square by assigning variables"""
        att = 0
        if args and len(args) != 0
