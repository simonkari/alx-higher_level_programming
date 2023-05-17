#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared_row = []
        for sk in row:
            squared_row.append(sk ** 2)
        result.append(squared_row)
    return result
