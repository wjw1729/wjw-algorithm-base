"""
author:wjw
分析：二分查找+广度优先搜索
"""

from collections import deque


class Solution:
    def latestDayToCross(self, row, col, cells):
        n = len(cells)
        left = 0
        right = n
        ans = 0

        while left <= right:
            board = [[0] * col for i in range(row)]
            mid = (left + right) // 2

            queue = deque()
            bin = set()

            for x, y in cells[:mid]:
                board[x - 1][y - 1] = 1
                bin.add((x-1,y-1))


            for j in range(col):
                if board[0][j] == 0:
                    queue.append((0, j))
                    bin.add((0, j))

            check = False
            while queue:
                r, c = queue.popleft()

                for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= x < row and 0 <= y < col and (x, y) not in bin:
                        if x == row - 1:
                            check = True
                            break
                        queue.append((x, y))
                        bin.add((x, y))

                if check:
                    break

            if check:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


row = 55
col = 2
cells = [[53, 1], [25, 1], [9, 2], [3, 1], [54, 1], [14, 2], [28, 1], [4, 1], [44, 1], [20, 2], [28, 2], [24, 2],
         [50, 1], [47, 2], [21, 1], [47, 1], [22, 2], [10, 1], [17, 1], [13, 1], [12, 1], [37, 2], [46, 2], [51, 1],
         [32, 1], [51, 2], [6, 2], [49, 2], [13, 2], [34, 1], [33, 1], [38, 2], [52, 2], [26, 2], [46, 1], [20, 1],
         [33, 2], [23, 2], [17, 2], [1, 2], [3, 2], [50, 2], [25, 2], [19, 1], [21, 2], [49, 1], [29, 1], [30, 2],
         [41, 1], [16, 1], [39, 2], [9, 1], [48, 2], [23, 1], [27, 1], [43, 1], [45, 1], [31, 1], [40, 1], [6, 1],
         [42, 1], [8, 2], [12, 2], [29, 2], [36, 2], [39, 1], [41, 2], [10, 2], [44, 2], [14, 1], [35, 1], [30, 1],
         [2, 2], [34, 2], [55, 1], [18, 1], [32, 2], [27, 2], [4, 2], [37, 1], [38, 1], [16, 2], [26, 1], [15, 2],
         [19, 2], [5, 1], [45, 2], [43, 2], [55, 2], [35, 2], [54, 2], [42, 2], [22, 1], [11, 1], [48, 1], [1, 1],
         [36, 1], [24, 1], [8, 1], [2, 1], [7, 1], [15, 1], [31, 2], [18, 2], [7, 2], [52, 1], [40, 2], [53, 2],
         [11, 2], [5, 2]]
"""
row = 2
col = 2
cells = [[1,1],[2,1],[1,2],[2,2]]
row = 2
col = 2
cells = [[1,1],[1,2],[2,1],[2,2]]
"""
res = Solution().latestDayToCross(row, col, cells)
print(res)
