#!/usr/bin/python3
'''Base Class Module'''
import json


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initialize base class'''
        if id is not None:
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

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the json string rep of list_objs to file'''
        file_name = cls.__name__ + '.json'
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(new_list))

    def from_json_string(json_string):
        '''returns the list of json string rep json_string'''
        if json_string is not None or json_string != []:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        '''returns and instance with all attrs set'''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        '''returns list of classes for json file'''
        filename = str(cls.__name__) + '.json'
        try:
            with open(filename, 'r') as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
