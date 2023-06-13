#!/usr/bin/python3


"""task 1 Write to a file """


def write_file(filename="", text=""):

    """Writes a string to a text file (UTF8), return the number
of characters written.

    Args:
        filename (str): the name of file to be opened
        text (str): chars to be written

    """

    with open(filename, 'w', encoding='utf-8') as file:

        chars_written = file.write(text)

        return chars_written
