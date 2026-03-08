#!/usr/bin/python3
"""Resul Shafili
in this code i am using pickle for 
seria/deserilizing and returnig
"""
import pickle


class CustomObject:
"""this is a class it is a mother of all process
(i dont know how to explain)
"""
    def __init__(self, name, age, is_student):
        """this is a simple init method"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """this is a method for display variables"""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename): 
        """this is a important method. which one is serializes our data"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """this is a method for deserializing"""
        with open(filename, "rb") as f:
            x = pickle.load(f)
        return x
            
    
