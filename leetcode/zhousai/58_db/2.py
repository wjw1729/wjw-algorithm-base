"""
author:wjw
分析：考场临时写的代码。不太行
"""
class Solution:
    def checkMove(self, board, rMove: int, cMove: int, color: str) -> bool:

        check = False
        anothercolor = False
        ac = 'B' if color == 'W' else 'W'

        searchlist = []

        searchlist.append([(i, cMove) for i in range(rMove - 1, -1, -1)])
        searchlist.append([(i, cMove) for i in range(rMove + 1, 8)])
        searchlist.append([(rMove, i) for i in range(cMove - 1, -1, -1)])
        searchlist.append([(rMove, i) for i in range(cMove + 1, 8)])
        searchlist.append([(rMove - i, cMove - i) for i in range(1, min(rMove, cMove) + 1)])
        searchlist.append([(rMove + i, cMove + i) for i in range(1, min(8 - rMove, 8 - cMove))])
        searchlist.append([(rMove + i, cMove - i) for i in range(1, min(8 - rMove, cMove + 1))])
        searchlist.append([(rMove - i, cMove + i) for i in range(1, min(8 - cMove, rMove + 1))])

        la = [(rMove + 1, cMove), (rMove - 1, cMove), (rMove, cMove + 1), (rMove, cMove - 1), (rMove + 1, cMove + 1),
              (rMove - 1, cMove - 1), (rMove - 1, cMove + 1), (rMove + 1, cMove - 1)]
        for k in range(8):
            """
            p, q = la[k]
            if 0 <= p < 8 and 0 <= q < 8 and board[p][q] == color:
                print(k)
                continue    
            """

            for i, j in searchlist[k]:
                if board[i][j] == '.':
                    break
                if board[i][j] == ac:
                    anothercolor = True
                if  board[i][j] == color:
                    if anothercolor:
                        print(i, j)
                        return True
                    else:
                        break
            anothercolor = False

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
