#!/usr/bin/python3


"""Define class Square"""


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        initialization data structure
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        fetch for the size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size property
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        return area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints to stdout the square with the character #
        """
        i = 0
        for i in range(0, self.__size):
            j = 0
            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        validates size, check errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
