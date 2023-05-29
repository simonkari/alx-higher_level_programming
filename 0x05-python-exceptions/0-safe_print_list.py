#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    sk = 0
    count = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[sk]), end="")
            count += 1
        except:
            continue
    print()
    return count
