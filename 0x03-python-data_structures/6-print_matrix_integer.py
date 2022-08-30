#!/usr/bin/python3
'''
a function that prints a matrix of integers
'''


def print_matrix_integer(matrix=[[]]):
    num = len(matrix)
    i = 0
    while i < num:
        for m in matrix[i]:
            end = " " if m != matrix[i][-1] else ""
            print('{:d}'.format(m), end=end)
        i = i + 1
        print('')
