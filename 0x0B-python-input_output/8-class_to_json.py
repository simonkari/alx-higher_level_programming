#!/usr/bin/python3


"""
task 8. Class to JSON, Returns the dictionary description with
simple data structure
"""


def class_to_json(obj):

    """Creates a dict description of obj

    Args:
        obj (any): the object to serialized

    """

    return obj.__dict__
