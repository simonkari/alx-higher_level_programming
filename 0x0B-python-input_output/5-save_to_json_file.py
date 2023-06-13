#!/usr/bin/python3


"""task 7 JSON file-writing function"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file

    Args:
        my_obj (any): the object to be serialized

    """
    import json
    with open(filename, 'w', encoding='utf-8') as file:

        json.dump(my_obj, file)
