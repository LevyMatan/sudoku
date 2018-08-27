'''
All classes and function which are about solving the board
'''

import numpy as np


class Board:


    valid_values = set(range(1,10))


    def __init__(self):
        self.values = np.full((9, 9), " ")


    def __getitem__(self, key):
        return self.values[key]


    def fill(self, index, value):
        """ index is a tuple containing where we would like to put the value"""
        i, j = index

        if not (value in Board.valid_values):
            raise Exception("You are trying to fill the board with a not valid value {}".format(value))
        
        
        if self.values[i,j] != " ":
            raise Exception("You are trying to fill a cell which is already has value!")
        
        
        self.values[i,j] = str(value)


    def __str__(self):
        b = self.values
        return """ 
        {} | {} | {} || {} | {} | {} || {} | {} | {} 
        __________________________________
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        __________________________________
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        ==================================
        {} | {} | {} || {} | {} | {} || {} | {} | {} 
        __________________________________
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        __________________________________
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        ==================================
        {} | {} | {} || {} | {} | {} || {} | {} | {} 
        __________________________________
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        __________________________________
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        """.format(
            b[0,0], b[0,1], b[0,2], b[0,3], b[0,4], b[0,5], b[0,6], b[0,7], b[0,8],
            b[1,0], b[1,1], b[1,2], b[1,3], b[1,4], b[1,5], b[1,6], b[1,7], b[1,8],
            b[2,0], b[2,1], b[2,2], b[2,3], b[2,4], b[2,5], b[2,6], b[2,7], b[2,8],
            b[3,0], b[3,1], b[3,2], b[3,3], b[3,4], b[3,5], b[3,6], b[3,7], b[3,8],
            b[4,0], b[4,1], b[4,2], b[4,3], b[4,4], b[4,5], b[4,6], b[4,7], b[4,8],
            b[5,0], b[5,1], b[5,2], b[5,3], b[5,4], b[5,5], b[5,6], b[5,7], b[5,8],
            b[6,0], b[6,1], b[6,2], b[6,3], b[6,4], b[6,5], b[6,6], b[6,7], b[6,8],
            b[7,0], b[7,1], b[7,2], b[7,3], b[7,4], b[7,5], b[7,6], b[7,7], b[7,8],
            b[8,0], b[8,1], b[8,2], b[8,3], b[8,4], b[8,5], b[8,6], b[8,7], b[8,8]
            )
        
        

        
