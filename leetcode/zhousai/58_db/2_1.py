"""
author:wjw
分析:
"""


class Solution:
    def checkMove(self, board, rMove, cMove, color):
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        if color == 'W':
            anothercolor = 'B'
        else:
            anothercolor = 'W'

        for k in range(8):

            check = False
            i, j = rMove, cMove
            curx, cury = direction[k]
            i += curx
            j += cury

            while 0 <= i < 8 and 0 <= j < 8:
                if board[i][j] == '.':
                    break

                if board[i][j] == anothercolor:
                    check = True

                if board[i][j] == color:
                    if check:
                        return True
                    else:
                        break

                i += curx
                j += cury

        return False

board = [["B", "B", ".", ".", "B", "W", "W", "."], [".", "W", "W", ".", "B", "W", "B", "B"],
         [".", "W", "B", "B", "W", ".", "W", "."], ["B", ".", ".", "B", "W", "W", "W", "."],
         ["W", "W", "W", "B", "W", ".", "B", "W"], [".", ".", ".", "W", ".", "W", ".", "B"],
         ["B", "B", "W", "B", "B", "W", "W", "B"], ["W", ".", "W", "W", ".", "B", ".", "W"]]
#board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]]
rMove = 2
cMove = 5
color = "W"
res = Solution().checkMove(board, rMove, cMove, color)
print(res)
