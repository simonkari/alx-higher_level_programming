#!/usr/bin/python3


def raise_exception():
    try:
        raise TypeError("Error Occured")
    except TypeError as e:
        print(e)
