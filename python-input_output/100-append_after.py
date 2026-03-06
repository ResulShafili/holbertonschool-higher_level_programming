#!/usr/bin/python3
"""
this is advanced task code
Resul Shafili
"""


def append_after(filename="", search_string="", new_string=""):
    """this is main method for adding text"""
    final = []
    with open(filename, "r", encoding="utf-8") as f:
        """this code piece is for searching"""
        for line in f:
            """i separeted main text line by line"""
            final.append(line)
            if search_string in line:
                """in here i am adding new string to here"""
                final.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        return f.writelines(final)
