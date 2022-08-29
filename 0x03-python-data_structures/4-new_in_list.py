#!/usr/bin/python3
'''
a function that replaces an element in a list at a
specific position without modifying the original list
'''


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    copy_list = my_list.copy()
    for elements in range(len(copy_list)):
        if idx == elements:
            copy_list[idx] = element
            return copy_list
