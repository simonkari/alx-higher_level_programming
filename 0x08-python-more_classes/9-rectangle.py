#!/usr/bin/python3


"""9-rectangle, built for alx Python project 0x08 task 9.
"""


class Rectangle:
    """A Rectangle class designed for printing or computation
    of dimensions of a rectangle.

    A Rectangle class that takes arguments for the width and height
    of a rectangle. It contains methods for calculating the area
    and perimeter of the rectangle, as well as creating a square
    by making a new instance with equal sides. Additionally,
    it defines functionality for
    the __str__, __repr__, and __del__ methods.

    Attributes:
        number_of_instances (int): represent the counter
        incrementing for everyinstantiation,
        and decrementing for everyinstance deletion.
        print_symbol (str): represet the single character
        to be used in assembling string
            representation of rectangle.

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Increments `number_of_instances` and calls setters for `__width`
        and `__height`.

        Args:
            width (int): represent horizontal dimension
            of rectangle, defaults to 0
            height (int): represent vertical dimension
            of rectangle, defaults to 0

        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """fetch __width.

        Returns:
            __width (int): representing the horizontal dimension
            of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): represent horizontal dimension of the rectangle.

        Attributes:
            __width (int): represent the horizontal dimension of the rectangle.

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
            value (int): representing vertical dimension of the rectangle.

        Attributes:
            __height (int): representing vertical dimension of the rectangle.

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
        """Returns area of rectangle of given `width` and `height`.

        Attributes:
            __width (int): represent the horizontal dimension of the rectangle.
            __height (int): represent the vertical dimension of the rectangle.

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle given `width` and `height`

        Attributes:
            __width (int): represent the horizontal dimension of the rectangle.
            __height (int): represent the vertical dimension of the rectangle.

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
        (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0

        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Formats string of '#' and '\n' chars to print rectangle
        represented by current instance.

        Attributes:
            __width (int): represent the horizontal dimension of the rectangle.
            __height (int): represent the vertical dimension of the rectangle.
            str (str): represent string to constructed for return

        Returns:
            str (str): string suitable for printing rectangle
            (final newline omitted)

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
        representation of rectangle appropriate for printing.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval().

        Returns:
            A string containing code needed to create an instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """subtruct `number_of_instances`, then prints message upon
        deletion.

        """
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of instances and returns the larger.

        Args:
            rect_1 (Rectangle object): represent the first instance
            to be compared.
            rect_2 (Rectangle object): represent the second instance
            to be compared.

        Raises:
            TypeError: if `rect_1` or `rect_2` is not an instance of cls.

        Returns:
            `rect_1` if `rect_1` has an area larger than or equal to `rect_2`,
        or `rect_2` if it has the larger area

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1

        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns instance with equal sides of the length `size`.

        Args:
            size (int): represent length of sides of square, defaults to 0.

        Returns:
            the new instance of class with equal sides.

        """

        return cls(size, size)
