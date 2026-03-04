#!/usr/bin/python3
"""this code converts json to the object(python)"""
import json


def load_from_json_file(filename):
    """convert to object method"""
    with open(filename, "w", encoding="utf-8") as f:
        """open file"""
        f.write(json.loads(JSON file))
