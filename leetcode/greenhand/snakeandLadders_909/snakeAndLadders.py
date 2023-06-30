"""
author:wjw
分析:
"""


class Solution:
    def snakeAndLadders(self, board):
        n = len(board)
        queue = [(1, 0)]
        bin = {1}

        val_list = [0]
        for i in range(n):
            if i % 2 == 0:
                val_list += board[n - 1 - i]
            else:
                val_list += list(reversed(board[n - 1 - i]))

        while queue:
            pos, level = queue.pop(0)
            for next_pos in range(pos + 1, pos + 7):

                if val_list[next_pos] != -1:
                    next_pos = val_list[next_pos]
                if next_pos == n * n:
                    return level + 1

                if next_pos not in bin:
                    queue.append((next_pos, level + 1))
                    bin.add(next_pos)

        return -1


board = [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]
board = [[-1, -1, 19, 10, -1], [2, -1, -1, 6, -1], [-1, 17, -1, 19, -1], [25, -1, 20, -1, -1], [-1, -1, -1, -1, 15]]

res = Solution().snakeAndLadders(board)
print(res)
