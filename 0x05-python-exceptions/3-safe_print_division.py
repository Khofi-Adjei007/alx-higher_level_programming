#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Safely divides two integers and prints the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float or None: The result of the division, or None if division by zero occurs.

    Description:
        This function takes two integers, a (numerator) and b (denominator), as input.
        It performs the division operation a / b and handles potential exceptions.

        If b is 0, a ZeroDivisionError occurs, and None is returned. Otherwise, the division is successful,
        and the result is stored in the 'result' variable.

        The function then enters the 'finally' block, where it prints the result using "{}".format() to format it,
        preceded by the text 'Inside result:'.

        Finally, the function returns the result, which can be a float or None.

        The use of try-except-finally allows for proper exception handling and ensures that the result is always printed.
    """
    result = None  # Initialize result to None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
