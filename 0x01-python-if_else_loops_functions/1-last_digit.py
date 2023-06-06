#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

new_positive_number = number % 10
new_zero_number = number % 10
new_negative_number = -number % 10

if new_positive_number > 5:
    print(
        f"Last digit of {number} is {new_positive_number} and is greater than 5")
elif new_zero_number == 0:
    print(f"Last digit of {number} is {new_zero_number} and is 0")
elif new_negative_number:
    print(
        f"Last digit of {number} is {new_negative_number} and is less than 6 and not 0")

