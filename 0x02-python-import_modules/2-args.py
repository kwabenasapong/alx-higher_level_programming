#!/usr/bin/python3
from sys import argv


def count_args(str):
    for count in range(len(str)):
        continue
    return count


def print_args(str):
    for arg in range(len(str)):
        if arg != 0:
            print("{0:d}: {1:s}".format(arg, str[arg]))


if __name__ == "__main__":

    num_args = count_args(argv)
    if num_args == 1:
        message = 'argument:'
    elif num_args == 0:
        message = 'arguments.'
    else:
        message = 'arguments:'

    print("{0:d} {1:s}".format(num_args, message))
    print_args(argv)
