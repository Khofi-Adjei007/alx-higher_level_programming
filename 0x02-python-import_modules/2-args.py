#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argStr = "{:d} argument"
    argc = len(sys.argv) - 1

    if argc == 0:
        argStr += 's.'
    elif argc == 1:
        argStr += ':'
    else:
        argStr += 's:'
    print(argStr.format(argc))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{:d}: {:s}".format(i, arg))
