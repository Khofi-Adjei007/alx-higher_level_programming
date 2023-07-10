#!/usr/bin/python3
def add_attribute(obj, attr_name, attr_value):
    # Check if the object has a __dict__ attribute
    if not hasattr(obj, '__dict__'):
        # Raise a TypeError if the object can't have new attributes added
        raise TypeError("can't add new attribute")

    # Add the attribute name and value to the object
    setattr(obj, attr_name, attr_value)
