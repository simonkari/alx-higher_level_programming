#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return None

    else:
        max_num = my_list[0]

        for sk in my_list:
            if sk > max_num:
                max_num = sk

        return max_num
