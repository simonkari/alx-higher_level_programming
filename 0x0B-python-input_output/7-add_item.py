#!/usr/bin/python3


"""
task 9 writes an Object to a text file,
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):

    """
    writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, 'w') as f:

        json.dump(my_obj, f)
