#!/usr/bin/python3
"""
This module implements `base` class of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json
import turtle


class Base:
    """
    implementation
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization
        Args:
            id (int, optional): object id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json rep of list_dictionaries"""
        if not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json rep of list_objs to a file
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        l_dict = []
        with open(cls.__name__ +".json", "w") as jfile:
            if list_objs:
                for objs in list_objs:
                    l_dict.append(objs.to_dictionary())
            return jfile.write(cls.to_json_string(l.dict))
