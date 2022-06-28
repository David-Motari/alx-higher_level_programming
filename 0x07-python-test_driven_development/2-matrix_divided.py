#!/usr/bin/python3
"""
2-matrix_divided.py
divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    args: matrix - list of integers of floats, \
        div - integer that divides the matrix.
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not isinstance(matrix[0], list) or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    initial_row_len = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if initial_row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for num in row:
            if type(num) not in (float, int):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            new_row.append(round(num/div, 2))
        new_matrix.append(new_row)
    return(new_matrix)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")