"""
author:wjw
"""

import collections


class Solution:
    def largestArea(self, grid) -> int:

        m = len(grid)
        n = len(grid[0])

        grid = [list(x) for x in grid]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '9' and grid[i][j] != '0' and (
                        i == 0 or i == m - 1 or j == 0 or j == n - 1 or grid[i - 1][j] == '0' or grid[i + 1][
                    j] == '0' or \
                        grid[i][j - 1] == '0' or grid[i][j + 1] == '0'):
                    neighbors = collections.deque()
                    neighbors.append((i, j))
                    areavalue = grid[i][j]
                    grid[i][j] = '9'
                    while neighbors:
                        r, c = neighbors.popleft()
                        for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == areavalue:
                                neighbors.append((x, y))
                                grid[x][y] = '9'
        max_area = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i - 1][j] != '0' and grid[i + 1][j] != '0' and grid[i][j - 1] != '0' and grid[i][
                    j + 1] != '0' and grid[i][j] != '9' and grid[i][j] != '0':
                    neighbors = collections.deque()
                    neighbors.append((i, j))
                    areavalue = grid[i][j]
                    ans = 1
                    grid[i][j] = '9'
                    while neighbors:
                        r, c = neighbors.popleft()
                        for x, y in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
                            if 0 <= x <= m and 0 <= y < n and grid[x][y] == areavalue:
                                neighbors.append((x, y))
                                ans += 1
                                grid[x][y] = '9'

                    max_area = max(max_area, ans)
        return max_area


grid = ["110", "231", "221"]
grid = ["11111100000", "21243101111", "21224101221", "11111101111"]
res = Solution().largestArea(grid)
print(res)
