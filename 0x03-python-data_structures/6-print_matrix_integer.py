#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for sk in range(len(row)):

            print("{:d}".format(row[sk]), end="")
            if sk < len(row) - 1:
                print(" ", end="")
        print("")
