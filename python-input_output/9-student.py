#!/usr/bin/python3
"""code starts"""


class Student:
    """class Strudent"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return dict object
        """
        return self.__dict__
