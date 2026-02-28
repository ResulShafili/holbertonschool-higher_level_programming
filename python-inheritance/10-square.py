#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry.
"""
Square = __import__('10-square').Square


class Rectangle(Square):
    """
    Rectangle class that inherits from Square.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle and validates width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
