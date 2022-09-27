#!/usr/bin/python3
'''The float and int addition module'''


def add_integer(a, b=98):
    '''a function that adds only 2 int or float type only'''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
