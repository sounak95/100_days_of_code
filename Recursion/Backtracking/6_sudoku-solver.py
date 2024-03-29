
# https://leetcode.com/problems/sudoku-solver/

class Solution(object):

    def isValid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] ==c:
                return False
            if board[row][i] ==c:
                return False
            if board[3*(row/3) + i/3][3*(col/3) + i%3]==c:
                return False

        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    for c in range(1, 10):
                        if self.isValid(board, i, j, str(c)):
                            board[i][j] = str(c)
                            if self.solveSudoku(board):
                                return True
                            # else:
                            board[i][j] ='.'
                    return False
        return True





