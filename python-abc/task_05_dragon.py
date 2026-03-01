#!/usr/bin/python3
"""
This module demonstrates the use of Mixins to compose class behaviors.
"""

class SwimMixin:
    """
    A mixin that provides swimming functionality.
    """
    def swim(self):
        """Prints the swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """
    A mixin that provides flying functionality.
    """
    def fly(self):
        """Prints the flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that combines SwimMixin and FlyMixin.
    """
    def roar(self):
        """Prints the dragon's unique roar behavior."""
        print("The dragon roars!")
