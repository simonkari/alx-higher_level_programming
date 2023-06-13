#!/usr/bin/python3


"""task 11. Student to JSON, defines a class Student"""


class Student:
    """respresents a class containing student data.

    Args:
        first_name (str): the given name of student
        last_name (str): the family name of student
        age (int): the age of student in years

    Attributes:
        first_name (str): the given name of student
        last_name (str): the family name of student
        age (int): the age of student

    """
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """fetches a dictionary representation of self.

        """

        return self.__dict__
