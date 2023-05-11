#!/usr/bin/env python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if (a < b):
        sk = add(a, b)

        for i in range(4, 6):
            sk = add(sk, i)

        return sk
    else:
        return sub(a, b)
    return sk
