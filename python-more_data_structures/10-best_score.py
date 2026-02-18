#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_student = list(a_dictionary.keys())[0]
    max_score = a_dictionary[best_student]
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            best_student = key
    return best_student
