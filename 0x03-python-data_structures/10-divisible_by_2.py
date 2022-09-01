#!/usr/bin/python3
'''
a function that finds all multiples of 2 in a list
'''


def divisible_by_2(my_list=[]):
    new_list = [not i % 2 for i in my_list]
    return new_list
