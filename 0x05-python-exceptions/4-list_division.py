#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Performs element-wise division between two lists and returns a new list.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of the new list.

    Returns:
        list: A new list of length `list_length` containing the division results.

    Description:
        This function takes two lists, my_list_1 and my_list_2, as well as an integer list_length, as input.
        It performs element-wise division between the two lists and returns a new list containing the division results.

        The function iterates over the range of list_length and performs division element by element.
        If both lists have elements at the current index, the division is performed using the numerator from my_list_1
        and the denominator from my_list_2.

        The function handles potential exceptions using try-except blocks:
        - If division by zero occurs, it catches the ZeroDivisionError and prints "division by 0".
        - If the index is out of range for either list, it catches the IndexError and prints "out of range".
        - If an element in either list is not an integer or float, it catches the TypeError or ValueError and prints "wrong type".

        The function appends the division result to a new_list during each iteration.
        Finally, it returns the new_list containing the division results.

        Note: If an exception occurs, the division result for that element is considered as 0.

    """
    new_list = []  # Initialize an empty list to store the division results
    for i in range(list_length):
        try:
            result = 0  # Initialize the result to 0
            if i < len(my_list_1) and i < len(my_list_2):  # Check if the index is within the bounds of both lists
                numerator = my_list_1[i]
                denominator = my_list_2[i]
                result = numerator / denominator  # Perform division
            elif i >= len(my_list_1) or i >= len(my_list_2):  # If the index is out of range for either list
                raise IndexError  # Raise an IndexError to indicate that the lists are too short
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            new_list.append(result)  # Append the division result to the new list
    return new_list
