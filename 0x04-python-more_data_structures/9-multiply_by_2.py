#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return None
    new = {}
    for i, j in a_dictionary.items():
        if j % 2 == 0:
            new[i] = j * 2
        else:
            new[i] = j
    return new
