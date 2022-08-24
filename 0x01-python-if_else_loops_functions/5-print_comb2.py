#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        print("{0:d}{1:d}".format(i,j), end='')
        if not(i == 9 and j == 9):
            print(", ", end='')
        else:
            print("")
