#!/usr/bin/python3
'''
a function that retrieves an element from a list like in C
'''


def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    for element in range(len(my_list)):
        if element == idx:
            return my_list[idx]
