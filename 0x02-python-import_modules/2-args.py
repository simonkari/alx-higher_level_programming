#!/usr/bin/python3

import sys

num_args = len(sys.argv) 1

if __name__ == "__main__":

    # number of arguments
    if num_args == 1:
        print("argument: ", end="")
    else:
        print("arguments: ", end="")
    print(num_args, end="")

    # list of arguments
    if num_args == 0:
        print("0 arguments.")
    else:
        print(":")
        for i in range(num_args):
            print(i+1, ":", sys.argv[i+1])
    exit()
