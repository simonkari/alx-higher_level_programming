#!/usr/bin/python3


"""task 1 writes to a file"""


def number_of_lines(filename=""):

    """Writes sting to text file.

    Args:
        filename (str): the name of file to be opened

    """

    line_count = 0
    with open(filename, encoding='utf-8') as file:

        while True:
            line = file.readline()
            if not line:
                break

            line_count += 1

    return line_count
