#!/usr/bin/python3

"""Define funciton and pass it the list argument"""
def print_list_integer(my_list=[]):
    for num in my_list:
        print("{}".format(num))

# Use Case - 1
my_list = []
print_list_integer(my_list)
