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
def roman_to_int(roman_string):
    number = 0

    if isinstance(roman_string, str) or roman_string is not None:

        for c in roman_string:
            number += roman_dict[c.upper()]
        return number

    else:
        return 0
