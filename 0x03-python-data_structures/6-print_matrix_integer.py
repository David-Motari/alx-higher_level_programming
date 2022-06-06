#!/usr/bin/python3


# print_matrix_integer -  prints the matrix provided
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        i = len(matrix[x])
        for y in range(i):
            print("{:d}".format(matrix[x][y]), end=" " if y != (i - 1) else "")

        print("")
