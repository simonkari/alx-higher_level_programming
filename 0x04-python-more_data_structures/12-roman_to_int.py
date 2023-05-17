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
    num = 0
    if isinstance(roman, str) or roman is not None:
        for c in roman:
            num += roman_dict[c.upper()]
        return num
    else:
        return 0
