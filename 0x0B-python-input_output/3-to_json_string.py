#!/usr/bin/python3
'''To_JSON_string module'''
import json


def to_json_string(my_obj):
    '''
    function that returns the JSON
    representation of an object (string)
    '''
    return json.dumps(my_obj)
