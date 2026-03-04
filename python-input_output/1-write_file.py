#!/usr/bin/python3
"""this code writes our text"""


def write_file(filename="", text=""):
    """def function"""
    with open(filename, "w", encoding="utf-8") as f:
        """create file"""
        return f.write(text)
