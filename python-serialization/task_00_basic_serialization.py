#!/usr/bin/python3
"""Resul Shafili
this code serializes data and saves
then deserializes and returns data
"""
import json


def serialize_and_save_to_file(data, filename):
    """this is a methot and it seriaizes data"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """this is the method for deserializing"""
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f) as x
    return x
    
        
    
