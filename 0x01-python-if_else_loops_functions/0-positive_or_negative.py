#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number < 0:
    print("The number is negative")
else:
    if number == 0:
        print("The number is equal to 0")
    else:
        print("The number is positive")
 