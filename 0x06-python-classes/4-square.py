#!/usr/bin/python3

'''Square Class'''


class Square:
    '''A class
    that defines a square
    '''
    def __init__(self, size=0):
        '''__init__method for class Square

        Args:
            param1 (size): private instance attribute
        '''

        if not type(size) is int:
            message_1 = "size must be an integer"
            raise TypeError(message_1)
        if size < 0:
            message_2 = "size must be >= 0"
            raise ValueError(message_2)

        self.__size = size

    def area(self):
        '''Public instance method:
        def area(self): that returns
        the current square area
        '''
        return (self.__size) ** 2

    @property
    def size(self):
        '''getter for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''property setter for size
        '''
        if not type(value) is int:
            message_1 = "size must be an integer"
            raise TypeError(message_1)
        if value < 0:
            message_2 = "size must be >= 0"
            raise ValueError(message_2)

        self.__size = value
