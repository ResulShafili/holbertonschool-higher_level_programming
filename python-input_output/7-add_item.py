#!/usr/bin/python3
"""this is code"""
import 5-save_to_json_file.py from save_to_json_file
import 6-load_from_json_file.py from load_from_json_file


with open("add_item.json", "w", encoding="utf-8") as f:
    f.save_to_json_file()
    f.load_from_json_file()
