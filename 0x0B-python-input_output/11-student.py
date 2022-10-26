#!/usr/bin/python3
"""module for 10. Student to JSON with filter"""


class Student:
    """A simple student class
    Attributes:
        first_name (str): name of student.
        last_name (str): name of student.
        age (int): age of student.
    Methods:
        __init__ - initializes the Student instance.
        to_json - retrieves dictionary repr of Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """initializing student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attr is not None:
            dict = {ky: self.__dict__[ky] for ky in self.__dict__.keys & attr}
            return dict
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """reloads attributes in Student instance"""
        for key in json:
            self.__dict__[key] = json[key]
