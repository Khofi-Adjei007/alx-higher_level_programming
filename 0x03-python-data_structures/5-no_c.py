#!/usr/bin/env python3
def no_c(my_string):
    string = ""

    for k in range(len(my_string)):
        if my_string[k] != "c" and my_string[k] != "C":
            string += my_string[k]

    return (string)
