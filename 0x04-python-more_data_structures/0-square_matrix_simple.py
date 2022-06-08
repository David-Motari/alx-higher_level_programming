#!/usr/bin/python3


# square_matrix computes the square value of
#   all integers of a matrix.
def square_matrix_simple(matrix=[]):
    # store len of matrix in rows variable.
    # store len rows in cols variable.
    # create new matrix new_matrix and return it.
    new_matrix = []
    rows = len(matrix)
    cols = len(matrix[0])
    for n in range(rows):
        # create new row
        n_row = []
        for m in range(cols):
            n_row.append((matrix[n][m] ** 2))
        new_matrix.append(n_row)
    return new_matrix
