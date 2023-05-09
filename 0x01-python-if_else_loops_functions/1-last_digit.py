#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print("Last digit of {} is {} and is ".format(number, digit), end="")
if digit > 5:
    print(f"The digit is greater than 5")
else:
    if digit == 0:
        print(f"The digit is equal to 0")
    else:
        print(f"The digit isless than 6 and not 0")
