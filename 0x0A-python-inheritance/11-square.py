#!/usr/bin/python3


"""task 11 Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represents a subclass of Rectangle that represents
    a square rectangle

    Args:
        size (int): length

    Attributes:
        __size (int): length

    """
    def __init__(self, size):
        self.integer_validator("size", size)

        super().__init__(size, size)

        self.__size = size

    def area(self):

        """ Return a compute operation area of square

        Attributes:
            __size (int): length of side of square

        Returns:
            __size ** 2

        """

        return self.__size ** 2

    def __str__(self):

        """ Provides printable representation

        """

        return '[Square] {}/{}'.format(self.__size, self.__size)
