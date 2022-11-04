#!/usr/bin/python3
"""
This module implements a Rectangle object that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle implementation"""

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """initialization"""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width: int):
        """width setter"""
        self.__width = width

    @property
    def height(self) -> int:
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height: int):
        """height setter"""
        self.__height = height

    @property
    def x(self) -> int:
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x: int):
        """x setter"""
        self.__x = x

    @property
    def y(self) -> int:
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y: int):
        """y setter"""
        self.__y = y
