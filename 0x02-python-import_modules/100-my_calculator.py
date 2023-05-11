#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


if len(sys.argv) != :
    print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
operator = sys.argv[2]

if operator == '+':
    result = add(a, b)
elif operator == '-':
    result = sub(a, b)
elif operator == '*':
    result = mul(a, b)
elif operator == '/':
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

print("{} {} {} = {}".format(a, operator, b, result))
exit()
