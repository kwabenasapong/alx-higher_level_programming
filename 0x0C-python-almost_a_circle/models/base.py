#!/usr/bin/python3
'''Base Class Module'''
import json
import csv
import turtle


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

    @classmethod
    def load_from_file_csv(cls):
        '''Return a list of classes instantiated from a CSV file'''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        '''
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
