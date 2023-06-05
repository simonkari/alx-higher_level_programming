#!/usr/bin/python3


"""A rectangle class named '1-rectangle' specifically
created for Python Project 0x08 Task 1.
"""


class Rectangle:
    """At this stage, the class initializes and creates
    private instance attributes by accepting two arguments.

    Args:
        width (int): Represents the horizontal
        dimension of the rectangle. Defaults to 0.
        height (int): Represents the vertical
        dimension of the rectangle. Defaults to 0."

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """fetch __width.

        Returns:
            __width (int): horizontal dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:

            value (int): Represents the horizontal
            dimension of the rectangle.
        Attributes:

            __width (int): Represents the horizontal
            dimension of the rectangle.
        Raises:

            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0."

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')

        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """fetch __height.

        Returns:
            __height (int): Represent vertical dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): Represents the horizontal
            dimension of the rectangle.

        Attributes:
            __height (int): vertical dimension of rectangle

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0."

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
