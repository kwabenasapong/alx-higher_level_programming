#!/usr/bin/python3

'''Square Class'''


class Square:
    '''A class
    that defines a square
    '''
    def __init__(self, size):
        '''__init__method for class Square

        Args:
            param1 (size): private instance attribute
        '''

        self.__size = size

        if not self.__size and self.__size != 0:
            message_1 = "size must be an integer"
            raise TypeError(message_1)
        if self.__size < 0:
            message_2 = "size must be >=0"
            raise ValueError(message_2)
