#!\usr\bin\python3
'''Square Class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square Class inherits from Rectangle Class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialize square class'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''print message'''
        return '[Square] ({}) {}/{} - {}/{}'\
            .format(self.id, self.x, self.y, self.width, self.height)

    @property
    def size(self):
        '''getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for size'''
        self.width = value
        self.height = value
