#!/usr/bin/python3
"""
Resul Shafili
serializetion csv to json
"""
import csv
import json


def convert_csv_to_json(filename):
    """this function converts csv to json"""
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as csvf:
            info = list(csv.DictReader(csvf))
        with open("data.json", mode="w", encoding="utf-8") as jsf:
            x = json.dump(info, jsf, indent=4)
    except Exception:
        return None
        break
    return True 
