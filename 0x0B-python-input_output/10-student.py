#!/usr/bin/python3
'''Student Module'''


class Student:
    '''Student Class'''

    first_name = ''
    last_name = ''
    age = 0

    def __init__(self, first_name, last_name, age):
        '''initialse attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary
        representation of a Student
        instance
        '''
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            in_list = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    in_list[key] = value
            return in_list
