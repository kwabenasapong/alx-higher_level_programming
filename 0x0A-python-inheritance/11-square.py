#!/usr/bin/python3

'''Square subClass to Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass
    that defines a Square inheriting
    from the Rectangle class
    '''

    def __init__(self, size):
        '''initialize class
        args:
            param1 (width): size of one side
            param2 (height): size of another side
        '''
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Calculates the area of the rectangle'''
        return self.__size ** 2

    def __str__(self):
        '''Prints the Rectangle'''
        return "[Square] {}/{}".format(self.__size, self.__size)

    def __repr__(self):
        '''Returns str() when called'''
        return "[Square] {}/{}".format(self.__size, self.__size)
