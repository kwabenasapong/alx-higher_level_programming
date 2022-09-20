#!/usr/bin/python3

'''Rectangle Class'''


class Rectangle:
    '''A class
    that defines a Rectangle
    '''
    def __init__(self, width=0, height=0):
        '''Intialise attributes

        Args:
        param1 width: rectangle width
        param2 height: rectangle height
        '''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width'''
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height'''
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
