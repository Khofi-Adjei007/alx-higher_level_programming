#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Safely prints the first x integers from a list.

    Args:
        my_list (list): The list of elements to access.
        x (int): The number of integers to print.

    Returns:
        int: The real number of integers printed.

    Description:
        This function takes a list (my_list) and an integer (x) as input.
        It iterates over the elements in my_list, attempts to format them as integers, and prints the integers on the same line, followed by a new line.
        Only the integers are printed; other types of values in the list are silently skipped.

        The function stops printing after x integers, even if my_list contains more integers.
        The real number of integers printed is returned.

        If an unsupported type is encountered while attempting to format an item as an integer, a ValueError or TypeError is raised.
        In such cases, the item is skipped, and the next item in the list is processed.

        If x is greater than the length of my_list, a TypeError is raised, and an error message is printed.
        The function returns the count of printed integers up to that point.
    """
    try:
        count = 0  # Counter for the number of integers printed
        for item in my_list:
            try:
                formatted_item = "{:d}".format(item)  # Attempt to format the item as an integer
                print(formatted_item, end=' ')
                count += 1
                if count == x:
                    break
            except (ValueError, TypeError):
                continue  # Skip to the next item if formatting fails for non-integer values
        print()
        return count
    except TypeError:
        print("Error: The list contains an unsupported type.")
        return count
