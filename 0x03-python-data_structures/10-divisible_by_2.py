#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    new_list = my_list[:]
    for k in range(0, len(my_list)):
        if my_list[k] % 2 == 0:
            new_list[k] = True

        else:
            new_list[k] = False
    return new_list
