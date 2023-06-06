#!/usr/bin/python3
def uppercase(string):
    for char in string:
        uppercase_char = chr(ord(char) & ~32)
        print("{}".format(uppercase_char), end="")
    print()
