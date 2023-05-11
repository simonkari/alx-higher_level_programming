#!/usr/bin/python3

import sys

from calculator_1 import add, sub, mul, div

args = sys.argv[1:]
operators = {'+': add, '-': sub, '*': mul, '/': div}

if __name__ == "__main__":
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if args[1] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(args[0])
            b = int(args[2])
            operator = args[1]
            print(f"{a} {operator} {b} = {operators[operator](a, b)}")
            exit()
