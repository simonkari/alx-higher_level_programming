#!/usr/bin/env python3
def uppercase(str):
    """Print a string in uppercase."""
    for sk in str:
        if ord(sk) >= 97 and ord(sk) <= 122:
            sk = chr(ord(sk) - 32)
        print("{}".format(sk), end="")
    print("")
    