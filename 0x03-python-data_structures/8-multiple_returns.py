#!/usr/bin/python3
def multiple_returns(sentence):

    if not sentence:
        return 0, None

    else:
        my_tuple = len(sentence), sentence[0]

    return my_tuple
    exit()
