#!/usr/bin/python3

'''Rectangle Class'''


class Rectangle:
    '''A class
    that defines a Rectangle
    '''
    number_of_instances = 0  # class variable, counting the no of instances

    def __init__(self, width=0, height=0):
        '''Intialise attributes

        Args:
        param1 width: rectangle width
        param2 height: rectangle height
        '''

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def area(self):
        '''returns area of rectangle'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''returns rectangle perimeter'''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        '''for printing the rectangle class'''
        if self.__height == 0 or self.__width == 0:
            return ''
        else:
            k = ''
            for h in range(self.__height):
                for w in range(self.__width):
                    k = k + '#'
                k = k + '\n'
            return k[: -1]

    def __repr__(self):
        '''for parsing and printing the rectangle class'''
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
