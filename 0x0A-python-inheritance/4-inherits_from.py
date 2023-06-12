#!/usr/bin/python3


"""task 4 defines inherits_form() function"""


def inherits_from(obj, a_class):
    """checks whether an object is an instance of a
    class inherited from a class

    Args:
        obj (any): Any type of object to be inherited
        a_class (class): class to test against inherited classes of this class

    Returns:
        True if obj is an instance of a subclass of a_class,
        False otherwise. If obj is not an instance of a_class then return
        False and return True otherwise return False

    """

    if type(obj) == a_class:
        return (False)

    return (issubclass(type(obj), a_class))
