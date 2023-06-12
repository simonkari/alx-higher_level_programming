#!/usr/bin/python3


"""Python - Inheritance, task 1 My list"""


class MyList(list):
    """Custom list type intended to only contain integers, inherits from list.

    """

    def print_sorted(self):
        """sorts the list in ascending orderand then prints the result

        """

        sorted_list = self[:]
        sorted_list.sort()

        print(sorted_list)
