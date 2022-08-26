#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    from sys import argv


# variables to be used in program
    y = argv[1]
    x = argv[3]
    a = int(y)
    b = int(x)
    error_arg_msg = 'Usage: ./100-my_calculator.py <a> <operator> <b>'
    error_opr_msg = 'Unknown operator. Available operators: +, -, * and /'
    opr = ['+', '-', '*', '/']
    c = add(a, b)
    d = sub(a, b)
    e = mul(a, b)
    f = div(a, b)


# Initial Conditions for calculator to work
    for i in range(len(argv)):
        if i != 3:
            print(error_arg_msg)
            exit(1)
        elif (
                argv[2] == opr[0] or
                argv[2] == opr[1] or
                argv[2] == opr[2] or
                argv[2] == opr[3]
                ):
            print(error_opr_msg)
            exit(1)

# Calculate the Arguments
    if argv[2] == opr[0]:  # Addition operation
        print("{0:d} + {1:d} = {2:d}".format(a, b, c))
    elif argv[2] == opr[1]:  # Subtraction operation
        print("{0:d} - {1:d} = {2:d}".format(a, b, d))
    elif argv[2] == opr[2]:  # Multiplication operation
        print("{0:d} * {1:d} = {2:d}".format(a, b, e))
    elif argv[3] == opr[3]:  # Division operation
        print("{0:d} / {1:d} = {2:d}".format(a, b, f))
