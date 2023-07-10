#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list of available attributes and methods of the object.
    """
    # Use the dir() function to retrieve a list of all names associated with the object
    all_names = dir(obj)

    # Initialize an empty list to store the available attributes and methods
    available_attributes_and_methods = []

    # Iterate through each name in the list of all names
    for name in all_names:
        # Check if the name does not start with '__' (double underscores)
        if not name.startswith('__'):
            # Append the name to the list of available attributes and methods
            available_attributes_and_methods.append(name)

    # Return the final list of available attributes and methods
    return available_attributes_and_methods
