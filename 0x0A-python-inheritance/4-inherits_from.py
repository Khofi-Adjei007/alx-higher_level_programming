#!/usr/bin/python3
def inherits_from(obj, a_class):
    # Check if the type of the object is a subclass of a_class
    # and ensure that the object is not an exact instance of a_class
    return issubclass(type(obj), a_class) and type(obj) != a_class
