#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    numrows = len(matrix)
    numcols = len(matrix[0])
    for k in range(0, numrows):
        for a in range(0, numcols):
            if a == numcols - 1:
                print('{:d}'.format(matrix[k][a]), end='')
            else:
                print('{:d}'.format(matrix[k][a]), end=' ')
        print()
