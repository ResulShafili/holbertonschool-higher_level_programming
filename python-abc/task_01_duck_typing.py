#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

"""
This program demonstrates abstract classes and duck typing with shapes.
"""

class Shape(ABC):
    """
    This is an abstract class for shapes.
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    Circle class that inherits from Shape.
    """
    def __init__(self, radius):
        """
        Initialize the circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    """
    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    This function uses duck typing. It doesn't check the type,
    it just assumes the object has area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
