#!/usr/bin/python3
'''Rectangle subclass Module'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle Class inherits from Base Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialize Rectangle class'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
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
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        return self.__height

    @property
    def x(self):
        '''getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter for x'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        return self.__x

    @property
    def y(self):
        '''getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter for y'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must >= 0')
        return self.__y
