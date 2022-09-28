#!/usr/bin/python3
'''load_from_json_file module'''
import json


def load_from_json_file(filename):
    '''
    function that writes an Object to a
    text file, using a JSON representation
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        json.load(f)
