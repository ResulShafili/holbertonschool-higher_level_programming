#!/usr/bin/python3
"""this code converts json to the object(python)"""
import json


def save_to_json_file(my_obj, filename):
    """convert to object method"""
    with open(filename, "w", encoding="utf-8") as f:
        """open file"""
        f.write(json.dumps(my_obj))
