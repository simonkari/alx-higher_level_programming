#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for sk in range(len(new_list)):

        if new_list[sk] == search:
            new_list[sk] = replace

    return (new_list)
