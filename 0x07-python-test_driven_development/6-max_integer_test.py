#!/usr/bin/python3


"""The module provides a function called find_max_integer
which takes a list as input
"""


def max_integer(list=[]):

    """The function find_max_integer takes a list lst as
    input.It first checks if the list is empty using the
    condition if not lst.If the list is empty, it returns
    None
    """

    if len(list) == 0:

        return None
    result = list[0]
    i = 1

    while i < len(list):

        if list[i] > result:
            result = list[i]
        i += 1

    return result
