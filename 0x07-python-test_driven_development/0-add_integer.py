#!/usr/bin/python3


"""Module created for alx project Python 0x07 task 0.
"""


def add_integer(a, b=98):
    """A function is a block of code that performs a specific task.
    In this case, the task is to add two integers together.
    The function takes two integer inputs and returns the
    result of their addition.

    Args:
        a ((int, (float)): represent the first arg
        to add to the sum.
        b ((int, (float)): represent the second arg
        to add to sum. Defaults to 98.

    Returns: sum of all values.

    """
    if type(a) is float:
        a = int(a)

    elif type(a) is not int:
        raise TypeError('a must be an integer')

    if type(b) is float:
        b = int(b)

    elif type(b) is not int:
        raise TypeError('b must be an integer')

    return a + b
