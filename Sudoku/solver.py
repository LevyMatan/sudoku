'''
All classes and function which are about solving the board
'''

import numpy as np


class Board:


    valid_values = set(range(1,10))


    def __init__(self):
        self.values = np.full((9, 9), None)


    def __getitem__(self, key):
        return self.values[key]


    def fill(self, index, value):
        """ 
        fill inserts a value to the cell by its index, 
        while making sure the number inserted obeys the rules
        of the game:
        * The value is in the range(1,10)
        * The given value doesn't appear already in the same raw, 
          column or square
        * The given cell is not already filled

        input: 
        index - (i,j) tuple, while i,j in range(0,9) 

        output:
        ["OK"] - if the value inserted successfully
        ["row", i] - if the value already apears in the row
        ["column", j] - if the value already apears in the column
        ["square", value, (i//3)*3 + j//3)] - if the value already apears in the sqaure
        ["invalid"] -  if the value is not in the allowed range]
        ["taken", (i,j)] - if the cell we are trying to fill is filled
        
        $ example
        -- fill((0,3), 7)
        """
        i, j = index

        if not (value in Board.valid_values):
            raise Exception("You are trying to fill the board with a not valid value {}".format(value))
            # return ["invalid"]
        
        
        if self.values[i,j]:
            raise Exception("You are trying to fill a cell which is already has value!")
            # return ["taken", (i,j)]
        
        # check for value in the given row
        if value in self.values[i,:]:
            raise Exception("The value {} already apears in the {}'th row".format(value, i))
            # return ["row", i]


        # check for value in the given column
        if value in self.values[:,j]:
            raise Exception("The value {} already apears in the {}'th column".format(value, j))
            # return ["column", j]

        # check for value in the given square
        if value in self.values[i-i%3 : i-i%3+3, j-j%3 : j-j%3+3]:
            raise Exception("The value {} already apears in the {}'th square".format(value, (i//3)*3 + j//3))
            # return ["square", (i//3)*3 + j//3)]
        
        
        self.values[i,j] = value
        # return ["OK"]


    def __str__(self):
        b = self.values.copy()
        b = b.astype(str)
        b[b == "None"] = " "
    
        return """ 
        {} | {} | {} || {} | {} | {} || {} | {} | {} 
        ==================================
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        ==================================
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        __________________________________
        {} | {} | {} || {} | {} | {} || {} | {} | {} 
        ==================================
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        ==================================
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        __________________________________
        {} | {} | {} || {} | {} | {} || {} | {} | {} 
        ==================================
        {} | {} | {} || {} | {} | {} || {} | {} | {}
        ==================================
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
        

    def validate_row(self, index):
        assert self.values.unique()

        
