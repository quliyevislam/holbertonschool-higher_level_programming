#!/usr/bin/python3

def matrix_divided(matrix, div):
    error = ("div must be a number",
             "division by zero",
             "Each row of the matrix must have the same size",
             "matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError(error[0])

    if div == 0:
        raise ZeroDivisionError(error[1])

    for row in matrix:
        if len(matrix) > 1 and len(row) != len(matrix[0]):
            raise TypeError(error[2])
        temp = []
        temp = row.copy()
        for i in range(len(temp)):
            if not isinstance(temp[i], (int, float)):
                raise TypeError(error[3])
            temp[i] = round(temp[i] / div, 2)
        new_matrix.append(temp)
    return new_matrix
