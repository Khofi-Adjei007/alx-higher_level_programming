def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    Args:
        obj: An object to inspect.
    Returns:
        A list of available attributes and methods of the object.
    """
    # Use the dir() function to get a sorted list of names in the object
    # This includes attributes, methods, and special methods
    names = dir(obj)
    # Filter out names starting with '__' (double underscores)
    # as these are typically considered private or special methods
    available_names = [name for name in names if not name.startswith('__')]
    # Return the list of available attributes and methods
    return available_names
