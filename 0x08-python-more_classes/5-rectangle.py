#!/usr/bin/python3


"""5-rectangle, built for Python project 0x08 task 5.
"""


class Rectangle:
    """A Rectangle class that takes arguments for the width and height
    of a rectangle. It contains methods for calculating the area
    and perimeter of the rectangle.

    __str__, __repr__, and __del__ fuctionality defined below.

    Args:
        width (int): horizontal dimension of a rectangle, defaults to 0
        height (int): vertical dimension of a rectangle, defaults to 0

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """fetch__width.

        Returns:
            __width (int): horizontal dimension of the  rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of the  rectangle

        Attributes:
            __width (int): representing horizontal dimension of the  rectangle

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
        """fetch__height.

        Returns:
            __height (int): vertical dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of rectangle

        Attributes:
            __height (int): represent vertical dimension of rectangle

        Raises:
            TypeError: If the provided `value` is not an int.
            ValueError: If the provided `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Returns area of rectangle of given `width` and `height`.

        Attributes:
            __width (int): represent horizontal dimension of rectangle
            __height (int): represent vertical dimension of rectangle

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle of a given `width` and `height`

        Attributes:
            __width (int): representing horizontal dimension of rectangle
            __height (int): representing vertical dimension of rectangle

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0

        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Formats a string of '#' and '\n' chars to print rectangle
        represented bycurrent instance.

        Attributes:
            __width (int): represent horizontal dimension of rectangle
            __height (int): represent vertical dimension of rectangle
            str (str): represent string to constructed for return

        Returns:
            str (str): The string suitable for printing rectangle
            (final newline omitted)

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'

            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'

        return str

    def __str__(self):
        """Allows printing of instances directly.

        Returns:
            The output of _draw_rectangle, which generate string
        representation of rectangle for printing.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval().

        Returns:
            A string of code needed to create an instance.

        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def __del__():
        """A Rectangle class that takes arguments for the width and height
        of a rectangle.it prints a message when an instance of the
        class is deleted

        """

        print('Bye rectangle...')
