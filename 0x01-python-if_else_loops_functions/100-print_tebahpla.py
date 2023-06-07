#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    letter = chr(i)
    case = 'lowercase' if i % 2 == 0 else 'uppercase'
    print("{:s}".format(letter.upper() if case ==
          'uppercase' else letter), end="")
print()
