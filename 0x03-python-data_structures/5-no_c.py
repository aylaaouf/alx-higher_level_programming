#!/usr/bin/python3
def no_c(my_string):
    nstr = ""
    for c in range(len(my_string)):
        if my_string[c] != 'c' and my_string[c] != 'C':
            nstr += my_string[c]
    return nstr
