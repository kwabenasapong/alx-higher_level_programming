#!/usr/bin/python3

'''Square Class'''


class Square:
    '''A class
    that defines a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''__init__method for class Square

        Args:
            param1 (size): private instance attribute
            param2 (position): tuple with 2 positive integers only
        '''

        if not type(size) is int:
            message_1 = "size must be an integer"
            raise TypeError(message_1)
        if size < 0:
            message_2 = "size must be >= 0"
            raise ValueError(message_2)

        self.__size = size
        self.__position = position

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

    def my_print(self):
        '''prints square with #'''
        if self.__size == 0:
            print()
        else:
            for s1 in range(self.__size):
                print('{}'.format(self.__position[0] * ' '), end='')
                for s2 in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        '''getter for position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''setter for position'''
        message = 'position must be a tuple of 2 positive integers'
        if len(value) != 2:
            raise TypeError(message)
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError(message)
        elif value[0] < 0 or value[1] < 0:
            raise TypeError(message)
        else:
            self.__position = value
