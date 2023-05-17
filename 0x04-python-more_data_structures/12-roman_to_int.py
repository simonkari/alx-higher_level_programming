#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    ri_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    num = 0

    for x in range(len(roman_string)):
        if ri_dict.get(roman_string[x], 0) == 0:
            return (0)

        if (x != (len(roman_string) - 1) and
                ri_dict[roman_string[x]] < ri_dict[roman_string[x + 1]]):
                num += ri_dict[roman_string[x]] * -1

        else:
            num += ri_dict[roman_string[x]]
    return (num)
