#!/usr/bin/python3


"""task 7 validation of integers"""


class BaseGeometry:

    """An empty area() method.

    """
    def area(self):

        """Raises exception to notify user.

        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):

        """Public instance method: that validates value

        Args:
            name (str): the name that is bound to the object
            value (any): value of object.

        Exceptions:
            TypeError: if `value` is not an int
            ValueError: if `value` is less than or equal to 0

        """

        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
