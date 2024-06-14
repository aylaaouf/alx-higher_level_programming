#!/usr/bin/python3
output = ""
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
            output += "{}".format(i)
        else:
            output += "{}".format(i)
    print(output, end="")
