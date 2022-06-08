#!/usr/bin/python3


# square_matrix computes the square value of
#   all integers of a matrix.
def square_matrix_simple(matrix=[]):
    nw_matrix = [[(row[i] ** 2) for row in matrix] for i in range(len(matrix))]
    return nw_matrix
