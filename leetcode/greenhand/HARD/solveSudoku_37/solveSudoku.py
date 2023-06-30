"""
author:wjw
分析：回溯算法。
"""
from collections import defaultdict
import sys

sys.setrecursionlimit(10000)

class Solution:
    def solveSudoku(self, board):
        self.find = False
        self.ans = []

        def isValid(board):

            rows = [defaultdict(int) for _ in range(n)]
            cols = [defaultdict(int) for _ in range(n)]
            boxes = [defaultdict(int) for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    if board[i][j] != '.':
                        rows[i][board[i][j]] += 1
                        cols[j][board[i][j]] += 1

                        box_index = (i // 3) * 3 + j // 3

                        boxes[box_index][board[i][j]] += 1

                        if rows[i][board[i][j]] == 2 or cols[j][board[i][j]] == 2 or boxes[box_index][board[i][j]] == 2:
                            return False
            return True

        def backtrack(board,blanks):
            if self.find:
                return

            if not isValid(board):
                return

            if blanks == []:
                self.find = True
                self.ans = board
                return

            i, j = blanks.pop(0)

            for val in range(1,10):
                board[i][j] = "{}".format(val)
                backtrack(board,blanks)

                board[i][j]='.'
                blanks = [(i, j)] + blanks

        n = len(board)
        blankls = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    blankls.append((i, j))
        backtrack(board,blankls)
        return self.ans


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
res = Solution().solveSudoku(board)
print(res)
print(board)
