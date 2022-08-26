#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    c = add(a, b)
    d = sub(a, b)
    e = mul(a, b)
    f = div(a, b)

    print("{0:d} + {1:d} = {2:d}".format(a, b, c))
    print("{0:d} - {1:d} = {2:d}".format(a, b, d))
    print("{0:d} * {1:d} = {2:d}".format(a, b, e))
    print("{0:d} / {1:d} = {2:d}".format(a, b, f))
