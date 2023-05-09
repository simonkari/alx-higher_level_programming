#!/usr/bin/python3

for one in range(0, 10):
    for two in range(one + 1, 10):
        if one == 8 and two == 9:
            print("{}{}".format(one, two))
        else:
            print("{}{}".format(one, two), end=", ")
