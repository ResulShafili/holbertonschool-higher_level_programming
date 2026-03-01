#!/usr/bin/python3
"""
This module explores multiple inheritance with Fish, Bird, and FlyingFish classes.
"""

class Fish:
    """Class representing a fish."""
    def swim(self):
        """Prints swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""
    def fly(self):
        """Prints flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird.
    This demonstrates multiple inheritance in Python.
    """
    def fly(self):
        """Overrides the fly method from Bird."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides the swim method from Fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides the habitat method from both Fish and Bird."""
        print("The flying fish lives both in water and the sky!")
