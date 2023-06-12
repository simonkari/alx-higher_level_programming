#!/usr/bin/python3


"""task 13 defines the function that adds attributes to objects"""


def add_attribute(obj, attribute, value):

    """Update `attribute` with `value`.

    Args:
        obj (any): the object to have attribute set
        attribute (str): the name of new/updated attribute
        value (any): the value to set to attribute

    Raises:
        TypeError: When adding or updating attribute not possible.

    """

    if hasattr(obj, "__dict__"):

        setattr(obj, attribute, value)

    elif hasattr(obj, "__slots__") and attribute in obj.__slots__:

        setattr(obj, attribute, value)

    else:

        raise TypeError("can't add new attribute")
