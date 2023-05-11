#!/usr/bin/python3

import sys

args = sys.argv[1:]
num_args = len(args)

if __name__ == "__main__":
    if num_args == 0:
        print("0 arguments.")
        exit()
    else:
        print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
        for i in range(num_args):
            print(f"{i+1}: {args[i]}")
    exit()
