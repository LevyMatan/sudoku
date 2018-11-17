# sudoku

This project will be devided to three main parts:

1) sudoku solver:
The solver will get an initilized board, and will output the missing numbers that solves the sudoku.
It also will check if the current board is valid (apply to all rules of the game)

2) A board reader:
The board reader takes as a input a photo of a sudoku board and output a digital version.
It should be able to tackle both hand written numbers and printed numbers.

a. preprocess the input image: gray scale and white balance

b. find the board

c. apply homographic transform (straighten the board)

d. split board to cells, and assgin index

e. classify each cell to one of the digits from 1 to 9 or empty cell

3) Android app interface:
An app the will warp the first two parts


Good Luck!!!
