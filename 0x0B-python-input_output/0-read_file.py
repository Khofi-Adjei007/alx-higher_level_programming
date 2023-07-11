#!/usr/bin/python3

def read_file(filename=""):

    """
    Reads a UTF-8 text file and prints its contents to stdout.
    Args:
        filename (str, optional): The name of the text file to be read.
                                 Defaults to an empty string.
    Raises:
        FileNotFoundError: If the specified file does not exist,
        this exception will not be raised
        as per the requirements.
    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the contents of the file
        contents = file.read()

        # Print the contents to stdout
        print(contents)
