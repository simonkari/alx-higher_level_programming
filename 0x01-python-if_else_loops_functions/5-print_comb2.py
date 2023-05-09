#!/usr/bin/python3
for sk in range(0, 100):
    if sk == 99:
        print("{}".format(sk))
    else:
        print("{:02}".format(sk), end=", ")
        