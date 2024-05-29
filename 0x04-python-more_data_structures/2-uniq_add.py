#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    new = []
    for i in my_list:
        if i not in new:
            new.append(i)
            total += i
    return total
