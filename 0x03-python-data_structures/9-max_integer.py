#!/usr/bin/python3
'''
a function that finds the biggest integer of a list
'''


def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        a = 0
        for i in range(len(my_list)):
            if my_list[a] < my_list[i]:
                a = i
            else:
                continue
        return my_list[a]
