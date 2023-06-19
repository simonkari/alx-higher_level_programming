#!/usr/bin/python3
""" 13-main """
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 2, 1, 9)
    print(r1)

    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(**r1_dictionary)
    print(r2)
    print(r1 == r2)
