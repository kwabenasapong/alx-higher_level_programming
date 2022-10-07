#!/usr/bin/python3
'''Base Class Module'''


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
