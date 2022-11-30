# Sudoku

This project will be devided to three main parts:
- Sudoku Solver
- Photo to Board
- Web App

[Click here](https://levymatan.github.io/sudoku/) to play on the very first board I created :)
## Sudoku solver

The solver will get an initilized board, and will output the missing numbers that solves the sudoku.
It also will check if the current board is valid (apply to all rules of the game)

## Photo to Board

The board reader takes as a input a photo of a sudoku board and output a digital version.
It should be able to tackle both hand written numbers and printed numbers.
A huerstic idea on basic steps:
1. preprocess the input image: gray scale and white balance
2. find the board
3. apply homographic transform (straighten the board)
4. split board to cells, and assgin index
5. classify each cell to one of the digits from 1 to 9 or empty cells

## Web App
An app the will warp the first two parts

Good Luck!!!
