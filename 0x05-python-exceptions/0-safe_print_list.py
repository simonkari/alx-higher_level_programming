#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    sk= 0
    count = 0
    try:
        for sk in range(x):
            print(my_list[sk], end=' ')
            count += 1
    except:
        pass

    print()
    return count
