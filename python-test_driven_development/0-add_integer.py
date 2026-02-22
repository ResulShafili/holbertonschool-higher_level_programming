#!/usr/bin/python3
"""
This module provides a function that adds two numbers.
The module contains one function, add_integer(a, b), which ensures
that the inputs are integers or floats before performing addition.
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).

    Args:
        a: The first number.
        b: The second number (defaults to 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
