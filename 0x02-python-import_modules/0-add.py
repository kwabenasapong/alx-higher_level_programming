#!/usr/bin/python3
if __name__ == "__main__":

    from add_0 import add as add_it

    a = 1
    b = 2
    c = add_it(a, b)
    print("{0:d} + {1:d} = {2:d}".format(a, b, c))
