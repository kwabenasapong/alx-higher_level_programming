#!/usr/bin/python3
from sys import argv
'''
Write a program that prints the number of and the list of its arguments.

The output should be:
Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no arguments were passed) followed by
a new line, followed by (if at least one argument),
one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
Your code should not be executed when imported
The number of elements of argv can be retrieved by using: len(argv)
You do not have to fully understand lists yet, but imagine that argv can be 
used just like a C array: you can use an index to walk through it. There are other ways 
(which will be preferred for future project tasks), if you know them you can use them.

guillaume@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
guillaume@ubuntu:~/0x02$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x02-python-import_modules
File: 2-args.py
'''


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
