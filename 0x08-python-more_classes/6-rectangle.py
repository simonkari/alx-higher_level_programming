#!/usr/bin/python3


"""6-rectangle, built for Python project 0x08 task 6.
"""


class Rectangle:
    """A Rectangle class that allows for printing and
    computation of the dimensions
    of a rectangle. It provides methods for printing
    the rectangle, as well as calculating its area
    and perimeter.

    A Rectangle class that takes arguments for the
    width and height of a rectangle.It contains methods
    for calculating the area and perimeter of the
    rectangle.Additionally, it defines functionality
    for
    the __str__, __repr__, and __del__ methods.

    Attributes:
        number_of_instances (int): counter incrementing for all
            instantiation, and subtracting for every instance deletion.

    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """A Rectangle class that increments number_of_instances
        and calls setters for __width and __height upon instantiation..

        Args:
            width (int): represent horizontal dimension of
            rectangle, defaults to 0
            height (int): represent vertical dimension of
            rectangle, defaults to 0

        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):

        """__width getter.

        Returns:
            __width (int): horizontal dimension of the rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle

        Attributes:
            __width (int): representing horizontal dimension of rectangle

        Raises:
            TypeError: If the provided  `value` is not an int.
            ValueError: If the provided  `value` is less than 0.

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
            __height (int): vertical dimension of the  rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of the rectangle

        Attributes:
            __height (int): represent vertical dimension of the  rectangle

        Raises:
            TypeError: If provided  `value` is not an int.
            ValueError: If provided `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Returns area of rectangle of given `width` and `height`.

        Attributes:
            __width (int): represent horizontal dimension of the rectangle
            __height (int): represent vertical dimension of the rectangle

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle of given `width` and `height`

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
        """Formats string of '#' and '\n' chars to print a rectangle
        represented by current instance.

        Attributes:
            __width (int): representing horizontal dimension of rectangle
            __height (int): representing vertical dimension of rectangle
            str (str): represent string to constructed for return

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
        """Allows printing of instances directly.

        Returns:
            The output of _draw_rectangle, which generates a string
        representation of the rectangle suitable for printing.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval().

        Returns:
            A string of code needed to create an instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """reduce `number_of_instances`, then prints message upon
        deletion.

        """
        cls.number_of_instances -= 1

        print('Bye rectangle...')
