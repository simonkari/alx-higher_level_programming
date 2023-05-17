#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_integers = set()
    for sk in my_list:
        unique_integers.add(sk)

    sum_of_unique = sum(unique_integers)

    return sum_of_unique
