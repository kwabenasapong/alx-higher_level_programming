#!/usr/bin/python3
'''MyList subclass'''


class MyList(list):
    '''Inherits from base class list'''

    def print_sorted(self):
        '''
        Public instance method:
        that prints the list, but sorted (ascending sort)
        '''
        sorted_list = []
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
