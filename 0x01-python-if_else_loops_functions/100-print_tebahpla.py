#!/usr/bin/python3
for x in range(26):
    if x % 2 == 0:
        co = 32
    else:
        co = 0
    print("{}".format(chr((26 - x + 64) + co)), end="")
