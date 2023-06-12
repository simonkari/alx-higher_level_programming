#!/usr/bin/python3


"""task 12 defines class MyInt that inherits from int. """


class MyInt(int):

    """Custom int type inverting behavior of != and == operators.

    """

    def __eq__(self, other):

        """Reverses == operator.

        """

        return int(self) != int(other)

    def __ne__(self, other):

        """Reverses != operator.

        """

        return int(self) == int(other)
