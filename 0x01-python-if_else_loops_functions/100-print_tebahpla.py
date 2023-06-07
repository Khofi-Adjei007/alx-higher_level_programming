#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    letter = chr(i)
    case = 'lowercase' if i % 2 == 0 else 'uppercase'
    print("{:s}".format(letter.lower() if case ==
          'lowercase' else letter.upper()), end="")

print()

