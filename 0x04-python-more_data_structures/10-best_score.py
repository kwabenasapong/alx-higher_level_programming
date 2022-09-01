#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    if a_dictionary == {}:
        return None
    else:
        max_key = max(a_dictionary)
        return max_key
