#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    result = []
    for sk in range(len(my_list)):

        if result[sk] % 2 == 0:
            result.append(True)

        else:
            result.append(False)

    return result
