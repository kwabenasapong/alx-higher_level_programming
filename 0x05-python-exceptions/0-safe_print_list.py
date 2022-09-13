#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    y = my_list[:x]
    for a in y:
        try:
            i += 1
            print("{}".format(a), end='')

        except IndexError:
            break
    print()
    return (i)
