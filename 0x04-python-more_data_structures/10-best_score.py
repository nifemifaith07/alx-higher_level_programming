#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    else:
        val = list(a_dictionary.values())
        key = list(a_dictionary.keys())
        return (key[val.index(max(val))])
