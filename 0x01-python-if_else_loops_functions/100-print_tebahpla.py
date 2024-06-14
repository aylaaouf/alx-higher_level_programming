#!/usr/bin/python3
for x in range(122, 96, -1):
    output = ""
    output += chr(x) if x % 2 == 0 else chr(x - 32)
print(output)
