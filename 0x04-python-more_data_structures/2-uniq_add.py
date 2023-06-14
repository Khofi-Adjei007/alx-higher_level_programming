#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_set = set()

    # Iterate over each element in the list
    for num in my_list:
        # Add the element to the set (sets only store unique values)
        unique_set.add(num)

    # Calculate the sum of all unique integers in the set
    sum_unique = sum(unique_set)

    return sum_unique
