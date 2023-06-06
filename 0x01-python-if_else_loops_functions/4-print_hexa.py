#!/usr/bin/python3
print("".join(["{} {}\n".format(num, hex(num)) if (num + 1) % 15 !=
      0 else "{} {}\n".format(num, hex(num))[:-1] for num in range(99)]))
