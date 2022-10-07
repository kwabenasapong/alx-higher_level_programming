#!/usr/bin/python3
'''Square Class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square Class inherits from Rectangle Class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialize square class'''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''print message'''
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        '''getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''for updating all initialised args'''
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.size = args[1]
                elif i == 2:
                    self.x = args[2]
                else:
                    self.y = args[3]
        else:
            keys = ['size', 'x', 'y', 'id']
            for k in kwargs.keys():
                if k in keys:
                    setattr(self, k, kwargs[k])

    def to_dictionary(self):
        '''returns dict rep of class'''
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
