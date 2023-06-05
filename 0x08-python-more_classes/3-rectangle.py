#!/usr/bin/python3


"""3-rectangle, built for alx-higher_level_programming
Python project 0x08 task 3.
"""


class Rectangle:
    """Rectangle class that takes arguments for the width and height
    of a rectangle. It contains methods for calculating the area
    and perimeter of the rectangle.

    __str__ fuctionality defined below.

    Args:
        width (int): represent horizontal dimension of rectangle, defaults to 0
        height (int): represent vertical dimension of rectangle, defaults to 0

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
            value (int): horizontal dimension of rectangle

        Attributes:
            __width (int): representing horizontal dimension of rectangle

        Raises:
            TypeError: If the provided `value` is not an int.
            ValueError: If the provided `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')

        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): vertical dimension of the rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of the rectangle

        Attributes:
            __height (int): representing vertical dimension of the  rectangle

        Raises:
            TypeError: If provided `value` is not an int.
            ValueError: If provided `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns area of a rectangle of a given `width` and `height`.

        Attributes:
            __width (int): representing horizontal dimension of rectangle
            __height (int): representing vertical dimension of rectangle

        Returns:
            Area of a rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle of given `width` and `height`

        Attributes:
            __width (int): represent horizontal dimension of rectangle
            __height (int): represent vertical dimension of rectangle

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Rectangle class that takes arguments for the width and height
        of a rectangle. It contains methods for calculating the area
        and perimeter of the rectangle. Additionally, it has a method
        for formatting a string representation of the rectangle
        using '#' and '\n' characters for printing.

        Attributes:
            __width (int): representing horizontal dimension of rectangle
            __height (int): representing vertical dimension of rectangle
            str (str): string to constructed for the  return

        Returns:
            str (str): string suitable for the  printing of a
            rectangle (final newline omitted)

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'

        return str

    def __str__(self):
        """Allows direct printing of the  instances.

        Returns:
            The output of _draw_rectangle, which creates string
        representation of a rectangle suitable for printing.

        """
        return self._draw_rectangle()
