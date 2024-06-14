#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    new = {}
    for key, value in a_dictionary.items():
        if value % 2 == 0:
            new[key] = value * 2
    return new
