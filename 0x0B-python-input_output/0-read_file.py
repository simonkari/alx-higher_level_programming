#!/usr/bin/python3


"""task 0 defines a text file-reading function"""


def read_file(filename=""):

    """print contents of a text file and print to stdout.

    Args:
        filename (str): The name of file to be opened

    """

    with open(filename, encoding='utf-8') as file:

        print(file.read(), end='')
