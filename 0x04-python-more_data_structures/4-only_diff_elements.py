#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the elements present in only one set
    diff_set = set()

    # Find elements in set_1 that are not in set_2
    for element in set_1:
        if element not in set_2:
            diff_set.add(element)

    # Find elements in set_2 that are not in set_1
    for element in set_2:
        if element not in set_1:
            diff_set.add(element)

    return diff_set
