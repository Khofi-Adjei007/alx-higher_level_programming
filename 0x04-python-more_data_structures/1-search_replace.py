#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = []

    # Iterate over each element in the original list
    for item in my_list:
        # Check if the current element matches the search element
        if item == search:
            # If it does, replace it with the new element
            new_list.append(replace)
        else:
            # If it doesn't, keep the original element
            new_list.append(item)

    return new_list
