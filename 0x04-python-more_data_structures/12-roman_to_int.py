#!/usr/bin/python3
def roman_to_int(roman_string):
    rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not roman_string:
        return 0
    else:
        sum = 0
        for k, v in rn.items():
            for ks in roman_string:
                if ks == k:
                    sum = sum + rn[k]
                else:
                    continue
        return sum
