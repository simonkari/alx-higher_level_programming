#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """Represents a square.
    class square that has attribute: size.
    creation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initialization of data."""

        self.__size = size
