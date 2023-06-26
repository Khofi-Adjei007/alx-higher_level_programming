#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct (function): The function to execute.
        *args: Variable-length argument
        list to pass to the function.

    Returns:
        Any: The result of the function if executed
        successfully, None otherwise.

    Description:
        This function takes a function, fct, and a
        variable number of arguments, *args, as input.
        It attempts to execute the function
        with the provided arguments.
        If the function executes successfully,
        the result is returned.
        If an exception occurs during the execution of the function,
        an error message is printed to stderr
        with the format "Exception: <error message>",
        and None is returned.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
