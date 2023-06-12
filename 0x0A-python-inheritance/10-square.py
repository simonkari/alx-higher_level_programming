#!/usr/bin/python3


"""task 8 a rectangle clas"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Represent a  subclass representing a rectangle.

    Args:
        size (int): length of side of square

    Attributes:
        __size (int): length of side of square

    """

    def __init__(self, size):
        self.integer_validator("size", size)

        super().__init__(size, size)

        self.__size = size

    def area(self):

        """returns the area of a square by multiplying
        the value of its size by itself (size * size).

        * Required by task instructions, but overloading Rectangle.area() is
        superfluous here, as it has the same result.

        Attributes:
            __size (int): length of side of square

        Returns:
            __size ** 2

        """

        return self.__size ** 2
