
# https://leetcode.com/problems/n-queens/

import copy
class Solution(object):
    def isSafe(self, row, col, board, n):
        duprow = row
        dupcol = col

        while(row>=0 and col>=0):
            if board[row][col] =='Q':
                return False
            row-=1
            col-=1

        col= dupcol
        row = duprow

        while(col>=0):
            if board[row][col] == 'Q':
                return False
            col-=1

        col = dupcol
        row = duprow

        while(row<n and col>=0):
            if board[row][col] == 'Q':
                return False
            col-=1
            row+=1

        return True

    def solve(self, col, board, ans, n):
        # print(board)
        if col==n:

            ans.append(copy.deepcopy(board))
            return

        for row in range(n):
            # print(self.isSafe(row, col, board, n))

            if self.isSafe(row, col, board, n):
                board[row][col] = 'Q'
                # print(row, col)
                # print(board)
                self.solve(col+1, board, ans, n)
                board[row][col] = '.'

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans=[]
        board = []
        s=['.'] *n
        for i in range(n):
            board.append(copy.deepcopy(s))

        self.solve(0, board, ans, n)
        # print(board)
        # board[0][0] ='Q'
        for i,row in enumerate(ans):
            l1 = []
            for j, item in enumerate(row):

                # print("".join(item))
                l1.append("".join(item))

            ans[i] = l1
        return ans

s=Solution()
print(s.solveNQueens(4))
