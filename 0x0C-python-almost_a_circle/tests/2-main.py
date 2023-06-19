#!/usr/bin/python3
"""2-main"""
from models.rectangle import Rectangle

if __name__ == "__main__":
    Rectangle._id = 0  # Initialize the class attribute

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
