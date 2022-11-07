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
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json rep of list_objs to a file
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        l_dict = []
        if list_objs:
            for objs in list_objs:
                l_dict.append(objs.to_dictionary())
        with open(filename, "w") as jfile:
            return jfile.write(cls.to_json_string(l_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string rep json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instances with all attr already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(5, 10)
            else:
                new = cls(5)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        file = cls.__name__ + ".json"
        try:
            with open(file, "r") as jfile:
                l_dict = cls.from_json_string(jfile.read())
                return [cls.create(**dict) for dict in l_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file"""
        ld = []
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as csvfile:
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        ld.append([
                            obj.id, obj.width, obj.height, obj.x, obj.y])
                    else:
                        ld.append([obj.id, obj.size, obj.x, obj.y])
            writer = csv.writer(csvfile)
            for row in ld:
                writer.writerow(row)


    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file"""
        try:
            ld = []
            with open(cls.__name__ + ".csv", "r" encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for key, val in row.items:
                        row[key] = int[val]
                ld.append(row)
                return [cls.create(**d) for d in ld]
        except FileNotFoundError:
            return []
