#!/usr/bin/python3
'''Append_write module'''


def append_write(filename="", text=""):
    '''
    function that appends at the end of a text
    file (UTF8) and returns the no of chars
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        output = f.write(text)
        return (output)
