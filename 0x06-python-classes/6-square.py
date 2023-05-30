#!/usr/bin/python3
"""Define class Square"""


class Square:
    """
    class square with attributes:
        size
    some attributes are protected from input.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialization function."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """fetch size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """fetch the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position attribute"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate the current square area."""
        return self.__size ** 2

    def my_print(self):
        """prints the square using '#' characters,
        at the position given by the position attribute.
        """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
