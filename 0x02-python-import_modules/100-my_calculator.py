#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

# Check if the module is being run as a standalone script
if __name__ == "__main__":
    argc = len(argv) - 1  # Count the number of command-line arguments (excluding the script name)

    # Check if the correct number of arguments is provided
    if argc != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    # Assign the appropriate function based on the operator provided
    if argv[2] == '+':
        func = add
    elif argv[2] == '-':
        func = sub
    elif argv[2] == '*':
        func = mul
    elif argv[2] == '/':
        func = div
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)

    # Perform the calculation using the selected function
    result = func(int(argv[1]), int(argv[3]))

    # Print the formatted calculation result
    print("{:d} {:s} {:d} = {:d}".format(int(argv[1]), argv[2], int(argv[3]), result))
