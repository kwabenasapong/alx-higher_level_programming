#!/usr/bin/python
'''
a function that prints all integers of a list, in reverse order
'''


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for element in my_list:
        print("{}".format(element))
