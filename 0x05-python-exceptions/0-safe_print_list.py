#!\usr\bin\python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        y = my_list[:x]
    except IndexError:
        pass
    else:
        for a in y:
            i += 1
            print("{}".format(a), end='')
            print()
    return (i)
