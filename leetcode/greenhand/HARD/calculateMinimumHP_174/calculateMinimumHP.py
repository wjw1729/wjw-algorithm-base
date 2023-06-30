"""
author:wjw
zhongwen:zhezhong fanxiangsikao defangfa youdaikaifa.
"""
from collections import deque


class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        queue = deque()

        minHealth = [[float("inf")] * n for _ in range(m)]

        dungeon = [[-x for x in l] for l in dungeon]
        queue.append((m - 1, n - 1, 1 + dungeon[m - 1][n - 1]))
        while queue:
            r, c, h = queue.popleft()
            if h <= 0:
                h = 1
            if h >= minHealth[r][c]:
                continue
            else:
                minHealth[r][c] = h

            for x, y in [(r - 1, c), (r, c - 1)]:
                if 0 <= x < m and 0 <= y < n:
                    queue.append((x, y, h + dungeon[x][y]))

        return minHealth[0][0]


dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
res = Solution().calculateMinimumHP(dungeon)
print(res)
