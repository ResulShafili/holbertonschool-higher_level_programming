#!/usr/bin/python3
"""
This module defines a CountedIterator class that keeps track of 
the number of items iterated over.
"""

class CountedIterator:
    """
    An iterator wrapper that maintains a counter of items fetched.
    """
    def __init__(self, some_iterable):
        """
        Initializes the iterator object and the counter.
        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """
        Returns the current value of the counter.
        """
        return self.counter

    def __next__(self):
        """
        Increments the counter and returns the next item from the iterator.
        """
        item = next(self.iterator)
        # Əgər yuxarıdakı sətir StopIteration atsa, aşağıdakı sətir işləməyəcək.
        # Bu da bizim üçün doğrudur, çünki olmayan elementi saymamalıyıq.
        self.counter += 1
        return item

    def __iter__(self):
        """
        Returns itself as an iterator. 
        (Optional but good practice for iterators).
        """
        return self
