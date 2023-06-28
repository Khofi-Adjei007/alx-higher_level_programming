#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """
        Initialize a Square object with an optional size.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Attributes:
            __size (int): The private instance
            attribute representing the size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size