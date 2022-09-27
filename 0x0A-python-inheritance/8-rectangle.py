#!/usr/bin/python3

'''Rectangle subClass to BaseGeometry'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass
    that defines a Rectangle inheriting
    from the BaseGeometry class
    '''

    def __init__(self, width, height):
        '''initialize class
        args:
            param1 (width): size of one side
            param2 (height): size of another side
        '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
