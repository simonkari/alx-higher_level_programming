#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number < 0:
    print(f"{number} is negative")
else:
    if number == 0:
        print(f"{number} 0 is zero")
    else:
        print(f"{number} is positive")
