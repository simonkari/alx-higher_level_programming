#!/usr/bin/python3
def best_score(a_dict):
    max_score = None
    max_key = None
    for key, value in a_dict.items():

        if isinstance(value, int) and (max_score is None or value > max_score):
            max_score = value
            max_key = key

    return max_key
