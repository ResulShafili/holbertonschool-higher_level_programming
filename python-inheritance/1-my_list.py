#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    MyList class provides a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        """
        print(sorted(self))
