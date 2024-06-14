#!/usr/bin/python3
def print_last_digit(number):
    last = str(number)[-1]
    n_int = int(last)
    print(n_int, end="")
    return n_int
