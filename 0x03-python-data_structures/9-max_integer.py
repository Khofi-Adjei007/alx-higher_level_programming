#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    max_int = my_list[0]

    for k in range(0, len(my_list)):
        if my_list[k] > max_int:
            max_int = my_list[k]
    return max_int
