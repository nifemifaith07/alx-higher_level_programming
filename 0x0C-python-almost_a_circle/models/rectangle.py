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

    def check_val_type(self, name: str, value: object, flag=False):
        """type and value validator"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not flag:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self) -> int:
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width: int):
        """width setter"""
        self.check_val_type('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height: int):
        """height setter"""
        self.check_val_type('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x: int):
        """x setter"""
        self.check_val_type('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y: int):
        """y setter"""
        self.check_val_type('y', y, True)
        self.__y = y

    def area(self) -> int:
        """area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the shape of the rectangle"""
        print('\n'*self.y, end='')
        for len in range(self.height):
            print(' '*self.x + '#'*self.width)

    def __str__(self) -> str:
        """overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
            Update Multiple Atrr of The Rectangle
        """
        a = 0
        if args:
            for arg in args:
                if a == 0:
                    self.id = arg
                if a == 1:
                    self.width = arg
                if a == 2:
                    self.height = arg
                if a == 3:
                    self.x = arg
                if a == 4:
                    self.y = arg
                a += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg)

    def to_dictionary(self):
        """
            returns the dictionary
            representation of a Rectangle
        """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
