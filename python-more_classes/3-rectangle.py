#!/usr/bin/python3
"""
Class rectangle
"""


class Rectangle:
    """represents Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Creates rectangle object
        Args:
            width (int):
            height (int):
        """
        self.width = width
        self.height = height 

    @property
    def width(self):
        """This is Getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """This is setter for Width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This is Getter height."""
        return self.__height

    @height.setter
    def height(self, value):
        """This is setter for Height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of Rectangle   (width*height)"""
        return self.__width * self.__height

    def perimeter(self):
        """
        perimeter of the rectangle if h or w
        0 perimeter 0 else 2*(width+height)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """show rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        for i in range(self.__height):
            rect_str += "#" * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str
