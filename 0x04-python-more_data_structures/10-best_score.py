#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = None
    neg = -1
    for k, v in a_dictionary.items():
        if v > neg:
            neg = v
            max = k
    return max
