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
<<<<<<< HEAD
            n_row.append((matrix[n][m]**2))
=======
            n_row.append((matrix[n][m] ** 2))
>>>>>>> 2cdd53dc430a63ab3d8cfb6ff9b2a6fdf7869a64
        new_matrix.append(n_row)
    return new_matrix
