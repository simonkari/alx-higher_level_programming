#!/usr/bin/python3


"""task 8 rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """derives from BaseGeometry, use with rectangular constructs.

    Args:
        width (int): x dimension of rectangle
        height (int): y dimension of rectangle

    Attributes:
        __width (int): x dimension of rectangle
        __height (int): y dimension of rectangle

    """
    def __init__(self, width, height):
        super().integer_validator("width", width)

        self.__width = width
        super().integer_validator("height", height)

        self.__height = height

    def area(self):

        """he code returns the area of a rectangle calculated by
        multiplying its width by its height.

        Attributes:
            __width (int): x dimension of rectangle
            __height (int): y dimension of rectangle

        Returns:
            __width * __height

        """
        return self.__width * self.__height

    def __str__(self):
        """ provides a string representation of a Rectangle
        object that can be printed or displayed.

        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
