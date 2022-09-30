#!/usr/bin/python3
'''Class to Object Module'''


def class_to_json(obj):
    '''
    function that returns the dict
    description with simple data
    structure
    '''
    return obj.__dict__
