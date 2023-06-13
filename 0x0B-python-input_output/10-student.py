#!/usr/bin/python3
"""
task 12 defines a class student
"""


class Student:

    """
    represents class containing student data.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """
        get dictionary representation of student, minus any elements
        whose keys are are not listed in `attrs`. If `attrs` is not a list of
        strings, returns entire dict of student.

        Args:
            attrs (list) of (str): the list of keys for items in the dictionary
        """

        ret_dict = {}
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:

                    return self.__dict_

            for key in attrs:
                if key in self.__dict__:

                    ret_dict.update({key: self.__dict__[key]})

            return ret_dict

        else:
            return self.__dict__
