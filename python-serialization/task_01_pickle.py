#!/usr/bin/python3
"""
Resul Shafili
Serialization and Deserialization using pickle.
"""
import pickle


class CustomObject:
    """A custom class to demonstrate pickling in Python."""

    def __init__(self, name, age, is_student):
        """Initialize the object with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object attributes in the specific required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object to a file. Returns None on failure."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes the object from a file. Returns None on failure."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
