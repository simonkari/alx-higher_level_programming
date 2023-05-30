#!/usr/bin/python3


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """

    def __init__(self, size=0):
        """
        initialization of data structure
        """

        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        fetch for theattribute:
        size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        set for the size attribute
        """

        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        get the area of the square
        """

        return self.__size ** 2

    def __validate_size(self, size):
        """
        validates the size of the square
        """

        if type(size) != int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        else:

            return True

        return False
