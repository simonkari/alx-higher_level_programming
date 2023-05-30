#!/usr/bin/python3


"""Define class Square"""


class Square:
    """
    class square with attributes:
        size
    some of the attributes are protected from input.
    instantiation with optional size.
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
        fetch size property
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        establish the size property
        """

        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        calculates area of square
        """

        return self.__size ** 2

    def my_print(self):
        """
        prints the square '#' characters
        """

        i = 0
        for i in range(0, self.__size):
            j = 0

            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        validates the size
        """

        if type(size) != int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            return True

        return False
