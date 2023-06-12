#!/usr/bin/python3


"""Python - Inheritance, task 2 defines is_same_class() function"""


def is_same_class(obj, a_class):

    """check if an object is exactly an instance of a specific class.

    Args:
        obj (any): object of any type
        a_class (object class):

    Returns:
        obj is an instance of a_class true, False otherwise.

    """

    return (type(obj) == a_class)
