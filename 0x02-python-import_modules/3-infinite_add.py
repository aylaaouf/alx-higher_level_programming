#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    argc = sys.argv[1:]
    for x in argc:
        total += int(x)
    print(total)