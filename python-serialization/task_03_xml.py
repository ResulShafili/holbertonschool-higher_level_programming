#!/usr/bin/python3
"""
Resul Shafili
this code make procces witf xml files
"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """this method converts to xml"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """xml to python"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text
        return deserialized_dict
    except FileNotFoundError:
        print(f"Xəta: {filename} tapılmadı.")
        return None
    except Exception as e:
        print(f"Gözlənilməz xəta: {e}")
        return None
