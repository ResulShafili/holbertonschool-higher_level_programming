#!/usr/bin/python3

class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list):
            return self.__dict__

        res = {}
        for attr in attrs:
            if isinstance(attr, str) and hasattr(self, attr):
                res[attr] = getattr(self, attr)
        
        return res
