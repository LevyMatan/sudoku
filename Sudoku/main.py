import solver
import numpy as np
import sys

def test_board(board):

    print(board)

b = solver.Board()

b.fill((0,0), 6)
b.fill((1,0), 5)
b.fill((1,1), 8)
b.fill((1,2), 4)
b.fill((0,1), 2)
b.fill((0, 2), 1)
b.fill((2,0), 9)
b.fill((2, 1), 3)
b.fill((2,2), 7)
# print(b[1,4])
# print(str(b.values).replace('.','').replace('[','').replace(']',''))
test_board(b)