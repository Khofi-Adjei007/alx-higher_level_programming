#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        # Raise an exception indicating that the area() method is not implemented
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        # Check if the value is not an integer and raise a TypeError exception
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        # Check if the value is less than or equal to 0 and raise a ValueError exception
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
