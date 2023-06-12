#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_list = list(tuple_a)
    b_list = list(tuple_b)
    for k in range(2):
        a_list.append(0)
        b_list.append(0)
    sum_0 = a_list[0] + b_list[0]
    sum_1 = a_list[1] + b_list[1]
    tuple_c = (sum_0, sum_1)
    return tuple_c
