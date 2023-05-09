#!/usr/bin/python3
def uppercase(str):
    temp = ""
    for sk in range(len(str)):
        if (ord(str[sk]) >= 97 and ord(str[sk]) <= 122):
            temp += chr(ord(str[sk]) - 32)
            continue
        temp += str[sk]
    print('{}'.format(temp))
