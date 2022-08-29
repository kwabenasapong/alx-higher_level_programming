#!/usr/bin/python3
'''
a function that removes all characters c and C from a string
'''


def no_c(my_string):
    str = ''
    for ch in range(len(my_string)):
        if 'c' in my_string[ch] or 'C' in my_string[ch]:
            continue
        else:
            str = str + my_string[ch]
    return str
