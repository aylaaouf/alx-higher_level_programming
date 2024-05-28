#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    result = []
    for row in matrix:
        new = []
        for i in row:
            new.append(i**2)
        result.append(new)
    return result
