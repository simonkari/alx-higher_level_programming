#!/usr/bin/python3
"""task 100 defines text file insertion functions"""


def append_after(filename="", search_string="", new_string=""):

    """
    Inserts a line of text to file after each line containing a
    string.

    Args:
        filename (str): the file to search for lines of text
        search_string (str): search term to insert after each line
        new_string (str): line to insert into file after line
        containing match string
    """

    with open(filename, 'r+', encoding='utf-8') as curr_file:

        lines = curr_file.readlines()
        curr_file.seek(0)

        for i, line in enumerate(lines):

            if search_string in line:
                lines[i] = line + new_string

        curr_file.writelines(lines)
