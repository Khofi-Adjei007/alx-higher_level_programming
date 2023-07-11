#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 encoded text file and
    returns the number of characters added.
    Args:
        filename: The name of the file to append (optional).
                  If no filename is provided, an empty string is assumed.
        text: The string to append to the file (optional).
              If no text is provided, an empty string is assumed.
    Returns:
        The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
