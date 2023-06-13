#!/usr/bin/python3


"""task 6 defines a JSON-to-object function"""


def from_json_string(my_str):

    """Returns an object represented by a JSON string.

    Args:
        my_obj (any): the object to be serialized

    """

    import json
    return json.loads(my_str)
