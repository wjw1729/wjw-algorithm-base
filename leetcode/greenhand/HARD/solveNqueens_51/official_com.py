"""
author:wjw
分析：
"""


class Solution:
    def solveNQueens(self, n):

        def getChessboard():

            chessboard = []
            board = ['.'] * n
            for i in range(n):
                board[queen[i]] = 'Q'
                chessboard.append('.'.join(board))
                board[queen[i]] = '.'

            return chessboard

        ans = []

        def trackback(r):
            if r == n:
                board = getChessboard()
                ans.append(board)

                return

            for c in range(n):
                if c in cols or r + c in diagnoal1 or r - c in diagnoal2:
                    continue

                cols.add(c)
                diagnoal1.add(r + c)
                diagnoal2.add(r - c)
                queen[r] = c
                trackback(r + 1)

                cols.remove(c)
                diagnoal1.remove(r + c)
                diagnoal2.remove(r - c)

        cols = set()
        diagnoal1 = set()
        diagnoal2 = set()
        queen = [-1] * n

        trackback(0)
        return ans


n = 4
res = Solution().solveNQueens(n)
print(len(res))
