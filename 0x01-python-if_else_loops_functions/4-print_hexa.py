#!/usr/bin/python3
print("".join([str(num) + " " + hex(num) + "\n" if (num + 1) %
      15 != 0 else str(num) + " " + hex(num) for num in range(99)]))
