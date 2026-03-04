#!/usr/bin/python3
"""code starts"""


class Student:
    """class Strudent"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name=name
        self.last_name=last_name
        self.age=age

    def class_to_json(obj):
    """
    return dict object
    """
    return obj.__dict__
    
