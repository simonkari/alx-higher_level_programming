#!/usr/bin/python3
"""3-main"""
from models.rectangle import Rectangle

if __name__ == "__main__":
    try:
        Rectangle(10, "2")
    except TypeError as e:
        print("[{}] {}".format(type(e).__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except ValueError as e:
        print("[{}] {}".format(type(e).__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except TypeError as e:
        print("[{}] {}".format(type(e).__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except ValueError as e:
        print("[{}] {}".format(type(e).__name__, e))
