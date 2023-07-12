#!/usr/bin/python3

    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Default is an empty string.

    Returns:
        None

    Raises:
        None
    """

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:

        # Read the contents of the file
        contents = file.read()

        # Print the contents to stdout
       ` print(contents)
