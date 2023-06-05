#!/usr/bin/python3


"""7-rectangle, built for alx Python project 0x08 task 7.
"""


class Rectangle:
    """A Rectangle class that provides functionality
    for printing and computation of the dimensions of
    a rectangle. It includes methods for printing the
    rectangle, as well as calculating its area perimeter

    calculation of the area or perimeter. __str__, __repr__, and __del__
    fuctionality defined below.

    Attributes:
        number_of_instances (int): representing the counter
        incrementing for everyinstantiation, and decrementing
        for every instance deletion.print_symbol (str):
        representing the single characterto be used in
        assembling stringrepresentation of rectangle

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Increments `number_of_instances` and calls setters for `__width`
        and `__height`.

        Args:
            width (int): representation of the horizontal dimension
            of rectangle, defaults to 0
            height (int): representation of the vertical dimension
            of rectangle, defaults to 0

        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """fetch __width.

        Returns:
            __width (int): horizontal dimension of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of the rectangle.

        Attributes:
            __width (int): horizontal dimension of the rectangle.

        Raises:
            TypeError: If provided `value` is not an int.
            ValueError: If provided `value` is less than 0.

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
            __height (int): vertical dimension of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of the rectangle.

        Attributes:
            __height (int): represent vertical dimension of rectangle.

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
        """Returns area of rectangle of a given `width` and `height`.

        Attributes:
            __width (int): representing horizontal dimension of rectangle
            __height (int): representing vertical dimension of rectangle

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of rectangle of a given `width` and `height`

        Attributes:
            __width (int): represent the horizontal dimension of rectangle
            __height (int): represnt the vertical dimension of rectangle

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
        represented by the present instance.

        Attributes:
            __width (int): representing horizontal dimension of rectangle
            __height (int): representing vertical dimension of rectangle
            str (str): representing string to constructed for return

        Returns:
            str (str): string suitable for printing rectangle (final newline
                omitted)

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "{}".format(self.print_symbol)

            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'

        return str

    def __str__(self):
        """Allows printing of instances directly.

        Returns:
            The output of _draw_rectangle, which creates string
        representation of rectangle suitable for printing.

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
        """subtruct`number_of_instances`, then prints message upon
        deletion of instance.

        """
        cls.number_of_instances -= 1

        print('Bye rectangle...')
