#!/usr/bin/python3
"""task 11 defines a class student"""


class Student:
    """
    represents a class containing student data.
    """
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """fetches a dictionary representation of student, minus any elements
        whose keys are are not listed in `attrs`.

        Args:
            attrs (list) of (str): the list of keys for
            the items in the dictionary
        """
        ret_dict = {}

        if type(attrs) is list:
            for item in attrs:

                if type(item) is not str:
                    return self.__dict__

            for key in attrs:
                if key in self.__dict__:

                    ret_dict.update({key: self.__dict__[key]})
            return ret_dict

        else:
            return self.__dict__

    def reload_from_json(self, json):

        """
        Modify all attributes of student with values from dict in json file.

        Args:
            json (dict): the dictionary of items to set as attributes

        """

        for key in json:

            self.__dict__.update({key: json[key]})
