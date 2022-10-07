#!/usr/bin/python3
'''Base Class Module'''
import json


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initialize base class'''
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns json string rep of dict arg'''
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
