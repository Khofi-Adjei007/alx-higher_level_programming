#!/usr/bin/python3
from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Initialize private width and height attributes
        self.__width = 0
        self.__height = 0

        # Validate and assign the width and height values
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        # Calculate and return the area based on the private width and height attributes
        return self.__width * self.__height
