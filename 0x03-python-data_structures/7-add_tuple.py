#!/usr/bin/python3
'''
a function that adds 2 tuples
'''


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    if (len(a) < 2 and len(a) == 1):
        a = (a[0], 0)
    elif len(a) == 0:
        a = (0, 0)
    elif (len(b) < 2 and len(b) == 1):
        b = (b[0], 0)
    elif len(b) == 0:
        b = (0, 0)
    return ("({0}, {1})". format((a[0] + b[0]), a[1] + b[1]))
