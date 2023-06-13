#!/usr/bin/python3


"""task 3 defines a string-to-JSON function """


def to_json_string(my_obj):

    """Return the JSON representation of an object

    Args:
        my_obj (any): the object to be serialized

    """

    import json
    return json.dumps(my_obj)
