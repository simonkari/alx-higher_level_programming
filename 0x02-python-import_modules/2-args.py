#!/usr/bin/python3

import sys

num_args = len(args)
args = sys.argv[1:]

if __name__ == "__main__":
    if num_args == 0:
        print("0 arguments.")
    else:
        print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
        for i in range(num_args):
            print(i+1, ":", sys.argv[1])
    exit()
