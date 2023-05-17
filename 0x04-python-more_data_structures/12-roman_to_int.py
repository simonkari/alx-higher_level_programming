#!/usr/bin/python3
roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_int(roman):
    """
        This function converts roman numerals to integers
    """
    number = 0
    if isinstance(roman, str) or roman is not None:
        for sk in roman:
            number += roman_dict[sk.upper()]
        return number
    else:
        return 0
