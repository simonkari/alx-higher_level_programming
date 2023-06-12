#!/usr/bin/python3


"""task 3 defines is_kind_of_cass() function"""


def is_kind_of_class(obj, a_class):

    """checks if an object is an instance of the specified class,
    or any class inherited from it.

    Args:
        obj (any): any type of object to check
        a_class (class): class to test against this object type of class

    Returns:
        True if obj is instance of a_class or a subclass of a_class,
            False otherwise.

    """

    return (isinstance(obj, a_class))
