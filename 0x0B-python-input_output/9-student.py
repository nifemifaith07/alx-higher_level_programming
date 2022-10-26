#!/usr/bin/python3
"""module for 9. Student to JSON"""


class Student:
    """A simple student class"""

    def __init__(self, first_name, last_name, age):
        """initializing student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__.copy()
