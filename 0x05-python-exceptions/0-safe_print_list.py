#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Safely prints the first x elements of a list.

    Args:
        my_list (list): The list of elements to print.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed.

    Description:
        This function takes a list (my_list) and an integer (x) as input.
        It iterates over the elements in my_list and prints them on the same line, followed by a new line.
        The function stops printing after x elements, even if my_list contains more elements.
        The real number of elements printed is returned.

        If an unsupported type is encountered while iterating over my_list, a TypeError is raised.
        In such cases, an error message is printed, and the function returns the current count of printed elements.
    """
    try:
        count = 0  # Counter for the number of elements printed
        for item in my_list:
            print(item, end=' ')  # Print the element on the same line
            count += 1
            if count == x:
                break
        print()  # Print a new line
        return count
    except TypeError:
        print("Error: The list contains an unsupported type.")
        return count
