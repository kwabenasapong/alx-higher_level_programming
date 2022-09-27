#!/usr/bin/python3

'''BaseGeometry Class'''


class BaseGeometry:
    '''A class
    that defines a BaseGeometry
    '''

    def __init__(self):
        '''initialize class'''
        pass

    def area(self):
        '''Area of Geometric figure'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validates value given'''
        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
