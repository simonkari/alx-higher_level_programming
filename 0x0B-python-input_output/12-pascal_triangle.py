#!/usr/bin/python3


"""
task 14 defines a Pascal's Triangle function
"""


def pascal_triangle(n):

    """
    represent a list of lists of integers, the Pascal's triangle of
    `n`.
    """

    triangle = []

    if n <= 0:
        return triangle

    for row in range(n):
        new_row = []

        triangle.append(new_row)
        new_row.append(1)

        for col in range(1, row):
            new_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])

        if row > 0:
            new_row.append(1)

    return triangle
