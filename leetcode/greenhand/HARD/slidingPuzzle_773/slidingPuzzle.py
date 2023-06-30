"""
author:wjw
分析：广度优先搜索+迭代
"""


class Solution:
    def slidingPuzzle(self, board):
        board = board[0] + board[1]
        if board==[1,2,3,4,5,0]:
            return 0

        swap_tab = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
        queue = [(board, 0)]
        board = tuple(board)
        status_his = {board}

        while queue:
            status, level = queue.pop(0)

            index = status.index(0)

            swap_indexs = swap_tab[index]

            for swap_index in swap_indexs:
                next_status = [0] * 6           #这两步注意下，很重要，一个是开辟新的空间，一个是防止修改status.
                next_status[:] = status
                next_status[index] = next_status[swap_index]
                next_status[swap_index] = 0

                if next_status == [1, 2, 3, 4, 5, 0]:
                    return level + 1
                if tuple(next_status) not in status_his:
                    queue.append((next_status, level + 1))
                    status_his.add(tuple(next_status))

        return -1


board = [[1, 2, 3], [4, 0, 5]]
board = [[1, 2, 3], [5, 4, 0]]
board = [[4, 1, 2], [5, 0, 3]]
board = [[3, 2, 4], [1, 5, 0]]
res = Solution().slidingPuzzle(board)
print(res)
