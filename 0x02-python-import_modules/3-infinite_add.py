#!/usr/bin/python3
import sys

# Check if the module is being run as a standalone script
if __name__ == "__main__":
    argc = len(sys.argv) - 1  # Count the number of command-line arguments (excluding the script name)

    i = 0  # Initialize the index for iterating over command-line arguments
    result = 0  # Initialize the variable to store the sum of arguments

    for arg in sys.argv:
        if i != 0:
            result += int(arg)  # Convert the argument to an integer and add it to the result
        else:
            i += 1

    print("{:d}".format(result))  # Print the sum of the arguments
