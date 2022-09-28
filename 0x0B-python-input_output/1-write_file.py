#!/usr/bin/python3
'''Write_file module'''


def write_file(filename="", text=""):
    '''
    function that writes a string to a text
    file (UTF8) and returns the no of chars
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        output = f.write(text)
        return (output)
