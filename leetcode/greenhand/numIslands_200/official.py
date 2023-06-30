"""
author:wjw
分析：DFS。
"""


class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        sum_r = len(grid)
        sum_c = len(grid[0])
        for i, j in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if i >= 0 and i < sum_r and j >= 0 and j < sum_c and grid[i][j] == '1':
                self.dfs(grid, i, j)

    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    self.dfs(grid, i, j)

        return ans


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
        ]

grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
grid = [['0']]
grid = [["0", "0", "0", "0", "0", "0", "1"]]
res = Solution().numIslands(grid)
print(res)
