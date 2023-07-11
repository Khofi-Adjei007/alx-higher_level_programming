#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Args:
        obj: An object to inspect.
    
    Returns:
        A list containing the names of attributes and methods of the object.
    """
    attributes_and_methods = []
    for attribute_name in obj.__dict__:
        attributes_and_methods.append(attribute_name)
    for class_name in obj.__class__.__dict__:
        attributes_and_methods.append(class_name)
    return attributes_and_methods
