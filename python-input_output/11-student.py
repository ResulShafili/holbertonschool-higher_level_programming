#!/usr/bin/python3
"""
Module for Student class
"""


class Student:
    """
    Defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize student attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary version of the student
        """
        if not isinstance(attrs, list):
            return self.__dict__

        res = {}
        for attr in attrs:
            if isinstance(attr, str) and hasattr(self, attr):
                res[attr] = getattr(self, attr)

        return res

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
