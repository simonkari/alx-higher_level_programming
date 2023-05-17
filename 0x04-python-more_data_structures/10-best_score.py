#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = None
    max_key = None
    Big = max(list(dict(a_dictionary).values()))
    for key in a_dictionary:
        if a_dictionary[key] == Big:
            return key
