#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """
    MyList class that provides a method to print a sorted list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order (sorted).
        """
        print(sorted(self))
