#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    from sys import argv


# variables for initialization
    error_arg_msg = 'Usage: ./100-my_calculator.py <a> <operator> <b>'
    error_opr_msg = 'Unknown operator. Available operators: +, -, * and /'
    opr = ["+", "-", "*", "/"]

# Initial Conditions for calculator to work
    num_args = len(argv)
    if num_args != 4:
        print(error_arg_msg)
        exit(1)

    else:
        a = int(argv[1])
        b = int(argv[3])
        c = add(a, b)
        d = sub(a, b)
        e = mul(a, b)
        f = div(a, b)

# Calculate the Arguments
        if argv[2] == opr[0]:  # Addition operation
            print("{0:d} + {1:d} = {2:d}".format(a, b, c))
        elif argv[2] == opr[1]:  # Subtraction operation
            print("{0:d} - {1:d} = {2:d}".format(a, b, d))
        elif argv[2] == opr[2]:  # Multiplication operation
            print("{0:d} * {1:d} = {2:d}".format(a, b, e))
        elif argv[2] == opr[3]:  # Division operation
            print("{0:d} / {1:d} = {2:d}".format(a, b, f))
        else:
            print(error_opr_msg)
            exit(1)
