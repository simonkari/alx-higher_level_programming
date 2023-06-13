#!/usr/bin/python3


"""0x0B.task 2. Append-file functionality """


def append_write(filename="", text=""):

    """Appends a string at the end of a text file (UTF8).

    Args:
        filename (str): the name of file to be opened
        text (str): string to append to the end of the file
    """

    with open(filename, 'a', encoding='utf-8') as file:

        chars_written = file.write(text)

        return chars_written
