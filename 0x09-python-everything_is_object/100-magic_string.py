#!/usr/bin/python3
def magic_string(n):
    result = ""
    for sk in range(1, n + 1):
        result += "BestSchool" * sk
    return result
