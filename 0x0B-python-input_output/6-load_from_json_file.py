#!/usr/bin/python3


"""task 8 JSON file-reading function"""


def load_from_json_file(filename):

    """Creates an object (python object) from a JSON file.

    Args:
        filename (str): file with serialized object string

    """

    import json
    with open(filename, encoding='utf-8') as file:

        return json.load(file)
