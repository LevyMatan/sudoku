import unittest

class SudokuBoardTest(unittest.TestCase):

    def test_is_valid(self):
        board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [4, 5, 6, 7, 8, 9, 1, 2, 3],
                 [7, 8, 9, 1, 2, 3, 4, 5, 6],
                 [2, 3, 4, 5, 6, 7, 8, 9, 1],
                 [5, 6, 7, 8, 9, 1, 2, 3, 4],
                 [8, 9, 1, 2, 3, 4, 5, 6, 7],
                 [3, 4, 5, 6, 7, 8, 9, 1, 2],
                 [6, 7, 8, 9, 1, 2, 3, 4, 5],
                 [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        board_obj = SudokuBoard(board)
        self.assertTrue(board_obj.is_valid())

    def test_insert(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        board_obj = SudokuBoard(board)
        board_obj.insert(0, 0, 1)
        self.assertEqual(board_obj.board[0][0], 1)
        self.assertEqual(board_obj.insert(0, 0, 1), None)
        self.assertEqual(board_obj.insert(1, 1, 1), [(1, 1)])


if __name__ == '__main__':
    unittest.main()
