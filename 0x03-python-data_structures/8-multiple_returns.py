#!/usr/bin/python3
'''
a function that returns a tuple with the
length of a string and its first character
'''


def multiple_returns(sentence):
    t_sen = tuple(sentence)
    length = len(t_sen)
    first = t_sen[0]
    return length, first
