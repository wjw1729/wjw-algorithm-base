"""
author:wjw
分析：逆流。迭代实现。
时间复杂度:O(m*n)
"""

from collections import deque


class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        pac = [[0] * n for _ in range(m)]
        atl = [[0] * n for _ in range(m)]
        ans = []

        pacqueue = deque()
        atlqueue = deque()
        for i in range(m):
            pacqueue.append((i, 0))
            atlqueue.append((i, n - 1))
        for j in range(1, n):
            pacqueue.append((0, j))
            atlqueue.append((m - 1, n - 1 - j))

        while pacqueue:
            r, c = pacqueue.popleft()

            if pac[r][c] == 0:
                pac[r][c] = 1
            else:
                continue
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[r][c] and pac[x][y] == 0:
                    pacqueue.append((x, y))

        while atlqueue:
            r, c = atlqueue.popleft()

            if atl[r][c] == 1:
                continue
            atl[r][c] = 1
            if pac[r][c] == 1:
                ans.append([r, c])

            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[r][c] and atl[x][y] == 0:
                    atlqueue.append((x, y))

        return ans


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
res = Solution().pacificAtlantic(heights)
print(res)
