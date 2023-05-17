#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    sk_dictionary = {}

    for sk, value in a_dictionary.items():
        sk_dictionary[sk] = value * 2

    return sk_dictionary
