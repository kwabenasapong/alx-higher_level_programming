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
        '''initialize class
        args:
            param1 (width): size of one side
            param2 (height): size of another side
        '''
        super().integer_validator(Rectangle.name_width, width)
        super().integer_validator(Rectangle.name_height, height)
        self.__width = width
        self.__height = height
