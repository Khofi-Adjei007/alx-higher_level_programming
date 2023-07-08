#!/usr/bin/python3
"""
Square Module

This module demonstrates the usage of the Square
class defined in the "0-square" module.
It creates a Square object, prints its type, and
displays its dictionary representation.
"""

Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
