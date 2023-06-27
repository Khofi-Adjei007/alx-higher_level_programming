#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a name exception with a message.

    Args:
        message (str): The message to include in
        the exception. Default is an empty string.

    Raises:
        NameError: Always raises a
        NameError with the provided message.

    Description:
        This function raises a NameError
        exception with the given message.
        If no message is provided, an empty
        string is used as the default.
    """
    raise NameError(message)


if __name__ == "__main__":
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)
