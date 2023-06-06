#!/usr/bin/python3
print("".join(chr(x) for x in range(ord('a'), ord('z')+1) if chr(x) not in ('q', 'e')), end='')
