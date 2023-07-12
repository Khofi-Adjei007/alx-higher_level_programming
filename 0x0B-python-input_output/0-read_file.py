#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:

        # Read the contents of the file
        contents = file.read()

        # Print the contents to stdout
        print(contents)
