"""
author:wjw
分析：
"""
import collections


class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    neighbors = collections.deque()
                    neighbors.append((i, j))
                    grid[i][j] = '0'
                    while neighbors:
                        r, c = neighbors.popleft()
                        for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                neighbors.append((x, y))
                                grid[x][y] = '0'

        return num_islands


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
"""
grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
        ]
"""
# grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
# grid = [['0']]
# grid = [["0", "0", "0", "0", "0", "0", "1"]]
res = Solution().numIslands(grid)
print(res)
