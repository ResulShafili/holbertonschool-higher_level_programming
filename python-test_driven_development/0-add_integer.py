#!/usr/bin/python3
"""
This module contains a function that adds two integers.
The function validates if inputs are integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: first number
        b: second number
    Returns:
        Sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və Infinity yoxlaması (Overflow xətası üçün)
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
