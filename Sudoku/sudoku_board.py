class SudokuBoard:

    def __init__(self, board):
        self.board = board

    def __repr__(self):
        return str(self.board)

    def is_valid(self):
        for row in self.board:
            if len(set(row)) != 9:
                return False
        for col in range(9):
            if len(set([row[col] for row in self.board])) != 9:
                return False
        for i in range(3):
            for j in range(3):
                if len(set([self.board[i * 3 + k][j * 3 + l] for k in range(3) for l in range(3)]) != 9):
                    return False
        return True

    def insert(self, row, col, value):
        if self.board[row][col] != 0:
            raise ValueError('The cell is already filled')
        exists = False
        indices = []
        if value in [row[col] for row in self.board]:
            exists = True
            indices.append((row, col))
        if value in [row[col] for col in range(9)]:
            exists = True
            indices.append((col, value))
        if value in [self.board[i * 3 + k][j * 3 + l] for k in range(3) for l in range(3)]:
            exists = True
            indices.append((i * 3 + k, j * 3 + l))
        if exists:
            return indices
        self.board[row][col] = value
        return None

