"""
author:wjw
分析：回溯算法
"""


def isnotValid(board, r, col):
    Q_col = [x.index('Q') for x in board if 'Q' in x]
    for i in range(r):
        if i + Q_col[i] == r + col or i - Q_col[i] == r - col or Q_col[i] == col:
            return True
    return False


class Solution:
    def solveNQueens(self, n):
        ans = []
        chessboard = [['.' for i in range(n)] for i in range(n)]

        def traceback(board, r):
            if r == n:
                ans.append([''.join(x) for x in board])
                return

            for col in range(n):
                if isnotValid(board, r, col):
                    continue

                board[r][col] = 'Q'
                traceback(board, r + 1)
                board[r][col] = '.'

        traceback(chessboard, 0)
        return ans


n = 7
res = Solution().solveNQueens(n)
print(res)
