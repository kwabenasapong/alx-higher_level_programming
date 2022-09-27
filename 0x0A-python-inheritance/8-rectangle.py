#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''Rectangle subClass to BaseGeometry'''


class Rectangle(BaseGeometry):
    '''A subclass
    that defines a Rectangle inheriting
    from the BaseGeometry class
    '''

    name_width = 'Width'
    name_height = 'Height'


    def __init__(self, width, height):
        '''initialize class'''
        self.__width = width
        self.__height = height

        super().integer_validator(Rectangle.name_width, self.__width)
        super().integer_validator(Rectangle.name_height, self.__height)
