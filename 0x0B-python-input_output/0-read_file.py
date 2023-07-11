#!/usr/bin/python3

def read_file(filename=""):

    """
    Reads a UTF-8 encoded text file and prints its content to stdout.
    
    Args:
        filename: The name of the file to read (optional).
                  If no filename is provided, an empty string is assumed.
    """
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
