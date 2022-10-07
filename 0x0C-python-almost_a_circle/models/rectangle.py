#!/usr/bin/python3
'''Rectangle subclass Module'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle Class inherits from Base Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialize Rectangle class'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
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
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter for x'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter for y'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''area of base'''
        return self.__width * self.__height

    def display(self):
        '''Displays rectangle in # format'''
        if self.__height == 0 or self.__width == 0:
            print()
        else:
            if self.__y > 0:
                for line in range(self.__y):
                    print()

            for h in range(self.height):
                if self.__x > 0:
                    print('{}'.format(' ' * self.__x), end='')
                for w in range(self.width):
                    print('#', end='')
                print()

    def __str__(self):
        '''print message'''
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''for updating all initialised args'''
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                else:
                    self.y = args[4]
        else:
            keys = ['width', 'height', 'x', 'y', 'id']
            for k in kwargs.keys():
                if k in keys:
                    setattr(self, k, kwargs[k])

    def to_dictionary(self):
        '''returns dict rep of class'''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
