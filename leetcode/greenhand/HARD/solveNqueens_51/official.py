"""
author：official
分析：随着搜索的进行，更新三个变量用于判断有效性，降低时间复杂度。+回溯算法。queens()记录每行Q的列数。
"""

class Solution:
    def solveNQueens(self, n: int):
        def generateBoard():#根据记录的列数来生成对应的棋盘的程序
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)

                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions


n = 5
res = Solution().solveNQueens(n)
print(res)