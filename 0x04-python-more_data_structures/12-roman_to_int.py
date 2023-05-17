#!/usr/bin/python3
def roman_to_int(roman_string):

    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    if not isinstance(roman_string, str):
        return 0

    number = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_map.get(char, 0)

        if value < prev_value:
            result -= value
        else:
            number += value
        prev_value = value

    return 0
