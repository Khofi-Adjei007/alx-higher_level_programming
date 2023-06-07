#!/usr/bin/python3
import sys

# Redirect the standard output to stderr
sys.stdout = sys.stderr

# Use the write function from the sys module to print the desired message
sys.stdout.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")

# Exit with status code 1
sys.exit(1)

