#!/usr/bin/python3
class MyInt(int):
    """
    MyInt is a rebel class that inherits from int and
    inverts the behavior of the == and != operators.
    """

    def __eq__(self, other):
        """
        Override the == operator to invert its behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to invert its behavior.
        """
        return super().__eq__(other)
