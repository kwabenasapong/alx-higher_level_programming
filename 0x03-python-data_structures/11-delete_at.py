#!/usr/bin/python3
'''
a function that deletes the item at a specific position in a list
'''


def delete_at(my_list=[], idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    for idx in range(len(my_list)):
        if idx:
            del my_list[idx]
            return my_list
