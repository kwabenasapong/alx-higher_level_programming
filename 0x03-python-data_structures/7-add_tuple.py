#!/usr/bin/python3
'''
a function that adds 2 tuples
'''


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return ("({0}, {1})". format((a[0] + b[0]), a[1] + b[1]))
