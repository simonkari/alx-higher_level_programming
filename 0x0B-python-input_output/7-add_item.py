#!/usr/bin/python3


"""task 7 writes an Object to a text file,
using a JSON representation"""


import sys
import json


def save_to_json_file(obj, filename):
    with open(filename, 'w') as file:
        json.dump(obj, file)


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


if __name__ == '__main__':
    argv_edit = sys.argv[1:]

    try:
        content_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        content_list = []
    finally:
        content_list.extend(argv_edit)
        save_to_json_file(content_list, "add_item.json")
