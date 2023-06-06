#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
ans = [number]

for answer in ans[-1:]:
    if answer > 5:
        print(f"Last digit of the number is {answer} and is greater than 5")

    elif answer == 0:
        print(f"Last digit of the number is {answer} and is 0")
    else:
        print(
            f"Last digit of the number is {answer} and is less than 6 and not 0")

