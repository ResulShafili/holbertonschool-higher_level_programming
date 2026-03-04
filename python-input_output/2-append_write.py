#!/usr/bin/python3
"""this program adds somethin atthe end of text"""


def append_write(filename="", text=""):
    """metheod for adding"""
    with open(filename, "a", encoding="utf-8") as f:
        """i am opening file here for add text"""
        return f.write(text)
